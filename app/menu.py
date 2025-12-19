from app.api import consultar_indicador
from app.models import Indicador
from app.repository import guardar_indicador

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
        print("\n=== CAMBIO DE MONEDA EN TIEMPO REAL ===")
        print("1. Dólar")
        print("2. Euro")
        print("3. UF")
        print("4. UTM")
        print("5. IPC")
        print("6. IVP")
        print("7. Salir")

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
