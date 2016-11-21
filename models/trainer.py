from database import base_model
from peewee import CharField, SmallIntegerField, DateTimeField


class Trainer(base_model):
    name = CharField(max_length=50, primary_key=True)
    team_id = SmallIntegerField()
    level = SmallIntegerField()
    last_seen = DateTimeField()
    last_modified = DateTimeField()
