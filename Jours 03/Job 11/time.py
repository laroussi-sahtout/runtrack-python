def time_to_text(minutes):
    if minutes < 0:
        return "Veuillez entrer un nombre de minutes positif."
    
    heures = minutes // 60
    minutes_restantes = minutes % 60

    return "{0} heures et {1} minutes".format(heures, minutes_restantes)

try:
    minutes_saisies = int(input("Entrer le nombre de minutes : "))
    resultat = time_to_text(minutes_saisies)
    print(resultat)
except ValueError:
    print("Veuillez entrer un nombre entier de minutes valide.")