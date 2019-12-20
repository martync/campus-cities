import matplotlib.pyplot as plt
from .controlers import get_school_results


def show_schools_plot():
    """Affiche un graphique des résultats de lycée
    """
    school_results = get_school_results()
    bar_plot = school_results.plot(kind="barh", x="nom", y="score", figsize=(12, 12))
    bar_plot.set_ylabel("Ville")
    bar_plot.set_xlabel("Score réussite au bac")
    plt.savefig("output/school_score.png")


def show_schools_table():
    """Print le dataframe des résultats de lycée
    """
    print(get_school_results())
