import os
import random
import shutil
from tqdm import tqdm

from src.session.datacls import Config
from src.utils.rundir.run_dir import get_run_dir


def prepare_data(cf: Config):
    """
    Prepare data by copying selected subjects from modality paths to the run directory.

    Args:
        cf (Config): Configuration object containing modality paths and split settings.
    """
    run_dir = get_run_dir()
    total_subjects = sum(len(os.listdir(os.path.abspath(modality_path))) for modality_path in cf.modality_paths)
    n_modalities = len(cf.modality_paths)

    with tqdm(total=int(total_subjects * cf.splits.preserve_perc), desc="Copying subjects with preserved modalities", unit="subject") as pgbar:
        for modality_index, modality_path in enumerate(cf.modality_paths):
            modality_dirname = os.path.basename(modality_path)
            modality_path = os.path.abspath(modality_path)

            subject_dirnames = os.listdir(modality_path)
            n_subjects = len(subject_dirnames)

            subjects_with_preserved_modalities = random.sample(
                range(n_subjects),
                int(n_subjects * cf.splits.preserve_perc),
            )

            for i, subject_dirname in enumerate(subject_dirnames):
                source_dir = os.path.join(modality_path, subject_dirname)
                pgbar.set_postfix({"copying": source_dir})

                if i in subjects_with_preserved_modalities:
                    # Preserve all modalities
                    destination_dir = os.path.join(run_dir, modality_dirname, subject_dirname)

                    shutil.copytree(source_dir, destination_dir, dirs_exist_ok=True)
                pgbar.update(1)

    # with tqdm(total=int(total_subjects*(1-cf.splits.preserve_perc)), desc="Copying subjects with dropped modalities"):
