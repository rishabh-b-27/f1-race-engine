from sklearn.calibration import CalibratedClassifierCV

from src.models.baseline import create_baseline_model


def create_calibrated_model():

    base_model = create_baseline_model()

    model = CalibratedClassifierCV(
        base_model,
        method="sigmoid",
        cv=3
    )

    return model
