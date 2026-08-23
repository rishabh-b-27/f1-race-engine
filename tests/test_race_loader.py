from src.data.race_loader import load_race


session = load_race(2025, "British Grand Prix")

print("Race:", session.event.EventName)
print("Laps:", session.laps.shape)
print("Weather:", session.weather_data.shape)
print("Race Control:", session.race_control_messages.shape)