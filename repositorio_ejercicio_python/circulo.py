import math

def calcular_area(r):
    area = math.pi * r**2
    return area

def calcular_perimetro(r):
    perimetro = 2 * math.pi * r
    return perimetro

def calcular_volumen_esfera(r):
    volumen = (4/3) * math.pi * r**3
    return volumen

r = int(input("Dame un radio: "))
print(calcular_area(r))
print(calcular_perimetro(r))
print(calcular_volumen_esfera(r))