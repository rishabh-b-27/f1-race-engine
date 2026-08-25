from src.data.multi_race_dataset import build_multi_race_dataset


races = [
    (2025, "Bahrain Grand Prix"),
    (2025, "Saudi Arabian Grand Prix"),
    (2025, "British Grand Prix"),
]


X, y = build_multi_race_dataset(races)


print("\n=== MULTI-RACE DATASET ===")

print("Samples:", len(X))
print("Features:", X.shape[1])
print("Target samples:", len(y))

print("\n=== TARGET DISTRIBUTION ===")
print(y.value_counts().sort_index())

print("\n=== RACE DISTRIBUTION ===")
print(X["GrandPrix"].value_counts())

print("\n=== YEAR DISTRIBUTION ===")
print(X["RaceYear"].value_counts())
