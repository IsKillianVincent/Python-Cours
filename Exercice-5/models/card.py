class Card:
    """ 
    Représente une carte à jouer avec une valeur et une couleur.
    
    Une carte est définie par :
    - Une valeur : "2" à "10", "Valet", "Dame", "Roi", "As"
    - Une couleur : "Cœur", "Carreau", "Trèfle", "Pique"
    """
    
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi", "As"]
    suits = ["Cœur", "Carreau", "Trèfle", "Pique"]

    def __init__(self, value, suit):
        if value not in Card.values or suit not in Card.suits:
            raise ValueError(f"Valeur ou couleur invalide : {value} de {suit}")
        self.value = value
        self.suit = suit

    def __str__(self):
        return f"{self.value} de {self.suit}"
    
    def __repr__(self):
        return self.__str__()