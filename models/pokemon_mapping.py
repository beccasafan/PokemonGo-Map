from database import base_model
from peewee import CharField, SmallIntegerField, ForeignKeyField
from spawnpoint import Spawnpoint
from pokestop import Pokestop


class PokemonMapping(base_model):
    id = CharField(max_length=64, primary_key=True)
    type_id = SmallIntegerField()
    spawnpoint_id = ForeignKeyField(Spawnpoint, null=True, db_column='spawnpoint_id')
    pokestop_id = ForeignKeyField(Pokestop, null=True, db_column='pokestop_id')

    class Meta:
        db_table = 'pokemon_mapping'
