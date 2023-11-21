def est_nombre_premier(i):
    if i < 2:
        return False
    for n in range(2, int(i ** 0.5) + 1):
        if i % n == 0:
            return False
    return True

for i in range(2, 1001):
    if est_nombre_premier(i):
        print(i)