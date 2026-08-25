import pandas as pd

from src.data.prepare_laps import prepare_laps
from src.features.build_features import build_features
from src.features.target import add_position_target


def build_training_data(session):

    # Prepare raw lap data
    laps = prepare_laps(session)

    # Build features using information available
    # at each point in the race.
    features = build_features(
        session,
        laps
    )

    # Add the 10-lap future target.
    data = add_position_target(
        features,
        session,
        horizon=10,
        top_n=8
    )

    return data