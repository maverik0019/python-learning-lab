from inventario import Servidor


def test_iguales_si_tienen_el_mismo_nombre():

    a = Servidor(
        "web001",
        "Ubuntu",
        "22.04",
        ["nginx", "ssh"]
    )

    b = Servidor(
        "web001",
        "Debian",
        "12.5",
        ["ssh"]
    )

    assert a == b

def test_version_mas_vieja_es_menor():

    servidor_antiguo = Servidor(
        "web001",
        "Ubuntu",
        "18.04",
        ["ssh"]
    )

    servidor_nuevo = Servidor(
        "web002",
        "Ubuntu",
        "22.04",
        ["ssh", "nginx"]
    )

    assert servidor_antiguo < servidor_nuevo

def test_comparacion_mayor():

    antiguo = Servidor("web001", "Ubuntu", "18.04", ["ssh"])

    nuevo = Servidor("web002", "Ubuntu", "22.04", ["nginx"])

    assert nuevo > antiguo

def test_longitud_es_la_cantidad_de_servicios():

    servidor = Servidor(
        "web001",
        "Ubuntu",
        "22.04",
        ["nginx", "ssh", "cron"]
    )

    assert len(servidor) == 3


def test_min_devuelve_el_mas_desactualizado():

    a = Servidor(
        "web001",
        "Ubuntu",
        "22.04",
        ["nginx"]
    )

    b = Servidor(
        "db001",
        "Ubuntu",
        "18.04",
        ["postgresql"]
    )

    c = Servidor(
        "app001",
        "Ubuntu",
        "9.10",
        ["python"]
    )

    servidores = [a, b, c]

    assert min(servidores) == c