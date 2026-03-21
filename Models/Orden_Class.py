from .Menu_Class import Menu
from utileria import *


class Orden(Menu):
    def __init__(self) -> None:
        super().__init__()
        self.lista_productos = []
        self.lista_precios = []
        pass

    def pedido(self) -> None:
        self.orden_Diccionario = {"Consumo": [[], []]}
        self.lista_productos = (
            self.listaAlimentos + self.listaBebidas
        )  # lista que contiene todos los productos (alimentos y bebidas)
        self.lista_precios = self.listaPrecios + self.listaPreciosBebidas

        while True:  # agregar un try catch por si se elige algo que no sea 1 o 2
            try:

                print(
                    "Eliga lo que desee realizar \n 1.Ordenar\n 2.Mostrar el menu\n 3.Pedir la cuenta"
                )
                accion = int(input("Ingrese la accion : "))

                if accion == 1:
                    print("Ingrese su orden: ")
                    orden_Usuario = input()
                    orden = (
                        orden_Usuario.upper()
                    )  # Agregar trycatch para que no se elija nada que no este en el menu

                    try:  # Este try Catch lo usamos para saber el indice en la lista de precios del producto que buscamos
                        posicion = self.lista_productos.index(orden)
                        self.orden_Diccionario["Consumo"][0].append(orden)
                        self.orden_Diccionario["Consumo"][1].append(
                            self.lista_precios[posicion]
                        )

                    except ValueError:
                        print("El producto no existe")

                elif accion == 2:
                    self.mostraMenu()
                elif accion == 3:
                    limpiarConsola()
                    break
                else:
                    print("Intruce una operacion valida.")

            except ValueError:
                print()
            crearJson(self.orden_Diccionario)
