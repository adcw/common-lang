from dataclasses import dataclass
from typing import List


class SplitsCfg:
    present_perc: float = 0.4
    max_modalities_to_drop: int = 1
    modality_drop_perc: float = 0.2


@dataclass
class Config:
    dataset_paths: List[str]
    splits: SplitsCfg
    runs_path: str
