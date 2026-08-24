"""
race_state.py

Purpose:
    Convert raw FastF1 TrackStatus values into a categorical
    race-state feature.

TrackStatus contains chronological status changes within a lap.

Examples:
    12   -> GREEN -> YELLOW
    14   -> GREEN -> SC
    41   -> SC -> GREEN
    6712 -> VSC -> VSC ending -> GREEN -> YELLOW

The final status is treated as the active race state for that lap.

Race state is a lap-level condition that is attached to
each driver's lap data.
"""


STATUS_MAP = {
    "1": "GREEN",
    "2": "YELLOW",
    "4": "SC",
    "5": "RED",
    "6": "VSC",
    "7": "GREEN"
}


def get_race_state(track_status):

    status = str(track_status)

    if not status:
        return "GREEN"

    last_status = status[-1]

    return STATUS_MAP.get(last_status, "GREEN")


def create_race_state(laps):

    laps = laps.copy()

    laps["RaceState"] = (
        laps["TrackStatus"]
        .apply(get_race_state)
    )

    return laps