import pandas as pd
from apps.cities.controlers import get_big_cities
from apps.cities.models import City
from apps.cities.utils import alter_insee_city_district
from settings import SCHOOL_FILE

from .models import School


def store_school_results():
    # On ouvre le fichier des résultats scolaires
    school_results = (
        alter_insee_city_district(
            pd.read_csv(
                SCHOOL_FILE,
                error_bad_lines=False,
                sep=";",
                low_memory=False,
                usecols=["Taux Brut de Réussite Total séries", "Taux_Mention_brut_toutes_series", "Code commune"],
            ),
            "Code commune",
        )
        .groupby(["Code commune"])
        .mean()
        .reset_index()
    )

    # Fusionne le tableau des résultats avec les grandes villes
    school_df = pd.merge(get_big_cities(), school_results, left_on="ville_code_commune", right_on="Code commune")

    # Calcule le score global (moyenne du taux de réussite et taux de mentions)
    school_df["school_score"] = (
        school_df["Taux_Mention_brut_toutes_series"] + school_df["Taux Brut de Réussite Total séries"]
    ) / 2

    school_df = school_df.rename(
        columns={
            "Code commune": "city_id",
            "school_score": "score",
            "Taux_Mention_brut_toutes_series": "taux_mention",
            "Taux Brut de Réussite Total séries": "taux_reussite",
        }
    )[["city_id", "score", "taux_mention", "taux_reussite"]]

    School.delete().execute()
    school_df = school_df.sort_values(by=["score"], ascending=False)[school_df["score"].notnull()]
    School.insert_many(list(school_df.to_dict("records"))).execute()


def get_school_results():
    return pd.DataFrame(School.select(City, School).join(City).dicts()).sort_values(by=["score"], ascending=False)
