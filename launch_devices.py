import inspect
import os
import subprocess
import sys
import glob
from pathlib import Path
from typing import List

if __name__ == "__main__":
    mode = sys.argv[0]

    processes: List[subprocess.Popen] = []

    if mode == "mdp":
        list_devices = glob.glob(f"actors_api/device_descriptions/[!template]*.json")
        for configuration_path in list_devices:
            process = subprocess.Popen([sys.executable, "run-service_mdp.py", "--spec", str(configuration_path)])
            processes.append(process)

        for process in processes:
            process.wait()
    elif mode == "plan":
        list_devices = glob.glob(f"actors_api/device_descriptions/[!template]*.json")
        for configuration_path in list_devices:
            process = subprocess.Popen([sys.executable, "run-service_plan.py", "--spec", str(configuration_path)])
            processes.append(process)

        for process in processes:
            process.wait()
    else:
        print("Unknown mode: {}, insert mdp or plan".format(mode))
