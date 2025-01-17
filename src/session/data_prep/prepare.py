import numpy as np
import zarr
from tqdm import tqdm

from src.session.datacls import Config
from src.utils.rundir.run_dir import get_run_dir


def prepare_data(cf: Config):
    run_dir = get_run_dir()

    num_cases = 1000
    tensor_shape = (10, 3)

    dataset = zarr.create_array(
        store=run_dir,
        name="acc",
        shape=(num_cases, *tensor_shape),
        chunks=(100, *tensor_shape),
        dtype=np.float32,
    )

    for i in tqdm(range(num_cases), desc="Writing to store"):
        tensor = np.random.rand(*tensor_shape).astype(np.float32)
        dataset[i] = tensor
