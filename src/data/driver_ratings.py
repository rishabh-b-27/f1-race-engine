import pandas as pd


def load_driver_ratings(path="data/raw/driver_ratings.csv"):
    ratings = pd.read_csv(path)

    return ratings