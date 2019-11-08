import argparse

import matplotlib.pyplot as plt
from settings import LIMIT_CITIES_NUMBER
from apps.cities.helpers import get_big_cities
from apps.school.helpers import compute_school_results


def main():
    cities = get_big_cities(LIMIT_CITIES_NUMBER)
    print(cities)
    # print(cities.to_dict(orient="records"))
    bar_plot = cities.plot(kind="barh", x="ville_nom", y="ville_population_2010", figsize=(8, 12))
    bar_plot.set_ylabel("Ville")
    bar_plot.set_xlabel("Population 2010 (habitants)")
    # plt.show()
    plt.savefig("output/big_cities.png")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "action", help="Choose an action to execute", nargs="?", default="cities", choices=["cities", "compute_school"]
    )
    args = parser.parse_args()
    if args.action == "compute_school":
        school_results = compute_school_results()
        bar_plot = school_results.plot(kind="barh", x="ville_nom", y="school_score", figsize=(8, 12))
        bar_plot.set_ylabel("Ville")
        bar_plot.set_xlabel("Score réussite au bac")
        # plt.show()
        plt.savefig("output/school_score.png")

    elif args.action == "cities":
        main()
