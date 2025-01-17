import os.path
from datetime import datetime

__run_dir = None


def new_run_dir(root: str):
    os.makedirs(root, exist_ok=True)

    global __run_dir

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    __run_dir = os.path.join(root, timestamp)

    os.makedirs(__run_dir)

    return __run_dir


def get_run_dir():
    return __run_dir
