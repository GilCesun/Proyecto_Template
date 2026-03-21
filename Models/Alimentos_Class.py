import json

#Clase que lee el archivo Menu.json y separa del diccionario el key Vaulue "Alimentos" para genererar una lista

class Alimento:
    def __init__(self) -> None:
        super().__init__()
        with open("Menu.json", "r", encoding="utf-8") as leerMenu: #leer el .json
            diccionario_LeerMenu = json.load(leerMenu)

        self.listaAlimentos = diccionario_LeerMenu["Alimentos"][0] #Crear una lista solo de alimentos
        self.listaPrecios = diccionario_LeerMenu["Alimentos"][1] #Cr                                                    ear una lista solo de Precios


