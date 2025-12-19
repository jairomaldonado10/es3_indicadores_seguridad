from app.auth import registrar_usuario, login_usuario
from app.menu import menu_principal

def valido_usuario(u):
    return u and len(u) >= 3

def valido_password(p):
    return p and len(p) >= 6

def run():
    while True:
        print("\n1. Registrar usuario")
        print("2. Login")
        print("3. Salir")

        op = input("Opción: ").strip()

        if op == "1":
            u = input("Usuario: ").strip()
            p = input("Password: ").strip()

            if not valido_usuario(u):
                print("Usuario inválido")
                continue

            if not valido_password(p):
                print("Password inválido")
                continue

            registrar_usuario(u, p)
            print("Usuario registrado")

        elif op == "2":
            u = input("Usuario: ").strip()
            p = input("Password: ").strip()

            if not valido_usuario(u) or not valido_password(p):
                print("Credenciales inválidas")
                continue

            if login_usuario(u, p):
                menu_principal(u)
            else:
                print("Credenciales inválidas")

        elif op == "3":
            break

        else:
            print("Opción inválida")

if __name__ == "__main__":
    run()
