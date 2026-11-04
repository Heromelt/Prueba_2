def calcular(a: float, b: float, operacion: str) -> float:
    if operacion == "+":
        return a + b
    elif operacion == "-":
        return a - b
    elif operacion == "*":
        return a * b
    elif operacion == "/":
        if b == 0:
            raise ZeroDivisionError("No se puede dividir por cero.")
        return a / b
    else:
        raise ValueError(f"Operación '{operacion}' no válida.")

if __name__ == "__main__":
    try:
        print("=== Calculadora en Python ===")
        print(f"10 + 5 = {calcular(10, 5, '+')}")
        print(f"10 / 2 = {calcular(10, 2, '/')}")
    except (ZeroDivisionError, ValueError) as e:
        print(f"Error: {e}")
