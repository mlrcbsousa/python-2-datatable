
import pandas as pd


def load(path: str) -> pd.DataFrame:
    '''Load CSV file into a pandas DataFrame'''

    try:
        assert isinstance(path, str), "Path has to be a string"
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return

    try:
        df = pd.read_csv(path)
    except Exception as e:
        print(f"Error: {e}")
        return

    print(f"Loading dataset of dimensions {df.shape}")
    return df
