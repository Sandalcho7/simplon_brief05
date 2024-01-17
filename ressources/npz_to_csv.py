import numpy as np
import pandas as pd

# Path definition
npz_path = r""
csv_path = r""

# Conversion
arrays = dict(np.load(npz_path))
data = {k: [s.decode("utf-8") for s in v.tobytes().split(b"\x00")] if v.dtype == np.uint8 else v for k, v in arrays.items()}
transactions = pd.DataFrame.from_dict(data)

transactions.to_csv(csv_path, header=True)