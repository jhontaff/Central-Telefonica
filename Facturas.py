from Abonados import *
import csv
import re

class Tiempo:
    def __init__(self,telefono,tiempo):
        self.telefono=telefono
        self.tiempo=tiempo

class Precio:
    def __init__(self):
        self.historiales=[]

    def factura(self, telefono):
        agenda = Agenda()
        with open('agenda.csv', 'r') as fichero:
            lector = csv.DictReader(fichero, delimiter=',')
            for fila in lector:
                agenda.agregar(fila['nombre'].capitalize(), fila['apellido'].capitalize(), fila['cedula'].capitalize(), fila['fijo'].capitalize(), fila['direccion'].capitalize())

        for contacto in agenda.contactos:
            if (re.findall(telefono, contacto.fijo)):
                telefono = contacto.fijo
                segundos = self.buscar(telefono)
                print('Nombre y Apellido: ',contacto.nombre,contacto.apellido)
                print('Cedula: ',contacto.cedula)
                print('Teléfono: ', contacto.fijo)
                print('Dirección: ',contacto.direccion)
                print('Segundos utilizados: {}'.format(segundos))
                tarifa=5; #5 pesos por segundo
                p=round(segundos*tarifa,2)
                print('Su factura es de: {} pesos'.format(p))
    def guardar(self):
        with open('historial.csv','w') as fichero:
            escribir=csv.writer(fichero)
            escribir.writerow(('telefono', 'tiempo'))
            for llamada in self.historiales:
                escribir.writerow((llamada.telefono, llamada.tiempo))
    def agregar(self, telefono, tiempo):
        llamada = Tiempo(telefono, tiempo)
        self.historiales.append(llamada)

    def buscar(self,telefono):
        t=0
        for llamada in self.historiales:
            if (re.findall(telefono, llamada.telefono)):
                t=float(llamada.tiempo)+t
        t = t
        return t

    def historial(self, telefono, tiempo):
        try:
            with open('historial.csv','r') as fichero:
                lector=csv.DictReader(fichero,delimiter=',')
                for fila in lector:
                    self.agregar(fila['telefono'].capitalize(),fila['tiempo'].capitalize())
        except:
            print('No se encontro el archivo')

        while True:
            self.agregar(telefono, tiempo)
            self.guardar()
            break

def facturacion():
    precio = Precio()
    try:
        with open('historial.csv', 'r') as fichero:
            lector = csv.DictReader(fichero, delimiter=',')
            for fila in lector:
                precio.agregar(fila['telefono'].capitalize(), fila['tiempo'].capitalize())
    except:
        print('No se encontro el archivo')

    while True:
        menu = str(input("""
        \nOPCIONES\n
        1 Generar factura segun numero: 
        2 Volver \n\n               
        """))
        if menu == '1':
            telefono = str(input("Ingrese el número del cual desea generar factura: "))
            precio.factura(telefono)
            precio.guardar()
        elif menu == '2':
            precio.guardar()
            break
        else:
            print('ERROR')



