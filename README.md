# AffinityMaster

## Description
AffinityMaster is a simple Python script that manages CPU affinity for a specified process. Usefull for older games that don't support multithreading. Possibly to improve performance in CPU bound games.

## Features
- Set CPU affinity for a specified process to improve performance.
- Automatically calculates number of threads on CPU.
- Forces the process to only use physical cores and avoid usage of E-Cores.
- Easy configuration using an INI file.

## Installation
1. **Ensure you have Python installed on your system.**

2. **Clone the repository:**
    ```sh
   git clone https://github.com/RedJohn260/AffinityMaster.git
3. **Navigate to the project directory:**
   ```sh
    cd AffinityMaster
4. **Install dependencies using pip:**
    ```sh
    pip install -r requirements.txt

## Building executable
1. **Run Pyinstaller build command:**
   ```sh
   pyinstaller AffinityMaster.py --onefile

## Usage
1. Copy **AffinityMaster.ini**, **AffinityMaster.py** or **AffinityMaster.exe** in your game directory.
2. Configure **AffinityMaster.ini** file with the desired settings. The file should have the following format: 
   ```sh
   [config]
   wait_duration = <wait duration in seconds>
   exe_name = <name of the executable to manage CPU affinity for>
   start_app = <0/1 to specify whether to start the executable with the AffinityMaster script>
   ```
3. Run the script using **Python** or **AffinityMaster.exe**:
   ```sh
   python AffinityMaster.py

## Troubleshooting 
Not every system will benefit from this script. There's nothing to troubleshoot.