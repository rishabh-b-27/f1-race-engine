from src.data.race_loader import load_race
from src.data.prepare_laps import prepare_laps
from src.features.tyre_degradation import calculate_tyre_degradation


session = load_race(2025, "British Grand Prix")

laps = prepare_laps(session)

degradation = calculate_tyre_degradation(laps)

print(degradation.to_string(index=False))