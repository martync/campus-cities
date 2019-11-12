import pandas as pd
from apps.cities.helpers import get_big_cities, alter_insee_city_district
from settings import SANTE_FILE


def compute_sante_results():
    sante_results = (
        alter_insee_city_district(
            pd.read_csv(SANTE_FILE, sep=",", low_memory=False, usecols=["gid", "c_depcom"]), "c_depcom"
        )
        .groupby("c_depcom")
        .c_depcom.agg("count")
        .to_frame("count")
        .reset_index()
    )
    sante_df = pd.merge(get_big_cities(), sante_results, left_on="ville_code_commune", right_on="c_depcom")
    sante_df["patients_per_medecin"] = sante_df["ville_population_2010"] / sante_df["count"]
    sante_df["patients_per_medecin"] = sante_df["patients_per_medecin"].astype(int)
    sante_df = sante_df.sort_values(by=["patients_per_medecin"])
    return sante_df
