import os
import random
import json

roles_possibles = [
    #de 6 à 8 joueurs
    [
        "Villageois", "Loup-Garou", "Sorcière",
        "Voyante", "Chasseur", "Loup-Garou",
        "Villageois", "Villageois"
    ],
    #de 9 à 11 joueurs
    [
        "Villageois", "Loup-Garou", "Sorcière", "Villageois",
        "Voyante", "Loup-Garou", "Chasseur", "Villageois",
        "Loup-Garou", "Villageois", "Cupidon"
    ],
    #de 12 à 15 joueurs
    [
        "Villageois", "Villageois", "Loup-Garou", "Sorcière", "Villageois",
        "Voyante", "Loup-Garou", "Chasseur", "Villageois",
        "Loup-Garou", "Villageois", "Cupidon", "Voleur", "Petite Fille",
        "Loup-Garou", "Villageois"
    ]
]

def afficher_menu():
    print("Menu :")
    print("0 - Quitter")
    print("1 - Inscrire joueur")
    print("2 - Règles du jeu")
    print("3 - Rôles")
    choix = input("Votre choix ? ")
    return choix

def charger_dossier(fichier: str) -> dict[str, str]:
    dossier: dict[str, str] = {}
    if os.path.exists(fichier):
        with open(fichier, "r") as f:
            for ligne in f:
                if "," in ligne:
                    numero, reg = ligne.strip().split(",", 1)
                    dossier[numero] = reg
    return dossier

def inscription(fichier_json: str, roles_possibles: list[list[str]]):
    nb_joueurs = int(input("Nombre de joueurs (entre 6 et 15) : "))
    try:
        with open(fichier_json, 'r') as f:
            joueurs = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        joueurs = []

    role_array = 0

    if 9 <= nb_joueurs <= 11:
            role_array = 1
    elif 12 <= nb_joueurs <= 15:
            role_array = 2
    elif not 6 <= nb_joueurs <= 8:
        print("Il y a trop ou pas assez de joueur. Nombre de joueur " + \
            "minimum : 6 ; nombre de joueur maximum : 15")
        return # On évite l'écriture inutile du fichier en arrêtant la fonction

    for i in range(nb_joueurs):
        nom = input(f"Nom du joueur {i+1} : ")
        role = random.choice(roles_possibles[0])
        roles_possibles[role_array].remove(role)
        statut = "Vivant"

        joueur = {
            "nom": nom,
            "role": role,
            "statut": statut
        }
        joueurs.append(joueur)
        print(f"{nom} a été inscrit avec son rôle {role}.")  # Affiche le rôle à chaque inscription

    # Sauvegarde tous les joueurs à la fin, une seule fois
    with open(fichier_json, "w") as f:
        json.dump(joueurs, f, indent=4)

def roles(fichier: str):
    roles_pers = charger_dossier(fichier)
    roles_available = ", ".join(roles_pers.keys())

    print(f"Les rôles possibles sont : {roles_available}")
    mot = input("Rôles à consulter : ").capitalize() # Le capitalize permet de ne mettre en majuscule que la première lettre de la chaîne (cela permet d'ignorer la casse)
    if mot in roles_pers:
        print(f"{mot} : {roles_pers[mot]}")
    else:
        print("Ce rôle n'existe pas")

def rec_reg(fichier: str):
    regles = charger_dossier(fichier)
    parts = ", ".join(list(regles.keys()))

    print(f"Les parties possibles sont : {parts}")
    mot = input("Consulter les règles pour la partie : ") # Le capitalize permet de ne mettre en majuscule que la première lettre de la chaîne (cela permet d'ignorer la casse)
    if mot in regles:
        print(f"{mot} : {regles[mot]}")
    else:
        print("Il n'existe pas de règles comportant ce mot")
