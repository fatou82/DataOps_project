import os
import shutil

dossier_hdfs = "./dossier_hdfs/utilisateurs.csv"
dossier_archive = "./dossier_archive"
def archive_script():
    os.makedirs(dossier_archive, exist_ok=True)
    shutil.move(dossier_hdfs, dossier_archive)
    print(f"Le dossier '{dossier_hdfs}' a été déplacé vers '{dossier_archive}'.")

archive_script()