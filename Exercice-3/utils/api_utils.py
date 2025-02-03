import requests

def fetch_api_data(url: str, method: str = "GET", payload: dict = None) -> dict:
    """
    Effectue une requête GET ou POST à une API et retourne les données en format dictionnaire.
    Gère les erreurs 4xx en affichant un message d'erreur.
    """
    try:
        response = requests.request(method.upper(), url, json=payload)
        
        if response.status_code >= 400:
            print(f"Erreur {response.status_code} : Impossible de récupérer les données.")
            return {}

        return response.json()  

    except requests.RequestException as e:
        print(f"Erreur lors de la requête API : {e}")
        return {}
