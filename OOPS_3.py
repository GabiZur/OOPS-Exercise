class Cuenta:

    def __init__(self, titular, cantidad=0):
        self.__titular = titular
        self.__cantidad = float(cantidad)

    def get_titular(self):
        return self.__titular

    def get_cantidad(self):
        return self.__cantidad

    def mostrar(self):
        print(f"Titular: {self.__titular}")
        print(f"Cantidad: {self.__cantidad}")

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad
            print(f"Se han ingresado {self.__cantidad} a la cuenta.")

    def retirar(self, cantidad):
        self.__cantidad -= cantidad
        print(f"Se han retirado {cantidad} de la cuenta.")


class cuentaJoven(Cuenta):

    def __init__(self, titular, edad, cantidad=0, bonificacion=0):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion
        self.edad = edad

    def esTitularValido(self):
        if 18 <= self.edad <= 25:
            return True
        else:
            return False

    def mostrar(self):
        super().mostrar()
        print(f"Cuenta joven - Bonificacion: {self.bonificacion}%")

    def retirar(self, cantidad):
        if self.esTitularValido():
            super().retirar(cantidad)
        else:
            print(f"Se han retirado {cantidad} de la cuenta.")


cj = cuentaJoven("Juan", 20, 1000, 10)
cj.mostrar()
cj.retirar(500)