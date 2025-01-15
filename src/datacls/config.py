from dataclasses import dataclass


@dataclass
class ConfigModel:
    data_path: str
    output_path: str
