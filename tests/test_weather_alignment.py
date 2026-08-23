from src.data.race_loader import load_race
from src.data.prepare_laps import prepare_laps
from src.features.weather import get_weather_data
from src.features.weather_alignment import align_weather_to_laps


session = load_race(2025, "British Grand Prix")

laps = prepare_laps(session)

weather = get_weather_data(session)

laps_with_weather = align_weather_to_laps(
    laps,
    weather
)


print("\n=== LAPS WITH WEATHER ===")

print(
    laps_with_weather[
        [
            "Driver",
            "LapNumber",
            "Time",
            "Rainfall",
            "TrackTemp",
            "AirTemp",
            "Humidity"
        ]
    ]
    .head(20)
    .to_string(index=False)
)