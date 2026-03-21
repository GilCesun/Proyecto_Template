import  json
from .constantes import orden_nombre_archivoJSON

def crearJson (diccionario) -> None : #funcion para escribir al json
    with open(orden_nombre_archivoJSON,'w', encoding= "UTF-8") as orden:
        json.dump(diccionario, orden, ensure_ascii=False, indent=4)

def leerJson() ->dict[str, list] : #Funcion para leer json
    with open (orden_nombre_archivoJSON, 'r',encoding= "UTF-8" ) as leer_Orden:
        return json.load(leer_Orden)

def dividirjSON () : #separa el ORDEN.JSON en 2 listas, una de los productos que se consumio y otra de sus precios.
    diccionario = leerJson()
    productos = diccionario["Consumo"][0]
    precios = diccionario["Consumo"][1]
    return productos, precios