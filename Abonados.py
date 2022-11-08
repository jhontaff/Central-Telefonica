import csv
import re

class Usuario:
    def __init__(self,nombre,apellido,cedula,fijo,direccion):
        self.nombre=nombre
        self.apellido=apellido
        self.cedula=cedula
        self.fijo=fijo
        self.direccion=direccion

class Agenda:
    def __init__(self):
        self.contactos=[]

    def mostrar(self):
        for contacto in self.contactos:
            self.imprimir(contacto)

    def imprimir(self,contacto):
        print('  ')
        print('Nombre: {}'.format(contacto.nombre))
        print('Apellidos: {}'.format(contacto.apellido))
        print('Cédula: {}'.format(contacto.cedula))
        print('Fijo: {}'.format(contacto.fijo))
        print('dirección: {}'.format(contacto.direccion))
        print('  ')

    def agregar(self,nombre,apellido,cedula,fijo,direccion):
        contacto=Usuario(nombre,apellido,cedula,fijo,direccion)
        self.contactos.append(contacto)

    def guardar(self):
        with open('agenda.csv','w') as fichero:
            escribir=csv.writer(fichero)
            escribir.writerow(('nombre','apellido','cedula','fijo','direccion'))
            for contacto in self.contactos:
                escribir.writerow((contacto.nombre,contacto.apellido,contacto.cedula,contacto.fijo,contacto.direccion))


def iniciarabonado():
    agenda = Agenda()
    try:
        with open('agenda.csv', 'r') as fichero:
            lector = csv.DictReader(fichero, delimiter=',')
            for fila in lector:
                agenda.agregar(fila['nombre'].capitalize(), fila['apellido'].capitalize(),fila['cedula'].capitalize(), fila['fijo'].capitalize(),fila['direccion'].capitalize())
    except:
        print('No se encontro el archivo')
    while True:
        menu = str(input("""
        \nSelecciona la opción que desee\n
        1 Usuarios inscritos en la central
        2 Inscribir nuevo usuario       
        3 Volver  \n\n               
        """))
        if menu == '1':
            agenda.mostrar()
        elif menu == '2':
            nombre = str(input('Nombre: '))
            apellido = str(input('Apellido: '))
            cedula = str(input('Cédula: '))
            fijo = str(input('Telefono fijo: '))
            direccion = str(input('Direccion: '))
            agenda.agregar(nombre.capitalize(), apellido.capitalize(), cedula.capitalize(), fijo.capitalize(),direccion.capitalize())
            agenda.guardar()
        elif menu == '3':
            agenda.guardar()
            break
        else:
            print('ERROR')



