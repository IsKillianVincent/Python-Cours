from peewee import Model, CharField
from models.database import db

class BaseModel(Model):
    class Meta:
        database = db

class Card(BaseModel):
    value = CharField()
    suit = CharField()

    def __str__(self):
        return f"{self.value} de {self.suit}"
