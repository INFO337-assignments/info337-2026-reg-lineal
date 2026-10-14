import pandas as pd


def read_mpg_data(path="data/auto-mpg.data"):
    df = pd.read_csv(path,
                     delim_whitespace=True,
                     index_col="car_name",
                     na_values="?",
                     names=[
                         "MPG", "cylinders", "displacement", "horsepower",
                         "weight", "acceleration", "model year", "origin",
                         "car_name"
                     ])
    return df.dropna()