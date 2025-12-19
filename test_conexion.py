from app.db import get_conn

try:
    c = get_conn()
    print("CONEXIÓN ORACLE OK")
    c.close()
except Exception as e:
    print("ERROR:", e)
