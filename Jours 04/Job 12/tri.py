def tri_croissant(liste):
    n = len(liste)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]
                
liste = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

tri_croissant(liste)

print("Liste après le tri croissant :", liste)