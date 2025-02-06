from models.card import Card
from services.deck import Deck

class Distributor:
    """
    Gère la distribution des cartes aux joueurs.
    """

    def __init__(self, deck: Deck):
        self.deck = deck

    def distribute(self, num_players: int):
        """
        Distribue les cartes entre les joueurs.
        """
        if num_players < 1:
            raise ValueError("Il doit y avoir au moins un joueur.")

        all_cards = list(Card.select())
        num_cards = len(all_cards)

        if num_cards < num_players:
            raise ValueError("Pas assez de cartes pour distribuer.")

        cards_per_player = num_cards // num_players

        players = {f"Joueur {i + 1}": [] for i in range(num_players)}

        for player in players:
            for _ in range(cards_per_player):
                card = self.deck.draw_card()
                if card:
                    formatted_card = f"{card.value} de {card.suit}"
                    players[player].append(formatted_card)

        return players