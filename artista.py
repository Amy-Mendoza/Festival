class Artista:
    def __init__(self, nombre, genero, popularidad):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        if not isinstance(genero, str) or not genero.strip():
            raise ValueError("El género no puede estar vacío.")
        if not isinstance(popularidad, int) or not 1 <= popularidad <= 100:
            raise ValueError("La popularidad debe ser un número entero del 1 al 100.")

        self.nombre = nombre.strip()
        self.genero = genero.strip()
        self.popularidad = popularidad

    def presentarse(self):
        print(f"Ahora, el artista que nos acompaña en el escenario es: {self.nombre} ({self.genero}), "
              f"popularidad {self.popularidad}/100.")

    def actuar(self):
        print(f"{self.nombre} realiza su presentación.")

    def despedirse(self):
        print(f"{self.nombre} se despide del público. Muchas gracias por asistir.")


class Solo(Artista):
    def __init__(self, nombre, genero, popularidad, cancion_mas_popular):
        super().__init__(nombre, genero, popularidad)
        if not isinstance(cancion_mas_popular, str) or not cancion_mas_popular.strip():
            raise ValueError("La canción más popular no puede estar vacía.")
        self.cancion_mas_popular = cancion_mas_popular.strip()

    def actuar(self):
        print(f"{self.nombre} canta su éxito {self.cancion_mas_popular} "
              f"con gran energía.")


class DJ(Artista):
    def __init__(self, nombre, genero, popularidad, estilo):
        super().__init__(nombre, genero, popularidad)
        if not isinstance(estilo, str) or not estilo.strip():
            raise ValueError("El estilo no puede estar vacío.")
        self.estilo = estilo.strip()

    def actuar(self):
        print(f"El DJ {self.nombre} mezcla temas de estilo {self.estilo}, "
              f"haciendo vibrar al público.")


class Banda(Artista):
    def __init__(self, nombre, genero, popularidad, integrantes):
        super().__init__(nombre, genero, popularidad)
        if not isinstance(integrantes, int) or integrantes < 2:
            raise ValueError("Una banda debe tener al menos 2 integrantes.")
        self.integrantes = integrantes

    def actuar(self):
        print(f"La banda {self.nombre} con {self.integrantes} integrantes "
              f"toca un poderoso solo de guitarra.")


def iniciar_festival(lista_artistas):
    print("\n" + "=" * 50)
    print("   INICIA EL FESTIVAL")
    print("=" * 50)

    for participante in lista_artistas:
        print()
        participante.presentarse()
        participante.actuar()
        participante.despedirse()
        print("-" * 50)
        print("Fin de la actuación")
        print("-" * 50)

    print("\nTermina el festival.")