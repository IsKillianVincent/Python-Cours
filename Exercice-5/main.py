from models.deck import Deck
from models.distribution import Distributor
from models.card import Card

def print_section_title(title: str):
    """
    Affiche un titre de section bien formaté avec une ligne de séparation.
    """
    print(f"\n{'-' * 20} {title} {'-' * 20}\n")

def main():
    """ 
    Programme principal : Création, mélange et distribution des cartes.
    """
    try:
        print_section_title("Création du paquet de cartes")
        deck = Deck()
        
        print_section_title("Mélange du paquet")
        deck.shuffle()

        while True:
            try:
                num_players = int(input("Combien de joueurs participent au jeu ? "))
                if num_players < 1:
                    raise ValueError("Le nombre de joueurs doit être supérieur à 0.")
                break
            except ValueError:
                print("Veuillez entrer un nombre entier valide.")

        print_section_title("Distribution des cartes")
        distributor = Distributor(deck)
        players = distributor.distribute(num_players)

        for player, cards in players.items():
            print(f"{player} a les cartes suivantes (triées) :")
            sorted_cards = sorted(cards, key=lambda c: (Card.values.index(c.value), c.suit))
            for card in sorted_cards:
                print(f"  - {card}")
            print()

    except ValueError as e:
        print(f"Erreur de valeur : {e}")
    except Exception as e:
        print(f"Une erreur inattendue est survenue : {e}")


if __name__ == "__main__":
    main()
