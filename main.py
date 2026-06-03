''' Exemple 3: compter le nombre de voyelles dans une phrase '''
def compter_voyelles(texte):
    voyelles = "aeiouyAEIOUY"
    compteur = 0

    for lettre in texte:
        if lettre in voyelles:
            compteur += 1

    return compteur


# 2 fonction 
''' Exemple 2: conversion d'un nombre entier en binaire '''
def chiffre_vers_binaire():
    n = int(input("Entrez un nombre entier : "))
    binaire = ""
    while n > 0:
        binaire = str(n % 2) + binaire
        n = n // 2
    print("Le nombre en binaire est :", binaire)


phrase = "Bonjour tout le monde"
print("Nombre de voyelles :", compter_voyelles(phrase)) 