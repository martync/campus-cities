import matplotlib.pyplot as plt
from .controlers import get_airquality_results


def show_air_quality_plot():
    air_results = get_airquality_results()
    x = air_results[["ville_nom", "NO2", "PM10", "PM25"]]
    y = x.set_index("ville_nom")
    y.plot.barh(stacked=True, figsize=(12, 12))
    plt.savefig("output/air.png")
    plt.show()


def show_air_quality_table():
    air_results = get_airquality_results()
    print(air_results)
