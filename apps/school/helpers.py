import pandas as pd
from apps.cities.helpers import get_big_cities, alter_insee_city_district
from settings import SCHOOL_FILE


def compute_school_results():
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

    school_df = school_df.sort_values(by=["school_score"], ascending=False)[school_df["school_score"].notnull()]

    return school_df
