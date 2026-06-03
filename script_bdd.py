import mysql.connector

# connexion
connexion = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "dataops_db"
)

connexion.close()