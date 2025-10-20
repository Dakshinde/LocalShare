# LocalShare 

> Simple, offline file sharing for your local network. No internet required.

Welcome to LocalShare! This tool lets you share files and folders to any device on your local network (like your phone) without needing an internet connection.

---

## 1️⃣ One-Time Setup (Do This First!)

You **must** complete these two parts **one time** before you can use the app.

### 🐍 Part 1: Install Python (If you don't have it)

> (If you already have Python 3, you can skip to Part 2!)

1.  Go to [python.org](https://www.python.org/downloads/)
2.  Download the latest Python 3 installer.
3.  Run the installer.
4.  ⚠️ **VERY IMPORTANT (for Windows):** On the first screen of the installer, **check the box** that says "**Add Python to PATH**". This is crucial for the app to work.
    

### 📦 Part 2: Install Project Requirements (MANDATORY)

This is the most important step. You must do this *after* installing Python but *before* running the app for the first time.

1.  **Get the Project Folder**
    * You should have a folder named `LocalShare-Project` (or similar) that contains all the app files (`run.bat`, `requirements.txt`, etc.).
    * Place this folder somewhere permanent, like your **Desktop** or **Documents**.

2.  **Open a Terminal INSIDE That Folder**
    * You must run the next command *inside* the project folder. Here’s how:
    * **Windows:**
        * **Method A (Easiest):** Open the `LocalShare-Project` folder in File Explorer. Click in the empty space of the address bar at the top, type `cmd`, and press **Enter**.
        * **Method B:** Right-click inside the `LocalShare-Project` folder and select **"Open in Terminal"** (this option is available in Windows 11 or with Windows Terminal installed).
    * **Mac/Linux:** Right-click inside the `LocalShare-Project` folder and choose **"Open in Terminal"**.

3.  **Install the Libraries**
    * A terminal window will now be open, and its path should be inside your `LocalShare-Project` folder.
    * Type (or copy-paste) this exact command and press **Enter**:

    ```bash
    pip install -r requirements.txt
    ```

    * Wait for it to finish installing. [cite_start]You will see it downloading packages like `fastapi`, `uvicorn`, `qrcode`, etc. [cite: 1]
    * Once it's done, you can close this terminal window.

### 🎉 Setup is complete! You only need to do this once. 🎉

---

## 2️⃣ How to Share (Day-to-Day Use)

Now for the easy part!

### ｪ On Windows (Easiest Way)

1.  Navigate to your `LocalShare-Project` folder.
2.  **Double-click** the `run.bat` file.
3.  A new black window will open, asking for the folder path.
4.  Open a *different* File Explorer window and find the folder you wish to share.
5.  **Drag that folder** from File Explorer and **drop it directly into the black terminal window**. The folder's path will appear automatically.
    [Image showing drag folder into cmd window]
6.  Press **Enter**.
7.  The app will start! It will show a **QR code** in the terminal and automatically open the sharing page in your web browser.
8.  Scan the QR code with your phone (or other device) to access the files!

### 克制 On Mac / Linux

1.  Open your regular terminal.
2.  `cd` into your `LocalShare-Project` folder.
    * *Example: `cd ~/Desktop/LocalShare-Project`*
3.  (First time only) Make the script executable. Type: `chmod +x run.sh`
4.  Run the script by typing:
    * `./run.sh`
5.  The script will prompt you for the folder path.
6.  Open your file manager and find the folder you want to share.
7.  **Drag the folder** from the file manager and **drop it into the terminal window**. The path will appear.
8.  Press **Enter**.
9.  The terminal will show the QR code. Scan it with your phone to connect!

---

## 3️⃣ How to Stop Sharing

When you are finished sharing, just go back to the **black terminal window** (the one showing the QR code).

1.  Press **Ctrl+C** (hold the Ctrl key and press C).
2.  **Close the terminal window.**

That's it! The server will shut down.
