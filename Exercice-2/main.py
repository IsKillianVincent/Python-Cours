import os
from utils.ip_utils import identify_ip_version, validate_ip_list, validate_ip_dict
from utils.file_utils import replace_letters_in_file, file_to_dict, display_file_dict


def get_user_ip():
    """
    Demande à l'utilisateur de saisir une adresse IP et retourne cette adresse.
    """
    ip = input("Veuillez saisir une adresse IP (IPv4 ou IPv6) : ")
    print(f"Adresse IP saisie : {ip}")
    return ip


def print_section_title(title: str):
    """
    Affiche un titre de section bien formaté avec une ligne de séparation.
    """
    print(f"\n{'-' * 20} {title} {'-' * 20}\n")


def main():
    """
    Fonction principale qui coordonne l'exécution des différentes actions : 
    - Validation de l'IP
    - Remplacement de lettres dans un fichier
    - Affichage du contenu du fichier sous forme de dictionnaire
    """
    # Question 1 : Validation d'une adresse IP (Try-Except)
    print_section_title("Question 1 : Validation de l'adresse IP")
    ip = '123.21' #get_user_ip()
    print(identify_ip_version(ip))

    # Question 2 - 3 - 4 : Manipulation du fichier
    print_section_title("Question 2: Manipulation du fichier")
    file_path = "./assets/test"
    if not os.path.exists(file_path):
        print(f"Le fichier {file_path} n'a pas été trouvé.")
        return

    # Remplacement des lettres dans le fichier
    print("Remplacer les lettres Z par X dans le fichier...")
    replace_letters_in_file(file_path, "z")

    # Lecture du fichier et conversion en dictionnaire
    print_section_title("Question 3: Lecture du fichier et conversion en dictionnaire")
    file_dict = file_to_dict(file_path)

    # Affichage du contenu du fichier sous forme de dictionnaire
    print_section_title("Question 4: Affichage du contenu du fichier sous forme de dictionnaire")
    display_file_dict(file_dict)


if __name__ == "__main__":
    main()