def pair (nombre): 
    if (nombre % 2) == 0:
      print("{0} est Paire".format(nombre))
    else:
      print("{0} est Impaire".format(nombre))

nombre = int(input("Entrer votre nombre : "))

result = pair(nombre)
print (result)