from Menu import afficher_menu, rec_reg, roles, inscription, roles_possibles

def main():
    fichier_json = "Joueurs.json"
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
            pass
        else:
            print("Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()
    