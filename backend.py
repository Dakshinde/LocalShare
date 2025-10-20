import os
import uvicorn
import aiofiles
import socket       # NEW: To get the local IP
import qrcode       # NEW: To print QR code to terminal
import webbrowser   # NEW: To auto-open the browser
import sys          # NEW: To exit the script
import shutil
from fastapi import FastAPI, Request, UploadFile, File
from fastapi.responses import StreamingResponse, HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from urllib.parse import quote
import stat
from typing import List
from fastapi.responses import FileResponse


# --- Configuration ---
PORT = 8000
FOLDER_TO_SHARE = os.environ.get("FOLDER_TO_SHARE")

# --- Helper Function (Copied from your old app.py) ---
def get_ip():
    """Gets the local IP address of the machine."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Doesn't have to be reachable
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip

# --- FastAPI App Setup (Your existing code) ---
app = FastAPI()

# Serve static CSS
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def index(request: Request):
    files = []
    folder_name = os.path.basename(FOLDER_TO_SHARE) if FOLDER_TO_SHARE else "No folder selected"
    if FOLDER_TO_SHARE:
        files = [f for f in os.listdir(FOLDER_TO_SHARE) if os.path.isfile(os.path.join(FOLDER_TO_SHARE, f))]
    files_safe = [{"name": f, "url": quote(f)} for f in files]
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "files": files_safe, "folder_name": folder_name}
    )

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    favicon_path = os.path.join("static", "favicon.ico")
    if os.path.exists(favicon_path):
        return FileResponse(favicon_path, media_type="image/vnd.microsoft.icon")
    else:
        # Optional: return a default response or error if favicon.ico is missing
        return JSONResponse(content={"error": "Favicon not found"}, status_code=404)
    

@app.get("/download/{filename:path}")
async def download_file(filename: str):
    if FOLDER_TO_SHARE:
        full_path = os.path.join(FOLDER_TO_SHARE, filename)
        if os.path.exists(full_path) and os.path.isfile(full_path):
            stat_result = os.stat(full_path)
            file_size = stat_result.st_size
            
            async def file_iterator():
                async with aiofiles.open(full_path, mode='rb') as f:
                    chunk_size = 1024 * 64
                    while True:
                        chunk = await f.read(chunk_size)
                        if not chunk:
                            break
                        yield chunk
            
            headers = {
                "Content-Disposition": f"attachment; filename=\"{filename}\"",
                "Content-Type": "application/octet-stream",
                "Content-Length": str(file_size)
            }
            return StreamingResponse(file_iterator(), headers=headers)
            
    return JSONResponse(content={"error": "File not found"}, status_code=404)


@app.post("/upload")
async def upload_files(files: List[UploadFile] = File(...)):
    if not FOLDER_TO_SHARE:
        return JSONResponse(
            status_code=400,
            content={"error": "No destination folder configured"}
        )
    
    uploaded_files = []
    for file in files:
        try:
            # Clean filename to prevent path traversal
            filename = os.path.basename(file.filename)
            if not filename: continue # Skip empty filenames

            file_path = os.path.join(FOLDER_TO_SHARE, filename)
            async with aiofiles.open(file_path, 'wb') as f:
                while content := await file.read(1024 * 64): # Read in chunks
                    await f.write(content)
            uploaded_files.append({"filename": filename, "status": "success"})
        except Exception as e:
            uploaded_files.append({"filename": file.filename, "status": "error", "error": str(e)})
    
    return {"uploaded_files": uploaded_files}

# --- Main Execution Block (UPDATED) ---
if __name__ == "__main__":

    # 1. Check if the folder was provided via environment variable (drag-and-drop/run.sh)
    FOLDER_TO_SHARE = os.environ.get("FOLDER_TO_SHARE")

    # 2. If not provided, ASK the user for the path
    if not FOLDER_TO_SHARE:
        print("="*50)
        print("📁 Please provide the folder path to share.")
        print("   Hint: Open the folder in File Explorer, copy the path")
        print("   from the address bar, and paste it below.")
        print("="*50)
        while True:
            try:
                user_path = input("Paste folder path here and press Enter: ").strip()
                # Remove quotes if user pasted them (common in Windows)
                if user_path.startswith('"') and user_path.endswith('"'):
                    user_path = user_path[1:-1]
                elif user_path.startswith("'") and user_path.endswith("'"):
                    user_path = user_path[1:-1]

                if os.path.isdir(user_path):
                    FOLDER_TO_SHARE = user_path
                    print(f"✅ Path accepted: {FOLDER_TO_SHARE}")
                    break # Exit the loop, path is valid
                else:
                    print(f"❌ ERROR: '{user_path}' is not a valid folder path. Please try again.")
            except Exception as e:
                print(f"❌ An error occurred: {e}. Please try again.")
                
    # --- The rest of the script remains the same ---

    # 3. Get IP and build URL
    HOST_IP = get_ip()
    URL = f"http://{HOST_IP}:{PORT}"

    # 4. Print the "GUI" to the terminal
    print("\n" + "="*50)
    print("         🚀 LocalShare Server is RUNNING! 🚀")
    print("="*50)
    print(f"📁 Sharing Folder: {os.path.basename(FOLDER_TO_SHARE)}")
    print(f"      Full Path: {FOLDER_TO_SHARE}")
    print("\n" + "-"*50)
    print(f"💻 Access from your PC at:   {URL}")
    print(f"📱 Access from your Phone at: {URL}")
    print("-" * 50)
    print("\n📱 Scan this QR code with your phone's camera:")

    # 5. Print the QR code to the terminal
    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(URL)
    qr.make(fit=True)
    qr.print_ascii(tty=True) # Print QR code

    print("\n" + "="*50)
    # print("🎉 Opening the share page in your default browser...") # We disabled this
    print("✅ Server is now running. Keep this window open.")
    print("🔴 To STOP the server, press: CTRL + C") # <-- ADD THIS LINE
    print("="*50)

    # 6. Auto-launch the browser
    try:
        #webbrowser.open(URL)
        pass
    except Exception as e:
        print(f"Could not open browser: {e}")


    # 7. Run the server
    os.environ["FOLDER_TO_SHARE"] = FOLDER_TO_SHARE
    uvicorn.run(app, host="0.0.0.0", port=PORT, log_level="warning")