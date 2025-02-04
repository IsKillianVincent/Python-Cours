from utils.ip_utils import identify_ip_version, validate_ip_list, validate_ip_dict

def print_section_title(title: str):
    """
    Affiche un titre de section bien formaté avec une ligne de séparation.
    """
    print(f"\n{'-' * 20} {title} {'-' * 20}\n")

def get_user_ip():
    ip = input("Veuillez saisir une adresse IP (IPv4 ou IPv6) : ")
    print(f"Adresse IP saisie : {ip}")
    return ip

def main():
    print_section_title("Questions 1 - 2 - 3 - 4 : Saisie et validation d'une adresse IP")
    ip = get_user_ip()
    print(identify_ip_version(ip))

    print_section_title("Question 5 : Vérification d'une liste d'adresses IP")
    test_ips = ["192.168.1.1", "256.256.256.256", "::1", "1234:5678::abcd"]
    print(validate_ip_list(test_ips))

    print_section_title("Question 6 : Vérification d'un dictionnaire d'adresses IP")
    test_ip_dict = {"localhost": "127.0.0.1", "google": "8.8.8.8", "invalid": "999.999.999.999"}
    print(validate_ip_dict(test_ip_dict))

if __name__ == "__main__":
    main()
