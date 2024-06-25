import csv
import re
import argparse
from datetime import datetime
from colorama import init, Fore, Back, Style

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('path', type=str, help='El path de la base de datos')
    args = parser.parse_args()

    path = args.path
    
    print()
    data = list(csv.reader(open(path, newline=''), delimiter=','))
    re_usuario = r'^[1-9]|^\d+(,\d+)?E[+-]?\d+$'
    re_fecha = r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$'
    usuarios = []
    
    print("USUARIOS".center(50, "-"))
    for i in range(len(data)):
        usuario = data[i][3]
        if (re.match(re_usuario, usuario)) and (usuario != 'Usuario') and (usuario != 'invitado-deca') and (usuario not in usuarios):
            usuarios.append(usuario)
            print(Style.BRIGHT + str(i + 1) + "-" + usuario)
    print("".center(50, "-"))
    
    while True:
        indice = int(input("Ingrese el índice de un usuario: "))
        if indice > 0 and indice < (len(usuarios) + 1):
            seleccion = usuarios[indice - 1]
            print("Usuario seleccionado: " + seleccion)
            break
        else:
            print("Error: Índice inválido.\nInténtelo nuevamente.")
        
    while True:
        inicio = input("Ingrese la fecha de inicio del rango (aaaa-mm-dd): ")
        fin = input("Ingrese la fecha del fin del rango (aaaa-mm-dd): ")        
        inicio_obj = datetime.strptime(inicio, "%Y-%m-%d").date()
        fin_obj = datetime.strptime(fin, "%Y-%m-%d").date()
        if not (re.match(re_fecha, inicio)) or not (re.match(re_fecha, fin)) or (inicio_obj > fin_obj):
            print("Error: Fechas inválidas.\nInténtelo nuevamente.")
        else:
            break
    
if __name__ == '__main__':
    main()