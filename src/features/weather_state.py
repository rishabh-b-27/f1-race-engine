def create_weather_state(weather):

    weather = weather.copy()

    weather["WeatherState"] = "DRY"

    weather.loc[
        weather["Rainfall"] == True,
        "WeatherState"
    ] = "WET"

    return weather