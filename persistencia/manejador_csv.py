import csv
from modelos.cliente import Cliente
from modelos.turno import Turno

class ManejadorCSV:

    
    # GUARDAR CLIENTES
    
    @staticmethod
    def guardar_clientes(ruta_archivo, diccionario_clientes):
        with open(ruta_archivo, "w", newline="", encoding="utf-8") as archivo:
            columnas = ["dni", "nombre", "telefono", "email"]
            escritor = csv.DictWriter(archivo, fieldnames=columnas)

            escritor.writeheader()

            for cliente in diccionario_clientes.values():
                escritor.writerow(cliente.a_diccionario())

    
    # CARGAR CLIENTES
    
    @staticmethod
    def cargar_clientes(ruta_archivo):
        clientes_cargados = {}

        try:
            with open(ruta_archivo, "r", encoding="utf-8") as archivo:
                lector = csv.DictReader(archivo)

                for fila in lector:
                    cliente = Cliente(**fila)
                    clientes_cargados[fila["dni"]] = cliente

        except FileNotFoundError:
            pass  # si no existe, devuelvo el diccionario vacío

        return clientes_cargados

    
    # GUARDAR TURNOS
    
    @staticmethod
    def guardar_turnos(ruta_archivo, diccionario_turnos):
        with open(ruta_archivo, "w", newline="", encoding="utf-8") as archivo:
            columnas = ["turno_id", "dni", "fecha", "servicio", "duracion", "estado"]
            escritor = csv.DictWriter(archivo, fieldnames=columnas)

            escritor.writeheader()

            for turno in diccionario_turnos.values():
                escritor.writerow(turno.a_diccionario())

    
    # CARGAR TURNOS
    
    @staticmethod
    def cargar_turnos(ruta_archivo):
        turnos_cargados = {}

        try:
            with open(ruta_archivo, "r", encoding="utf-8") as archivo:
                lector = csv.DictReader(archivo)

                for fila in lector:
                    turno = Turno(
                        dni=fila["dni"],
                        fecha=fila["fecha"],
                        servicio=fila["servicio"],
                        duracion=fila["duracion"]
                    )
                    turno.turno_id = int(fila["turno_id"])
                    turno.estado = fila["estado"]

                    turnos_cargados[turno.turno_id] = turno

        except FileNotFoundError:
            pass

        return turnos_cargados
