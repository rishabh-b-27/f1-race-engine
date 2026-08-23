def prepare_laps(session):
    laps = session.laps.copy()

    columns = [
        "Driver",
        "Team",
        "LapNumber",
        "Time",
        "LapTime",
        "Position",
        "Compound",
        "TyreLife",
        "Stint",
        "TrackStatus"
    ]

    return laps[columns].copy()