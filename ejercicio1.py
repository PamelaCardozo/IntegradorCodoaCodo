
#1. Escribir una función que calcule el máximo común divisor entre dos números.

def calcular_mcd(a, b):
    if a < b:
        a,b = b,a
    while b:
        a, b = b, a % b
    return a

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

#Nos aseguramos que los número sean positivo, pidiendo el valo absoluto

num1 = abs(num1)
num2 = abs(num2)

mcd = calcular_mcd(num1, num2)
print(f"El Máximo Común Divisor de {num1} y {num2} es {mcd}")



