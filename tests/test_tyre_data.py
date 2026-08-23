from src.data.race_loader import load_race
from src.data.prepare_laps import prepare_laps


session = load_race(2025, "British Grand Prix")

laps = prepare_laps(session)


print("\n=== DRIVER CODES ===")
print(laps["Driver"].unique())


print("\n=== TYRE DATA ===")

print(
    laps[
        [
            "Driver",
            "Team",
            "LapNumber",
            "Compound",
            "TyreLife",
            "Stint",
            "LapTime"
        ]
    ]
    .head(50)
    .to_string(index=False)
)


print("\n=== VERSTAPPEN STINTS ===")

verstappen = laps[laps["Driver"] == "VER"]

print(
    verstappen[
        [
            "LapNumber",
            "Compound",
            "TyreLife",
            "Stint",
            "LapTime"
        ]
    ]
    .head(52)
    .to_string(index=False)
)

print("\n=== ALL DRIVER STINTS ===")

print(
    laps
    .groupby(["Driver", "Stint", "Compound"])
    .agg(
        StartLap=("LapNumber", "min"),
        EndLap=("LapNumber", "max"),
        MaxTyreAge=("TyreLife", "max")
    )
    .to_string()
)