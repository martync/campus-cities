import pandas as pd
from settings import *
from .models import City


def store_cities():
    """Enregistre les villes de France dans la table.
    """
    df = pd.read_csv(
        CITIES_FILE,
        low_memory=False,
        usecols=[
            "ville_nom",
            "ville_population_2012",
            "ville_code_commune",
            "ville_longitude_deg",
            "ville_latitude_deg",
        ],
    ).rename(
        columns={
            "ville_nom": "nom",
            "ville_population_2012": "population_2012",
            "ville_code_commune": "code_commune",
            "ville_longitude_deg": "longitude_deg",
            "ville_latitude_deg": "latitude_deg",
        }
    )
    City.delete().execute()
    City.insert_many(df.to_dict("records")).execute()


def get_big_cities(length=LIMIT_CITIES_NUMBER):
    """
    Retourne les villes les plus grandes de France.

    Args:
        length (int): Nombre de villes souhaité

    Returns:
        pandas.DataFrame

    """
    return (
        pd.DataFrame(list(City.select().dicts()))
        .rename(
            columns={
                "nom": "ville_nom",
                "population_2012": "ville_population_2012",
                "code_commune": "ville_code_commune",
                "longitude_deg": "ville_longitude_deg",
                "latitude_deg": "ville_latitude_deg",
            }
        )
        .sort_values(by="ville_population_2012", ascending=False)
        .head(length)
    )
