from datetime import datetime
import os
name = "journal"

def ecrire (tache,heures):
    global name
    try:
        comptes = int(NbSessions()) + 1
    except(FileNotFoundError):
        comptes = 1
    date = datetime.now().strftime("%Y-%m-%d")

    rappel()
    with open(f"{name}.txt","a",encoding="utf-8") as fichier:
        fichier.write(f"Nom: {name}\n\n")
        fichier.write(f"Entré: {comptes}\n\n")
        fichier.write(f"Tâches: {tache}\n")
        fichier.write(f"Heures: {heures}\n")
        fichier.write(f"Date: {date}\n")
        fichier.write("""
        -----------------

        """)


def lire():
    global name
    rappel()
    try:
        with open(f"{name}.txt","r",encoding="utf-8") as fichier:
            contenu = fichier.read()
            print(contenu)
    except FileNotFoundError:
        print("Aucun journal trouvé.")

def rappel():
    global name
    try:
        with open("sauvegarde.txt","r") as fichier:
                contenu = fichier.read()
                lignes = contenu.splitlines()
                ligne = lignes[-1]
                if ligne.startswith("Nom:"):
                    nom = ligne.replace("Nom:","")
                    nom = nom.strip()
                    name = nom
    except(FileNotFoundError):
        print("Erreur. Fichier de sauvegarde non trouvé.")

def supprime():
    global name
    supprimer = int(input("Êtes-vous certain de vouloir supprimer le journal?\n1.OUI\n2.NON"))
    while supprimer != 1.5:
        try:
            if supprimer == 1:
                try:
                    rappel()
                    os.remove(f"{name}.txt")
                    print("Journal supprimé!")
                    supprimer = float(1.5)
                    os.remove("sauvegarde.txt")
                except(FileNotFoundError):
                    print("Aucun journal à supprimer.")
            elif supprimer == 2:
                print("Suppression annulé.")
                supprimer = float(1.5)
            else:
                print("Veullez choisir entre un et deux.")
                supprimer = int(input("Êtes-vous certain de vouloir supprimer le journal?\n1.OUI\n2.NON "))
        except(ValueError):
            print("Veullez choisir entre un et deux.")
            supprimer = int(input("Êtes-vous certain de vouloir supprimer le journal?\n1.OUI\n2.NON "))

def nom():
    global name
    renommer = int(input("Êtes-vous certain de vouloir renommer le journal?\n1.OUI\n2.NON"))
    while renommer != 1.5:
        try:
            if renommer == 1:
                rappel()
                oldname = name
                name = input("Veuillez entrer le nouveau nom du journal. ")
                try:
                    os.rename(f"{oldname}.txt",f"{name}.txt")
                    with open("sauvegarde.txt","a",encoding="utf-8") as fichier:
                        fichier.write(f"\nNom:{name}\n")
                    print("Journal renommé!")
                    renommer = float(1.5)
                except(FileNotFoundError):
                    print("Aucun journal à rennomeré")
            elif renommer == 2:
                print("Annulation.")
                renommer = float(1.5)
            else:
                print("Veullez choisir entre un et deux.")
                renommer = int(input("Êtes-vous certain de vouloir rennomer le journal?\n1.OUI\n2.NON"))
        except(ValueError):
            print("Veullez choisir entre un et deux.")
            renommer = int(input("Êtes-vous certain de vouloir rennomer le journal?\n1.OUI\n2.NON"))

def NbSessions():
    global name
    try:
        rappel()
        with open(f"{name}.txt","r",encoding="utf-8") as fichier:
            contenu = fichier.read()
            compte = contenu.count("Entré:")
    except(FileNotFoundError):
        print("Aucune entrée.")
        compte = 0
    return compte

def NbHeures():
    global name
    try:
        rappel()
        with open(f"{name}.txt","r",encoding="utf-8") as fichier:
            contenu = fichier.read()
            lignes = contenu.splitlines()
            total = 0
            for ligne in lignes:
                if ligne.startswith("Heures:"):
                    nombre = ligne.replace("Heures:","")
                    nombre = nombre.strip()
                    nombre = float(nombre)
                    total = total + nombre
    except(FileNotFoundError):
        print("Aucun journal.")
    return total

def dernieresession():
    global name
    try:
        rappel()
        with open(f"{name}.txt", "r", encoding="utf-8") as fichier:
            contenu = fichier.read()

        sessions = contenu.split("----------------")
        sessions = [session.strip() for session in sessions if session.strip() != ""]

        print(sessions[-1])

    except FileNotFoundError:
        print("Aucun journal.")
    except IndexError:
        print("Aucune entrée dans le journal.")

def ouverture():
    choix = ""

    while choix !=3:
        print("""
        1.Ajouter une entrée.
        2.Voir l'historique.
        3.Quitter.
        4.Supprimer le journal.
        5.Renommer le journal.
        6.Lire la dernière entrée.
        7.Afficher les stats
              """)
        
        choix = int(input("Choississer une option: "))
        if choix == 1:
            tache = input("Qu'as tu travaillé aujourd'hui?")
            heures = float(input("Combien d'heure as tu travailler aujourd'hui?"))
            ecrire(tache,heures)
        elif choix == 2:
            lire()
        elif choix == 3:
            print("À la prochaine!")
        elif choix == 4:
            supprime()
        elif choix == 5:
            nom()  
        elif choix == 6:
            dernieresession()
        elif choix == 7:
            compte = NbSessions()
            heures = NbHeures()
            print(f"Votre journal contient {compte} entrée.")
            print(f"Vous avez travaillé un total de {heures} heures.")
        else:
            print("Option invalide")
ouverture()


    