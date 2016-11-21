from database import base_model
from peewee import CharField, IntegerField, DateTimeField, ForeignKeyField
from main_worker import MainWorker


class WorkerStatus(base_model):
    username = CharField(max_length=50, primary_key=True)
    pid = ForeignKeyField(MainWorker, db_column='pid')
    success = IntegerField()
    fail = IntegerField()
    no_items = IntegerField()
    skip = IntegerField()
    message = CharField(max_length=255)
    last_modified = DateTimeField()

    class Meta:
        db_table = 'worker_status'
