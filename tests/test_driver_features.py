from src.data.race_loader import load_race
from src.data.prepare_laps import prepare_laps
from src.data.driver_ratings import load_driver_ratings
from src.features.driver_features import add_driver_ratings


session = load_race(2025, "British Grand Prix")

laps = prepare_laps(session)

ratings = load_driver_ratings()

laps_with_ratings = add_driver_ratings(laps, ratings)


print("\n=== LAPS WITH DRIVER RATINGS ===")

print(
    laps_with_ratings[
        [
            "Driver",
            "Team",
            "LapNumber",
            "LapTime",
            "OverallElo",
            "DryElo",
            "WetDelta"
        ]
    ]
    .head(20)
    .to_string(index=False)
)

print("\n=== DRIVER RATING CHECK ===")

print(
    laps_with_ratings[
        [
            "Driver",
            "OverallElo",
            "DryElo",
            "WetDelta"
        ]
    ]
    .drop_duplicates()
    .sort_values("OverallElo", ascending=False)
    .to_string(index=False)
)

print("\n=== MISSING DRIVER RATINGS ===")

print(
    laps_with_ratings[
        laps_with_ratings["OverallElo"].isna()
    ]["Driver"].unique()
)