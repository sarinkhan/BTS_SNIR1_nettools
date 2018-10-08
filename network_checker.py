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
import subprocess
import sys

# ce bloc sert à faire un code qui fonctionne même sous windows
COUNT_TAG = "-n"
if os.name == "posix":  # si on est sous posix (linux, unix, etc)
    COUNT_TAG = "-c"

DOMAINS_LIST = [
    "gwadalug.org",
    "lebiklab.com",
    "localhost"
    ]


def host_up(host):
    """Teste un hote via un ping pour voir s'il est joignable.

    Cette fonction envoie un ping à l'hote passé en paramètre pour tester la
    connectivité vers celui ci. S'il répond au ping, on retourne True, et
    False si ce n'est pas le cas.

    Args:
        host: le nom de l'hote à tester ou son adresse IP.

    Returns:
        L'état de l'hote testé. True s'il est joignable, False sinon.

    """
    ping_proc = subprocess.Popen(['ping', COUNT_TAG,
                                  '1', host], stdout=subprocess.PIPE)
    ping_proc.communicate()

    if ping_proc.returncode == 0:
        return True
    return False


def main():
    """Fonction principale du programme.

    Returns:
        La valeur de retour. 0 si réussite,
        toute autre valeur signifie un echec.

    """

    # affiche le premier argument saisi, s'il y en a un
    arg1 = None
    if len(sys.argv) > 1:
        arg1 = str(sys.argv[1])
        print(arg1)

    return 0  # on indique que le programme s'est exécuté correctement


if __name__ == "__main__":
    # execute only if run as a script
    main()
