
filas = int(input("Ingresa el numero de filas: "))
columnas = int(input("Ingresa el numero de columnas: "))

asientos = []

for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append("L")
    asientos.append(fila)


def mostrar_sala():
    print("\n----- SALA DE CINE -----")

    print("    ", end="")
    for j in range(columnas):
        print(j + 1, end="   ")

    print()

    for i in range(filas):
        print(f"{i + 1} | ", end="")
        for j in range(columnas):
            print(asientos[i][j], end="   ")
        print()


def reservar_asiento():
    mostrar_sala()

    fila = int(input("\nIngresa la fila: "))
    columna = int(input("Ingresa la columna: "))

    if 1 <= fila <= filas and 1 <= columna <= columnas:

        if asientos[fila - 1][columna - 1] == "L":
            asientos[fila - 1][columna - 1] = "X"
            print("Asiento reservado correctamente.")

        else:
            print("Este asiento ya esta ocupado.")

    else:
        print("El asiento seleccionado no existe.")



def liberar_asiento():
    mostrar_sala()

    fila = int(input("\nIngresa la fila: "))
    columna = int(input("Ingresa la columna: "))

    if 1 <= fila <= filas and 1 <= columna <= columnas:

        if asientos[fila - 1][columna - 1] == "X":
            asientos[fila - 1][columna - 1] = "L"
            print("Asiento liberado correctamente.")

        else:
            print("Este asiento ya esta libre.")

    else:
        print("El asiento seleccionado no existe.")


def contar_asientos():
    libres = 0
    ocupados = 0

    for i in range(filas):
        for j in range(columnas):

            if asientos[i][j] == "L":
                libres += 1
            else:
                ocupados += 1

    print("\n----- ESTADISTICAS -----")
    print("Asientos libres:", libres)
    print("Asientos ocupados:", ocupados)



while True:

    print("\n===== SISTEMA DE CINE =====")
    print("1. Mostrar sala")
    print("2. Reservar asiento")
    print("3. Liberar asiento")
    print("4. Contar asientos ocupados y libres")
    print("5. Salir")

    opcion = input("\nSelecciona una opcion: ")

    if opcion == "1":
        mostrar_sala()

    elif opcion == "2":
        reservar_asiento()

    elif opcion == "3":
        liberar_asiento()

    elif opcion == "4":
        contar_asientos()

    elif opcion == "5":
        print("Gracias por utilizar el sistema de cine.")
        break

    else:
        print("Opcion no valida. Intenta nuevamente.")
