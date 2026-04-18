from Models import EditarMenu, Menu, Orden, Cuenta, Ticket
#from utileria import *


def main():
    _= EditarMenu()  # Recargar el menu si hay cambios4

    prueba = Menu()
    prueba.mostraMenu()
    Orden1 = Orden()
    Orden1.pedido()
    Cuenta()


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    main()

    ticket = Ticket()

    # ticket.mostrar()
    print("Testing")
