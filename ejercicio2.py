# Escribir una función que calcule el mínimo común múltiplo entre dos números

def calcular_mcd(a, b):
    while b:
        a, b = b, a % b
    return a

def calcular_lcm(a, b):
    return (a * b) // calcular_mcd(a, b)

numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))

lcm = calcular_lcm(numero1, numero2)
print(f"El mínimo común múltiplo entre {numero1} y {numero2} es {lcm}")
