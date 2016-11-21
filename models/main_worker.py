from database import base_model
from peewee import IntegerField, CharField, DateTimeField


class MainWorker(base_model):
    pid = IntegerField(primary_key=True)
    name = CharField(max_length=50)
    message = CharField(max_length=255)
    method = CharField(max_length=50)
    last_modified = DateTimeField()

    class Meta:
        db_table = 'main_worker'
