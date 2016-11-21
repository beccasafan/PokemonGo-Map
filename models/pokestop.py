from database import base_model
from peewee import CharField, DoubleField, DateTimeField


class Pokestop(base_model):
    id = CharField(max_length=35, primary_key=True)
    latitude = DoubleField()
    longitude = DoubleField()
    lure_expiration = DateTimeField(null=True)
    last_scanned = DateTimeField()
    last_modified = DateTimeField()
