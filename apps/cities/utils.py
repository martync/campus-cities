import numpy as np
from settings import *


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
