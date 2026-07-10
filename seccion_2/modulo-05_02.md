# Test unitarios

## Test unitarios
- Un test unitario le entrega al desarrollador herramientas para construir y ejecutar pruebas.
- Estas pruebas se puede ejecutar en componentes individuales o en unidades de código, como funciones o métodos.
- Al ejecutar pruebas podemos identificar y corregir errores en el código antes de que se conviertan en problemas más grandes.
- Conceptos:
    - `test fixture` (Dispositivo de prueba): Se refiere a la preparación de 1 o más pruebas, tambien incluye cualquier acción que involucre la limpieza de los recursos utilizados durante la prueba.
    - `test case`(caso de prueba): Esta es una prueba unitaria que busca una respuesta específica para un conjunto de entradas.
    - `Test suite`(conjunto de pruebas): Es un conjunto de casos de prueba o conjuntos de pruebas o una combinación de ambos, Se usa para compilar tests que se pueden ejecutar juntos.
    - `Test runner`(ejecutor de pruebas): Este ejecuta y entrega al desarrollador los resultados de las pruebas, pueden usar diferentes interfaces como la línea de comandos, una interfaz gráfica o un navegador web.
- Caso de uso:
    - Este código Python simula una fábrica de pasteles y realiza diversas funciones.
    - Estas incluyen la selección de distintos tamaños y sabores de pastel (pequeño, mediano y grande), así como chocolate o vainilla.
    - Además, la sencilla clase permite a los desarrolladores añadir chispas de colores o cerezas al pastel, obtener una lista de ingredientes y calcular el precio según el tamaño y los ingredientes adicionales.
    - Ejecute el siguiente código:
```Python
from typing import List


class CakeFactory:
 def __init__(self, cake_type: str, size: str):
   self.cake_type = cake_type
   self.size = size
   self.toppings = []

   # Price based on cake type and size
   self.price = 10 if self.cake_type == "chocolate" else 8
   self.price += 2 if self.size == "medium" else 4 if self.size == "large" else 0

 def add_topping(self, topping: str):
     self.toppings.append(topping)
     # Adding 1 to the price for each topping
     self.price += 1

 def check_ingredients(self) -> List[str]:
     ingredients = ['flour', 'sugar', 'eggs']
     ingredients.append('cocoa') if self.cake_type == "chocolate" else ingredients.append('vanilla extract')
     ingredients += self.toppings
     return ingredients

 def check_price(self) -> float:
     return self.price

# Example of creating a cake and adding toppings
cake = CakeFactory("chocolate", "medium")
cake.add_topping("sprinkles")
cake.add_topping("cherries")
cake_ingredients = cake.check_ingredients()
cake_price = cake.check_price()


cake_ingredients, cake_price
```
- En el código anterior, se definen la clase y los métodos de la fábrica de pasteles.
- Ahora es el momento de definir los métodos de prueba unitaria para probar las diferentes funciones del código.
- El conjunto de pruebas incluye pruebas para el sabor, el tamaño, los ingredientes, los aderezos y el precio del pastel.
- El primer caso de prueba del conjunto proporcionará intencionalmente un valor incorrecto, ¡y eso es lo que buscamos!
- Crea instrucciones específicas para asegurarte de que el programa se comporta como debería.
- Esto incluye proporcionar datos incorrectos para determinar si el programa arrojará resultados fallidos.
- Dado que las pruebas unitarias se basan en clases, encapsula estas instrucciones en métodos de prueba.
```Python
import unittest

class TestCakeFactory(unittest.TestCase):
 def test_create_cake(self):
   cake = CakeFactory("vanilla", "small")
   self.assertEqual(cake.cake_type, "vanilla")
   self.assertEqual(cake.size, "small")
   self.assertEqual(cake.price, 8) # Vanilla cake, small size

 def test_add_topping(self):
     cake = CakeFactory("chocolate", "large")
     cake.add_topping("sprinkles")
     self.assertIn("sprinkles", cake.toppings)

 def test_check_ingredients(self):
     cake = CakeFactory("chocolate", "medium")
     cake.add_topping("cherries")
     ingredients = cake.check_ingredients()
     self.assertIn("cocoa", ingredients)
     self.assertIn("cherries", ingredients)
     self.assertNotIn("vanilla extract", ingredients)

 def test_check_price(self):
     cake = CakeFactory("vanilla", "large")
     cake.add_topping("sprinkles")
     cake.add_topping("cherries")
     price = cake.check_price()
     self.assertEqual(price, 13) # Vanilla cake, large size + 2 toppings


# Running the unittests
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestCakeFactory))
```
- Resultado
```bash
..F.
======================================================================
FAIL: test_check_price (__main__.TestCakeFactory)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "<ipython-input-9-32dbf74b3655>", line 33, in test_check_price
    self.assertEqual(price, 13) # Vanilla cake, large size + 2 toppings
AssertionError: 14 != 13

----------------------------------------------------------------------
Ran 4 tests in 0.007s

FAILED (failures=1)
<unittest.runner.TextTestResult run=4 errors=0 failures=1>
```
- El programa llama al método TextTestRunner(), que devuelve un objeto runner (TextTestResult).
- Indica que se produjo un error: la instrucción self.assertEqual(price, 13) era incorrecta, ya que debería haber sido 14.
- ¿Cómo podemos corregir esa parte de la prueba? Actualice esa parte del código de la siguiente manera:
```Python
 import unittest


# Fixing the test_check_price method
class TestCakeFactory(unittest.TestCase):
 # ... Other tests remain the same

 def test_check_price(self):
     cake = CakeFactory("vanilla", "large")
     cake.add_topping("sprinkles")
     cake.add_topping("cherries")
     price = cake.check_price()
     self.assertEqual(price, 14) # Vanilla cake, large size + 2 toppings

# Re-running the unittests
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestCakeFactory))
```
- Resultado
```bash
----------------------------------------------------------------------
Ran 1 test in 0.002s

OK
<unittest.runner.TextTestResult run=1 errors=0 failures=0>
```

