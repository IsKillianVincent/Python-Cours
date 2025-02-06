# Jeu de cartes FastAPI

## Description du projet
Cette API permet de :
- Générer un paquet de __52__ cartes mélangé.
- Distribuer ces cartes à __X__ joueurs de manière équitable.

Elle est construite avec **FastAPI** et utilise **Peewee** pour la gestion de la base de données.

## **Architecture du projet**
L'application est divisée en plusieurs modules pour une meilleure organisation :
- **`api/routes.py`** : Gère les endpoints de l’API.
- **`models/`** : Contient les modèles de la base de données (Card, Player).
- **`services/`** : Gère la logique métier (Deck, Distribution).

## **Installation et exécution**
### Prérequis
- Python
- FastAPI
- Uvicorn
- Peewee

### Installation
```bash
git clone https://github.com/votre-repo.git
```
```bash
cd Exercice-8
```
```bash
pip install -r requirements.txt
```

### Démarrer l'application
```bash
uvicorn main:app --reload
```

## Patron de Conception : Méthod Fabrique 

### Pourquoi Méthod Fabrique  ?

Encapsulation de la création des objets :
 - Deck crée automatiquement les 52 cartes.
 - Distributor gère la distribution sans exposer directement les cartes.

Réutilisabilité et évolutivité :
 - Facile d'ajouter des cartes spéciales ou d'autres types de jeux.

Séparation des responsabilités :
 - Card gère une seule carte.
 - Deck gère un paquet entier.
 - Distributor distribue aux joueurs.

## Requêtes
|Méthode|Route|Description|
|---|---|---|
|GET|/deck|Récupère le paquet de cartes|
|GET|/shuffle|Mélange les cartes|
|GET|/distribute/{num_players}|Distribue les cartes entre les joueurs|

## Pourquoi Méthod Fabrique  ?
- Encapsulation de la logique de création :
    - La classe 'Deck' crée automatiquement les 52 cartes.
    - La classe 'Distributor' gère la distribution sans exposer directement la liste de cartes.
- Réutilisabilité et évolutivité :
    - Si on veut ajouter des cartes spéciales ou autres types de jeux de cartes, on pourra facilement étendre les classes existantes.
- Sapération des responsabilités :
    - 'Card' gère les propriétés d’une carte.
    - 'Deck' gère la gestion du paquet.
    - 'Distributor' gère la répartition des cartes entre les joueurs.
