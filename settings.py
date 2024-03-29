CITIES_FILE = "datas/villes_france.csv"
LIMIT_CITIES_NUMBER = 50

SCHOOL_FILE = "datas/school.csv"
SANTE_FILE = "datas/donnees_sante_insee_metropole_d201_bpe_.csv"
WATER_FILE = "datas/qualite_eau.json"
AIR_DIRECTORY = "datas/air/"
AIR_TYPES = ["NO2", "PM10", "PM25"]

# fmt: off
LYON = ["69123", ["69300", "69381", "69382", "69383", "69384", "69385", "69386", "69387", "69388", "69389", "69901"]]  # noqa
PARIS = ["75056", ["75100", "75110", "75111", "75112", "75113", "75114", "75115", "75116", "75117", "75118", "75119", "75101", "75120", "75102", "75103", "75104", "75105", "75106", "75107", "75108", "75109", ], ]  # noqa
MARSEILLE = ["13055", ["13200", "13210", "13211", "13212", "13213", "13214", "13215", "13216", "13201", "13202", "13203", "13204", "13205", "13206", "13207", "13208", "13209", ], ]  # noqa
CITIES_WITH_DISTRICT = [PARIS, LYON, MARSEILLE]
# fmt: on


DB_NAME = "cities.db"
