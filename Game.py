import os
import random
import json
import time
from Menu import nbv, nblp

def sorciere():
        pass
#faire les potions, et les supprimer si déjà utilisées
def election():
        pass
def voleur():
        pass
#interchanger les rôles entre le voleur et un joueur, joue qu'une fois, et discours même si abs
# if voleur in or not in (fichier_json[i][2]) :
#       print("nanannannanaifjkehdcimsudtesud")

def tour1(fichier_json, a: int):
        for i in range(len(fichier_json)):

                if fichier_json[i][2] == "voleur" in fichier_json:

                        print("C'est la nuit, tout le village s'endort, " \
                        "les joueurs ferment les yeux." \
                        "Le voleur se réveille !")
        
                        reponse = input("Avec qui veux tu échanger ta carte : ")

                        print("Le voleur regarde la carte qu'il a volé et se rendort, ensuite," \
                        "la personne qui s'est fait volé sa carte se réveille et regarde son rôle.")
                        #fonction qui va échanger le rôle du voleur, avec le volé
                
                elif fichier_json[i][2] == "cupidon" in fichier_json:
                       
                        print("Cupidon se réveille !")
        
                        amoureux1 = input("Désigne le premier amoureux :")
                        amoureux2 = input("désigne le second amoureux : ")

                        #fonction qui va lier 2 personnes ensemble

                        print("Cupidon se rendort. Les 2 amoureux se réveillent, se regardent et tombe amoureux" \
                        "l'un pour l'autre, puis ils se rendorment")
                        
#cupidon, voleur, maire, normal


def demarrer(fichier_json, a: int):
        
        a += 1
        
        if a == 1:
                tour1(fichier_json, a)
        
        for i in range(len(fichier_json)):
        
        

                print("La voyante se réveille, et désigne un joueur dont \
                elle veut sonder la véritable personnalité !")
        
        reponse2 = input("De quel joueur souhaites-tu connaître la véritable identité ? : ")

        print("Voici le rôle de", reponse2, ": ", "La voyante se rendort")

        print("les Loups-Garous se réveillent, se reconnaissent et désignent une nouvelle victime !")

        reponse3 = input("Qui voulez-vous tuer ce soir : ")

        #fonction qui va tuer la personne (changer son statut)

        print("Les Loups-garous se rendorment")

        print("La Sorcière se réveille, voici la victime des Loups-Garous.")

        reponse4 = input("Veux-tu la Soigner, ne rien faire (neutre), ou Tuer quelqu'un : ")

        # soit faire une fonction qui gère les 3 réponses différentes, soit faire 3 fonctions différentes
        if reponse4 == "Soigner" :
                pass
        elif reponse4 == "Neutre":
                pass
        elif reponse4 == "Tuer":
                pass
        else:
                print("Ce choix n'existe pas.")

        print("c'est le matin, le village se réveille, tout le monde se réveille et ouvre les yeux…")
        
        if reponse4 == "Soigner" :
                print("Une personne a été tuée, mais elle fût sauvée par la socière.")

        elif reponse4 == "Tuer":
                print(reponse3, "a été tué(e) par les loups, ainsi que", None,", tué(e) par la sorcière.")

        else:
                print(reponse3, "a été tué(e) cette nuit")
        
        print("Il est maintenant l'heure de débattre et de laisser vos instincts où vos rôles désigner une personne à exécuter")
        
        execution = input("Personne à exécuter : ")

        #fonction qui change le statut de la personne

        print("Il est l'heure d'élire un maire")
        maire = election()
