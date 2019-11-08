import numpy as np
import pandas as pd
from settings import *


def get_big_cities(length=LIMIT_CITIES_NUMBER):
    """
    Retourne les villes les plus grandes de France.

    Args:
        length (int): Nombre de villes souhaité

    Returns:
        pandas.DataFrame

    """
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


def alter_insee_city_district(dataframe, column_name):
    """
    Remplace les codes insee des arrondissement des
    grandes villes par le code insee unique

    Args:
        dataframe (pandas.DataFrame): Le tableau de données pandas
        column_name (str): le nom de la colonne contenant le code insee

    Returns:
        pandas.DataFrame: Le tableau modifié

    """
    for unique_insee, districts_insee in CITIES_WITH_DISTRICT:
        dataframe[column_name] = np.where(
            dataframe[column_name].isin(districts_insee), unique_insee, dataframe[column_name]
        )
    return dataframe
