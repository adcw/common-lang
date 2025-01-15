from src.datacls import ConfigModel
from src.session import SessionManager
from src.utils.yaml import load_config

if __name__ == '__main__':
    sm = SessionManager()
    sm.start()
