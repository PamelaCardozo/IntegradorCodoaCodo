'''
Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase
CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase,
además del titular y la cantidad se debe guardar una bonificación que estará expresada en
tanto por ciento. Crear los siguientes métodos para la clase:
 Un constructor.
 Los setters y getters para el nuevo atributo.
 En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo
tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es
mayor de edad pero menor de 25 años y falso en caso contrario.
 Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
 El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la
cuenta.
'''
from ejercicio6 import Persona
from ejercicio7 import Cuenta

class CuentaJoven (Cuenta):
    def __init__(self,titular,cantidad = 0.0,bonificacion = 0):
        super().__init__(titular,cantidad)
        self._bonificacion = bonificacion

    @property
    def bonificacion(self):
        return self._bonificacion
    
    @bonificacion.setter
    def bonificacion(self, value):
        self._bonificacion = value

    def es_titular_valido(self):
        edad_titular = self.titular.edad
        return 18 < edad_titular < 25
    
    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
        else:
            print("Titular no válido para retirar dinero.")

    def mostrar(self):
        print("Cuenta Joven")
        print(f"Bonificación: {self._bonificacion}%")
        
    
titular_joven = Persona("Pamela", 23, "29939349")
cuenta_joven = CuentaJoven(titular_joven,10000,5)

print (f"Bonificación actual: {cuenta_joven.bonificacion}%")

cuenta_joven.mostrar()
cuenta_joven.retirar(200)