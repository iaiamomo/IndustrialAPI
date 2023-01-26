import inspect
import os
import subprocess
import sys
import glob
from pathlib import Path
from typing import List

if __name__ == "__main__":

    processes: List[subprocess.Popen] = []
    list_devices = glob.glob(f"actors_api/device_descriptions/[!template]*.json")
    for configuration_path in list_devices:
        process = subprocess.Popen([sys.executable, "run-service.py", "--spec", str(configuration_path)])
        processes.append(process)

    for process in processes:
        process.wait()
