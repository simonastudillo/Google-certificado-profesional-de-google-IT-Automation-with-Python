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