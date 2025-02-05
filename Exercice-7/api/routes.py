from fastapi import APIRouter
from models.deck import Deck
from models.distribution import Distributor

router = APIRouter()

@router.get("/deck", summary="Récupère un paquet de 52 cartes mélangé")
def get_deck():
    """
    Génère et retourne un paquet de 52 cartes mélangé.
    """
    deck = Deck()
    deck.shuffle()
    return {"deck": [str(card) for card in deck.cards]}

@router.get("/players/{num_players}", summary="Distribue les cartes entre X joueurs")
def get_players(num_players: int):
    """
    Distribue les cartes entre un certain nombre de joueurs.
    Retourne un dictionnaire contenant les cartes de chaque joueur.
    """
    if num_players < 1:
        return {"error": "Le nombre de joueurs doit être positif."}

    deck = Deck()
    deck.shuffle()
    distributor = Distributor(deck)

    try:
        players_hands = distributor.distribute(num_players)
    except ValueError as e:
        return {"error": str(e)}

    return {player: [str(card) for card in hand] for player, hand in players_hands.items()}
