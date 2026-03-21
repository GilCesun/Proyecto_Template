import json
#Esta clase genera un archivo JSON con el menu del bar, esta estructurado mediante un diccionario y listas de listas
# por ejemplo :Diccionario { "Key": [[Lista de alimentos],[Lista de precios]]}.

class EditarMenu:
    def __init__(self) -> None:
        #Diccionario que contiene los alimentos y bebidas del bar junto con su precio. utilizando una lista de listas

        menu_diccionario = {"Alimentos":[["ALIMENTO1","ALIMENTO2"],[323.4,123.4,324]],
                           "Bebidas":[["BEBIDA1","BEBIDA2"],[543.55,45.6,100]],
                            }

        with open("Menu.json", "w", encoding="utf-8") as menu: #Genera un archivo .json al cual se le puede escribir.
            json.dump(menu_diccionario, menu, indent=4, ensure_ascii=False) #Vacia el diccionario en el archivo .json

