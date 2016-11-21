from database import base_model
from peewee import ForeignKeyField, CharField, SmallIntegerField, IntegerField, FloatField, DateTimeField
from trainer import Trainer


class TrainerPokemon(base_model):
    uid = CharField(max_length=25, primary_key=True)
    pokedex_id = SmallIntegerField()
    trainer_name = ForeignKeyField(Trainer, db_column='trainer_name', to_field='name')
    cp = IntegerField()
    cp_multiplier = IntegerField()
    additional_cp_multiplier = FloatField()
    num_upgrades = IntegerField()
    height = FloatField()
    weight = FloatField()
    stamina = FloatField()
    stamina_max = FloatField()
    iv_attack = IntegerField()
    iv_defense = IntegerField()
    iv_stamina = IntegerField()
    move_1 = IntegerField()
    move_2 = IntegerField()
    last_seen = DateTimeField()
    last_modified = DateTimeField()

    class Meta:
        db_table = 'trainer_pokemon'