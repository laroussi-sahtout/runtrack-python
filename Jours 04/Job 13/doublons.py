def doublon(liste):
    liste_sans_doublons = []

    for element in liste:
        if element not in liste_sans_doublons:
            liste_sans_doublons.append(element)

    return liste_sans_doublons

liste = [10,20,30,20,10,50,60,40,80,50,40]

ma_liste_sans_doublons = doublon(liste)

print (ma_liste_sans_doublons)