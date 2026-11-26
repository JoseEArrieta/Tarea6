"""Ejercicio 1: Registro de paquetes procesados durante cinco días."""

DIAS = 5
LIMITE = 20


def leer_entero_no_negativo(mensaje):
    """Pide un entero y repite hasta que sea válido y no negativo."""
    while True:
        try:
            valor = int(input(mensaje))
        except ValueError:
            print("Error: ingrese un número entero.")
            continue
        if valor < 0:
            print("Error: la cantidad no puede ser negativa.")
        else:
            return valor


def leer_paquetes():
    """Solicita las cantidades de los cinco días y devuelve el vector."""
    paquetes = []
    for dia in range(1, DIAS + 1):
        paquetes.append(leer_entero_no_negativo(f"Paquetes del día {dia}: "))
    return paquetes


def calcular_total(paquetes):
    """Devuelve el total de paquetes procesados."""
    total = 0
    for cantidad in paquetes:
        total += cantidad
    return total


def buscar_mayor(paquetes):
    """Devuelve la mayor cantidad registrada."""
    mayor = paquetes[0]
    for cantidad in paquetes:
        if cantidad > mayor:
            mayor = cantidad
    return mayor


def contar_dias_mayores(paquetes):
    """Devuelve cuántos días se procesaron más de 20 paquetes."""
    contador = 0
    for cantidad in paquetes:
        if cantidad > LIMITE:
            contador += 1
    return contador


def mostrar_resultados(paquetes, total, mayor, cantidad_dias):
    """Muestra el vector y los resultados calculados."""
    print("\n--- Resultados ---")
    print("Vector de paquetes:", paquetes)
    print("Total de paquetes procesados:", total)
    print("Cantidad mayor registrada:", mayor)
    print(f"Días con más de {LIMITE} paquetes:", cantidad_dias)


def main():
    paquetes = leer_paquetes()
    total = calcular_total(paquetes)
    mayor = buscar_mayor(paquetes)
    cantidad_dias = contar_dias_mayores(paquetes)
    mostrar_resultados(paquetes, total, mayor, cantidad_dias)


if __name__ == "__main__":
    main()
