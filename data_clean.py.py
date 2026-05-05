import pandas as pd

def load_and_clean_data(file_path):
    df = pd.read_csv(file_path)

    df = df.drop_duplicates()
    df = df.dropna()

    return df