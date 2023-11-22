num1 = input("Entrer un chiffre entier : ")
num2 = input("Entrer un chiffre entier : ")
operator = input("Entrer votre operation: ")

def calcule(num1, operator, num2):
    if operator == '+':
        return int(num1) + int(num2)
    elif operator == '-':
        return int(num1) - int(num2)
    elif operator == '/':
        if num2 != 0:
           return int(num1) / int(num2)
        else:
            return "La division par 0 est impossible"
    elif operator == 'x': 
        return int(num1) * int(num2)
    elif operator == '%':
        if num2 != 0:
            return int(num1) / int(num2)
        else:
            return "la division par 0 est impossible"
    else: 
        return "Operateur introuvable"

resultat = calcule(num1, operator, num2)

print("Résultat de l'opération :", resultat)
