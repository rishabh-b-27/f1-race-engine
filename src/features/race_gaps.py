"""
race_gaps.py

Purpose:
    Calculate live race gaps for each driver.

Features:
    GapToLeader
    GapToAhead

Gaps are calculated separately for each lap using the
cumulative lap completion Time and current Position.

These are timestamp-derived gaps and may differ from
official timing gaps during safety-car periods, pit stops,
or lapped situations.
"""

import numpy as np


def add_race_gaps(laps):

    laps = laps.copy()
    
    laps["GapToLeader"] = np.nan
    laps["GapToAhead"] = np.nan

    for lap_number, lap_data in laps.groupby("LapNumber"):

        valid = lap_data.dropna(subset=["Position", "Time"]).copy()

        valid = valid.sort_values("Position")

        if valid.empty:
            continue

        leader_time = valid.iloc[0]["Time"]

        for index, row in valid.iterrows():

            current_time = row["Time"]

            laps.loc[index, "GapToLeader"] = (
                current_time - leader_time
            ).total_seconds()

            if row["Position"] == 1:
                laps.loc[index, "GapToAhead"] = 0.0

            else:
                position_ahead = row["Position"] - 1

                car_ahead = valid[
                    valid["Position"] == position_ahead
                ]

                if not car_ahead.empty:

                    ahead_time = car_ahead.iloc[0]["Time"]

                    laps.loc[index, "GapToAhead"] = (
                        current_time - ahead_time
                    ).total_seconds()

    return laps