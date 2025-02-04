from utils.ip_utils import IPValidator
from models.bank import PersonalBankAccount
from utils.utils import print_section_title

def main():
    print_section_title("Validation des IPs")
    ip_list = ["192.168.1.1", "256.256.256.256", "::1", "1234:5678::abcd"]
    print(IPValidator.validate_ip_list(ip_list))

    ip_dict = {"localhost": "127.0.0.1", "google": "8.8.8.8", "invalid": "999.999.999.999"}
    print(IPValidator.validate_ip_dict(ip_dict))

    print_section_title("Gestion de Compte Bancaire")
    client = PersonalBankAccount(name="Killian VINCENT", age=21, address="15 Rue des smarties", account_number="FR123456789", balance=5000)
    
    print(client)
    client.deposit(500)
    client.withdraw(300)
    client.withdraw(7000)

if __name__ == "__main__":
    main()
