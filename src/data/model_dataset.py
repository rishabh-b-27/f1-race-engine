import pandas as pd

from src.data.build_training_data import build_training_data


CATEGORICAL_COLUMNS = [
    "Driver",
    "Team",
    "Compound",
    "TrackStatus",
    "RaceState",
    "Rainfall",
]


DROP_COLUMNS = [
    "FuturePosition",
    "PositionTarget10",
    "Time",
    "LapStartTime",
    "LapStartDate",
    "PitInTime",
    "PitOutTime",
    "IsPersonalBest",
    "Deleted",
    "DeletedReason",
    "FastF1Generated",
    "IsAccurate",
]


TIME_COLUMNS = [
    "LapTime",
    "Sector1Time",
    "Sector2Time",
    "Sector3Time",
]


def build_model_dataset(session):

    data = build_training_data(session)

    data = data[
        data["PositionTarget10"].notna()
    ].copy()

    y = data["PositionTarget10"].astype(int)

    X = data.drop(
        columns=DROP_COLUMNS,
        errors="ignore"
    ).copy()

    X = X.drop(
        columns=["DriverNumber"],
        errors="ignore"
    )

    for column in TIME_COLUMNS:
        if column in X.columns:
            X[column] = X[column].dt.total_seconds()

    if "FreshTyre" in X.columns:
        X["FreshTyre"] = X["FreshTyre"].astype(str)

    X = pd.get_dummies(
        X,
        columns=CATEGORICAL_COLUMNS + ["FreshTyre"],
        dummy_na=True,
        dtype=int
    )

    # Remove duplicate feature names.
    X = X.loc[:, ~X.columns.duplicated()].copy()

    return X, y
