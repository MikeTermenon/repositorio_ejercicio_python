import math

def calcular_area(r):
    area = math.pi * r**2
    return area

def calcular_perimetro(r):
    perimetro = 2 * math.pi * r
    return perimetro

r = int(input("Dame un radio: "))
print(calcular_area(r))
print(calcular_perimetro(r))