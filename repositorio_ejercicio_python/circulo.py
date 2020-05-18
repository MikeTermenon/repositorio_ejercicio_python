import math

def calcular_area(r):
    area = math.pi * r**2
    return area

r = int(input("Dame un radio: "))
print(calcular_area(r))