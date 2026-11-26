"""Ejercicio 3: Empaque de artículos en cajas de 12 unidades."""

CAPACIDAD_CAJA = 12


def leer_cantidad():
    """Solicita la cantidad total de artículos (no negativa)."""
    while True:
        try:
            cantidad = int(input("Cantidad total de artículos: "))
        except ValueError:
            print("Error: ingrese un número entero.")
            continue
        if cantidad < 0:
            print("Error: la cantidad no puede ser negativa.")
        else:
            return cantidad


def calcular_cajas(cantidad):
    """Devuelve cuántas cajas completas se pueden llenar."""
    return cantidad // CAPACIDAD_CAJA


def calcular_sobrantes(cantidad):
    """Devuelve cuántos artículos quedan sin empacar."""
    return cantidad % CAPACIDAD_CAJA


def calcular_faltantes(sobrantes):
    """Devuelve cuántos artículos faltan para completar otra caja (0 si no hay sobrantes)."""
    if sobrantes > 0:
        return CAPACIDAD_CAJA - sobrantes
    return 0


def mostrar_resultado(cajas, sobrantes, faltantes):
    """Muestra los resultados de forma clara."""
    print("\n--- Resultados ---")
    print("Cajas completas:", cajas)
    print("Artículos sin empacar:", sobrantes)
    if sobrantes > 0:
        print("Artículos que faltan para completar otra caja:", faltantes)
    else:
        print("No hay sobrantes: no se necesita otra caja.")


def main():
    cantidad = leer_cantidad()
    cajas = calcular_cajas(cantidad)
    sobrantes = calcular_sobrantes(cantidad)
    faltantes = calcular_faltantes(sobrantes)
    mostrar_resultado(cajas, sobrantes, faltantes)


if __name__ == "__main__":
    main()
