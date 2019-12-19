from peewee import *
from database import db


class City(Model):
    code_commune = CharField(primary_key=True)
    nom = CharField()
    population_2012 = IntegerField()
    longitude_deg = DecimalField(max_digits=9, decimal_places=6)
    latitude_deg = DecimalField(max_digits=9, decimal_places=6)

    class Meta:
        database = db


City.create_table()
