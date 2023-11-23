def liste(fruit):
    return list(fruit)

fruits = ["pomme", "cerise", "orange"]
result = liste(fruits)

if len(result) >= 2:
    deuxieme_element = result[1]
    print(deuxieme_element)