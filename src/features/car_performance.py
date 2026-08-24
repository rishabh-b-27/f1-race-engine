"""
car_performance.py

Purpose:
    Estimate relative constructor performance during a race.

Method:
    Divide the race into 10-lap windows and compare each team's
    mean lap time against the fastest team in that window.

Output:
    CarPerformanceDelta for each team and lap window.

Important limitations:
    Lap time is affected by tyres, traffic, fuel, weather,
    safety cars and driver behaviour.
"""

import pandas as pd


def calculate_car_performance(laps, window_size=10):

    results = []

    max_lap = int(laps["LapNumber"].max())

    for start_lap in range(1, max_lap + 1, window_size):

        end_lap = start_lap + window_size - 1

        window = laps[
            (laps["LapNumber"] >= start_lap) &
            (laps["LapNumber"] <= end_lap)
        ].copy()

        team_pace = (
            window
            .groupby("Team")["LapTime"]
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

    return pd.concat(results, ignore_index=True)