
def ajouter_melon(fruit):
    fruit.insert(2, "Mangue")
    return fruit

fruits = ["pomme", "cerise", "orange", "Melon"]
result = ajouter_melon(fruits)

print(result)