from src.datacls import ConfigModel
from src.session.utils import query_action, validate_config
from src.utils.yaml import load_config


class SessionManager:
    DEFAULT_CONFIG_FILEPATH = "config.yaml"

    def __init__(self, config_filepath: str = DEFAULT_CONFIG_FILEPATH):
        """
        Initialize the session manager with a configuration file.

        Args:
            config_filepath (str): Path to the configuration file.
        """
        config = load_config(config_filepath, ConfigModel)
        validate_config(config)
        self.config = config

    def start(self):
        """
        Start the session by querying the user for an action.

        Raises:
            NotImplementedError: If the selected option is not implemented.
        """

        action = query_action()

        if action == "train":
            self.train()
        elif action == "test":
            self.test()
        elif action == "exit":
            print("Exiting the application.")
        else:
            raise NotImplementedError(f"The action '{action}' is not implemented.")

    def train(self):
        """
        Placeholder method for the training action.
        """
        print("Training process started...")

    def test(self):
        """
        Placeholder method for the testing action.
        """
        print("Testing process started...")
