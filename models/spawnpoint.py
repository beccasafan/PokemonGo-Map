from peewee import CharField, SmallIntegerField, DoubleField, DateTimeField, ForeignKeyField, BooleanField
from spawnpoint_type import SpawnpointType
from database import base_model


class Spawnpoint(base_model):
    id = CharField(max_length=12, primary_key=True)
    spawnpoint_type_id = ForeignKeyField(SpawnpointType, null=True, db_column='spawnpoint_type_id')
    latitude = DoubleField()
    longitude = DoubleField()
    offset_sec = SmallIntegerField()
    active = BooleanField(null=True)
    empty = SmallIntegerField()
    last_scanned = DateTimeField()
    last_modified = DateTimeField()
