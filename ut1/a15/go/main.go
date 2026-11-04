package main

import (
	"errors"
	"fmt"
)

func Calcular(a, b float64, operacion string) (float64, error) {
	switch operacion {
	case "+":
		return a + b, nil
	case "-":
		return a - b, nil
	case "*":
		return a * b, nil
	case "/":
		if b == 0 {
			return 0, errors.New("no se puede dividir por cero")
		}
		return a / b, nil
	default:
		return 0, fmt.Errorf("operación '%s' no válida", operacion)
	}
}

func main() {
	fmt.Println("=== Calculadora en Go ===")
	res, err := Calcular(10, 5, "+")
	if err == nil {
		fmt.Printf("10 + 5 = %.2f\n", res)
	}
}
