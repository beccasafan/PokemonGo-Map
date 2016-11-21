from database import base_model
from peewee import ForeignKeyField, IntegerField, DateTimeField
from pokemon import Pokemon


class PokemonIV(base_model):
    pokemon_id = ForeignKeyField(Pokemon, db_column='pokemon_id')
    attack = IntegerField()
    defense = IntegerField()
    stamina = IntegerField()
    move_1 = IntegerField()
    move_2 = IntegerField()
    scanned = DateTimeField()

    class Meta:
        db_table = 'pokemon_iv'
