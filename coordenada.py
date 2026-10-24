class Coordenada:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, otra):
        if not isinstance(otra, Coordenada):
            return NotImplemented

        return Coordenada(
            self.x + otra.x,
            self.y + otra.y
        )

    def __repr__(self):
        return f"Coordenada({self.x}, {self.y})"


punto1 = Coordenada(2, 3)
punto2 = Coordenada(4, 5)
punto3 = punto1 + punto2

resultado = punto1 + punto2
print(resultado)

