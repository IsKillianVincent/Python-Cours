# Card Game API
API FastAPI pour la gestion d'un paquet de cartes et la distribution aux joueurs.

## Description du projet
Cette API permet de :
- Générer un paquet de __52__ cartes mélangé.
- Distribuer ces cartes à __X__ joueurs de manière équitable.

Elle est construite en FastAPI, avec une architecture propre et modulaire.

## Patron de Conception Utilisé : Factory Method
Ce projet applique le patron de conception de [Fabrique](https://refactoring.guru/fr/design-patterns/factory-method) pour la création des objets 'Card', 'Deck', et 'Distributor'.

## Pourquoi Factory Method ?
- Encapsulation de la logique de création :
    - La classe 'Deck' crée automatiquement les 52 cartes.
    - La classe 'Distributor' gère la distribution sans exposer directement la liste de cartes.
- Réutilisabilité et évolutivité :
    - Si on veut ajouter des cartes spéciales ou autres types de jeux de cartes, on pourra facilement étendre les classes existantes.
- Sapération des responsabilités :
    - 'Card' gère les propriétés d’une carte.
    - 'Deck' gère la gestion du paquet.
    - 'Distributor' gère la répartition des cartes entre les joueurs.
