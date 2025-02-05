class Distributor:
    """
    Gère la distribution des cartes aux joueurs.
    """

    def __init__(self, deck):
        self.deck = deck
    
    def distribute(self, num_players):
        """ 
        Distribue les cartes entre les joueurs.
        """
        if num_players < 1:
            raise ValueError("Il doit y avoir au moins un joueur.")
        
        num_cards = len(self.deck.cards)
        if num_cards < num_players:
            raise ValueError("Pas assez de cartes pour distribuer à tous les joueurs.")

        if num_cards % num_players != 0:
            print("Attention : Les cartes ne peuvent pas être distribuées de manière égale. Certaines seront mises de côté.")

        cards_per_player = num_cards // num_players
        players = {f"Joueur {i + 1}": [] for i in range(num_players)}

        for _ in range(cards_per_player):
            for player in players:
                card = self.deck.draw_card()
                if card:
                    players[player].append(card)

        return players