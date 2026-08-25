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


def calculate_car_performance(laps, window_size=10):

    clean_laps = laps[
        laps["LapTime"].notna()
    ].copy()

    clean_laps["LapTimeSeconds"] = (
        clean_laps["LapTime"].dt.total_seconds()
    )

    results = []

    max_lap = int(clean_laps["LapNumber"].max())

    for start_lap in range(1, max_lap + 1, window_size):

        end_lap = start_lap + window_size - 1

        window = clean_laps[
            (clean_laps["LapNumber"] >= start_lap)
            & (clean_laps["LapNumber"] <= end_lap)
        ].copy()

        team_pace = (
            window
            .groupby("Team")["LapTimeSeconds"]
            .mean()
            .sort_values()
        )

        if team_pace.empty:
            continue

        fastest_team_time = team_pace.iloc[0]

        car_delta = (
            (team_pace - fastest_team_time)
            / fastest_team_time
        )

        window_result = pd.DataFrame({
            "WindowStart": start_lap,
            "WindowEnd": end_lap,
            "Team": team_pace.index,
            "MeanLapTime": team_pace.values,
            "CarPerformanceDelta": car_delta.values
        })

        results.append(window_result)

    if not results:
        return pd.DataFrame(
            columns=[
                "WindowStart",
                "WindowEnd",
                "Team",
                "MeanLapTime",
                "CarPerformanceDelta"
            ]
        )

    return pd.concat(results, ignore_index=True)