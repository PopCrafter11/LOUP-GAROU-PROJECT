import os
import random
import json
import time

def demarrer():
        
        print("C'est la nuit, tout le village s'endort, " \
        "les joueurs ferment les yeux." \
        "Le voleur se réveille !")
        
        reponse = input("Avec qui veux tu échanger ta carte : ")
        
        print("Le voleur regarde la carte qu'il a volé et se rendort, ensuite," \
        "la personne qui s'est fait volé sa carte se réveille et regarde son rôle.")
        
        print("Cupidon se réveille !")
        
        amoureux1 = input("Désigne le premier amoureux :")
        amoureux2 = input("désigne le second amoureux : ")

        print("Cupidon se rendort. Les 2 amoureux se réveillent, se regardent et tombe amoureux" \
        "l'un pour l'autre, puis ils se rendorment")

        print("La voyante se réveille, et désigne un joueur dont \
              elle veut sonder la véritable personnalité !")
        
        reponse2 = input("De quel joueur souhaites-tu connaître la véritable identité ? : ")

        print("Voici le rôle de", reponse2, ": ", "La voyante se rendort")

        print("les Loups-Garous se réveillent, se reconnaissent et désignent une nouvelle victime !")

        reponse3 = input("Qui voulez-vous tuer ce soir : ")

        print("Les Loups-garous se rendorment")

        print("La Sorcière se réveille, voici la victime des Loups-Garous.")

        reponse4 = input("Veux-tu la Soigner, ne rien faire (neutre), ou Tuer quelqu'un : ")

        if reponse4 == "Soigner" :
                pass
        elif reponse4 == "Neutre":
                pass
        elif reponse4 == "Tuer":
                pass
        else:
                print("Ce choix n'existe pas.")

        