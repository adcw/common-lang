import os
import random

import numpy as np

from src.session.datacls import Config


def prepare_data(cf: Config):
    for modality_path in cf.modality_paths:
        modality_path = os.path.abspath(modality_path)

        subject_paths = os.listdir(modality_path)
        n_subjects = len(subject_paths)
        chosen_subjects_indices = random.sample([i for i in range(n_subjects)], int(n_subjects * cf.splits.present_perc))

        pass

    pass
