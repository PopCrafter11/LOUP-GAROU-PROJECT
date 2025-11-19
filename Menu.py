import os
import random
import json
import time

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
    print("4 - Lancer la partie")
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
    nbv, nblp = 0, 0
    nb = 2
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
        role = random.choice(roles_possibles[role_array])
        
        if role in roles_possibles[role_array]:
            roles_possibles[role_array].remove(role)
        
        else:
            print(f"Erreur : le rôle {role} n'est pas dans la liste.")
        
        if role == "Villageois":
            nbv += 1
        elif role == "Loup-Garou":
            nblp += 1
        else:
            nb += 1

        statut = "Vivant"

        joueur = {
            "nom": nom,
            "role": role,
            "statut": statut
        }
        joueurs.append(joueur)

        # Demande d'appuyer sur Entrée avant de révéler le rôle pour être un peu plus secret hihi ^^"
        input(f"{nom}, appuie sur Entrée pour découvrir ton rôle en toute discrétion...")
        # Affiche le rôle à chaque inscription
        print(f"{nom} a été inscrit avec son rôle {role}.")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')

    print(f"Il y a {nb} rôles différents dont {nbv} villageois et {nblp} Loup-Garou(s).")
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
    # Sauvegarde tous les joueurs à la fin, une seule fois
    with open(fichier_json, "w") as f:
        json.dump(joueurs, f, indent=4)

    return nbv, nblp

def roles(fichier: str):
    roles_pers = charger_dossier(fichier)
    roles_available = ", ".join(roles_pers.keys())

    print(f"Les rôles possibles sont : {roles_available}")
    # Le capitalize permet de ne mettre en majuscule que 
    # la première lettre de la chaîne (cela permet d'ignorer la casse)
    mot = input("Rôles à consulter : ").capitalize()
    
    if mot in roles_pers:
        print(f"{mot} : {roles_pers[mot]}")
    
    else:
        print("Ce rôle n'existe pas")

def rec_reg(fichier: str):
    regles = charger_dossier(fichier)
    mot = input("mot à chercher : ").capitalize
    
    if mot in regles:
        print(f"{mot} : {regles[mot]}")
    
    else:
        print("Il n\'existe pas de règles comportant ce mot")