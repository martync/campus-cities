from decimal import Decimal
import pandas as pd
from apps.cities.utils import alter_insee_city_district
from apps.cities.controlers import get_big_cities
from apps.cities.models import City


def test_alter_insee_city_district():
    df = alter_insee_city_district(
        pd.DataFrame(
            [{"Lycee": "Albert CAMUS", "arrondissement": "69385"}, {"Lycee": "PRAVAZ", "arrondissement": "69386"}]
        ),
        "arrondissement",
    )
    expected_df = pd.DataFrame(
        [{"Lycee": "Albert CAMUS", "arrondissement": "69123"}, {"Lycee": "PRAVAZ", "arrondissement": "69123"}]
    )

    assert df.to_dict() == expected_df.to_dict()


def test_get_big_cities():
    City.delete().execute()
    datas = [
        {
            "code_commune": "XX",
            "nom": "XX",
            "population_2012": "1000",
            "longitude_deg": "12.999",
            "latitude_deg": "12.999",
        },
        {
            "code_commune": "YYY",
            "nom": "YYY",
            "population_2012": "100",
            "longitude_deg": "12.999",
            "latitude_deg": "12.999",
        },
        {
            "code_commune": "ZZ",
            "nom": "ZZ",
            "population_2012": "10000",
            "longitude_deg": "12.999",
            "latitude_deg": "12.999",
        },
    ]
    for data in datas:
        City.create(**data)

    big_cities = get_big_cities(length=2)
    assert isinstance(big_cities, pd.DataFrame)
    assert big_cities.shape[0] == 2
    assert big_cities.to_dict("records") == pd.DataFrame(
        [
            {
                "ville_code_commune": "ZZ",
                "ville_nom": "ZZ",
                "ville_population_2012": 10000,
                "ville_longitude_deg": Decimal("12.999"),
                "ville_latitude_deg": Decimal("12.999"),
            },
            {
                "ville_code_commune": "XX",
                "ville_nom": "XX",
                "ville_population_2012": 1000,
                "ville_longitude_deg": Decimal("12.999"),
                "ville_latitude_deg": Decimal("12.999"),
            },
        ]
    ).to_dict("records")
