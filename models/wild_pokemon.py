from database import base_model
from peewee import ForeignKeyField
from pokemon import Pokemon
from spawnpoint import Spawnpoint


class WildPokemon(base_model):
    pokemon_id = ForeignKeyField(Pokemon, db_column='pokemon_id')
    spawnpoint_id = ForeignKeyField(Spawnpoint, db_column='spawnpoint_id')

    class Meta:
        db_table = 'wild_pokemon'
