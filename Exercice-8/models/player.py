from peewee import Model, CharField
from models.database import db

class BaseModel(Model):
    class Meta:
        database = db

class Player(BaseModel):
    name = CharField(unique=True)
