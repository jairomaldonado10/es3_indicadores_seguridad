from app.auth import registrar_usuario, login_usuario
from app.menu import menu_monedas

def run():
    while True:
        print("\n1. Registrar usuario")
        print("2. Login")
        print("3. Salir")

        op = input("Opción: ").strip()

        if op == "1":
            u = input("Usuario: ").strip()
            p = input("Password: ").strip()
            registrar_usuario(u, p)
            print("Usuario registrado")

        elif op == "2":
            u = input("Usuario: ").strip()
            p = input("Password: ").strip()
            if login_usuario(u, p):
                menu_monedas(u)
            else:
                print("Credenciales inválidas")

        elif op == "3":
            break

        else:
            print("Opción inválida")

if __name__ == "__main__":
    run()
