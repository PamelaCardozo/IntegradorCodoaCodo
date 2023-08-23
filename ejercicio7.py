'''
Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una
persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
opcional. Crear los siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. El atributo no se puede modificar
directamente, sólo ingresando o retirando dinero.
 mostrar(): Muestra los datos de la cuenta.
 ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es
negativa, no se hará nada.
 retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números
rojos.
'''

from ejercicio6 import Persona

class Cuenta(Persona):
    def __init__(self,titular,cantidad = 0.0):
        self._titular = titular
        self._cantidad = cantidad


    def mostrar_informacion(self):
        print(f"Titular: {self._titular.nombre}")
        print(f"Edad del titular: {self._titular.edad}")
        print(f"DNI del Titular: {self._titular.dni} ")
        print(f"Cantidad: {self._cantidad}")

    @property
    def titular(self):
        return self._titular
    

    
    def ingresar(self,cantidad):
        saldo_anterior = self._cantidad
        if cantidad > 0:
            self._cantidad += cantidad
            print (f"El saldo se modifico de ${saldo_anterior} a ${self._cantidad}")
        else:
            print(f"No se han realizado modificaciones el saldo es ${self._cantidad}") 

    def retirar(self,cantidad):
        saldo_anterior = self._cantidad        
        if cantidad >0:
            self._cantidad -=cantidad
            print(f"El saldo se modificó de ${saldo_anterior} a ${self._cantidad}")
        else:
            print(f"No se han realizado modificaciones el saldo es ${self._cantidad}") 


persona = Persona("Pamela", 40, "29939349")
cuenta = Cuenta(persona, 10000)         

cuenta.mostrar_informacion()

cuenta.ingresar(500)
cuenta.retirar(150)

cuenta.ingresar(-150)
cuenta.mostrar_informacion()

    
    
    
    
    
    
    
