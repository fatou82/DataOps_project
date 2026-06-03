import os
import shutil

def collect():
    source_distant = "./source_distant/utilisateurs.csv"
    dossier_destination = "./dossier_hdfs/"
    
    cible = os.path.join(dossier_destination, os.path.basename(source_distant))

    if not os.path.exists(cible):
        shutil.copy(source_distant, cible)

collect()