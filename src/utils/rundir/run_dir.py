import os.path
from datetime import datetime


run_dir = None


def new_run_dir(root: str):
    if not os.path.exists(root):
        raise OSError(f"Directory {root} does not exist.")

    global run_dir

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    run_dir = os.path.join(root, timestamp)

    os.makedirs(run_dir)

    return run_dir


def get_run_dir():
    return run_dir