from run import routes


def test_routes():
    assert len(routes) == 12
    assert sorted(list(routes.keys())) == sorted(
        [
            "store_all",
            "store_cities",
            "show_cities_plot",
            "show_cities_table",
            "show_sante_table",
            "show_sante_plot",
            "compute_air",
            "show_air",
            "show_air_table",
            "store_school_results",
            "show_schools_table",
            "show_schools_plot",
        ]
    )
