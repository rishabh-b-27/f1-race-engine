from sklearn.metrics import log_loss, accuracy_score


def evaluate_model(model, X_test, y_test):

    probabilities = model.predict_proba(X_test)
    predictions = model.predict(X_test)

    results = {
        "LogLoss": log_loss(
            y_test,
            probabilities,
            labels=model.classes_
        ),
        "Accuracy": accuracy_score(
            y_test,
            predictions
        )
    }

    return results
