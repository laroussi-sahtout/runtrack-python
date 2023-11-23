def ajouter_melon(fruit):
    fruit.append("melon")
    return fruit

fruits = ["pomme", "cerise", "orange"]
result = ajouter_melon(fruits)

print(result)