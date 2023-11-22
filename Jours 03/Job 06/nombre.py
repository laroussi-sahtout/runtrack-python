Chiffre = float(input("Entrer un nombre : "))

def nombre(Chiffre):
    if Chiffre < 0:
        return "Negatif"
    elif Chiffre > 0:
        return "Positif"
    else:
        return "Nul"

result = nombre(Chiffre)
print(result)