from database import base_model
from peewee import ForeignKeyField, CharField, TextField, DateTimeField
from gym import Gym


class GymDetails(base_model):
    gym_id = ForeignKeyField(Gym, db_column='gym_id')
    name = CharField(max_length=255)
    url = CharField(max_length=255)
    description = TextField()
    last_scanned = DateTimeField()

    class Meta:
        db_table = 'gym_details'
