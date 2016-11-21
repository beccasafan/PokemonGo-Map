from database import base_model
from peewee import IntegerField, DateTimeField, BigIntegerField, ForeignKeyField
from wild_pokemon import WildPokemon


class SpawnpointDetection(base_model):
    id = IntegerField(primary_key=True)
    spawnpoint_id = ForeignKeyField(WildPokemon, to_field='spawnpoint_id', related_name='spawnpoint_detection__spawnpoint')
    pokemon_id = ForeignKeyField(WildPokemon, to_field='pokemon_id', null=True, related_name='spawnpoint_detection__pokemon')
    scan_time = DateTimeField()
    tth_ms = BigIntegerField(null=True)

    class Meta:
        db_table = 'spawnpoint_detection'
