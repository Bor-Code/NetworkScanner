@echo off
echo ========================================
echo  Network Scanner Pro - Installation
echo ========================================
echo.

echo Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed!
    echo Please install Python 3.8 or higher from https://www.python.org
    pause
    exit /b 1
)

echo.
echo Installing dependencies...
python -m pip install --upgrade pip
pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo ERROR: Installation failed!
    pause
    exit /b 1
)

echo.
echo ========================================
echo  Installation completed successfully!
echo ========================================
echo.
echo To run the application:
echo   - GUI Mode: python app.py
echo   - CLI Mode: python src/main.py -t 192.168.1.0/24
echo.
pause
