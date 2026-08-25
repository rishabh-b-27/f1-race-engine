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

    laps["TimestampGapToLeader"] = np.nan
    laps["TimestampGapToAhead"] = np.nan

    for _, lap_data in laps.groupby("LapNumber"):

        valid = (
            lap_data
            .dropna(subset=["Position", "Time"])
            .sort_values("Position")
        )

        if valid.empty:
            continue

        leader_time = valid.iloc[0]["Time"]

        for index, row in valid.iterrows():

            current_time = row["Time"]

            laps.loc[index, "TimestampGapToLeader"] = (
                current_time - leader_time
            ).total_seconds()

            if row["Position"] == 1:
                laps.loc[index, "TimestampGapToAhead"] = 0.0
                continue

            ahead = valid[
                valid["Position"] == row["Position"] - 1
            ]

            if not ahead.empty:

                ahead_time = ahead.iloc[0]["Time"]

                laps.loc[index, "TimestampGapToAhead"] = (
                    current_time - ahead_time
                ).total_seconds()

    return laps