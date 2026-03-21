from Models import Orden, Cuenta
from utileria import *
from utileria.serializar import dividirjSON
import datetime


class Ticket(Cuenta, Orden):

    def __init__(self) -> None:
        super().__init__()
        self.fecha_formateada = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.generarTicket()

    def generarTicket(self) -> None:
        # limpiar la consola al mandar llamar el ticket
        print("**********   CASH BAR   **********")
        print("     Av. de la Luz 4827, Laescondida, 22146 Tijuana, B.C.")  # direccion
        print(f"           Fecha: {self.fecha_formateada}")
        print("=======================================")

        productoConsumido, precioProducto = dividirjSON()

        for productos, precio in zip(productoConsumido, precioProducto):
            print(f"{productos} ..........${precio}")

        print(f"Total de articulos..#  {len(productoConsumido)}")  # subtotal
        print(f"       TOTAL NETO: $ {self.total()}")  # Total
        print("         ========================")  # total en string
        print("           Importe en pesos")  # numero de articulos vendidos
        print("")  # un codigo de barras x
        print("*************   GRACIAS POR SU COMPRA*************   ")  # alguna frase
        print("")  # fecha y hora
