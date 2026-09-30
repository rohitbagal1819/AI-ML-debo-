@echo off
REM One-step setup for Windows: creates a virtual environment and installs dependencies.
cd /d "%~dp0"
python -m venv venv
if errorlevel 1 (
  echo Python was not found. Install Python 3.10+ from python.org and tick "Add Python to PATH".
  exit /b 1
)
call venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt
if not exist .env copy .env.example .env
echo.
echo Setup complete. Next: put client_secret.json in the credentials folder, then run:
echo     venv\Scripts\python authorize.py
