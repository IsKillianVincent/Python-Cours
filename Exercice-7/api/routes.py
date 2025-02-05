from fastapi import APIRouter, Depends
from models.deck import Deck
from models.distribution import Distributor

router = APIRouter()

def get_deck() -> Deck:
    deck = Deck()
    deck.shuffle()
    return deck

@router.get("/deck", summary="Récupère un paquet de 52 cartes mélangé")
def get_deck_cards(deck: Deck = Depends(get_deck)):
    """
    Génère et retourne un paquet de 52 cartes mélangé.
    """
    return {"deck": [str(card) for card in deck.cards]}

@router.get("/players/{num_players}", summary="Distribue les cartes entre X joueurs")
def get_players(num_players: int, deck: Deck = Depends(get_deck)):
    """
    Distribue les cartes entre un certain nombre de joueurs.
    Retourne un dictionnaire contenant les cartes de chaque joueur.
    """
    if num_players < 1:
        return {"error": "Le nombre de joueurs doit être positif."}

    distributor = Distributor(deck)

    try:
        players_hands = distributor.distribute(num_players)
    except ValueError as e:
        return {"error": str(e)}

    return {player: [str(card) for card in hand] for player, hand in players_hands.items()}
