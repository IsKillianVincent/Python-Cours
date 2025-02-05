class Card:
    """
    Représente une carte à jouer avec une valeur et une couleur.
    """

    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi", "As"]
    suits = ["Cœur", "Carreau", "Trèfle", "Pique"]

    def __init__(self, value: str, suit: str):
        if value not in Card.values or suit not in Card.suits:
            raise ValueError("Valeur ou couleur de carte invalide.")
        self.value = value
        self.suit = suit

    def __str__(self):
        return f"{self.value} de {self.suit}"

    def __repr__(self):
        return self.__str__()
