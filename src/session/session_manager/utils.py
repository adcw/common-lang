import os

import inquirer

from src.session.datacls import Config
from src.session.datacls.modes import MODE


def query_mode() -> MODE:
    questions = [
        inquirer.List(
            "mode",
            message="Select mode",
            choices=[MODE.PREPARE_DATA.value, MODE.TRAIN.value],
        )
    ]

    answers = inquirer.prompt(questions)

    if not answers:
        raise ValueError("No action selected")

    return MODE.from_value(answers["mode"])


def validate_config(config: Config):
    """
    Validate the configuration to ensure required paths exist.

    Raises:
        FileNotFoundError: If the datasets path does not exist.
        FileNotFoundError: If the output path does not exist.
    """
    for path in config.dataset_paths:
        if not os.path.exists(path):
            raise FileNotFoundError(f"The datasets path is invalid: {config.dataset_paths}")

    if not os.path.exists(config.runs_path):
        raise FileNotFoundError(f"The output path does not exist: {config.runs_path}")
