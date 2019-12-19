from peewee import *
from database import db
from apps.cities.models import City


class Air(Model):
    city = ForeignKeyField(City)
    latitude = CharField()
    longitude = CharField()
    polluant = CharField()
    daily_avg = FloatField()
    date = CharField()

    class Meta:
        database = db


Air.create_table()
