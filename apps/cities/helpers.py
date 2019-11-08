import pandas as pd
from settings import *


def get_big_cities(length):
    df = pd.read_csv(
        CITIES_FILE,
        low_memory=False,
        usecols=[
            "ville_nom",
            "ville_population_2010",
            "ville_code_commune",
            "ville_longitude_deg",
            "ville_latitude_deg",
        ],
    )
    cities = df.sort_values(by="ville_population_2010", ascending=False).head(length)
    return cities
