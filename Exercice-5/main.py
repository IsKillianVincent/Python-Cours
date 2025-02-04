from models.deck import Deck
from models.distribution import Distributor

def print_section_title(title: str):
    """
    Affiche un titre de section bien formaté avec une ligne de séparation.
    """
    print(f"\n{'-' * 20} {title} {'-' * 20}\n")

def main():
    try:
        # Créer un paquet de cartes
        print_section_title("Question 1 : Créer un paquet de cartes")
        deck = Deck()
        
        # Melanger le paquet
        print_section_title("Question 2 : Melanger le paquet")
        deck.shuffle()

        # Demander le nombre de joueurs
        num_players = int(input("Combien de joueurs participent au jeu ? "))

        if num_players < 1:
            raise ValueError("Le nombre de joueurs doit être supérieur à 0.")

        # Créer une instance du distributeur
        print_section_title("Question 3 : Distribuer les cartes")
        distributor = Distributor(deck)

        # Distribuer les cartes
        players = distributor.distribute(num_players)

        # Afficher les cartes de chaque joueur
        for player, cards in players.items():
            print(f"{player} a les cart suivantes:")
            for card in cards:
                print(f"  - {card}")
            print()

    except ValueError as e:
        print(f"Erreur de valeur : {e}")
    except TypeError as e:
        print(f"Erreur de type : {e}")
    except IndexError as e:
        print(f"Erreur d'index : {e}")
    except Exception as e:
        print(f"Une erreur inattendue est survenue : {e}")

if __name__ == "__main__":
    main()
