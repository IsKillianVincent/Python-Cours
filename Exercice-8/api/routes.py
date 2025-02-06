from fastapi import APIRouter
from services.deck import Deck
from models.card import Card
from models.database import db, init_db
from services.distributor import Distributor

router = APIRouter()

@router.on_event("startup")
def startup():
    """ S'assure que les cartes par défaut sont insérées au démarrage de l'application. """
    deck = Deck()

@router.get("/deck", summary="Récupère un paquet de cartes mélangé depuis la base de données")
def get_deck_cards():
    """ Retourne les cartes stockées en base. """
    cards = [str(card) for card in Card.select()]
    return {"deck": cards}

@router.get("/shuffle", summary="Mélange les cartes du paquet")
def shuffle_deck():
    """ Mélange les cartes en base. """
    deck = Deck()
    deck.shuffle()
    return {"message": "Le paquet a été mélangé."}

@router.get("/distribute/{num_players}", summary="Distribue les cartes entre les joueurs")
def distribute_cards(num_players: int):
    """ Distribue les cartes entre les joueurs. """
    deck = Deck()
    distributor = Distributor(deck)
    players = distributor.distribute(num_players)
    return {"players": players}
