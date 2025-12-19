from app.api import consultar_indicador
from app.models import Indicador
from app.repository import guardar_indicador, obtener_historial

def menu_principal(usuario):
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Ver cambio de moneda en tiempo real")
        print("2. Ver historial de consultas")
        print("3. Salir")

        op = input("Opción: ").strip()

        if op == "1":
            menu_monedas(usuario)

        elif op == "2":
            historial = obtener_historial(usuario)
            if not historial:
                print("\nNo hay registros aún.")
            else:
                print("\n=== HISTORIAL ===")
                for h in historial:
                    print(f"{h[0]} | {h[1]} | {h[2]} | {h[3]} | {h[4]}")

        elif op == "3":
            break

        else:
            print("Opción inválida")

def menu_monedas(usuario):
    mapa = {
        "1": "dolar",
        "2": "euro",
        "3": "uf",
        "4": "utm",
        "5": "ipc",
        "6": "ivp"
    }

    while True:
        print("\n=== CAMBIO DE MONEDA ===")
        print("1. Dólar")
        print("2. Euro")
        print("3. UF")
        print("4. UTM")
        print("5. IPC")
        print("6. IVP")
        print("7. Volver")

        op = input("Opción: ").strip()

        if op == "7":
            break

        if op not in mapa:
            print("Opción inválida")
            continue

        try:
            data = consultar_indicador(mapa[op])
            ind = Indicador(data)

            print("\nIndicador:", ind.nombre)
            print("Valor:", ind.valor)
            print("Fecha:", ind.fecha_valor)

            g = input("¿Guardar en base de datos? (s/n): ").lower()
            if g == "s":
                guardar_indicador(ind, usuario)
                print("Guardado correctamente")

        except Exception as e:
            print("Error:", e)
