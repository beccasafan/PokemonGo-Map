from database import base_model
from peewee import ForeignKeyField, CompositeKey
from gym import Gym
from trainer_pokemon import TrainerPokemon


class GymSlot(base_model):
    gym_id = ForeignKeyField(Gym, db_column='gym_id')
    pokemon_uid = ForeignKeyField(TrainerPokemon, db_column='pokemon_uid')

    class Meta:
        db_table = 'gym_slot'
        primary_key = CompositeKey('gym_id', 'pokemon_uid')
