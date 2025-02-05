from models.deck import Deck
from models.distribution import Distributor
from tests.deck_test import run_tests_without_pytest

def print_section_title(title: str):
    """
    Affiche un titre de section bien formaté avec une ligne de séparation.
    """
    print(f"\n{'-' * 20} {title} {'-' * 20}\n")

def main():
    try:
        print_section_title("Test sans pytest de la classe deck")
        run_tests_without_pytest()
    except Exception as e:
        print(f"Une erreur est survenue : {e}")

if __name__ == "__main__":
    main()
