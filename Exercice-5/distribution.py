from deck import Deck

class Distributor:
    """Handles the distribution of cards to players."""
    
    def __init__(self, deck):
        self.deck = deck
    
    def distribute(self, num_players):
        """Distributes cards equally among players."""
        if num_players < 1:
            raise ValueError("Il doit y avoir au moins un joueur.")
        
        num_cards = len(self.deck.cards)
        
        # Check if the cards can be evenly distributed
        if num_cards % num_players != 0:
            print("Les cartes ne peuvent pas être distribuées de manière égale. Certaines cartes seront jetées.")
        
        cards_per_player = num_cards // num_players
        players = {f"Joueur {i + 1}": [] for i in range(num_players)}

        for i in range(cards_per_player):
            for player in players:
                card = self.deck.draw_card()
                if card:
                    players[player].append(card)

        return players
