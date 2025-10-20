@echo off
rem This is the Windows launcher for LocalShare

TITLE LocalShare Server

rem Check if a file/folder was dragged onto the script
if NOT "%~1"=="" (
    rem If something was dropped, set the environment variable
    echo Setting folder from Drag-and-Drop: %~1
    set FOLDER_TO_SHARE=%~1
) else (
    rem If nothing was dropped, clear the variable (Python script will ask)
    echo No folder dropped, will prompt for path...
    set FOLDER_TO_SHARE=
)

echo =========================================
echo          Starting LocalShare...
echo =========================================
echo.

rem Run the Python server (it will now ask if FOLDER_TO_SHARE is empty)
python backend.py

rem Keep the window open after the server stops
echo.
echo Server has been stopped. Press any key to close this window.
pause > nul