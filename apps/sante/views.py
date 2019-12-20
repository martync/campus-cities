import matplotlib.pyplot as plt
from .controlers import compute_sante_results


def show_sante_plot():
    """Affiche un graphique du nombre d'habitants par médecin
    """
    df = compute_sante_results()
    bar_plot = df.plot(kind="barh", x="ville_nom", y="patients_per_medecin", figsize=(12, 12))
    bar_plot.set_ylabel("Ville")
    bar_plot.set_xlabel("Nb de patients par médecin")
    plt.savefig("output/patients_per_medecin.png")


def show_sante_table():
    """Print le dataframe du nombre d'habitants par médecin
    """
    df = compute_sante_results()
    print(df)
