from app.db import get_conn

def guardar_indicador(ind, usuario):
    c = get_conn()
    cur = c.cursor()
    cur.execute(
        """
        INSERT INTO indicadores
        (codigo, nombre, valor, fecha_valor, fecha_consulta, usuario, fuente)
        VALUES
        (:c, :n, :v,
         TO_TIMESTAMP(:fv,'YYYY-MM-DD"T"HH24:MI:SS.FF3"Z"'),
         SYSTIMESTAMP, :u, :f)
        """,
        {
            "c": ind.codigo,
            "n": ind.nombre,
            "v": ind.valor,
            "fv": ind.fecha_valor,
            "u": usuario,
            "f": ind.fuente
        }
    )
    c.commit()
    cur.close()
    c.close()
