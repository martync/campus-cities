from haversine import haversine
import pandas as pd

from apps.cities.controlers import get_big_cities
from .models import Air
from .utils import concatenate_air_results


def store_air_results_to_db():
    """
    Aggrège et calcul les relevés d'air.
    Enregistre une entrée pour chaque relevé situé à 15km et moins
    de la ville.
    """
    Air.delete().execute()
    big_cities = get_big_cities()
    data = concatenate_air_results()
    for row_city in big_cities.to_dict("records"):
        for row in data.to_dict("records"):
            distance = haversine(
                (row["Latitude"], row["Longitude"]), (row_city["ville_latitude_deg"], row_city["ville_longitude_deg"])
            )
            if distance <= 15:
                Air.create(
                    latitude=row.get("Latitude"),
                    longitude=row.get("Longitude"),
                    polluant=row.get("Polluant"),
                    daily_avg=row.get("Moyenne journaliere"),
                    date=row.get("date"),
                    city_id=row_city["ville_code_commune"],
                )


def get_airquality_results():
    """Retourne un DataFrame contenant les
    données de qualité de l'air pour chaque
    ville.

    Returns:
        pandas.DataFrame
    """
    df = pd.DataFrame(list(Air.select().dicts()))

    dfs = []
    for polluant in ["NO2", "PM10", "PM25"]:
        polluant_df = (
            df[df["polluant"] == polluant]
            .groupby(["city"])
            .mean()
            .rename(columns={"daily_avg": polluant})
            .drop(["id"], axis=1)
        )
        dfs.append(polluant_df)

    data = pd.concat(dfs, axis=1)
    data["total"] = data["NO2"] + data["PM10"] + data["PM25"]

    polluant_df = pd.merge(get_big_cities(), data, left_on="ville_code_commune", right_index=True).sort_values(
        by=["total"], ascending=False
    )
    polluant_df = polluant_df[polluant_df["total"].notnull()].sort_values(by=["total"], ascending=False)
    return polluant_df
