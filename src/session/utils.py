import os

import inquirer

from src.datacls import ConfigModel


def query_action():
    questions = [
        inquirer.List(
            "action",
            message="Select an option to proceed",
            choices=["Train", "Test", "Exit"],
        )
    ]

    answers = inquirer.prompt(questions)

    if not answers:
        raise ValueError("No action selected")

    return answers["action"].lower()


def validate_config(config: ConfigModel):
    """
    Validate the configuration to ensure required paths exist.

    Raises:
        FileNotFoundError: If the data path does not exist.
        FileNotFoundError: If the output path does not exist.
    """
    if not os.path.exists(config.data_path):
        raise FileNotFoundError(f"The data path is invalid: {config.data_path}")

    if not os.path.exists(config.output_path):
        raise FileNotFoundError(f"The output path does not exist: {config.output_path}")
