from app.db import get_conn
from datetime import datetime

def guardar_indicador(indicador, usuario):
    c = get_conn()
    cur = c.cursor()
    cur.execute(
        """
        INSERT INTO indicadores
        (codigo, nombre, valor, fecha_valor, fecha_consulta, usuario, fuente)
        VALUES (:c, :n, :v, :fv, :fc, :u, :f)
        """,
        {
            "c": indicador.codigo,
            "n": indicador.nombre,
            "v": indicador.valor,
            "fv": indicador.fecha_valor,
            "fc": datetime.now(),
            "u": usuario,
            "f": indicador.fuente
        }
    )
    c.commit()
    cur.close()
    c.close()

def obtener_historial(usuario):
    c = get_conn()
    cur = c.cursor()
    cur.execute(
        """
        SELECT nombre, valor, fecha_valor, fecha_consulta, fuente
        FROM indicadores
        WHERE usuario = :u
        ORDER BY fecha_consulta DESC
        """,
        {"u": usuario}
    )
    rows = cur.fetchall()
    cur.close()
    c.close()
    return rows
