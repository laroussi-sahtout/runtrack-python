def moyenne(moyenne_etudiant):
    if moyenne_etudiant >= 15 and moyenne_etudiant <= 20:
        return "Tres bon élève"
    elif moyenne_etudiant >= 14 and moyenne_etudiant <= 11:
        return "Bon élève"
    elif moyenne_etudiant >= 10 and moyenne_etudiant <= 8:
        return "Eleve Moyen"
    elif moyenne_etudiant >= 0 and moyenne_etudiant <= 7:
        return "Eleve devant faire des efforts"

Note1 = int(input("Entrer votre note: "))
Note2 = int(input("Entrer votre note: "))
Note3 = int(input("Entrer votre note: "))

moyenne_etudiant = (Note1 + Note2 + Note3) / 3

result = moyenne(moyenne_etudiant)
print (result)