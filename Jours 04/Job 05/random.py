import random 

def remplacer_element(liste, index):
    if 1 <= index < len(liste) - 1:
        liste[index] = liste[index - 1] + liste[index + 1]

liste = [random.randint(0, 10) for _ in range(5)]

print (liste)

print("Deuxième valeur de la liste :", liste[1])

remplacer_element(liste, 3)
print("Liste après remplacement de L[3] :", liste)

print("Dernière valeur de la liste :", liste[-1])


