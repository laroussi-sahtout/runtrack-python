L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

nombre_chiffres = sum(1 for chiffre in L if 25 <= chiffre <= 90)

print("Le nombre de chiffres dans l'intervalle [25, 90] est :", nombre_chiffres)