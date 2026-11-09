from artista import Solo, DJ, Banda, iniciar_festival


def pedir_entero(texto):
    while True:
        try:
            return int(input(texto))
        except ValueError:
            print("Debes escribir un número entero.")


# Artistas que ya están en la lista del festival
cartelera = [
    Banda("Ateez", "Kpop", 65, 8),
    Banda("5 Seconds of Summer", "PopRock", 80, 4),
    Solo("The Weeknd", "R&B", 100, "Blinding Lights"),
]

print("FESTIVAL MUSICAL")
print(f"Ya hay {len(cartelera)} artistas en la cartelera.")

total_nuevos = pedir_entero("¿Cuántos artistas más se presentarán? ")

for numero in range(1, total_nuevos + 1):
    print(f"\n--- Artista nuevo {numero} ---")

    while True:
        tipo_elegido = input("Tipo (Solo, DJ o Banda): ").strip().lower()
        if tipo_elegido in ("solo", "dj", "banda"):
            break
        print("Tipo no válido.")

    nombre_artista = input("Nombre: ")
    genero_artista = input("Género musical: ")
    popularidad_artista = pedir_entero("Popularidad (1 a 100): ")

    try:
        if tipo_elegido == "solo":
            cancion_estrella = input("Canción más popular: ")
            nuevo_artista = Solo(nombre_artista, genero_artista,
                                 popularidad_artista, cancion_estrella)
        elif tipo_elegido == "dj":
            estilo_dj = input("Estilo: ")
            nuevo_artista = DJ(nombre_artista, genero_artista,
                               popularidad_artista, estilo_dj)
        else:
            cantidad_miembros = pedir_entero("Número de integrantes: ")
            nuevo_artista = Banda(nombre_artista, genero_artista,
                                  popularidad_artista, cantidad_miembros)

        cartelera.append(nuevo_artista)
        print("Artista agregado.")
    except ValueError as error_registro:
        print(f"No se pudo agregar: {error_registro}")

iniciar_festival(cartelera)