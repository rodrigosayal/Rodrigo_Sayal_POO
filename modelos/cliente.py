class Cliente:
    def __init__(self, **datos):
        self.dni = datos.get("dni")
        self.nombre = datos.get("nombre")
        self.telefono = datos.get("telefono")
        self.email = datos.get("email")

    def a_diccionario(self):
        return {
            "dni": self.dni,
            "nombre": self.nombre,
            "telefono": self.telefono,
            "email": self.email
        }
