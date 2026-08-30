import fastf1


def load_race(year, grand_prix):
    session = fastf1.get_session(year, grand_prix, "R")
    session.load()  #It retrieves/processes the relevant race data and makes it accessible through the session object.

    return session 
