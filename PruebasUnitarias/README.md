# Pruebas Unitarias

## ¿Que son?
Son pequeños programas que se pueden ejecutar de forma independiente y cuyo objetivo es verificar el buen funcionamiento de partes aisladas de tu aplicación (función, clase).
En la practica las pruebas unitarias tiene la estructura siguiente (patrón AAA)

Otra forma de verlo es que las pruebas unitarias son como una interpolación de una función 
![alt text](/PruebasUnitarias/interpolacion.png)


* ARRANGE
 * Se preparan los datos
* ACT
 * Se estimula el sistema a probar
* ASSERT
 * Se verifica que el sistema se comporta como esperado

 Ejemplo:

 ```
# coding=utf-8
import unittest

def suma(a,b):
	res = a + b
	return res

class TestEjemplo(unittest.TestCase):

	#El objetivo de este test es validar que la función suma puede sumar dos numeros correctamente
	def testSuma(self):

		# ARRANGE
		# Se preparan los valores de ejemplo
		a = 3
		b = 5

		# ACT
		# Se estimula el sistema (aqui función suma)
		resultado = suma(a,b)

		# ASSERT
		resultado_esperado = 8
		self.assertEquals(resultado_esperado,resultado)

# Para ejecutar el test

if __name__ == "__main__":
	unittest.main()
 ```


## ¿Porque es importante hacer pruebas unitarias?

* Sin ellas nunca sabes realmente si lo estas haciendo bien o no
* Te ahorra mucho tiempo para verificar que tu aplicación sigue funcionando bien
* Te permite hacer cambios mucho más rápido y de forma más confiable
* Las pruebas unitarias son una excelente documentación
* No vas a tener miedo a mejorar la calidad de tu código (ya no más el "si funcion no lo toques")
* A la larga vas a aprender y mejorar mucho más escribiendo tests
* Vas a poder dormir mejor en la noche
* Tus clientes te van a amar y no lo van a poder creer (me paso)

## Desarrollo Guiado por Test (Test Driven Development : TDD)

* Es una práctica que consiste en escribir el test primero y luego el código que pasa el test
* Es un poco antituitivo pero tiene muchas gracias:
 * Permite separar el problema (que es lo que tiene que hacer mi clase, función) de la solución (como se implementa)
 * Te aseguras de cubrir tu código con tests ya que si escribes el test después la tentación es grande de pasar a otra cosa y nunca hacerlo al final
 * Te fuerza a hacerte buenas preguntas (que nombre poner a la función, cuantos parametros, que metodos, ...).
  * Si te cuesta escribir el test es problablemente porque algo anda mal con tu diseño. 
 * Una vez que el test esta escrito solamente lo ejecutas y arreglas lo errores, el test te guia. Esto te permite resolver un solo problema a la vez

## Ejemplo

### Ciclo de desarrollo con test (TDD)
1. Diseño
2. Escribir Test
3. Hacer fallar el test
4. Hacer pasar el test
5. Mejorar 
6. Volver a 1

### Implementemos una pila

Nos inspiramos del articulo [How to Write Good Unit Tests](https://developer.salesforce.com/page/How_to_Write_Good_Unit_Tests) pero lo vamos a hacer en Python

#### Diseño
La pila tiene los metodos siguientes
* ```push()```: poner un elemento arriba
* ```pop():``` sacar un elemento de arriba
* ```isEmpty()```: chequear si es vacia
* ```top()```: ver el valor de arriba

#### Pasos

1. Probar que los metodos ```push(),pop(),top(),isEmpty()``` funcionan bien con un elemento
2. Probar que los metodos ```push(),pop(),top(),isEmpty()``` funcionan bien varios elementos
3. Probar las excepciones / casos de bordes ()