---

## pytest
- Pytest es una potente herramienta de pruebas para Python que ayuda a los programadores a escribir programas más eficaces y estables.
- Permite escribir diversos tipos de pruebas, como pruebas de integración, de extremo a extremo y funcionales.
- Ofrece detección automática de pruebas y genera informes detallados.
- Como escribir tests
    - Las pruebas de Python se escriben con funciones que utilizan la operación `assert()`.
    - `assert` es una herramienta de depuración común en Python que permite a los programadores incluir comprobaciones de integridad en su código.
    - Estas comprobaciones garantizan que ciertas condiciones o suposiciones se cumplan durante la ejecución.
    - Si la condición proporcionada a `assert()` resulta ser falsa, indica un error en el código, se genera una excepción y se detiene la ejecución del programa.
    - Normalmente, el código proporciona una condición de `assert` seguida de un mensaje opcional. Un ejemplo es:
```Python
def divide(a, b):
	assert b != 0, "Cannot divide by zero"
	return a / b
```
- La aserción `assert b != 0` garantiza que el divisor `b` no sea cero antes de realizar la operación de división.
- fixtures de Pytest
    - Los fixtures se utilizan para separar partes del código que solo se ejecutan para las pruebas.
    - Son fragmentos reutilizables de código de configuración y limpieza de pruebas que se comparten entre varias pruebas.
    - Los fixtures benefician a los desarrolladores al ayudar a mantener sus pruebas limpias y evitar la duplicación de código.
```Python
import pytest
class Fruit:
    def __init__(self, name):
        self.name = name
        self.cubed = False


    def cube(self):
        self.cubed = True


class FruitSalad:
    def __init__(self, *fruit_bowl):
        self.fruit = fruit_bowl
        self._cube_fruit()


    def _cube_fruit(self):
        for fruit in self.fruit:
            fruit.cube()


# Arrange
@pytest.fixture
def fruit_bowl():
    return [Fruit("apple"), Fruit("banana")]


def test_fruit_salad(fruit_bowl):
    # Act
    fruit_salad = FruitSalad(*fruit_bowl)


    # Assert
    assert all(fruit.cubed for fruit in fruit_salad.fruit)
```
- En este ejemplo, `test_fruit_salad` solicita `fruit_bowl`.
- Cuando pytest reconoce esto, ejecuta la función de prueba `fruit_bowl` y toma el objeto que devuelve como argumento `fruit_bowl` en `test_fruit_salad`.

---

## Comparando unittest vs pytest
- Tanto unittest como pytest proporcionan a los desarrolladores herramientas para crear código robusto y fiable mediante diferentes tipos de pruebas.
- Ambas se pueden usar al crear programas en Python, y la elección depende de las preferencias del desarrollador.
- Diferencias clave:
    - Unittest es una herramienta integrada en Python, mientras que pytest debe importarse desde fuera del script.
    - La detección de pruebas funciona de manera diferente para cada tipo de prueba.
    - Unittest tiene la funcionalidad de detectar automáticamente casos de prueba dentro de una aplicación, pero debe ejecutarse desde la línea de comandos.
    - Las pruebas de pytest se ejecutan automáticamente usando el prefijo `test_`.
    - Unittest utiliza un enfoque orientado a objetos para escribir pruebas, mientras que pytest utiliza un enfoque funcional.
    - Pytest utiliza sentencias `assert` integradas, lo que facilita la lectura y escritura de las pruebas.
    - Por otro lado, unittest proporciona métodos de aserción especiales como `assertEqual()` o `assertTrue()`.
    - Existe compatibilidad con versiones anteriores entre unittest y pytest.
    - Dado que unittest está integrado en Python, estos conjuntos de pruebas se ejecutan con mayor facilidad.
    - Gracias a la compatibilidad con versiones anteriores, el framework unittest se puede ejecutar sin problemas utilizando el framework pytest sin grandes modificaciones.
    - Esto permite a los desarrolladores adoptar pytest gradualmente e integrarlo en su código.

---

## Revisión: Unit test
- Los siguientes bloques de código se usarán en el próximo video:
```Python
#!/usr/bin/env python3
import re
def rearrange_name(name):
  result = re.search(r"^([\w .]*), ([\w .]*)$", name)
  return "{} {}".format(result[2], result[1])
from rearrange import rearrange_name


rearrange_name("Lovelace, Ada")  
```