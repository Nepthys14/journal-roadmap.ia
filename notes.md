```markdown
# Notes — Projet 3 : Journal Roadmap IA

## But de l'étape 3

Le but de cette étape était d'apprendre à utiliser Python pour créer un petit programme utile avec des fichiers. Avant cette étape, je connaissais déjà les bases comme les variables, les conditions, les boucles et les fonctions simples. Avec ce projet, j'ai commencé à utiliser Python pour sauvegarder et relire de vraies données.

## Ce que j'ai appris

### 1. Les fichiers

J'ai appris à ouvrir un fichier avec `open()`.

Les modes importants sont :

```python
"r"  # read / lire
"w"  # write / écrire en effaçant l'ancien contenu
"a"  # append / ajouter à la fin

Le mode "a" est important parce qu'il permet d'ajouter une nouvelle entrée sans effacer les anciennes.

Exemple :

with open("journal.txt", "a", encoding="utf-8") as fichier:
    fichier.write("Nouvelle entrée\n")
2. with open(...)

J'ai appris qu'on utilise souvent with open(...) parce que Python ferme automatiquement le fichier après l'utilisation. C'est plus propre et plus sécuritaire que d'ouvrir et fermer manuellement un fichier.

Exemple :

with open("journal.txt", "r", encoding="utf-8") as fichier:
    contenu = fichier.read()
3. Les erreurs

J'ai appris à utiliser try et except pour éviter que le programme crash.

Exemple :

try:
    with open("journal.txt", "r", encoding="utf-8") as fichier:
        contenu = fichier.read()
except FileNotFoundError:
    print("Aucun journal trouvé.")

FileNotFoundError arrive quand Python essaie d'ouvrir un fichier qui n'existe pas.

4. Les variables ne restent pas après la fermeture du programme

J'ai compris que quand le programme se ferme, les variables sont perdues. Par exemple, une variable comme name = "journal" existe seulement pendant que le programme roule. Donc si je veux garder une information après la fermeture, je dois la sauvegarder dans un fichier.

C'est pour ça que j'ai créé sauvegarde.txt. Ce fichier garde le nom du journal actuel.

5. Sauvegarder le nom du journal

J'ai appris à utiliser un fichier pour garder une préférence ou une donnée importante.

Exemple :

with open("sauvegarde.txt", "w", encoding="utf-8") as fichier:
    fichier.write(f"Nom:{name}")

Le mode "w" est utile ici parce que je veux remplacer l'ancien nom par le nouveau.

6. Lire plusieurs lignes

J'ai appris à lire un fichier et à le séparer en lignes.

Exemple :

lignes = contenu.splitlines()

Ça permet de vérifier chaque ligne une par une.

Exemple :

for ligne in lignes:
    if ligne.startswith("Heures:"):
        nombre = ligne.replace("Heures:", "").strip()
        nombre = float(nombre)
7. Calculer le total des heures

Pour calculer les heures, il faut lire le fichier, trouver les lignes qui commencent par Heures:, enlever le texte Heures:, transformer le résultat en nombre avec float() et additionner avec total.

Exemple :

total = total + nombre
8. Afficher la dernière session

J'ai appris à utiliser split() pour séparer les sessions.

Exemple :

sessions = contenu.split("----------------")

Le problème rencontré était que si le fichier finissait par "----------------", la dernière partie pouvait être vide. La solution est d'ignorer les sessions vides avant de prendre la dernière.

9. Organisation avec les fonctions

J'ai séparé mon code en fonctions comme ecrire(), lire(), rappel(), supprime(), nom(), NbSessions(), NbHeures(), dernieresession() et ouverture().

C'est mieux que de tout mettre dans un seul gros bloc. Chaque fonction a une responsabilité précise.

Problèmes rencontrés
Problème 1 — Le nom du journal disparaissait

Quand je fermais le programme, la variable name revenait à sa valeur de départ. La solution a été de sauvegarder le nom dans sauvegarde.txt, puis de le relire avec rappel().

Problème 2 — La dernière session affichait mal

La fonction utilisait :

sessions = contenu.split("----------------")
derniere = sessions[-1]

Mais si la dernière partie était vide, ça affichait une entrée vide. La solution a été de nettoyer la liste et d'enlever les éléments vides.

Problème 3 — Le total d'heures comptait mal au début

Au début, le programme ne gardait pas bien le total. J'ai compris qu'il fallait mettre total = 0 avant la boucle, puis additionner chaque ligne Heures: trouvée dans le fichier.

Ce que je dois retenir

Je dois retenir que "r" sert à lire, "w" sert à écrire en effaçant l'ancien contenu et "a" sert à ajouter à la fin. append() ajoute un élément dans une liste. try et except évitent que le programme crash. Les variables disparaissent quand le programme se ferme. Pour garder une donnée, il faut la sauvegarder dans un fichier. Les fonctions rendent le code plus clair. split() sépare un texte. strip() enlève les espaces et les retours à la ligne autour d'un texte. float() transforme du texte en nombre à virgule.

Ce que je pourrais améliorer plus tard

Plus tard, je pourrais utiliser un fichier .json au lieu d'un fichier .txt, ajouter une vraie interface graphique, ajouter une option pour modifier une entrée, ajouter une option pour exporter les stats, ajouter une moyenne d'heures par session, ajouter une recherche par date ou par tâche et sauvegarder plusieurs journaux différents plus proprement.

Validation de l'étape 3

Je considère l'étape 3 réussie si je suis capable d'ajouter une entrée, de lire l'historique, d'afficher la dernière entrée, de compter le nombre d'entrées, de calculer le total d'heures, de renommer le journal, de sauvegarder le nom du journal, de gérer les erreurs si un fichier n'existe pas et d'expliquer les fonctions principales de mon code