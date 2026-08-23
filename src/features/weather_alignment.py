import pandas as pd


def align_weather_to_laps(laps, weather):

    laps = laps.copy()
    weather = weather.copy()

    laps["Time"] = pd.to_timedelta(laps["Time"])
    weather["Time"] = pd.to_timedelta(weather["Time"])

    weather = weather.sort_values("Time")
    laps = laps.sort_values("Time")

    result = pd.merge_asof(
        laps,
        weather,
        on="Time",
        direction="backward"
    )

    return result