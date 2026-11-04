package main

import "testing"

func TestCalcularExito(t *testing.T) {
	res, err := Calcular(10, 5, "+")
	if err != nil || res != 15 {
		t.Errorf("Error en suma")
	}
}

func TestFallidoIntencional(t *testing.T) {
	res, _ := Calcular(2, 2, "+")
	if res != 5 {
		t.Errorf("Resultado incorrecto: obtuve %.2f, esperaba 5.00", res)
	}
}
