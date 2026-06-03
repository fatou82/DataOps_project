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