import random
from models.card import Card
from models.database import db

class Deck:
    def __init__(self):
        """ Initialise un paquet de cartes. Si le paquet n'existe pas, l'insère dans la base. """
        if not self.cards_exist():
            self.insert_default_cards()

    def cards_exist(self):
        """ Vérifie si des cartes existent déjà dans la base de données. """
        return Card.select().exists()

    def insert_default_cards(self):
        """ Insère toutes les cartes par défaut dans la base de données. """
        with db.atomic():
            for suit in ["Cœur", "Carreau", "Trèfle", "Pique"]:
                for value in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi", "As"]:
                    Card.create(value=value, suit=suit)

    def save_to_db(self):
        """ Enregistre le deck dans la base de données (si ce n'est pas déjà fait). """
        if not self.cards_exist():
            self.insert_default_cards()

    def shuffle(self):
        """ Mélange les cartes en base et met à jour l'ordre dans la base de données. """
        all_cards = list(Card.select())
        random.shuffle(all_cards)

        with db.atomic():
            for index, card in enumerate(all_cards):
                card.id = index + 1
                card.save()

    def draw_card(self):
        """ Tire une carte de la base de données. """
        card = Card.select().order_by(Card.id.desc()).first()
        if card:
            card.delete_instance()
            return card
        return None
