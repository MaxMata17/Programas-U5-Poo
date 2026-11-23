
nombres = []
artistas = []
duraciones = []
popularidades = []


def pedir_entero(mensaje, minimo=None, maximo=None):
    while True:
        try:
            valor = int(input(mensaje))

            if minimo is not None and valor < minimo:
                print(f"El valor debe ser como minimo {minimo}.")
            elif maximo is not None and valor > maximo:
                print(f"El valor debe ser como maximo {maximo}.")
            else:
                return valor

        except ValueError:
            print("Ingresa un numero entero valido.")


def pedir_float(mensaje, minimo=None):
    while True:
        try:
            valor = float(input(mensaje))

            if minimo is not None and valor <= minimo:
                print(f"El valor debe ser mayor que {minimo}.")
            else:
                return valor

        except ValueError:
            print("Ingresa una duracion numerica valida.")


def agregar_canciones():
    cantidad = pedir_entero(
        "Cuantas canciones deseas agregar? ", 1
    )

    for i in range(cantidad):
        print(f"\nCancion {i + 1}")

        nombre = input("Nombre: ").strip()
        artista = input("Artista: ").strip()
        duracion = pedir_float("Duracion en minutos: ", 0)
        popularidad = pedir_entero(
            "Popularidad (1-100): ", 1, 100
        )

        nombres.append(nombre)
        artistas.append(artista)
        duraciones.append(duracion)
        popularidades.append(popularidad)

    print("\nCanciones agregadas correctamente.")


def ver_reportes():
    if not nombres:
        print("\nTodavia no hay canciones registradas.")
        return

    total = len(nombres)
    duracion_total = sum(duraciones)

    indice_mayor = popularidades.index(max(popularidades))
    indice_menor = popularidades.index(min(popularidades))

    promedio = sum(popularidades) / total

    print("\n--- REPORTES DE LA PLAYLIST ---")
    print(f"Numero total de canciones: {total}")
    print(f"Duracion total: {duracion_total:.2f} minutos")

    print(
        f"Cancion mas popular: {nombres[indice_mayor]} - "
        f"{artistas[indice_mayor]} "
        f"({popularidades[indice_mayor]})"
    )

    print(
        f"Cancion menos popular: {nombres[indice_menor]} - "
        f"{artistas[indice_menor]} "
        f"({popularidades[indice_menor]})"
    )

    print(f"Promedio de popularidad: {promedio:.2f}")


def buscar_canciones():
    if not nombres:
        print("\nNo hay canciones para buscar.")
        return

    print("\n1. Buscar por artista")
    print("2. Buscar por rango de popularidad")

    opcion = input("Elige una opcion: ").strip()

    encontrados = []

    if opcion == "1":
        artista_buscado = input(
            "Nombre del artista: "
        ).strip().lower()

        for i in range(len(nombres)):
            if artista_buscado in artistas[i].lower():
                encontrados.append(i)

    elif opcion == "2":
        minimo = pedir_entero(
            "Popularidad minima (1-100): ", 1, 100
        )

        maximo = pedir_entero(
            "Popularidad maxima (1-100): ", minimo, 100
        )

        for i in range(len(nombres)):
            if minimo <= popularidades[i] <= maximo:
                encontrados.append(i)

    else:
        print("Opcion no valida.")
        return

    if encontrados:
        print("\n--- RESULTADOS DE BUSQUEDA ---")

        for i in encontrados:
            print(
                f"{nombres[i]} - {artistas[i]} | "
                f"{duraciones[i]:.2f} min | "
                f"Popularidad: {popularidades[i]}"
            )
    else:
        print("\nNo se encontraron canciones.")


def playlist_recomendada():
    if not nombres:
        print("\nTodavia no hay canciones registradas.")
        return

    promedio = sum(popularidades) / len(popularidades)

    print(
        f"\n--- PLAYLIST RECOMENDADA "
        f"(mayor a {promedio:.2f}) ---"
    )

    hay_recomendadas = False

    for i in range(len(nombres)):
        if popularidades[i] > promedio:
            print(
                f"{nombres[i]} - {artistas[i]} "
                f"({popularidades[i]} puntos)"
            )

            hay_recomendadas = True

    if not hay_recomendadas:
        print("No hay canciones por encima del promedio.")

def menu():
    while True:
        print("\n========== FESTIVAL PLAYLIST ==========")
        print("1. Agregar canciones")
        print("2. Ver reportes")
        print("3. Buscar canciones")
        print("4. Playlist recomendada")
        print("5. Salir")

        opcion = input("Selecciona una opcion: ").strip()

        if opcion == "1":
            agregar_canciones()

        elif opcion == "2":
            ver_reportes()

        elif opcion == "3":
            buscar_canciones()

        elif opcion == "4":
            playlist_recomendada()

        elif opcion == "5":
            print("bye")
            break

        else:
            print("Opcion no valida")


if __name__ == "__main__":
    menu()
