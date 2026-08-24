import pandas as pd


def add_driver_ratings(laps, ratings):

    result = laps.merge(
        ratings[
            [
                "Driver",
                "OverallElo",
                "DryElo",
                "WetDelta"
            ]
        ],
        on="Driver",
        how="left"
    )

    return result


