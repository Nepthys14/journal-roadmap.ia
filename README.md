# Journal Roadmap IA

Petit programme Python créé dans le cadre de l'étape 3 de ma roadmap IA.

Ce projet sert à suivre mes sessions de travail/apprentissage en programmation et en IA.  
Il permet d'ajouter des entrées dans un journal, de lire l'historique, de voir la dernière session, de calculer le nombre total d'entrées et de compter le total d'heures travaillées.

## Objectif du projet

L'objectif était de pratiquer les bases de Python appliquées à un vrai petit outil :

- lecture et écriture de fichiers;
- ajout de texte sans effacer l'ancien contenu;
- gestion d'erreurs avec `try` / `except`;
- utilisation de modules comme `datetime` et `os`;
- organisation du code avec des fonctions;
- sauvegarde d'une donnée importante entre deux lancements du programme.

## Fonctionnalités

Le programme permet de :

1. Ajouter une entrée dans le journal.
2. Voir tout l'historique.
3. Quitter le programme.
4. Supprimer le journal.
5. Renommer le journal.
6. Lire la dernière entrée.
7. Afficher des statistiques :
   - nombre total d'entrées;
   - nombre total d'heures travaillées.

## Fichiers du projet

- `journal_roadmap.py` : fichier principal du programme.
- `sauvegarde.txt` : fichier qui garde en mémoire le nom du journal actuel.
- `journal.txt` ou autre nom choisi : fichier contenant les entrées du journal.
- `README.md` : présentation du projet.
- `notes.md` : notes personnelles sur ce que j'ai appris.

## Ce que j'ai appris

Pendant ce projet, j'ai appris à :

- utiliser `open()` avec les modes `"r"`, `"w"` et `"a"`;
- comprendre que les variables disparaissent quand le programme se ferme;
- sauvegarder une information dans un fichier pour la récupérer plus tard;
- utiliser `FileNotFoundError` pour éviter que le programme crash;
- découper un programme en plusieurs fonctions;
- lire un fichier ligne par ligne;
- extraire des nombres à partir de texte;
- additionner les heures enregistrées;
- utiliser `split()` pour séparer les différentes sessions.

## Exemple d'entrée sauvegardée

```text
Nom: journal

Entrée: 1

Tâches: Apprendre les fichiers en Python

Heures: 1.5

Date: 2026-05-21

----------------

Problèmes rencontrés

Un problème important était que la variable contenant le nom du journal revenait à sa valeur par défaut quand le programme était fermé. Pour régler ça, j'ai créé un fichier sauvegarde.txt qui garde le nom du journal. Au lancement du programme, une fonction lit ce fichier pour retrouver le dernier nom utilisé.

Un autre problème était l'affichage de la dernière session. Le programme séparait les sessions avec split(), mais comme le fichier finissait par une ligne de séparation, la dernière partie pouvait être vide. La solution est d'ignorer les sessions vides avant d'afficher la dernière vraie entrée.

Comment lancer le programme

Dans le terminal, utiliser :

python journal_roadmap.py

ou selon la configuration :

py journal_roadmap.py
Statut du projet

Projet terminé pour l'étape 3 de la roadmap IA. Ce projet valide les bases pratiques de Python avec les fichiers, les erreurs, les fonctions et la sauvegarde de données simples.
