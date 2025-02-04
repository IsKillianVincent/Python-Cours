class Identity:
    """
    Représente l'identité d'un client bancaire.
    """
    def __init__(self, name: str, age: int, address: str):
        self.name = name
        self.age = age
        self.address = address

    def __str__(self):
        return f"{self.name}, {self.age} ans, adresse: {self.address}"


class BankAccount:
    """
    Classe représentant un compte bancaire de base.
    """
    def __init__(self, account_number: str, balance: float = 0.0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount: float):
        """Ajoute de l'argent au compte."""
        if amount > 0:
            self.balance += amount
            print(f"Dépôt de {amount}€ effectué. Nouveau solde : {self.balance}€")
        else:
            print("Montant invalide pour le dépôt.")

    def withdraw(self, amount: float):
        """Retire de l'argent du compte, si le solde le permet."""
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Retrait de {amount}€ effectué. Nouveau solde : {self.balance}€")
        else:
            print("Fonds insuffisants ou montant invalide.")

    def __str__(self):
        return f"Compte n°{self.account_number} - Solde : {self.balance}€"


class PersonalBankAccount(BankAccount, Identity):
    """
    Classe héritant de BankAccount et Identity pour gérer un compte bancaire de particulier.
    """
    def __init__(self, name: str, age: int, address: str, account_number: str, balance: float = 0.0):
        BankAccount.__init__(self, account_number, balance)
        Identity.__init__(self, name, age, address)

    def __str__(self):
        return f"{Identity.__str__(self)}\n{BankAccount.__str__(self)}"
