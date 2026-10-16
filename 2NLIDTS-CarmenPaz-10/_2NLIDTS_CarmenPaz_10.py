def suma_recursiva(n):
    """Solución recursiva. Caso base: n <= 9 (un solo dígito)."""
    if n <= 9:
        return n
    return suma_recursiva(n // 10) + n % 10


def suma_iterativa(n):
    """Solución iterativa. Acumula el último dígito y lo elimina mientras n > 9."""
    suma = 0
    while n > 9:
        suma += n % 10
        n //= 10
    return suma + n


def leer_entero(mensaje, minimo):
    """Pide un entero hasta que sea válido y mayor o igual a 'minimo'."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor >= minimo:
                return valor
            print(f"Debe ser un número mayor o igual a {minimo}.")
        except ValueError:
            print("Entrada no válida. Ingrese un número entero.")


def main():
    # Preguntar cuántos números se van a ingresar
    cantidad = leer_entero("¿Cuántos números va a ingresar? ", 1)

    for i in range(1, cantidad + 1):
        # Solo se aceptan números naturales (n >= 0)
        n = leer_entero(f"\nIngrese el número {i} de {cantidad}: ", 0)

        print(f"Suma de dígitos (recursiva): {suma_recursiva(n)}")
        print(f"Suma de dígitos (iterativa): {suma_iterativa(n)}")


if __name__ == "__main__":
    main()
