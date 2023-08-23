'''
Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los
siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. Hay que validar las entradas de
datos.
 mostrar(): Muestra los datos de la persona.
 Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad
'''


class Persona:
    def __init__(self,nombre = "", edad = 0, dni = ""):
        self._nombre = nombre
        self._edad = edad
        self._dni = dni

    def mostrar(self):
        print(f"Nombre: {self._nombre}\nEdad: {self._edad}\nDNI: {self._dni}") 

#getters y setters

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = self.validar_nombre(nombre)

    @property
    def edad(self):
        return self._edad    

    @edad.setter
    def edad(self,edad):
        self._edad = self.validar_edad(edad)

    @property
    def dni(self):
        return self._dni
    
    @dni.setter
    def dni(self,dni):
        self._dni = self.validar_dni(dni)

    # VALIDACIONES
    @staticmethod
    def validar_nombre(nombre):
        if nombre is None:
            return None
        if isinstance(nombre, str) and len(nombre) >= 3:  # Cambio en la validación
            return nombre.strip()
        raise ValueError("El nombre debe ser una cadena de al menos 3 caracteres.")
        

    @staticmethod
    def validar_edad(edad):
        if edad is None:
            return None
        if (edad, int) and 0 <= edad <= 150:
            return edad
        raise ValueError ("La edad debe ser un número entero entre el 0 y 150.")

    @staticmethod
    def validar_dni(dni):
        if dni is None:
            return None
        if (dni, str) and len(dni) == 8 and dni.isdigit():
            return dni
        raise ValueError("El DNI debe ser una cadena de 8 dígitos numéricos.")  

    def es_mayor_de_edad(self):
        if self._edad >=18:
            return True
        else:
            return False
        


persona1 = Persona("Pamela", 40, "29939349")
persona1.mostrar()

persona2 = Persona()
persona2.nombre = "María"
persona2.edad = 30
persona2.dni = "98765432"
persona2.mostrar()        

    