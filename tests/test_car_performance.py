from src.data.race_loader import load_race
from src.data.prepare_laps import prepare_laps
from src.features.car_performance import calculate_car_performance


session = load_race(2025, "British Grand Prix")

laps = prepare_laps(session)

result = calculate_car_performance(laps)

print("Shape:")
print(result.shape)

print("\nFirst 10 rows:")
print(result.head(10))

print("\nWindows:")
print(result["WindowStart"].unique())

print("\nTeams:")
print(result["Team"].unique())

print("\n=== LAPS 1-10 ===")
print(
    result[result["WindowStart"] == 1]
    .sort_values("CarPerformanceDelta")
)

print("\n=== LAPS 11-20 ===")
print(
    result[result["WindowStart"] == 11]
    .sort_values("CarPerformanceDelta")
)

print("\n=== LAPS 21-30 ===")
print(
    result[result["WindowStart"] == 21]
    .sort_values("CarPerformanceDelta")
)

print("\n=== LAPS 31-40 ===")
print(
    result[result["WindowStart"] == 31]
    .sort_values("CarPerformanceDelta")
)

print("\n=== LAPS 41-50 ===")
print(
    result[result["WindowStart"] == 41]
    .sort_values("CarPerformanceDelta")
)

print("\n=== LAPS 51-52 ===")
print(
    result[result["WindowStart"] == 51]
    .sort_values("CarPerformanceDelta")
)