class Indicador:
    def __init__(self, data):
        self.codigo = data["codigo"]
        self.nombre = data["nombre"]
        self.valor = data["serie"][0]["valor"]
        self.fecha_valor = data["serie"][0]["fecha"]
        self.fuente = "mindicador.cl"
