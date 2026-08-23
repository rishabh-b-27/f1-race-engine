from src.data.race_loader import load_race
from src.features.weather import get_weather_data


session = load_race(2025, "British Grand Prix")

weather = get_weather_data(session)


print("\n=== WEATHER DATA ===")

print(weather.columns)

print(
    weather.head(20).to_string(index=False)
)


print("\n=== RAINFALL EVENTS ===")

print(
    weather[weather["Rainfall"] == True]
    [
        [
            "Time",
            "Rainfall",
            "TrackTemp",
            "AirTemp",
            "Humidity"
        ]
    ]
    .to_string(index=False)
)


print("\n=== WEATHER RANGE ===")

print("Air temperature:")
print(
    weather["AirTemp"].min(),
    "→",
    weather["AirTemp"].max()
)

print("Track temperature:")
print(
    weather["TrackTemp"].min(),
    "→",
    weather["TrackTemp"].max()
)

print("Humidity:")
print(
    weather["Humidity"].min(),
    "→",
    weather["Humidity"].max()
)


print("\n=== RAINFALL COUNT ===")

print(
    weather["Rainfall"]
    .value_counts()
)