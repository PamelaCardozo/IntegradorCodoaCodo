# Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una
# cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero
# del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el
# ejercicio tanto de manera iterativa como recursiva.

def get_int_iterativa():
    while True:
        try:
            valor = int(input("Ingresa un valor entero: "))
            return valor
        except ValueError:
            print("Valor incorrecto. Inténtalo de nuevo.")


def get_int_recursiva():
    try:
        valor = int(input("Ingresa un valor entero: "))
        return valor
    except ValueError:
        print("Valor incorrecto. Inténtalo de nuevo.")
        return get_int_recursiva()

       

entero = get_int_iterativa()
print(f"Valor entero ingresado: {entero}")

entero = get_int_recursiva()
print(f"Valor entero ingresado: {entero}")    