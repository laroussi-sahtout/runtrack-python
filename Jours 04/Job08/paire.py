L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]

calcul = sum(1 for nombre in L if nombre % 2 == 0)

print("Nombre de multiples de 3 dans la liste :", calcul)
