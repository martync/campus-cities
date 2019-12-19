import argparse

from apps.cities.controlers import store_cities
from apps.cities.views import show_cities_plot, show_cities_table
from apps.sante.views import show_sante_table, show_sante_plot
from apps.school.controlers import store_school_results
from apps.school.views import show_schools_plot, show_schools_table
from apps.air.controlers import store_air_results_to_db
from apps.air.views import show_air_quality_plot, show_air_quality_table
from database import db


def store_all():
    store_cities()
    store_air_results_to_db()
    store_school_results()

    show_cities_plot()
    show_sante_plot()
    show_air_quality_plot()
    show_schools_plot()


def total_result():
    pass


#     from apps.air.controlers import get_airquality_results
#     from apps.cities.controlers import get_big_cities
#     from apps.sante.controlers import compute_sante_results
#     from apps.school.controlers import get_school_results

#     cities = get_big_cities()
#     air = get_airquality_results()
#     sante = compute_sante_results()
#     school = get_school_results()

#     print(air["total"].max())
#     print(air["total"].min())


routes = {
    # MAIN
    "store_all": store_all,
    # CITIES
    "store_cities": store_cities,
    "show_cities_plot": show_cities_plot,
    "show_cities_table": show_cities_table,
    # SANTE
    "show_sante_table": show_sante_table,
    "show_sante_plot": show_sante_plot,
    # AIR
    "compute_air": store_air_results_to_db,
    "show_air": show_air_quality_plot,
    "show_air_table": show_air_quality_table,
    # SCHOOL
    "store_school_results": store_school_results,
    "show_schools_table": show_schools_table,
    "show_schools_plot": show_schools_plot,
    "show_schools_plot": show_schools_plot,
    # TOTAL
    "total_result": total_result,
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "action", help="Choose an action to execute", nargs="?", default="cities", choices=list(routes.keys())
    )
    args = parser.parse_args()
    routes[args.action]()


if __name__ == "__main__":
    db.connect(reuse_if_open=True)
    main()
    db.close()
