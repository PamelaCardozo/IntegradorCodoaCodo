# Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con
# cada palabra que contiene y la cantidad de veces que aparece (frecuencia).

def contar_palabras(cadena):
    palabras = cadena.split()
    frecuencia = {}
    
    for palabra in palabras:
        palabra = palabra.lower()  # Convertir a minúsculas para considerar mayúsculas y minúsculas iguales
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    
    return frecuencia

'''
cadena = input("Ingresa una cadena de caracteres: ")
resultado = contar_palabras(cadena)

print("Frecuencia de palabras:")
for palabra, cantidad in resultado.items():
    print(f"'{palabra}': {cantidad}")
'''

# Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada
# palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función
# que reciba el diccionario generado con la función anterior y devuelva una tupla con la
# palabra más repetida y su frecuencia.

def palabra_mas_repetida(diccionario):
    palabra_max = None
    frecuencia_max = 0
    
    for palabra, frecuencia in diccionario.items():
        if frecuencia > frecuencia_max:
            palabra_max = palabra
            frecuencia_max = frecuencia
    
    return (palabra_max, frecuencia_max)

cadena = input("Ingresa una cadena de caracteres: ")
resultado = contar_palabras(cadena)

print("Frecuencia de palabras:")
for palabra, cantidad in resultado.items():
    print(f"'{palabra}': {cantidad}")

palabra, frecuencia = palabra_mas_repetida(resultado)
print(f"Palabra más repetida: '{palabra}' (Frecuencia: {frecuencia})")