def type_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return "Triangle équilatéral"
        elif a == b or a == c or b == c:
            if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
                return "Triangle rectangle isocèle"
            else:
                return "Triangle isocèle"
        elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            return "Triangle rectangle"
        else:
            return "Triangle quelconque"
    else:
        return "Les longueurs ne peuvent pas former un triangle"

a = float(input("Entrez la longueur a : "))
b = float(input("Entrez la longueur b : "))
c = float(input("Entrez la longueur c : "))

resultat = type_triangle(a, b, c)
print(resultat)
