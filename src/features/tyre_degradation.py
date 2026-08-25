import numpy as np
import pandas as pd


def calculate_tyre_degradation(laps):

    clean_laps = laps[
        laps["LapTime"].notna()
        & laps["TyreLife"].notna()
        & laps["Stint"].notna()
    ].copy()

    clean_laps["LapTimeSeconds"] = (
        clean_laps["LapTime"].dt.total_seconds()
    )

    degradation = []

    for (driver, stint), stint_data in clean_laps.groupby(
        ["Driver", "Stint"]
    ):

        stint_data = stint_data.sort_values("TyreLife")

        if len(stint_data) < 2:
            continue

        x = stint_data["TyreLife"].to_numpy()
        y = stint_data["LapTimeSeconds"].to_numpy()

        degradation_rate = np.polyfit(x, y, 1)[0]

        degradation.append(
            {
                "Driver": driver,
                "Stint": stint,
                "Compound": stint_data["Compound"].iloc[0],
                "DegradationRate": degradation_rate,
            }
        )

    return pd.DataFrame(degradation)