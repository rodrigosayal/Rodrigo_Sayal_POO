from gestor_turnos import GestorTurnos

def main():
    gestor = GestorTurnos()

    while True:
        print("\n========== SISTEMA DE TURNOS  DE RODRIGO SAYAL ==========")
        print("1) Registrar un cliente")
        print("2) Sacar un turno")
        print("3) Ver todos los clientes")
        print("4) Ver todos los turnos")
        print("5) Cancelar turno por DNI")
        print("6) Salir")
        print("========================================")

        opcion_elegida = input("Elegí una opción: ")

        
        # 1) Registro de  cliente
      
        if opcion_elegida == "1":
            dni_ingresado = input("DNI del cliente: ")
            nombre_completo = input("Nombre y apellido: ")
            telefono_ingresado = input("Teléfono: ")
            email_ingresado = input("Email (opcional): ")

            mensaje = gestor.registrar_cliente(
                dni_ingresado,
                nombre_completo,
                telefono_ingresado,
                email_ingresado
            )

            print("\n" + mensaje)

        
        # 2) Pedir turno
        
        elif opcion_elegida == "2":
            dni_ingresado = input("DNI del cliente: ")
            fecha_ingresada = input("Fecha (DD/MM/AAAA HH:MM): ")
            servicio_elegido = input("Servicio (corte, color, etc.): ")
            duracion_minutos = input("Duración en minutos: ")

            mensaje = gestor.pedir_turno(
                dni_ingresado,
                fecha_ingresada,
                servicio_elegido,
                duracion_minutos
            )

            print("\n" + mensaje)

        
        # 3) Listado de  clientes
        
        elif opcion_elegida == "3":
            lista_de_clientes = gestor.listar_clientes()

            if not lista_de_clientes:
                print("\nNo hay clientes cargados.")
            else:
                print("\n======= LISTA DE CLIENTES =======")
                for cliente in lista_de_clientes:
                    print(f"DNI: {cliente.dni} | Nombre: {cliente.nombre} | Teléfono: {cliente.telefono}")

        
        # 4) Listado de  turnos
        
        elif opcion_elegida == "4":
            lista_de_turnos = gestor.listar_turnos()

            if not lista_de_turnos:
                print("\nNo hay turnos cargados.")
            else:
                print("\n========= LISTA DE TURNOS =========")
                for turno in lista_de_turnos:
                    print(
                        f"Turno Nº: {turno.turno_id} | "
                        f"DNI cliente: {turno.dni} | "
                        f"Fecha: {turno.fecha} | "
                        f"Servicio: {turno.servicio} | "
                        f"Estado: {turno.estado}"
                    )

        
        # 5) Cancelar turno por DNI
        
        elif opcion_elegida == "5":
            dni_ingresado = input("DNI del cliente: ")

            mensaje = gestor.cancelar_turno_por_dni(dni_ingresado)

            print("\n" + mensaje)

        
        # 6) Salir
        
        elif opcion_elegida == "6":
            print("\nSaliendo del sistema...")
            break

        else:
            print("\nOpción incorrecta, intentá otra vez.")

if __name__ == "__main__":
    main()
