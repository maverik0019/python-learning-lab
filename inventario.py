
class Servidor:
    def __init__(self, nombre, sistema_operativo, version, servicios):
        self.nombre = nombre
        self.sistema_operativo = sistema_operativo
        self.version = version
        self.servicios = servicios

    def __repr__(self):
        return (
            f"Servidor({self.nombre}, {self.sistema_operativo} "
            f"{self.version}, {len(self.servicios)} servicios)"
        )
    def __eq__(self, otro):
        if not isinstance(otro, Servidor):
            return NotImplemented
        return self.nombre == otro.nombre
    
    def _version(self):
        return tuple(int(parte) for parte in self.version.split("."))
    
    def __lt__(self, otro):
        if not isinstance(otro, Servidor):
            return NotImplemented
        return self._version() < otro._version()

    def __len__(self):
        return len(self.servicios)
    
a = Servidor("web001", "Ubuntu", "22.04", ["nginx", "ssh", "cron"])
b = Servidor("web001", "Ubuntu", "22.04", ["nginx", "ssh", "cron"])
c = Servidor("db001", "Ubuntu", "18.04", ["postgresql", "ssh"])
d = Servidor("app001", "Ubuntu", "9.10", ["python"])

print(a == b)
print(a < c)
print(len(a))