from playhouse.flask_utils import FlaskDB
from peewee import SqliteDatabase
from playhouse.shortcuts import RetryOperationalError, MySQLDatabase
import config
from web_server import app


class MyRetryDatabase(RetryOperationalError, MySQLDatabase):
    pass

db = None

if config.get_arg('db_type') == 'mysql':
    _db = MyRetryDatabase(
        database=config.get_arg('db_name'),
        user=config.get_arg('db_user'),
        password=config.get_arg('db_pass'),
        host=config.get_arg('db_host'),
        port=config.get_arg('db_port'),
    )
else:
    _db = SqliteDatabase(config.get_arg('db'))

__db = FlaskDB(app, _db)

base_model = __db.Model
db = __db.database


def raw_query(query):
    return __db.database.execute_sql(query)
