import subprocess
import sys
import psutil
import time
import configparser
import logging
from colorama import init, Fore, Style

init()

welcome_screen = """
            __  __ _       _ _         __  __           _            
     /\    / _|/ _(_)     (_) |       |  \/  |         | |           
    /  \  | |_| |_ _ _ __  _| |_ _   _| \  / | __ _ ___| |_ ___ _ __ 
   / /\ \ |  _|  _| | '_ \| | __| | | | |\/| |/ _` / __| __/ _ \ '__|
  / ____ \| | | | | | | | | | |_| |_| | |  | | (_| \__ \ ||  __/ |   
 /_/    \_\_| |_| |_|_| |_|_|\__|\__, |_|  |_|\__,_|___/\__\___|_|   
                                  __/ |                              
                                 |___/                                  

                            version 1.0.0
                            author: RedJohn260
"""

def print_green_message(col_message):
    print(Fore.GREEN + col_message + Style.RESET_ALL)

def print_separator():
    print_green_message("=======================================================================")
    
def read_configuration():
    config = configparser.ConfigParser()
    config.read("PlayGTAIV.ini")
    wait_duration = int(config.get("config", "wait_duration"))
    main_exe_name = config.get("config", "main_exe_name")
    launcher_exe_name = config.get("config", "launcher_exe_name")
    start_app = int(config.get("config", "start_app"))
    mode = int(config.get("config", "mode"))
    return wait_duration, main_exe_name, launcher_exe_name, start_app, mode

def configure_logging():
    logging.basicConfig(filename='PlayGTAIV.log', filemode='w', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def track_progress_sleep(duration, interval=1):
    remaining_time = duration

    while remaining_time > 0:
        progress_percent = 100 - (remaining_time / duration) * 100
        message = f"Application wait time: {remaining_time:.2f} seconds [{progress_percent:.2f}%]"
        sys.stdout.write("\r" + f"Application wait time: {remaining_time:.2f} seconds [{progress_percent:.2f}%]")
        sys.stdout.flush()
        logging.info(message)
        logging.getLogger().handlers[0].flush()
        time.sleep(interval)
        remaining_time -= interval

    print(f"\nApplication wait time complete.")
    logging.info(f"Application wait time complete.")
    
def filter_processes(processes, main_exe_name):
    filtered_processes = []
    for process in processes:
        if process.name() == main_exe_name:
            filtered_processes.append(process)
    if not filtered_processes:
        error_message = f"{main_exe_name} process not running!"
        print(error_message)
        logging.error(error_message)
    return filtered_processes
        
def set_cpu_affinity(main_exe_name):
    logical_cores = psutil.cpu_count(logical=True)
    physical_cores = psutil.cpu_count(logical=False)

    if logical_cores == physical_cores:
        available_cores = list(range(1, physical_cores))
    else:
        available_cores = list(range(2, (logical_cores - physical_cores) * 2, 2))

    for process in filter_processes(psutil.process_iter(['pid', 'name']), main_exe_name):
        if process.name() == main_exe_name:
            pid = process.pid
            psutil.Process(pid).cpu_affinity(available_cores)
            message = f"Successfully set CPU affinity for process {main_exe_name} with PID {pid}"
            print(message)
            logging.info(message)
            return
    else:
        error_message = f"Unable to set CPU affinity on {main_exe_name} process!"
        print(error_message)
        logging.error(error_message)
        
def set_cpu_priority(main_exe_name):
    
    for process in filter_processes(psutil.process_iter(['pid', 'name']), main_exe_name):
        if process.name() == main_exe_name:
            pid = process.pid
            p = psutil.Process(pid)
            p.nice(psutil.HIGH_PRIORITY_CLASS)
            message = f"Successfully set CPU priority HIGH for process {main_exe_name} with PID {pid}"
            print(message)
            logging.info(message)
            return
    else:
        error_message = f"Unable to set CPU priority on {main_exe_name} process!"
        print(error_message)
        logging.error(error_message)

def main():
    print_green_message(welcome_screen)
    print_separator()
    wait_duration, main_exe_name, launcher_exe_name, start_app, mode = read_configuration()
    configure_logging()
    if start_app is 1:
        try:
            subprocess.Popen(launcher_exe_name, shell=True)
            message = f"{launcher_exe_name} process launched successfully."
            print(message)
            logging.info(message)
        except Exception as e:
            message1 = f"Error launching {launcher_exe_name} process: {e}"
            print(message1)
            logging.error(message1)
            return
    track_progress_sleep(wait_duration)
    if mode is 1:
        message2 = f"Setting up {main_exe_name} in mode {mode}: -- priority only mode"
        print(message2)
        logging.info(message2)
        set_cpu_priority(main_exe_name)
    elif mode is 2:
        message3 = f"Setting up {main_exe_name} in mode {mode}: -- affinity & priority mode"
        print(message3)
        logging.info(message3)
        set_cpu_priority(main_exe_name)
        set_cpu_affinity(main_exe_name)
    elif mode is 0:
        message3 = f"Setting up {main_exe_name} in mode {mode}: -- affinity & priority mode disabled"
        print(message3)
        logging.info(message3)
    print_separator()

if __name__ == "__main__":
    main()