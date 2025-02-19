class Persona:
    def __init__(self, nombre="", edad=0, DNI=0):

        self._nombre = nombre
        self._edad = edad
        self._DNI = DNI

    def get_nombre(self):
        return self._nombre

    def get_edad(self):
        return self._edad

    def get_DNI(self):
        return self._DNI

    def esMayorDeEdad(self):
        if self._edad >= 18:
            print("Es mayor de edad")
        elif self._edad > 0:
            print("Es menor de edad")
        else:
            print("edad no valida")

    def mostrar(self):
        print(f"Nombre: {self._nombre}")
        print(f"Edad: {self._edad}")
        print(f"DNI: {self._DNI}")


persona1 = Persona("Juan", 25, 123456789)
persona1.mostrar()
persona1.esMayorDeEdad()

persona1 = Persona()
persona1.mostrar()
persona1.esMayorDeEdad()