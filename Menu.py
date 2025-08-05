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
    print('Menu :')
    print("0 - Quitter")
    print("1 - inscrire joueur")
    print("2 - Règles du jeu")
    print("3 - Rôles")
    choix = input("Votre choix ? ")
    return choix

def charger_dossier(fichier):
    dossier = {}
    if os.path.exists(fichier):
        with open(fichier, 'r') as f:
            for ligne in f:
                if ',' in ligne:
                    numero, reg = ligne.strip().split(',', 1)
                    dossier[numero] = reg
    return dossier

def inscription(fichier_json, roles_possibles):
    nb_joueurs = int(input("Nombre de joueurs : "))
    try:
        with open(fichier_json, 'r') as f:
            joueurs = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        joueurs = []
    
    if 6 <= nb_joueurs <= 8:
        for i in range(nb_joueurs):
            nom = input(f"Nom du joueur {i+1} : ")
            role = random.choice(roles_possibles[0])
            roles_possibles[0].remove(role)
            statut = "Vivant"

            joueur = {
                "nom": nom,
                "role": role,
                "statut": statut
            }
            joueurs.append(joueur)
            print(f"{nom} a été inscrit avec son rôle {role}.")  # Affiche le rôle à chaque inscription
    
    elif 9 <= nb_joueurs <= 11:
        for i in range(nb_joueurs):
            nom = input(f"Nom du joueur {i+1} : ")
            role = random.choice(roles_possibles[1])
            roles_possibles[1].remove(role)
            statut = "Vivant"

            joueur = {
                "nom": nom,
                "role": role,
                "statut": statut
            }
            joueurs.append(joueur)
            print(f"{nom} a été inscrit avec son rôle {role}.")  # Affiche le rôle à chaque inscription
    
    elif 12 <= nb_joueurs <= 15:
        for i in range(nb_joueurs):
            nom = input(f"Nom du joueur {i+1} : ")
            role = random.choice(roles_possibles[2])
            roles_possibles[2].remove(role)
            statut = "Vivant"

            joueur = {
                "nom": nom,
                "role": role,
                "statut": statut
            }
            joueurs.append(joueur)
            print(f"{nom} a été inscrit avec son rôle {role}.")  # Affiche le rôle à chaque inscription
    
    else:
        print("Il y a trop ou pas assez de joueur. Nombre de joueur" \
        "minimum : 6 ; nombre de joueur maximum : 15")

    # Sauvegarde tous les joueurs à la fin, une seule fois
    with open(fichier_json, 'w') as f:
        json.dump(joueurs, f, indent=4)
                                      
def roles(fichier):
    roles_pers = charger_dossier(fichier)
    mot = input("Rôles à chercher : ")
    if mot in roles_pers:
        print(f"{mot} : {roles_pers[mot]}")
    else:
        print("Ce rôle n\'existe pas")

def rec_reg(fichier):
    regles = charger_dossier(fichier)
    mot = input("mot à chercher : ")
    if mot in regles:
        print(f"{mot} : {regles[mot]}")
    else:
        print("Il n\'existe pas de règles comportant ce mot")