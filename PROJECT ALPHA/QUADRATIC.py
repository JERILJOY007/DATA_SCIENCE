import math

a = int(input("ENTER THE NUMBER A: "))
b = int(input("ENTER THE NUMBER B: "))
c = int(input("ENTER THE NUMBER C: "))
discriminant = b ** 2 - 4 * a * c
if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    root1 = round(root1, 2)
    root2 = round(root2, 2)
    print("ROOT 1:", root1)
    print("ROOT 2:", root2)
else:
    print("NO REAL ROOTS")