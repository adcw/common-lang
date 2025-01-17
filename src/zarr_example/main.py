import numpy as np
import zarr

# import torch
# import cProfile
# import tempfile

def main():
    num_cases = 1000
    tensor_shape = (10, 3)

    dataset = zarr.create_array(
        store="D:\Projekty\common-lang\datasets\zarr",
        name="acc",
        shape=(num_cases, *tensor_shape),
        chunks=(100, *tensor_shape),
        dtype=np.float32,
    )

    for i in range(num_cases):
        tensor = np.random.rand(*tensor_shape).astype(np.float32)
        dataset[i] = tensor

    pass


if __name__ == '__main__':
    # with cProfile.Profile() as profile:
    main()

    # stats = pstats.Stats(profile)
    # stats.sort_stats(pstats.SortKey.TIME)
    # stats.print_stats()
