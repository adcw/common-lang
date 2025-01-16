from src.session.datacls import Config
from src.session.datacls.mode import MODE
from src.session.session_manager.utils import query_mode, validate_config
from src.utils.yaml import load_config


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
            self.train()
        elif mode == MODE.PREPARE_DATA:
            self.prepare_data()
        elif mode == MODE.EXIT:
            print("Exiting the application.")
        else:
            raise NotImplementedError(f"The mode '{mode}' is not implemented.")

    def train(self):
        """
        Placeholder method for the training action.
        """
        print("Training process started...")

    def prepare_data(self):
        """
        Placeholder method for preparing data.
        """
        print("Preparing data started...")
