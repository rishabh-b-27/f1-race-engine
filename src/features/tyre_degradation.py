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

    results = []

    for (driver, stint), stint_data in clean_laps.groupby(
        ["Driver", "Stint"]
    ):

        stint_data = stint_data.sort_values("TyreLife")

        tyre_life_values = stint_data["TyreLife"].to_numpy()
        lap_time_values = stint_data["LapTimeSeconds"].to_numpy()

        for i in range(len(stint_data)):

            if i < 2:
                continue

            x = tyre_life_values[:i + 1]
            y = lap_time_values[:i + 1]

            degradation_rate = np.polyfit(x, y, 1)[0]

            results.append(
                {
                    "Driver": driver,
                    "Stint": stint,
                    "TyreLife": tyre_life_values[i],
                    "DegradationRate": degradation_rate,
                }
            )

    return pd.DataFrame(results)