"""Ejercicio 2: Control de espacios ocupados (matriz de 2 x 3)."""

FILAS = 2
COLUMNAS = 3


def leer_valor_binario(mensaje):
    """Pide un valor y acepta únicamente 0 o 1."""
    while True:
        try:
            valor = int(input(mensaje))
        except ValueError:
            print("Error: ingrese 0 o 1.")
            continue
        if valor in (0, 1):
            return valor
        print("Error: solo se permiten los valores 0 y 1.")


def leer_espacios():
    """Solicita los valores y devuelve la matriz de 2 por 3."""
    matriz = []
    for i in range(FILAS):
        fila = []
        for j in range(COLUMNAS):
            fila.append(leer_valor_binario(f"Espacio fila {i + 1}, columna {j + 1} (1=ocupado, 0=disponible): "))
        matriz.append(fila)
    return matriz


def mostrar_matriz(matriz):
    """Muestra la matriz de forma ordenada."""
    print("\nMatriz de espacios:")
    for fila in matriz:
        print("  ".join(str(valor) for valor in fila))


def contar_ocupados(matriz):
    """Devuelve el total de espacios ocupados (valor 1)."""
    ocupados = 0
    for fila in matriz:
        for valor in fila:
            if valor == 1:
                ocupados += 1
    return ocupados


def contar_disponibles(matriz):
    """Devuelve el total de espacios disponibles (valor 0)."""
    disponibles = 0
    for fila in matriz:
        for valor in fila:
            if valor == 0:
                disponibles += 1
    return disponibles


def ocupados_por_fila(matriz):
    """Devuelve una lista con los espacios ocupados de cada fila."""
    resultado = []
    for fila in matriz:
        contador = 0
        for valor in fila:
            if valor == 1:
                contador += 1
        resultado.append(contador)
    return resultado


def main():
    matriz = leer_espacios()
    mostrar_matriz(matriz)
    ocupados = contar_ocupados(matriz)
    disponibles = contar_disponibles(matriz)
    por_fila = ocupados_por_fila(matriz)
    print("\n--- Resultados ---")
    print("Espacios ocupados:", ocupados)
    print("Espacios disponibles:", disponibles)
    for i, cantidad in enumerate(por_fila, start=1):
        print(f"Ocupados en la fila {i}: {cantidad}")


if __name__ == "__main__":
    main()
