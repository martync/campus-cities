import matplotlib.pyplot as plt
from settings import LIMIT_CITIES_NUMBER
from apps.cities.helpers import get_big_cities


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
    main()
