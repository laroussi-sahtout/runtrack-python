x = int(input("Entrer votre variable : "))
space = " " * x

for i in range(x):
    if i == 0:
        print(space + "/" + "\\")
    elif i == x - 1:
        print(" " * (x - i) + "/" + "_" * (x + i - 1) + "\\")
    else:
        print(" " * (x - i) + "/" + " " * (i * 2) + "\\")

        