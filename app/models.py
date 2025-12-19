from datetime import datetime

class Indicador:
    def __init__(self, data):
        self.codigo = data["codigo"]
        self.nombre = data["nombre"]
        self.valor = float(data["serie"][0]["valor"])
        self.fecha_valor = datetime.fromisoformat(
            data["serie"][0]["fecha"].replace("Z", "")
        )
        self.fuente = "mindicador.cl"
