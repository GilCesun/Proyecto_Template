import os

def limpiarConsola(): #metodo estatico
 os.system('cls' if os.name == 'nt' else 'clear')

