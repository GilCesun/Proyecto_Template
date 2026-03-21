from Models import Alimento, Bebidas #Importar clases "padre"

#Clase que reune las propiedades de alimento, su precio, bebida y su precio, heredado de las clases Alimento y Bebida
class Menu(Alimento,Bebidas):
    #Clase Menu
    def __init__(self) -> None:
          super().__init__() #Herencia de las clases padre

    def mostraMenu(self) -> None: #Funcion que imprime el menu en la consola
          for bebida, precio, alimento, precioAlimento in zip(self.listaBebidas, self.listaPreciosBebidas, self.listaAlimentos, self.listaPrecios):
              print(f"🍔{alimento}.....${precioAlimento}|||||||🍸{bebida}.....${precio}")

