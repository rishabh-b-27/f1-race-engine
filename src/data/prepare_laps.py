def prepare_laps(session):

    laps = session.laps.copy()

    columns = [

        # Driver / team
        "Driver",
        "DriverNumber",
        "Team",

        # Race timing / position
        "LapNumber",
        "Time",
        "LapStartTime",
        "LapStartDate",
        "Position",
        "TrackStatus",

        # Lap performance
        "LapTime",
        "Sector1Time",
        "Sector2Time",
        "Sector3Time",

        # Tyres
        "Compound",
        "TyreLife",
        "FreshTyre",
        "Stint",

        # Pit stops
        "PitInTime",
        "PitOutTime",

        # Speed
        "SpeedI1",
        "SpeedI2",
        "SpeedFL",
        "SpeedST",

        # Data quality
        "IsPersonalBest",
        "Deleted",
        "DeletedReason",
        "FastF1Generated",
        "IsAccurate"
    ]

    return laps[columns].copy()