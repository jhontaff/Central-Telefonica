from Abonados import *
from Central import *
from Facturas import *

def realizar():
    while True:
        menu = str(input("""
        \nBIENVENIDO A LA CENTRAL TELEFONICA\n MENÚ DE OPCIONES: \n
        1 Llamar
        2 Informacion usuarios inscritos en la cental     
        3 Facturacion       
        4 Salir de la central \n\n               
        """))
        if menu == '1':
            central()
        elif menu == '2':
            iniciarabonado()
        elif menu == '3':
            facturacion()
        elif menu == '4':
            print('Hasta pronto!')
            break
        else:
            print('Opcion invalida, ingrese una opcion valida: ')

if __name__ == '__main__':
    realizar()

