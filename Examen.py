# -------------------- PERSONA --------------------
class Persona:
    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso


# -------------------- CABINA --------------------
class Cabina:
    def __init__(self, nroCabina):
        self.nroCabina = nroCabina
        self.personasAbordo = []

    def agregarPersona(self, p):
        # Máximo 10 personas
        if len(self.personasAbordo) >= 10:
            return False

        # Peso máximo total por cabina: 500 kg
        total_peso = sum(x.peso for x in self.personasAbordo)
        if total_peso + p.peso > 500:
            return False

        self.personasAbordo.append(p)
        return True


# -------------------- LINEA --------------------
class Linea:
    def __init__(self, color):
        self.color = color
        self.cabinas = []

    def agregarCabina(self):
        nro = len(self.cabinas) + 1
        nueva = Cabina(nro)
        self.cabinas.append(nueva)

    def agregarPersona(self, persona):
        # Agregar a la PRIMERA cabina siempre
        if len(self.cabinas) == 0:
            self.agregarCabina()

        cabina = self.cabinas[0]
        return cabina.agregarPersona(persona)


# -------------------- MI TELEFERICO --------------------
class MiTeleferico:
    def __init__(self):
        self.lineas = []
        self.cantidadIngresos = 0.0

    # Crear una línea nueva
    def agregarLinea(self, color):
        l = Linea(color)
        self.lineas.append(l)

    # Agregar cabina a una línea dada
    def agregarCabina(self, colorLinea):
        for l in self.lineas:
            if l.color == colorLinea:
                l.agregarCabina()

    # Agregar persona a la PRIMERA cabina de la línea X
    def agregarPersona(self, colorLinea, persona):
        for l in self.lineas:
            if l.color == colorLinea:
                agregado = l.agregarPersona(persona)
                if agregado:
                    # Calcular el ingreso
                    if persona.edad < 25 or persona.edad > 60:
                        self.cantidadIngresos += 1.5
                    else:
                        self.cantidadIngresos += 3
                return agregado
        return False

    # b) verificar que todas las cabinas cumplan reglas
    def verificarReglas(self):
        for linea in self.lineas:
            for cab in linea.cabinas:
                if len(cab.personasAbordo) > 10:
                    return False
                if sum(p.peso for p in cab.personasAbordo) > 500:
                    return False
        return True

    # c) calcular ingreso total
    def ingresoTotal(self):
        return self.cantidadIngresos

    # d) mostrar línea con MÁS ingreso (solo tarifa regular 3 bs)
    def lineaMasIngresoRegular(self):
        ingresos_por_linea = {}

        for linea in self.lineas:
            total = 0
            for cabina in linea.cabinas:
                for p in cabina.personasAbordo:
                    if 25 <= p.edad <= 60:
                        total += 3
            ingresos_por_linea[linea.color] = total

        if not ingresos_por_linea:
            return None

        return max(ingresos_por_linea, key=ingresos_por_linea.get)
mi = MiTeleferico()

mi.agregarLinea("Rojo")
mi.agregarCabina("Rojo")

p1 = Persona("Ana", 20, 50)
p2 = Persona("Luis", 30, 60)
p3 = Persona("Mario", 70, 55)

mi.agregarPersona("Rojo", p1)  # paga 1.5
mi.agregarPersona("Rojo", p2)  # paga 3
mi.agregarPersona("Rojo", p3)  # paga 1.5

print("Ingreso total:", mi.ingresoTotal())
print("Línea más ingreso regular:", mi.lineaMasIngresoRegular())

