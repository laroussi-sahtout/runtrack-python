def tri(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def arrondir(liste):
    for i in range(len(liste)):
        liste[i] = int(liste[i] + 0.5)

numbers = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

arrondir(numbers)

tri(numbers)

print("Liste arrondie et triée :", numbers)
