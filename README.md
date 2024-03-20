# AffinityMaster

## Description
AffinityMaster is a simple Python script that manages CPU affinity for a specified process. Usefull for older games that don't support multithreading.

## Features
- Set CPU affinity for a specified process to improve performance.
- Easy configuration using an INI file.

## Installation
1. **Clone the repository:**
    ```sh
   git clone https://github.com/RedJohn260/AffinityMaster.git

2. **Navigate to the project directory:**
   ```sh
    cd AffinityMaster

3. **Install dependencies using pip:**
    ```sh
    pip install -r requirements.txt

## Usage
1. Ensure you have Python installed on your system.
2. Run the script using Python:
   ```sh
   python AffinityMaster.py

## Configuration
Before running the script, make sure to configure the **AffinityMaster.ini** file with the desired settings. The file should have the following format: 
   ```sh
   [config]
   wait_duration = <wait duration in seconds>
   exe_name = <name of the executable to manage CPU affinity for>
   start_app = <0/1 to specify whether to start the executable>
   ```
## Support
For any questions, issues, or feature requests, please open an issue.