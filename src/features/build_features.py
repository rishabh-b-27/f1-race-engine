from src.data.driver_ratings import load_driver_ratings

from src.features.race_state import create_race_state
from src.features.race_gaps import add_race_gaps
from src.features.tyre_degradation import calculate_tyre_degradation
from src.features.car_performance import calculate_car_performance
from src.features.driver_features import add_driver_ratings
from src.features.weather import get_weather_data
from src.features.weather_alignment import align_weather_to_laps


def build_features(session, laps):

    laps = laps.copy()
    laps["_OriginalRow"] = range(len(laps))

    # Race state
    laps = create_race_state(laps)

    # Live race gaps
    laps = add_race_gaps(laps)

    # Tyre degradation
    tyre_degradation = calculate_tyre_degradation(laps)

    if not tyre_degradation.empty:
        laps = laps.merge(
            tyre_degradation,
            on=["Driver", "Stint", "TyreLife"],
            how="left"
        )

    # Constructor performance
    car_performance = calculate_car_performance(laps)

    if not car_performance.empty:
        laps = laps.merge(
            car_performance[
                [
                    "LapNumber",
                    "Team",
                    "CarPerformanceDelta"
                ]
            ],
            on=["LapNumber", "Team"],
            how="left"
        )

    # Driver ratings
    ratings = load_driver_ratings()

    laps = add_driver_ratings(
        laps,
        ratings
    )

    # Weather
    weather = get_weather_data(session)

    if not weather.empty:
        laps = align_weather_to_laps(
            laps,
            weather
        )

    # Restore original row order
    laps = laps.sort_values("_OriginalRow")

    laps = laps.drop(
        columns="_OriginalRow"
    )

    return laps
