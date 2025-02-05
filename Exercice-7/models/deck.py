import random
from models.card import Card

class Deck:
    """
    Représente un paquet de 52 cartes standard.
    """

    def __init__(self):
        """ Initialise un paquet de cartes complet. """
        self.cards = [Card(value, suit) for suit in Card.suits for value in Card.values]

    def shuffle(self):
        """ Mélange le paquet de manière aléatoire. """
        random.shuffle(self.cards)

    def draw_card(self):
        """ Tire une carte du dessus du paquet. Lève une erreur si le paquet est vide. """
        if not self.cards:
            raise IndexError("Le paquet est vide. Impossible de tirer une carte.")
        return self.cards.pop()

    def __str__(self):
        return f"Paquet avec {len(self.cards)} cartes restantes"
