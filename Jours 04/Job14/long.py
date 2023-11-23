def my_long_word(longueur_minimale, phrase):
    mots = phrase.split()
    mots_filtres = [mot for mot in mots if len(mot) > longueur_minimale]
    resultat = " ".join(mots_filtres)
    return resultat

longueur_minimale = int(input("Entrez la longueur minimale des mots à afficher : "))

phrase = input("Entrez la phrase : ")

resultat = my_long_word(longueur_minimale, phrase)
print("Output :", resultat)
