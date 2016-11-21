from database import base_model
from peewee import DoubleField, SmallIntegerField, DateTimeField, CompositeKey


class ScannedLocation(base_model):
    latitude = DoubleField()
    longitude = DoubleField()
    radius = SmallIntegerField()
    scanned = DateTimeField()

    class Meta:
        db_table = 'scanned_location'
        primary_key = CompositeKey('latitude', 'longitude')
