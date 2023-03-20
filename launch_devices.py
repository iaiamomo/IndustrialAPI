import subprocess
import sys
import glob
from typing import List
import json


config_json = json.load(open('config.json', 'r'))
mode = config_json['mode']
phase = config_json['phase']


if __name__ == "__main__":

    processes: List[subprocess.Popen] = []
    
    list_devices = glob.glob(f"actors_api_{mode}/descriptions_phase{phase}/*.json")
    for configuration_path in list_devices:
        script = f"run_target_{mode}.py" if "target" in configuration_path else f"run_service_{mode}.py"
        process = subprocess.Popen([sys.executable, script, configuration_path])
        processes.append(process)

    for process in processes:
        process.wait()
