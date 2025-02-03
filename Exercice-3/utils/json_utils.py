import json

def export_to_json(data: dict, output_file: str):
    """
    Exporte des données dans un fichier JSON.
    """
    try:
        with open(output_file, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)
        print(f"Données exportées en JSON sous : {output_file}")

    except Exception as e:
        print(f"Erreur lors de l'export en JSON : {e}")
