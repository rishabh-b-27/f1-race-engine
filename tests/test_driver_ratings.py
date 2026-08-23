from src.data.driver_ratings import load_driver_ratings


ratings = load_driver_ratings()

print("\n=== DRIVER RATINGS ===")

print(ratings.to_string(index=False))

print("\n=== TOP 5 ===")

print(
    ratings
    .sort_values("OverallElo", ascending=False)
    .head(5)
    .to_string(index=False)
)