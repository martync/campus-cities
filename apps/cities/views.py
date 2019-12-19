import matplotlib.pyplot as plt
from settings import LIMIT_CITIES_NUMBER
from .controlers import get_big_cities


def show_cities_table():
    cities = get_big_cities(LIMIT_CITIES_NUMBER)
    print(cities)


def show_cities_plot():
    cities = get_big_cities(LIMIT_CITIES_NUMBER)
    bar_plot = cities.plot(kind="barh", x="ville_nom", y="ville_population_2012", figsize=(12, 12))
    bar_plot.set_ylabel("Ville")
    bar_plot.set_xlabel("Population 2012 (habitants)")
    plt.savefig("output/big_cities.png")
