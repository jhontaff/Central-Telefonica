import random
import time
import pyglet
from pynput import keyboard as kb
from Facturas import Precio

class Central:
    def __init__(self):
        self.disponibles = []
        self.fueradeservicio = []
        self.ocupados = []
        self.emisor = []
        self.duracionllamadas = []

    def abonadosdisponibles(self):
        for i in range(0,20):
            self.disponibles.append(8603900 + i)
        return self.disponibles

    def abonadosfueradeservicio(self): #15% fuerda de servicion
        for i in range(0, 3):
            numescogido1 = random.choice(self.disponibles)
            self.fueradeservicio.append(numescogido1)
            self.disponibles.remove(numescogido1)
        return self.disponibles,self.fueradeservicio

    def abonadosocupados(self): #25% ocupados
        for i in range(0, 5):
            numescogido2 = random.choice(self.disponibles)
            self.ocupados.append(numescogido2)
            self.disponibles.remove(numescogido2)

        return self.disponibles,self.fueradeservicio,self.ocupados

    def usuario(self,emisor):
        if emisor in self.disponibles:
            self.emisor.append(emisor)
            self.disponibles.remove(emisor)
            return emisor
        else:
            print('Numero no disponible, por favor seleccione un numero disponoble')
            emisor=int(input("Ingrese numero del cual desea llamar: "))
            self.usuario(emisor)

    def llamar(self, numero,emisor):
        if (numero > 8603900 and numero < 8603920):
            player = pyglet.media.Player()
            if numero in self.disponibles:
                print ('Llamando...')
                marcacion = pyglet.resource.media('tonoMarcando.wav')
                player.queue(marcacion)
                player.play()
                time.sleep(7)
                tiempoinicio=time.time()
                player.next_source()
                conversacion = pyglet.resource.media(self.conversaciones())
                player.queue(conversacion)
                player.play()
                time.sleep(conversacion.duration)
                tiempofinal=time.time()
                tiempo=tiempofinal-tiempoinicio
                precio = Precio()
                precio.historial(str(emisor), str(tiempo))

            if (numero in self.ocupados or numero in self.emisor):
                print('Telefono ocupado')
                tono = pyglet.resource.media('tonOcupado.wav')
                tono.play()
                time.sleep(5)
            if numero in self.fueradeservicio:
               print('Telefono fuera de servicio')
               tono= pyglet.resource.media('tonoFueradeServicio.mp3')
               tono.play()
               time.sleep(5)

        else:
            numero=int(input("Marcación incorrecta, Digite el número del receptor: "))
            self.llamar(numero,emisor)

    def conversaciones(self):
            print('En llamada')
            conversaciones = ["conversacion1.wav", "conversacion2.mp3", "conversacion3.wav"]
            conversacion = random.choice(conversaciones)
            return conversacion
def central():
    while True:
        menu = str(input("""
        \n¿Que desea realizar?\n
        1 Usuarios inscritos en la Central
        2 Volver \n\n               
        """))
        if menu == '1':
            user = Central()
            user.abonadosdisponibles()
            user.abonadosfueradeservicio()
            user.abonadosocupados()
            print("Números disponibles: ", user.disponibles)
            print("Números ocupados: ", user.ocupados)
            print("Números fuera de servicio: ", user.fueradeservicio)
            emisor = int(input("Digite el número telefónico del cual desea llamar: "))
            emisor = user.usuario(emisor)

            receptor = int(input("Digite el número telefónico al cual desea llamar: "))
            user.llamar(receptor, emisor)
        elif menu == '2':
            break
        else:
            print('Opción no valida')



