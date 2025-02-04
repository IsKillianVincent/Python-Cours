from models.deck import Deck
from models.distribution import Distributor
from models.card import Card
import pytest

def run_tests_without_pytest():
    # Initialisation du deck
    deck = Deck()
    assert len(deck.cards) == 52, "Le paquet doit contenir 52 cartes au départ."
    assert isinstance(deck.cards[0], Card), "Les éléments du paquet doivent être des instances de Card."

    # Test du melange
    original_deck = deck.cards[:]
    deck.shuffle()
    assert original_deck != deck.cards, "Le melange doit modifier l'ordre des cartes."
    assert len(deck.cards) == 52, "Le paquet doit toujours contenir 52 cartes après mélange."

    # Test de pioche d'une carte
    initial_count = len(deck.cards)
    drawn_card = deck.draw_card()
    assert len(deck.cards) == initial_count - 1, "Une carte doit être retirée du paquet après la pioche."
    assert isinstance(drawn_card, Card), "L'élément pioché doit être une instance de Card."

    # Test de pioche d'un paquet vide
    for _ in range(51):
        deck.draw_card()

    try:
        deck.draw_card()
        assert False, "Tirer une carte d'un paquet vide doit lever une exception."
    except IndexError:
        pass

    # Test de la méthode __str__
    deck = Deck()
    assert str(deck) == "Paquet avec 52 cartes restantes", "La représentation en chaîne est incorrecte."
    deck.draw_card()
    assert str(deck) == "Paquet avec 51 cartes restantes", "La représentation en chaîne après une pioche est incorrecte."

    print("Tous les tests sont passés avec succès.")

# Test de la classe Deck
def test_deck_initialization():
    deck = Deck()
    assert len(deck.cards) == 52
    assert isinstance(deck.cards[0], Card)

def test_deck_shuffle():
    deck = Deck()
    original_deck = deck.cards[:]
    deck.shuffle()
    assert original_deck != deck.cards
    assert len(deck.cards) == 52

def test_deck_draw_card():
    deck = Deck()
    initial_count = len(deck.cards)
    drawn_card = deck.draw_card()
    assert len(deck.cards) == initial_count - 1
    assert isinstance(drawn_card, Card)

def test_deck_draw_card_empty():
    deck = Deck()
    for _ in range(52):
        deck.draw_card()
    with pytest.raises(IndexError):
        deck.draw_card()

def test_deck_str():
    deck = Deck()
    assert str(deck) == "Paquet avec 52 cartes restantes"
    deck.draw_card()
    assert str(deck) == "Paquet avec 51 cartes restantes"

# Test de la classe Distributor
def test_distribute_cards():
    deck = Deck()
    distributor = Distributor(deck)
    
    players = distributor.distribute(4)
    
    num_cards_per_player = 52 // 4
    for player, cards in players.items():
        assert len(cards) == num_cards_per_player, f"Le joueur {player} doit avoir {num_cards_per_player} cartes, mais en a {len(cards)}."
    
    total_distributed_cards = sum(len(cards) for cards in players.values())
    assert total_distributed_cards == 52, f"Le total des cartes distribuées doit être 52, mais est {total_distributed_cards}."


def test_distribute_invalid_num_players():
    deck = Deck()
    distributor = Distributor(deck)
    with pytest.raises(ValueError):
        distributor.distribute(0)
