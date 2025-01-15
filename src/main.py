from src.datacls import ConfigModel
from src.utils.yaml import load_config

if __name__ == '__main__':
    cf = load_config("./config.yaml", ConfigModel)
    print(cf)
