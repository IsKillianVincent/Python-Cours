from peewee import SqliteDatabase

db = SqliteDatabase("card")

def init_db():
    """ Initialise la connexion et les tables de la base de données. """
    from models.card import Card
    from models.player import Player
    db.connect()
    db.create_tables([Card, Player], safe=True)
    db.close()
