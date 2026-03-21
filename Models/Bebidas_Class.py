import json

#Separa del menu las bebidas y sus precios.

class Bebidas:
    def __init__(self) -> None:
        super().__init__()
        with open("Menu.json",'r', encoding="UTF-8") as leerMenu:
            diccionarioLeerBebidas = json.load(leerMenu)

        self.listaBebidas = diccionarioLeerBebidas["Bebidas"][0]
        self.listaPreciosBebidas = diccionarioLeerBebidas["Bebidas"][1]




