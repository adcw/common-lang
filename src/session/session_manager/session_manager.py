import os.path

from src.session.datacls import Config
from src.session.datacls.mode import MODE
from src.session.session_manager.utils import query_mode, validate_config

from src.utils.rundir import new_run_dir
from src.utils.yaml import load_config
from src.session.zarr import generate_zarr_dataset


class SessionManager:
    DEFAULT_CONFIG_FILEPATH = "config.yaml"

    def __init__(self, config_filepath: str = DEFAULT_CONFIG_FILEPATH):
        """
        Initialize the session manager with a configuration file.

        Args:
            config_filepath (str): Path to the configuration file.
        """
        config = load_config(config_filepath, Config)
        validate_config(config)
        self.config = config

    def start(self):
        """
        Start the session by querying the user for an action.

        Raises:
            NotImplementedError: If the selected option is not implemented.
        """

        mode = query_mode()

        if mode == MODE.TRAIN:
            self.train_helper()
        elif mode == MODE.GENERATE_ZARR:
            self.generate_zarr_helper()
        elif mode == MODE.EXIT:
            print("Exiting the application.")
        else:
            raise NotImplementedError(f"The mode '{mode}' is not implemented.")

    def train_helper(self):
        """
        Placeholder method for the training action.
        """
        print("Training process started...")

    def generate_zarr_helper(self):
        """
        Placeholder method for preparing data.
        """
        new_run_dir(os.path.join(self.config.runs_path, "zarr"))

        print("Generating zarr dataset...")
        generate_zarr_dataset(self.config)
