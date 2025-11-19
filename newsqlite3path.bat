echo "Script to set the sqlite path"
@echo off
set script=%~dp0newsqlite3path.ps1

set newpath=C:\sqlite3

:: Check if running as admin
net session >nul 2>&1
if %errorlevel% NEQ 0 (
    echo Requesting administrator privileges...
    powershell -Command "Start-Process '%~0' -Verb RunAs" 
    exit /b
)

:: Now running as admin - run the PowerShell script
powershell -NoProfile -ExecutionPolicy Bypass -File "%script%" -NewPath %newpath% 

