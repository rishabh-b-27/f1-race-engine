from src.data.race_loader import load_race
from src.data.prepare_laps import prepare_laps
from src.features.build_features import build_features


session = load_race(2025, "British Grand Prix")

laps = prepare_laps(session)

features = build_features(session, laps)

print("\n=== FINAL FEATURE DATASET ===")
print(features.columns.tolist())

print("\n=== SHAPE ===")
print(features.shape)

print("\n=== SAMPLE ===")
print(
    features[
        [
            "Driver",
            "Team",
            "LapNumber",
            "Position",
            "TimestampGapToLeader",
            "TimestampGapToAhead",
            "Compound",
            "TyreLife",
            "CarPerformanceDelta",
            "OverallElo",
            "DryElo",
            "WetDelta",
        ]
    ]
    .head(20)
    .to_string(index=False)
)

print("\n=== DUPLICATE DRIVER/LAP CHECK ===")
duplicates = features.duplicated(
    subset=["Driver", "LapNumber"]
).sum()

print("Duplicate driver/lap rows:", duplicates)
