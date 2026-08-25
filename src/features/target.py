import pandas as pd


def add_position_target(laps, session, horizon=10, top_n=8):

    laps = laps.copy()

    laps["LapNumber"] = laps["LapNumber"].astype(int)

    # ---------------------------------------------------------
    # Driver race status
    # ---------------------------------------------------------

    results = session.results[
        [
            "Abbreviation",
            "Status"
        ]
    ].copy()

    results = results.rename(
        columns={
            "Abbreviation": "Driver"
        }
    )

    # Normalize status strings so values such as
    # "Did not start " are handled correctly.
    status_map = {
        driver: str(status).strip()
        for driver, status in zip(
            results["Driver"],
            results["Status"]
        )
    }

    # ---------------------------------------------------------
    # Position at t + horizon
    # ---------------------------------------------------------

    future_positions = laps[
        [
            "Driver",
            "LapNumber",
            "Position"
        ]
    ].copy()

    future_positions["TargetLap"] = (
        future_positions["LapNumber"] - horizon
    )

    future_positions = future_positions.rename(
        columns={
            "Position": "FuturePosition"
        }
    )

    laps = laps.merge(
        future_positions[
            [
                "Driver",
                "TargetLap",
                "FuturePosition"
            ]
        ],
        left_on=["Driver", "LapNumber"],
        right_on=["Driver", "TargetLap"],
        how="left"
    )

    laps = laps.drop(
        columns=["TargetLap"]
    )

    # ---------------------------------------------------------
    # Generate target
    #
    # 1-8  = P1-P8
    # 9    = P9+
    # 10   = DNF
    # NaN  = no valid training target
    # ---------------------------------------------------------

    targets = []

    for _, row in laps.iterrows():

        driver = row["Driver"]
        future_position = row["FuturePosition"]

        status = status_map.get(driver)

        # DNS is not a prediction sample.
        if status == "Did not start":
            targets.append(float("nan"))
            continue

        # If the driver has a valid position at t+10,
        # that position is the target.
        if pd.notna(future_position):

            if future_position <= top_n:
                targets.append(int(future_position))
            else:
                targets.append(top_n + 1)

            continue

        # No position exists at t+10.
        #
        # If the driver retired, the target is DNF.
        if status == "Retired":
            targets.append(top_n + 2)
            continue

        # No usable future target.
        targets.append(float("nan"))

    laps["PositionTarget10"] = targets

    return laps
