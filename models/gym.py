from database import base_model
from peewee import CharField, DoubleField, IntegerField, DateTimeField, SmallIntegerField


class Gym(base_model):
    id = CharField(max_length=35, primary_key=True)
    latitude = DoubleField()
    longitude = DoubleField()
    team_id = SmallIntegerField(null=True)
    guard_pokedex_id = SmallIntegerField(null=True)
    gym_points = IntegerField(null=True)
    last_scanned = DateTimeField()
    last_modified = DateTimeField()
