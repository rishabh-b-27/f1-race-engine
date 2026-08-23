from src.data.race_loader import load_race
from src.data.prepare_laps import prepare_laps
from src.features.race_state import create_race_state


session = load_race(2025, "British Grand Prix")

laps = prepare_laps(session)

laps = create_race_state(laps)


print("\n=== RACE STATE ===")

print(
    laps[
        [
            "LapNumber",
            "TrackStatus",
            "RaceState"
        ]
    ]
    .drop_duplicates()
    .to_string(index=False)
)