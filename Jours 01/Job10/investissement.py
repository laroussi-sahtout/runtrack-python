montant_initial = float(input("Entrez le montant initial de l'investissement : "))
taux_rendement_annuel = 2

gain_annuel = montant_initial * (taux_rendement_annuel / 100)
print(f"Gain annuel initial : {gain_annuel:.2f} euros")

montant_initial += 5000.0
taux_rendement_annuel += 2.0

nouveau_gain_annuel = montant_initial * (taux_rendement_annuel / 100)
print(f"Nouveau gain annuel pour 5000euros d'investissement en plus : {nouveau_gain_annuel:.2f} euros")

retrait = 0.10 * montant_initial
montant_initial -= retrait
taux_rendement_annuel -= 1.0

montant_final = montant_initial * (1 + taux_rendement_annuel / 100)
nouveau_gain_annuel = montant_final - montant_initial

print("\nRésultats après retrait et diminution du taux de rendement :")
print(f"Montant final de l'investissement : {montant_final:.2f} euros")
print(f"Nouveau gain annuel : {nouveau_gain_annuel:.2f} euros")
