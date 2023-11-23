import random 

liste = [random.randint(0, 10) for _ in range(5)]


index1 = 0
index2 = 4


print("Avant l'inversion :", liste)


liste[index1], liste[index2] = liste[index2], liste[index1]


print("Après l'inversion :", liste)