from src.data.race_loader import load_race
from src.data.prepare_laps import prepare_laps
from src.features.target import add_position_target


session = load_race(2025, "British Grand Prix")

laps = prepare_laps(session)

laps = add_position_target(
    laps,
    session,
    horizon=10,
    top_n=8
)

print("\n=== TARGET SAMPLE ===")

print(
    laps[
        [
            "Driver",
            "LapNumber",
            "Position",
            "FuturePosition",
            "PositionTarget10"
        ]
    ]
    .sort_values(["Driver", "LapNumber"])
    .head(50)
    .to_string(index=False)
)

print("\n=== TARGET DISTRIBUTION ===")

print(
    laps["PositionTarget10"]
    .value_counts(dropna=False)
    .sort_index()
)

print("\n=== DNF CHECK ===")

print(
    laps[
        laps["Driver"].isin(
            ["ANT", "HAD", "BOR", "LAW"]
        )
    ][
        [
            "Driver",
            "LapNumber",
            "Position",
            "FuturePosition",
            "PositionTarget10"
        ]
    ]
    .head(100)
    .to_string(index=False)
)
