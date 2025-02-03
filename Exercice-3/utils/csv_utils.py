import csv

def modify_csv(input_file: str, output_file: str, modification_func):
    """
    Charge un fichier CSV, modifie son contenu avec modification_func et sauvegarde un fichier modifié.
    """
    try:
        with open(input_file, mode='r', encoding='utf-8') as infile, \
             open(output_file, mode='w', encoding='utf-8', newline='') as outfile:
            
            reader = csv.reader(infile)
            writer = csv.writer(outfile)
            
            for row in reader:
                modified_row = modification_func(row)
                writer.writerow(modified_row)
        
        print(f"Fichier modifié sauvegardé sous : {output_file}")

    except FileNotFoundError:
        print(f"Erreur : Le fichier {input_file} n'existe pas.")
    except Exception as e:
        print(f"Erreur lors du traitement du fichier CSV : {e}")

def export_to_csv(data: dict, output_file: str):
    """
    Exporte des données dans un fichier CSV avec des noms de colonnes.
    """
    try:
        with open(output_file, mode="w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            
            if isinstance(data, dict):
                headers = ["Clé", "Valeur"]
                writer.writerow(headers)
                
                for key, value in data.items():
                    writer.writerow([key, value])

            print(f"Données exportées en CSV sous : {output_file}")

    except Exception as e:
        print(f"Erreur lors de l'export en CSV : {e}")

# Exemple de modification : convertir en majuscules
def uppercase_row(row):
    return [cell.upper() for cell in row]
