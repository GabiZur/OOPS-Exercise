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


cuenta1 = Cuenta("Juan", 1000)
cuenta1.mostrar()
cuenta1.ingresar(-500)
cuenta1.retirar(1200)
cuenta1.mostrar()