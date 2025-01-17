from dataclasses import dataclass
from typing import List


@dataclass
class SplitsCfg:
    preserve_perc: float = 0.4
    max_modalities_to_drop: int = 1
    modality_drop_perc: float = 0.2


@dataclass
class Config:
    modality_paths: List[str]
    modality_names: List[str]

    runs_path: str

    splits: SplitsCfg
