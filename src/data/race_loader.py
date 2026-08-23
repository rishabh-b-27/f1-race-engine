import fastf1


def load_race(year, grand_prix):
    session = fastf1.get_session(year, grand_prix, "R")
    session.load()

    return session 