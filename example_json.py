#! /usr/bin/env python3
"""Programme testant des machines sur un réseau

Ce module est un programme d'aprentissage pour des BTS info.
Le programme doit ouvrir un fichier contenant une liste d'adresses IP
au format JSON, et charger le contenu de ce fichier dans une variable
de type liste.
Pour chaque entrée de la liste, nous allons lancer un ping permettant
de vérifier si la machine est active ou pas.
Le résultat sera affiché à l'écran de façon claire, et un fichier
de compte rendu devra être généré.

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""

import os
import sys
import json
import net_check


# ce bloc sert à faire un code qui fonctionne même sous windows
COUNT_TAG = "-n"
if os.name == "posix":  # si on est sous posix (linux, unix, etc)
    COUNT_TAG = "-c"

DOMAINS_LIST = [
    "gwadalug.org",
    "lebiklab.com",
    "localhost"
    ]


def main():
    """Fonction principale du programme.

    Returns:
        La valeur de retour. 0 si réussite,
        toute autre valeur signifie un echec.

    """

    # affiche le premier argument saisi, s'il y en a un
    arg1 = None
    if len(sys.argv) > 1:  # Si il y a un argument ou plus
        arg1 = str(sys.argv[1])  # on récupère le premier argument
        print(arg1)

    print(net_check.host_up("127.0.0.1"))

    file = open("host_list.json", "r")
    json_list = json.load(file)

    for host in json_list["hosts"]:  # on parcourt la liste
        print("host " + host)

    return 0  # on indique que le programme s'est exécuté correctement


if __name__ == "__main__":
    # execute only if run as a script
    main()
