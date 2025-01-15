from dataclasses import asdict, is_dataclass, fields
from typing import Type, TypeVar
import yaml

T = TypeVar("T")

def _dict_to_dataclass(data: dict, cls: Type[T]) -> T:
    """
    Convert a dictionary to a dataclass instance.

    Args:
        data (dict): The dictionary containing the data.
        cls (Type[T]): The dataclass type to convert the dictionary to.

    Returns:
        T: An instance of the specified dataclass type.

    Raises:
        TypeError: If the provided class is not a dataclass.
    """
    if not is_dataclass(cls):
        raise TypeError(f"{cls} is not a dataclass")

    init_args = {}
    for field in fields(cls):
        field_name = field.name
        field_type = field.type
        value = data.get(field_name)

        # Recursive handling for nested datacls
        if is_dataclass(field_type) and isinstance(value, dict):
            init_args[field_name] = _dict_to_dataclass(value, field_type)
        else:
            init_args[field_name] = value

    return cls(**init_args)

def load_config(file_path: str, cls: Type[T]) -> T:
    """
    Load a YAML configuration file and parse it into a dataclass instance.

    Args:
        file_path (str): Path to the YAML configuration file.
        cls (Type[T]): The dataclass type to parse the configuration into.

    Returns:
        T: An instance of the specified dataclass type.
    """
    with open(file_path, "r") as f:
        data = yaml.safe_load(f)
    return _dict_to_dataclass(data, cls)

def save_config(config: T, file_path: str):
    """
    Save a dataclass instance to a YAML configuration file.

    Args:
        config (T): The dataclass instance to save.
        file_path (str): Path to the output YAML configuration file.
    """
    with open(file_path, "w") as f:
        yaml.dump(asdict(config), f)
