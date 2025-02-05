import pytest
from models.deck import Deck
from models.distribution import Distributor
from models.card import Card

def run_tests_without_pytest():
    """Exécute une série de tests sans utiliser pytest."""
    deck = Deck()
    assert len(deck.cards) == 52, "Le paquet doit contenir 52 cartes au départ."
    
    original_order = deck.cards[:]
    deck.shuffle()
    assert original_order != deck.cards, "Le mélange doit modifier l'ordre des cartes."
    
    drawn_card = deck.draw_card()
    assert isinstance(drawn_card, Card), "La carte piochée doit être une instance de Card."
    
    print("Tous les tests sans pytest ont été exécutés avec succès.")

def test_deck_initialization():
    """Vérifie que le paquet contient bien 52 cartes au départ."""
    deck = Deck()
    assert len(deck.cards) == 52, "Le paquet doit contenir 52 cartes."
    assert all(isinstance(card, Card) for card in deck.cards), "Toutes les cartes doivent être des instances de Card."

def test_deck_shuffle():
    """Vérifie que le mélange modifie l'ordre des cartes sans changer leur nombre."""
    deck = Deck()
    original_order = deck.cards[:]
    deck.shuffle()
    assert deck.cards != original_order, "Le mélange doit modifier l'ordre des cartes."
    assert len(deck.cards) == 52, "Le nombre de cartes doit rester 52 après mélange."

def test_deck_draw_card():
    """Vérifie que tirer une carte réduit la taille du paquet et retourne une carte valide."""
    deck = Deck()
    initial_count = len(deck.cards)
    drawn_card = deck.draw_card()
    assert len(deck.cards) == initial_count - 1, "Le paquet doit perdre une carte après pioche."
    assert isinstance(drawn_card, Card), "La carte piochée doit être une instance de Card."

def test_deck_draw_card_empty():
    """Vérifie que piocher dans un paquet vide lève une exception."""
    deck = Deck()
    for _ in range(52):
        deck.draw_card()
    with pytest.raises(IndexError, match="Le paquet est vide. Impossible de tirer une carte."):
        deck.draw_card()

def test_deck_str():
    """Vérifie la représentation textuelle du paquet."""
    deck = Deck()
    assert str(deck) == "Paquet avec 52 cartes restantes"
    deck.draw_card()
    assert str(deck) == "Paquet avec 51 cartes restantes"

def test_distribute_cards():
    """Vérifie que la distribution de cartes fonctionne correctement pour plusieurs joueurs."""
    deck = Deck()
    distributor = Distributor(deck)
    num_players = 4
    players = distributor.distribute(num_players)
    
    expected_cards_per_player = 52 // num_players
    for player, cards in players.items():
        assert len(cards) == expected_cards_per_player, f"{player} doit avoir {expected_cards_per_player} cartes."
    
    total_distributed = sum(len(cards) for cards in players.values())
    assert total_distributed == 52, "Toutes les cartes doivent être distribuées."

def test_distribute_invalid_num_players():
    """Vérifie que la distribution échoue si le nombre de joueurs est invalide."""
    deck = Deck()
    distributor = Distributor(deck)
    with pytest.raises(ValueError, match="Il doit y avoir au moins un joueur."):
        distributor.distribute(0)

def test_distribute_unequal_cards():
    """Vérifie que le distributeur gère le cas où les cartes ne peuvent pas être réparties équitablement."""
    deck = Deck()
    distributor = Distributor(deck)
    num_players = 3  # 52 cartes pas / par 3
    players = distributor.distribute(num_players)
    
    min_cards = 52 // num_players
    max_cards = min_cards + 1
    
    cards_counts = [len(cards) for cards in players.values()]
    assert all(c == min_cards or c == max_cards for c in cards_counts), "Les joueurs doivent avoir un nombre de cartes proche."
