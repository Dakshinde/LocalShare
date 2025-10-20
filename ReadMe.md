# LocalShare 

Simple, offline file sharing for your local network. No internet required.

## One-Time Setup (Do This Only Once)

Before you can share, you need two things: **Python** and the **app files**.

### 1. Install Python

If you don't have it, install Python 3.
* Go to [python.org](https://www.python.org/downloads/)
* Download the installer.
* **IMPORTANT (for Windows):** On the first screen of the installer, **check the box** that says "**Add Python to PATH**". This is crucial.

### 2. Get the App & Install Libraries

1.  Click the green "Code" button at the top of this GitHub page and choose "**Download ZIP**".
2.  Unzip the file. You'll have a folder named `LocalShare-Project`. Place this folder somewhere permanent (like your Desktop or Documents).
3.  Open your terminal in this folder:
    * **Windows:** Click in the address bar of the folder, type `cmd`, and press Enter.
    * **Mac/Linux:** Right-click in the folder and choose "Open in Terminal".
4.  In the terminal window that pops up, type this one command and press Enter:

    ```
    pip install -r requirements.txt
    ```

That's it! Setup complete.

---

## How to Share (Day-to-Day Use)

### On Windows 🪟 (Easiest Way)

1.  Navigate to your `LocalShare-Project` folder.
2.  **Double-click** the `run.bat` file.
3.  A black window will open asking for the folder path.
4.  Open File Explorer and find the folder you want to share.
5.  **Drag that folder** from File Explorer and **drop it directly into the black terminal window**. The folder's path will appear automatically.
    [Image showing drag folder into cmd window]
6.  Press **Enter**.
7.  The script confirms the path, shows a QR code, and opens the share page in your browser.
8.  Scan the QR code with your phone.

**(Alternative) Copy-Paste:** You can still copy the path from the File Explorer address bar and paste it into the terminal window (right-click to paste).

**(Alternative) Drag-and-Drop onto Icon:** You can also drag the folder onto the `run.bat` file icon itself (or a shortcut).

### On Mac / Linux 🍎🐧

1.  Open your terminal.
2.  `cd` into the `LocalShare-Project` folder.
    * *Example: `cd ~/Desktop/LocalShare-Project`*
3.  (First time only) Make the script executable: `chmod +x run.sh`
4.  Run the script **without** arguments:
    * `./run.sh`
5.  The script will prompt you for the folder path.
6.  Open your file manager, find the folder.
7.  **Drag the folder** from the file manager and **drop it into the terminal window**. The path will appear.
8.  Press **Enter**.
9.  The terminal shows the QR code and opens your browser.

**(Alternative) Argument:** You can still run it like `./run.sh /path/to/your/folder`.

---

## How to Stop Sharing

Simply **close the black terminal window**.

1.  Go back to the **black terminal window** where LocalShare is running (the one showing the QR code).
2.  Press **Ctrl+C** (hold down the Ctrl key and press C).
3.  The server will shut down. You can then close the terminal window (it might prompt you to "Press any key").
