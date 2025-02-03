import fileinput
import os

def replace_letters_in_file(file_path: str, letters_to_replace: str):
    """
    Remplace certaines lettres dans un fichier donné et affiche les modifications.

    :param file_path: Chemin du fichier à modifier.
    :param letters_to_replace: Lettres à remplacer par 'x'.
    """
    try:
        # Vérification de l'existence du fichier
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Le fichier {file_path} n'existe pas.")
        
        # Traitement du fichier ligne par ligne
        with fileinput.FileInput(file_path, inplace=True, backup='.bak') as file:
            for line in file:
                original_line = line
                # Remplacer les lettres spécifiées par 'x'
                for letter in letters_to_replace:
                    line = line.replace(letter, 'x')
                # Affichage de la modification effectuée
                if line != original_line:
                    print(f"Modification : {original_line.strip()} → {line.strip()}")
                # Sauvegarde de la ligne modifiée
                print(line, end='')

    except FileNotFoundError as e:
        print(f"Erreur : {str(e)}")
    except Exception as e:
        print(f"Erreur lors du traitement du fichier : {str(e)}")


def file_to_dict(file_path: str) -> dict:
    """
    Lit un fichier et le convertit en un dictionnaire où la clé est le numéro de ligne et la valeur est le contenu de la ligne.

    :param file_path: Chemin du fichier à lire.
    :return: Un dictionnaire représentant les lignes du fichier.
    """
    try:
        # Vérification de l'existence du fichier
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Le fichier {file_path} n'existe pas.")
        
        with open(file_path, 'r', encoding='utf-8') as file:
            # Création d'un dictionnaire où les clés sont les numéros de ligne
            return {i + 1: line.strip() for i, line in enumerate(file.readlines())}
    
    except FileNotFoundError as e:
        print(f"Erreur : {str(e)}")
        return {}
    except PermissionError:
        print(f"Erreur : Permission refusée pour accéder à {file_path}.")
        return {}
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {str(e)}")
        return {}


def display_file_dict(file_dict: dict):
    """
    Affiche le contenu du dictionnaire de lignes sous un format lisible.

    :param file_dict: Dictionnaire contenant les lignes du fichier.
    """
    if not file_dict:
        print("Le dictionnaire est vide ou une erreur est survenue.")
        return

    # Affichage de chaque ligne du fichier avec son numéro et sa longueur
    for line_num, content in file_dict.items():
        print(f"Ligne numéro {line_num} : {len(content)} caractères → \"{content}\"")
