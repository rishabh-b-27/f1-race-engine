from src.data.race_loader import load_race
from src.data.prepare_laps import prepare_laps
from src.features.race_gaps import add_race_gaps


session = load_race(2025, "British Grand Prix")

laps = prepare_laps(session)

laps = add_race_gaps(laps)


print("\n=== RACE GAPS ===")

print(
    laps[
        [
            "Driver",
            "LapNumber",
            "Position",
            "GapToLeader",
            "GapToAhead"
        ]
    ]
    .head(30)
    .to_string(index=False)
)

print("\n=== RACE GAPS: LAP 1 ===")

print(
    laps[laps["LapNumber"] == 1][
        [
            "Driver",
            "LapNumber",
            "Position",
            "GapToLeader",
            "GapToAhead"
        ]
    ]
    .sort_values("Position")
    .to_string(index=False)
)


print("\n=== RACE GAPS: LAP 20 ===")

print(
    laps[laps["LapNumber"] == 20][
        [
            "Driver",
            "LapNumber",
            "Position",
            "GapToLeader",
            "GapToAhead"
        ]
    ]
    .sort_values("Position")
    .to_string(index=False)
)