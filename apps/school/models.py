from peewee import *
from database import db
from apps.cities.models import City


class School(Model):
    city = ForeignKeyField(City)
    taux_reussite = FloatField()
    taux_mention = FloatField()
    score = FloatField()

    class Meta:
        database = db


School.create_table()
