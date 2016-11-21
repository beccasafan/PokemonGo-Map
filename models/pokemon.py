from database import base_model
from peewee import CharField, SmallIntegerField, DateTimeField


class Pokemon(base_model):
    id = CharField(max_length=64, primary_key=True)
    encounter_id = CharField(max_length=24)
    pokedex_id = SmallIntegerField()
    scanned = DateTimeField()
