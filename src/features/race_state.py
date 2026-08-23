def create_race_state(laps):

    laps = laps.copy()

    laps["RaceState"] = "GREEN"

    laps.loc[
        laps["TrackStatus"].astype(str).str.contains("2"),
        "RaceState"
    ] = "YELLOW"

    laps.loc[
        laps["TrackStatus"].astype(str).str.contains("6"),
        "RaceState"
    ] = "VSC"

    laps.loc[
        laps["TrackStatus"].astype(str).str.contains("4"),
        "RaceState"
    ] = "SC"

    return laps