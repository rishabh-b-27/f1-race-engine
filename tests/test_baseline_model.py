from src.data.race_loader import load_race
from src.data.model_dataset import build_model_dataset
from src.models.baseline import create_baseline_model


session = load_race(
    2025,
    "British Grand Prix"
)

X, y = build_model_dataset(
    session
)

model = create_baseline_model()

model.fit(
    X,
    y
)

print("\n=== BASELINE MODEL ===")

print("Samples:", len(X))
print("Features:", X.shape[1])
print("Classes:", model.classes_)

print("\n=== PROBABILITY CHECK ===")

probabilities = model.predict_proba(
    X.iloc[[0]]
)[0]

for class_id, probability in zip(
    model.classes_,
    probabilities
):
    print(
        f"Class {class_id}: "
        f"{probability:.4f}"
    )

print(
    "\nProbability sum:",
    probabilities.sum()
)
