from database import base_model
from peewee import ForeignKeyField, DateTimeField
from pokemon import Pokemon
from pokestop import Pokestop


class LuredPokemon(base_model):
    pokemon_id = ForeignKeyField(Pokemon, db_column='pokemon_id')
    pokestop_id = ForeignKeyField(Pokestop, db_column='pokestop_id')
    expire_time = DateTimeField()

    class Meta:
        db_table = 'lured_pokemon'
