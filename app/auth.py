import bcrypt
from app.db import get_conn

def registrar_usuario(username, password):
    h = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    c = get_conn()
    cur = c.cursor()
    cur.execute(
        "INSERT INTO usuarios (username, password) VALUES (:u, :p)",
        {"u": username, "p": h}
    )
    c.commit()
    cur.close()
    c.close()

def login_usuario(username, password):
    c = get_conn()
    cur = c.cursor()
    cur.execute(
        "SELECT password FROM usuarios WHERE username = :u",
        {"u": username}
    )
    row = cur.fetchone()
    cur.close()
    c.close()
    if not row:
        return False
    return bcrypt.checkpw(password.encode(), row[0])
