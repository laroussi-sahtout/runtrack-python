def afficher_produits(type, saison):
    if type == "fruits" and saison == "hiver":
        return "Orange, mandarine et kiwi"
    elif type == "fruits" and saison == "ete":
        return "Poire, fraise, cassis"
    elif type == "legume" and saison == "hiver":
        return "Carotte, topinambour, endive"
    elif type == "legume" and saison == "ete":
        return "Artichaut, aubergine, navet"
    else:
        return "Aucune correspondance trouvée."

type = input("Choisissez 'fruits' ou 'legume' : ")
saison = input("Choisissez 'hiver' ou 'ete' : ")


resultat = afficher_produits(type, saison)
print(resultat)
