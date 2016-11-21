from database import base_model, db, raw_query
from peewee import IntegerField, DateTimeField, fn
from datetime import datetime, timedelta
from models import SpawnpointType, Pokemon, Spawnpoint, WildPokemon, SpawnpointDetection, Pokestop, Gym, PokemonMapping, LuredPokemon, PokemonIV, GymDetails, Trainer, TrainerPokemon, GymSlot, ScannedLocation, MainWorker, WorkerStatus
import sys
import os
from logger import log
import json

db_version = 1


class Migration(base_model):
    id = IntegerField(primary_key=True)
    pid = IntegerField()
    migration_start = DateTimeField()
    migration_end = DateTimeField(null=True)

    class Meta:
        primary_key = False

    @classmethod
    def run_migration(cls, id, migration):
        log.info('Upgrading database to schema version {}'.format(id))
        db.connect()
        m = Migration.create(id=id, pid=os.getpid(), migration_start=datetime.utcnow())
        migration()
        m.migration_end = datetime.utcnow()
        m.save()

    @classmethod
    def verify_schema(cls):
        # TODO: exclusive lock around everything this function does

        # TODO: do we want to create a class for the old Versions table so that we're not executing a raw query here?
        is_old_db = raw_query('SHOW TABLES LIKE \'versions\'').fetchall()

        if is_old_db:
            sys.exit('Database not compatibile. Please start with a fresh db')
        else:
            version = 0

            if not Migration.table_exists():
                db.connect()
                db.create_tables([Migration])
                m = Migration.create(id=0, pid=os.getpid(), migration_start=datetime.utcnow())
                db.close()

                version = m.id
            else:
                version = Migration.select(Migration.id).where(Migration.migration_end >> None).order_by(Migration.id.desc()).limit(1).get()

            if version < db_version:
                if version < 1:
                    Migration.run_migration(1, lambda: db.create_tables([SpawnpointType, Pokemon, Spawnpoint, WildPokemon, SpawnpointDetection, Pokestop, Gym, PokemonMapping, LuredPokemon, PokemonIV, GymDetails, Trainer, TrainerPokemon, GymSlot, ScannedLocation, MainWorker, WorkerStatus]))

            log.info('Schema up to date')
            # x = Migration.select((Migration.migration_start + timedelta(minutes=30)).alias('migration_start')).limit(1).get()
            # print(x.migration_start)

            y = Migration.select(fn.date_add(Migration.migration_start, timedelta(minutes=30))).where(Migration.migration_start < timedelta(minutes=30) + datetime.utcnow()).limit(1).sql()
            print(y.migration_start)
