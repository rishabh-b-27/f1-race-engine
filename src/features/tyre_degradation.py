import pandas as pd


def calculate_tyre_degradation(laps):

    clean_laps = laps[
        laps["LapTime"].notna()
    ].copy()

    clean_laps["LapTimeSeconds"] = (
        clean_laps["LapTime"].dt.total_seconds()
    )

    degradation = (
        clean_laps
        .groupby(["Compound", "TyreLife"])["LapTimeSeconds"]
        .mean()
        .reset_index()
    )

    return degradation