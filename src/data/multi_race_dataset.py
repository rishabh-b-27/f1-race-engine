


import pandas as pd


from src.data.race_loader import load_race
from src.data.model_dataset import build_model_dataset


def build_multi_race_dataset(races):

    datasets = []

    for year, grand_prix in races:

        print(
            f"Loading {year} {grand_prix}..."
        )

        session = load_race(
            year,
            grand_prix
        )

        X, y = build_model_dataset(
            session
        )

        X = X.copy()
        X["RaceYear"] = year
        X["GrandPrix"] = grand_prix

        datasets.append(
            (X, y)
        )

    if not datasets:
        raise ValueError(
            "No races were provided."
        )

    X = pd.concat(
        [item[0] for item in datasets],
        ignore_index=True
    )

    y = pd.concat(
        [item[1] for item in datasets],
        ignore_index=True
    )

    return X, y
