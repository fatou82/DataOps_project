import csv
import mysql.connector

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "dataops_db"
}

def connect_insert_bdd():
    connexion = mysql.connector.connect(**db_config)
    cursor = connexion.cursor()

    chemin_hdfs = "./dossier_hdfs/utilisateurs.csv"

    # ouverture du fichier 
    with open(chemin_hdfs, "r", encoding="utf-8") as fichier:
        lecteur_csv = csv.reader(fichier, delimiter=",")
        next(lecteur_csv)  # Ignorer l'en-tête du CSV
        for ligne in lecteur_csv:
            sql = "INSERT INTO utilisateurs (id, nom, email, age) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, tuple(ligne))
    connexion.commit()
    print("Données insérées avec succès dans la base de données.")
    cursor.close()
    connexion.close()

connect_insert_bdd()
