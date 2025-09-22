from Menu import afficher_menu, rec_reg, roles, inscription, roles_possibles
from Game import demarrer
import os

def main():
    
    print(f"Suppression de la sauvegarde précédente...")
    fichier_json = "Joueurs.json"

    with open("Joueurs.json", "w") as f:
        f.write("[]") 
        print(f'Sauvegarde précédente supprimée..!')
        os.system('cls' if os.name == 'nt' else 'clear')

    while True:
        choix = afficher_menu()
        print(f"DEBUG: choix = '{choix}'")
        
        if choix == "0":
            print("Programme terminé.")
            break
        
        elif choix == "1":
            inscription(fichier_json, roles_possibles)
        
        elif choix == "2":
            rec_reg("regles.txt")
        
        elif choix == "3":
            roles("roles.txt")
        
        elif choix == "4":
            demarrer(fichier_json)
        
        else:
            print("Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()