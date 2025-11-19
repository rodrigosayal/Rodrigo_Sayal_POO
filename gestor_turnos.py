from modelos.cliente import Cliente
from modelos.turno import Turno
from persistencia.manejador_csv import ManejadorCSV

class GestorTurnos:
    def __init__(self):
        # Cargo lo que ya estaba guardado
        self.clientes = ManejadorCSV.cargar_clientes("data/clientes.csv")
        self.turnos = ManejadorCSV.cargar_turnos("data/turnos.csv")

    
    # VALIDACION DE DNI
    
    def validar_dni(self, dni_ingresado):
        if not dni_ingresado.isdigit():
            return False
        if len(dni_ingresado) < 7 or len(dni_ingresado) > 8:
            return False
        return True

    
    # REGISTRAR CLIENTE
    
    def registrar_cliente(self, dni_ingresado, nombre_completo, telefono_ingresado, email_ingresado=None):

        if not self.validar_dni(dni_ingresado):
            return "El DNI no es válido."

        if dni_ingresado in self.clientes:
            return "Ese DNI ya está registrado."

        datos_cliente = {
            "dni": dni_ingresado,
            "nombre": nombre_completo,
            "telefono": telefono_ingresado,
            "email": email_ingresado
        }

        cliente_nuevo = Cliente(**datos_cliente)
        self.clientes[dni_ingresado] = cliente_nuevo

        ManejadorCSV.guardar_clientes("data/clientes.csv", self.clientes)

        return "Cliente registrado correctamente."

    
    # PEDIR TURNO
    
    def pedir_turno(self, dni_ingresado, fecha_ingresada, servicio_elegido, duracion_minutos):

        if dni_ingresado not in self.clientes:
            return "Ese DNI no está registrado."

        datos_turno = {
            "dni": dni_ingresado,
            "fecha": fecha_ingresada,
            "servicio": servicio_elegido,
            "duracion": duracion_minutos
        }

        turno_nuevo = Turno(**datos_turno)
        self.turnos[turno_nuevo.turno_id] = turno_nuevo

        ManejadorCSV.guardar_turnos("data/turnos.csv", self.turnos)

        return f"Turno creado. Número: {turno_nuevo.turno_id}"

   
    # LISTAR CLIENTES
    
    def listar_clientes(self):
        return list(self.clientes.values())

    
    # LISTAR TURNOS
    
    def listar_turnos(self):
        return list(self.turnos.values())

    
    # CANCELAR TURNO POR DNI
    
    def cancelar_turno_por_dni(self, dni_ingresado):

        if dni_ingresado not in self.clientes:
            return "Ese DNI no está registrado."

        turnos_del_cliente = []

        for turno in self.turnos.values():
            if turno.dni == dni_ingresado:
                turnos_del_cliente.append(turno)

        if not turnos_del_cliente:
            return "Este cliente no tiene turnos."

        for turno_en_lista in turnos_del_cliente:
            turno_en_lista.estado = "cancelado"

        ManejadorCSV.guardar_turnos("data/turnos.csv", self.turnos)

        return "Turno cancelado."
