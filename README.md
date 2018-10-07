# Nettools
## Cadre du projet
Ce dépot est un mini projet dont l'objectif est de fournir une petite suite d'outils de diagnostic réseau. Il ne s'agit pas cependant de réaliser un logiciel sophistiqué pour un usage pratique, mais de fournir une base permettant à des personnes apprenant python (testé avec des BTS 1ère année, après un mois de cours) de réaliser un mini-projet sans que ce soit un exercice purement académique.
En effet, on cherche à fournir un probleme intéréssant, ayant une application pratique réelle, et fournissant un cadre permettant de découvrir divers outils et techniques (git, json, etc).

## Comment utiliser ce projet?
Ce projet à vocation à ne pas être complet. De fait, pour s'en servir, il faut réaliser un fork, et compléter, modifier et étendre le code afin de réaliser les objectifs.
Une fonction est fournie pour tester un hote, `host_up(host)`, qui lance un ping dans un sous-processus.

## Objectifs à accomplir
### Test d'un hote simple
Réaliser un programme qui teste un hote sur un réseau afin de déterminer si on parvient à le joindre. Le programme devra ainsi afficher clairement si l'hote est accessible ou non.
L'objectif ici est de créer un programme complet, doccumenté, et d'apprendre à récupérer un argument de la ligne de commande.

### Test d'une liste d'hotes
Réaliser un programme qui teste une liste d'hotes. Le but est ici de manipuler une liste, et d'apprendre à la parcourir.
Pour ce programme, on déclarera donc une liste, et on la parcourera avec une boucle pour tester chaque hote de la liste.
Pour chaque hote, on aura un affichage clair à l'écran du statut de celui ci.

#### Modification : Test d'une liste d'hotes depuis un fichier en entrée
Modifier le programme précédent pour charger la liste depuis un fichier texte. Chaque ligne du fichier correspond à un hote.

#### Modification : Test d'une liste d'hotes depuis un fichier JSON
Modifier le programme précédent pour charger un fichier au format json plutôt qu'un simple fichier texte.

#### Modification : test d'une liste d'hote depuis un fichier JSON et sauvegarde du résultat dans un fichier
Modifier le programme précédent pour ajouter le fait que le programme sauvegarde également les résultats obtenus dans un fichier "output.txt"

### Test d'une plage d'IP
Réaliser un autre programme qui permet cette fois ci de tester une plage d'IP.
Pour faire simple, on testera uniquement le dernier octet de l'adresse. 
par exemple, il testera le réseau 192.168.0.0 avec le masque 255.255.255.0, donc les machines de 192.168.0.1 à 192.168.0.254.

