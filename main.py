''' Exemple 1: Tri de trois nombres dans l'ordre croissant '''
def tri_croissant():
    a = int(input("Entrez le premier nombre : "))
    b = int(input("Entrez le deuxième nombre : "))
    c = int(input("Entrez le troisième nombre : "))

    if a <= b and a <= c:
        print(a)
        if b <= c:
            print(b)
            print(c)
        else:
            print(c)
            print(b)
tri_croissant()

''' Exemple 2: conversion d'un nombre entier en binaire '''
def chiffre_vers_binaire():
    n = int(input("Entrez un nombre entier : "))
    binaire = ""
    while n > 0:
        binaire = str(n % 2) + binaire
        n = n // 2
    print("Le nombre en binaire est :", binaire)

chiffre_vers_binaire()\

''' Exemple 3: compter le nombre de voyelles dans une phrase '''
def compter_voyelles(texte):
    voyelles = "aeiouyAEIOUY"
    compteur = 0

    for lettre in texte:
        if lettre in voyelles:
            compteur += 1

    return compteur


phrase = "Bonjour tout le monde"
print("Nombre de voyelles :", compter_voyelles(phrase))