# AffinityMaster

## Description
AffinityMaster is a simple Python script that manages CPU affinity and priority for a specified process. Usefull for older games that don't support multithreading. Possibly to improve performance in CPU bound games.

## Features
- Set CPU affinity and priority for a specified process to improve performance.
- Automatically calculates number of threads on CPU.
- Forces the process to only use physical cores and avoid usage of E-Cores.
- Easy configuration using an INI file.

## Building the exe application
### Option1:
1. **Ensure you have Python 3.9.20 installed on your system.**

2. **Clone the repository:**
    ```sh
   git clone https://github.com/RedJohn260/AffinityMaster.git
3. **Navigate to the project directory:**
   ```sh
    cd AffinityMaster
4. **Install dependencies using pip:**
    ```sh
    pip install -r requirements.txt
5. **Buld the executable with pyinstaller:**
   ```sh
    pyinstaller --clean --onefile AffinityMaster.py
### Option2:
1. **Build using provided batch script:**
   ```sh
    run build_app.bat file

## Usage
1. Copy **AffinityMaster.ini**, **AffinityMaster.py** or **AffinityMaster.exe** in your game directory.
2. Configure **AffinityMaster.ini** file with the desired settings. The file should have the following format: 
   ```sh
   [config]
   wait_duration = <wait duration in seconds before executing main executable>
   main_exe_name = <name of the main executable to manage CPU affinity and priority>
   launcher_exe_name = <name of the launcher executable to launch main executable>
   start_app = <0/1 to specify whether to start the executable with the PlayGTAIV script>
   mode = <0/1 to specify whether to set just process priority or affinity and priority>
   ```
3. Run the script using **Python** or **AffinityMaster.exe**:
   ```sh
   python AffinityMaster.py

## Troubleshooting 
Not every system will benefit from this script. There's nothing to troubleshoot.