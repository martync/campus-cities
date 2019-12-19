import matplotlib.pyplot as plt
from .controlers import get_school_results


def show_schools_table():
    print(get_school_results())


def show_schools_plot():
    school_results = get_school_results()
    bar_plot = school_results.plot(kind="barh", x="nom", y="score", figsize=(12, 12))
    bar_plot.set_ylabel("Ville")
    bar_plot.set_xlabel("Score réussite au bac")
    # plt.show()
    plt.savefig("output/school_score.png")
