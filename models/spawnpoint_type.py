from database import base_model
from peewee import IntegerField, CharField


class SpawnpointType(base_model):
    id = IntegerField(primary_key=True)
    code = CharField(max_length=6)
    description = CharField(max_length=255)

    class Meta:
        db_table = 'spawnpoint_type'