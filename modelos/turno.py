class Turno:
    numero_turnos = 1   # contador simple para identificar turnos

    def __init__(self, **datos):
        self.turno_id = Turno.numero_turnos
        Turno.numero_turnos += 1

        self.dni = datos.get("dni")
        self.fecha = datos.get("fecha")
        self.servicio = datos.get("servicio")
        self.duracion = datos.get("duracion")
        self.estado = "activo"

    def a_diccionario(self):
        return {
            "turno_id": self.turno_id,
            "dni": self.dni,
            "fecha": self.fecha,
            "servicio": self.servicio,
            "duracion": self.duracion,
            "estado": self.estado
        }
