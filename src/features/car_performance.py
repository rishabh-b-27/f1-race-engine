"""
car_performance.py

Purpose:
    Estimate relative constructor performance during a race.

Method:
    Divide the race into 10-lap windows and compare each team's
    mean lap time against the fastest team in that window.

Output:
    CarPerformanceDelta for each team and lap window.

Note:
    This is an observed relative-pace measure, not a pure measure
    of car performance. Lap time is also affected by tyres,
    traffic, fuel load, weather, driver performance, and strategy.
"""

import pandas as pd


def calculate_car_performance(laps, min_history=10):

    laps = laps.copy()

    # Convert lap time to seconds
    laps["LapTimeSeconds"] = (
        laps["LapTime"].dt.total_seconds()
    )

    # Work in chronological order
    laps = laps.sort_values(
        ["LapNumber", "Driver"]
    ).copy()

    # Cumulative state for each driver
    driver_sum = {}
    driver_count = {}

    results = []

    for lap_number in sorted(laps["LapNumber"].dropna().unique()):

        current_lap = laps[
            laps["LapNumber"] == lap_number
        ]

        # ---------------------------------------------------------
        # 1. Calculate team pace using ONLY previous laps
        # ---------------------------------------------------------

        team_paces = {}

        for team in current_lap["Team"].dropna().unique():

            team_drivers = current_lap[
                current_lap["Team"] == team
            ]["Driver"].dropna().unique()

            active_driver_paces = []

            for driver in team_drivers:

                if (
                    driver in driver_sum
                    and driver in driver_count
                    and driver_count[driver] > 0
                ):
                    active_driver_paces.append(
                        driver_sum[driver]
                        / driver_count[driver]
                    )

            if not active_driver_paces:
                continue

            # Normal case:
            # both drivers have accumulated data.
            #
            # DNF case:
            # only one driver remains -> use that driver's pace.
            #
            # If both remain, average their cumulative means.
            team_paces[team] = (
                sum(active_driver_paces)
                / len(active_driver_paces)
            )

        # ---------------------------------------------------------
        # 2. Require at least min_history laps of history
        # ---------------------------------------------------------

        if lap_number > min_history and team_paces:

            fastest_team_time = min(
                team_paces.values()
            )

            for team, mean_lap_time in team_paces.items():

                performance_delta = (
                    (mean_lap_time - fastest_team_time)
                    / fastest_team_time
                )

                results.append(
                    {
                        "LapNumber": lap_number,
                        "Team": team,
                        "MeanLapTime": mean_lap_time,
                        "CarPerformanceDelta": performance_delta,
                    }
                )

        # ---------------------------------------------------------
        # 3. AFTER calculating the feature,
        #    add the CURRENT lap to history.
        #
        #    This prevents future leakage.
        # ---------------------------------------------------------

        for _, row in current_lap.iterrows():

            driver = row["Driver"]
            lap_time = row["LapTimeSeconds"]

            if pd.isna(lap_time):
                continue

            if driver not in driver_sum:
                driver_sum[driver] = 0.0
                driver_count[driver] = 0

            driver_sum[driver] += lap_time
            driver_count[driver] += 1

    return pd.DataFrame(results)