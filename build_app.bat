@echo off
setlocal enabledelayedexpansion

:: === Step 1: Check if Python is installed ===
echo Step 1: Checking if Python is installed...
python --version >nul 2>&1
if %errorlevel% equ 0 (
    echo Python is already installed.
) else (
    echo Python is not installed. Proceeding to install Python 3.9.20.
    goto install_python
)
echo Python version check passed.
echo.
goto upgrade_pip

:: === Step 2: Install Python ===
:install_python
echo Step 2: Installing Python 3.9.20...

:: Set Python version and installer URL
set PYTHON_VERSION=3.9.20
set PYTHON_INSTALLER=python-%PYTHON_VERSION%-amd64.exe
set PYTHON_URL=https://www.python.org/ftp/python/%PYTHON_VERSION%/%PYTHON_INSTALLER%

:: Download Python installer
echo Downloading Python installer from %PYTHON_URL%...
powershell -Command "Invoke-WebRequest -Uri %PYTHON_URL% -OutFile %PYTHON_INSTALLER%"
if not exist %PYTHON_INSTALLER% (
    echo Failed to download Python installer. Exiting.
    pause >nul
    exit /b
)

:: Install Python silently
echo Installing Python...
start /wait %PYTHON_INSTALLER% /quiet InstallAllUsers=1 PrependPath=1
if %errorlevel% neq 0 (
    echo Python installation failed. Exiting.
    pause >nul
    exit /b
)

:: Clean up installer
del %PYTHON_INSTALLER%
echo Python installed successfully.
echo.
goto upgrade_pip

:: === Step 3: Upgrade pip ===
:upgrade_pip
echo Step 3: Upgrading pip...
python -m pip install --upgrade pip
if %errorlevel% neq 0 (
    echo Failed to upgrade pip. Exiting.
    pause >nul
    exit /b
)
echo Pip upgraded successfully.
echo.
goto install_requirements

:: === Step 4: Install requirements ===
:install_requirements
echo Step 4: Installing dependencies from requirements.txt...

if not exist requirements.txt (
    echo requirements.txt not found. Ensure the file exists in this directory.
    pause >nul
    exit /b
)

python -m pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Failed to install dependencies. Please check requirements.txt. Exiting.
    pause >nul
    exit /b
)
echo Dependencies installed successfully.
echo.
goto build_executable

:: === Step 5: Build executable ===
:build_executable
echo Step 5: Building AffinityMaster.exe...

if not exist AffinityMaster.py (
    echo AffinityMaster.py not found. Ensure the file exists in this directory.
    pause >nul
    exit /b
)

python -m pip install pyinstaller
if %errorlevel% neq 0 (
    echo Failed to install PyInstaller. Exiting.
    pause >nul
    exit /b
)

pyinstaller --clean --onefile AffinityMaster.py
if exist dist\AffinityMaster.exe (
    echo Build successful! Executable is located in the "dist" folder.
) else (
    echo Build failed. Please check PyInstaller logs. Exiting.
    pause >nul
    exit /b
)

:: === Step 6: Copy AffinityMaster.ini to dist folder ===
echo Step 6: Copying AffinityMaster.ini to dist folder...
if exist AffinityMaster.ini (
    copy AffinityMaster.ini dist\
    if %errorlevel% equ 0 (
        echo AffinityMaster.ini copied successfully.
    ) else (
        echo Failed to copy AffinityMaster.ini.
    )
) else (
    echo AffinityMaster.ini not found. Skipping copy.
)

:: End of script
echo.
echo Script completed successfully!
pause >nul
exit /b
