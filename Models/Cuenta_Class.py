from .Orden_Class import Orden
from utileria import *

#Clase que genera el total de la cuenta $$$$$
class Cuenta (Orden):

    def __init__(self) -> None:
        super().__init__()
        self._listaCuenta = leerJson()
        self._total = 0
        self._iva = iva
        self._subtotal = 0

    def soloPrecios (self) -> list[float]: #funcion que separa del diccionario, solo la lista de precios
         listaPrecios = self._listaCuenta["Consumo"][1]
         return listaPrecios

    def subtotal(self) -> float: #calcula el subtotal
        total = sum(self.soloPrecios())
        return total


    def iva_Calculo(self) -> float: #calcula el IVA
        iva = self.subtotal() * self._iva
        return iva

    def total(self) -> float: #Calcula el total
        total = self.subtotal() + self.iva_Calculo()
        return total



