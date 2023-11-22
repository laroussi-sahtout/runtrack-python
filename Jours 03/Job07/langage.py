def string(langage):
    if langage == "JavaScript":
        return "tu est un developpeur web"
    if langage == "python":
        return "tu est un developpeur IA"
    if langage == "java":
        return "tu est un developpeur logiciel"
    if langage == "reactjs":
        return "tu est un developpeur mobile"
    else:
        return "tu seras un meilleur developpeur"
    
langage = input ("Choisissez un langage entre JavaScript, python, java, reactjs : ")


result = string(langage)
print (result)
