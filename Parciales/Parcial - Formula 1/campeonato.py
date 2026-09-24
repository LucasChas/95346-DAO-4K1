
from titular import Titular
from suplente import Suplente
from novato import Novato

class Campeonato():
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.pilotos = []
        self.cargar_pilotos()

    def cargar_pilotos(self):
        archivo = open(self.nombre_archivo, "rt")
        for linea in archivo:
            campos = linea[:-1].split(",")
            tipo = int(campos[0])
            numero = int(campos[1])
            nombre = campos[2]
            escuderia = campos[3]
            sueldo_b = float(campos[4])
            puntos = int(campos[5])

            if tipo == 1:
                victorias = int(campos[6])
                piloto = Titular(numero,nombre,escuderia,sueldo_b,puntos,victorias)
            elif tipo == 2:
                carreras = int(campos[6])
                piloto = Suplente(numero,nombre,escuderia,sueldo_b,puntos,carreras)
            else:
                premio = campos[6]
                piloto = Novato(numero,nombre,escuderia,sueldo_b,puntos,premio)
            self.pilotos.append(piloto)
        archivo.close()

    def calcular_promedio_puntos(self):
        total = 0
        cantidad = len(self.pilotos)

        for piloto in self.pilotos:
            total += piloto.puntos
        
        return total // cantidad

    def obtener_piloto_mejor_pago(self):
        primero = True
        corredor = None

        for piloto in self.pilotos:
            if primero:
                mayor = piloto.calcular_pago()
                primero = False
                corredor = piloto
            else:
                if piloto.calcular_pago() > mayor:
                    mayor= piloto.calcular_pago()
                    corredor = piloto
        return corredor

    def calcular_total_pagos(self):
        total = 0
        for piloto in self.pilotos:
            total += piloto.calcular_pago()
        
        return total

    def contar_titulares_con_bonus(self):
        cantidad = 0
        for piloto in self.pilotos:
            if piloto.tipo == 1 and piloto.victorias >= 5:
                cantidad += 1
        return cantidad

    def contar_novatos_premiados(self):
        cantidad = 0
        for piloto in self.pilotos:
            if piloto.tipo == 3 and piloto.premio == "si":
                cantidad += 1
        return cantidad

    def cantidad_por_tipo(self):
        contador = {
            "Titular":0,
            "Suplente":0,
            "Novato":0
        }
        for piloto in self.pilotos:
            if piloto.tipo == 1:
                contador["Titular"] +=1
            elif piloto.tipo ==2:
                contador["Suplente"] += 1
            else:
                contador["Novato"] +=1
        return contador

    def puntos_por_escuderia(self):
        contador = {
        "Red Bull": 0,
        "McLaren": 0,
        "Ferrari": 0,
        "Mercedes": 0,
        "RB": 0,
        "Williams": 0
    }
        for piloto in self.pilotos:
            if piloto.escuderia in contador:
                contador[piloto.escuderia] += piloto.puntos
        return contador

    def escuderia_campeona(self):
        campeonato = self.puntos_por_escuderia()
        return max(campeonato, key=campeonato.get)

    def buscar_piloto(self, numero):
        piloto = None
        for corredor in self.pilotos:
            if corredor.numero == numero:
                piloto = corredor
                return piloto
        return piloto

    def ranking(self, n):
        pilotos_ordenados = sorted(self.pilotos, key=lambda p: p.puntos, reverse=True)
        return [p.nombre for p in pilotos_ordenados[:n]]
