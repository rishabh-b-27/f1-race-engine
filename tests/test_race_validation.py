from src.data.multi_race_dataset import build_multi_race_dataset
from src.models.calibrated import create_calibrated_model
from src.models.validation import evaluate_model


# Chronological 2025 races.
# Each race is tested only after all previous races
# have been used for training.
races = [
    (2025, "Australian Grand Prix"),
    (2025, "Japanese Grand Prix"),
    (2025, "Bahrain Grand Prix"),
    (2025, "Saudi Arabian Grand Prix"),
    (2025, "Miami Grand Prix"),
    (2025, "Emilia Romagna Grand Prix"),
    (2025, "Monaco Grand Prix"),
    (2025, "Spanish Grand Prix"),
    (2025, "Canadian Grand Prix"),
    (2025, "Austrian Grand Prix"),
    (2025, "British Grand Prix"),
]


total_log_loss = 0.0
total_accuracy = 0.0
validation_count = 0


for i in range(2, len(races)):

    train_races = races[:i]
    test_race = [races[i]]

    print(
        f"\n=== VALIDATING ON "
        f"{races[i][1]} ==="
    )

    X_train, y_train = build_multi_race_dataset(
        train_races
    )

    X_test, y_test = build_multi_race_dataset(
        test_race
    )

    # Remove race identifiers.
    X_train = X_train.drop(
        columns=["RaceYear", "GrandPrix"],
        errors="ignore"
    )

    X_test = X_test.drop(
        columns=["RaceYear", "GrandPrix"],
        errors="ignore"
    )

    # Ensure train and test have identical feature columns.
    X_test = X_test.reindex(
        columns=X_train.columns,
        fill_value=0
    )

    # Create calibrated Random Forest.
    model = create_calibrated_model()

    # Train only on races before the test race.
    model.fit(
        X_train,
        y_train
    )

    # Evaluate on completely unseen race.
    results = evaluate_model(
        model,
        X_test,
        y_test
    )

    print(
        "Training races:",
        len(train_races)
    )

    print(
        "Training samples:",
        len(X_train)
    )

    print(
        "Test samples:",
        len(X_test)
    )

    print(
        "Log Loss:",
        results["LogLoss"]
    )

    print(
        "Accuracy:",
        results["Accuracy"]
    )

    total_log_loss += results["LogLoss"]
    total_accuracy += results["Accuracy"]
    validation_count += 1


print("\n=== ROLLING VALIDATION SUMMARY ===")

print(
    "Validation races:",
    validation_count
)

print(
    "Average Log Loss:",
    total_log_loss / validation_count
)

print(
    "Average Accuracy:",
    total_accuracy / validation_count
)
