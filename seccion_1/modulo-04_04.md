# Progrmación orientada a objetos

## Introducción
- Programación orientada a objetos, ​que es una forma de pensar ​e implementar nuestro código.

---

## Que es un método?
- En Python, los métodos son comportamientos asociados a parámetros de objetos que modifican el estado de dichos objetos.
- Son, esencialmente, funciones que pertenecen a una instancia específica de una clase.
- Esto significa que, por ejemplo, al llamar a un método en una lista, solo se modifica esa instancia de la lista, y no todas las listas en general.
- Categorías de métodos:
  - Métodos de instancia: Operan sobre una instancia específica de la clase.
  - Métodos de clase: Operan sobre la clase en sí, no sobre instancias individuales.
  - Métodos estáticos: No dependen de la instancia ni de la clase, y se utilizan para funciones que no necesitan acceder a datos de instancia o clase.

- Métodos de instancia
Se definen dentro de una clase creando funciones en su definición. Al crear instancias de una clase, se pueden llamar a sus métodos para que el programa pueda controlarlas y modificarlas directamente. Los métodos de instancia pueden recibir un parámetro llamado `self`, que representa la instancia sobre la que se ejecuta el método. Este parámetro permite acceder a los atributos de la instancia mediante la notación de punto, como `self.name`, que accede al atributo `name` de esa instancia específica del objeto de la clase. Cuando se tienen variables con valores diferentes para distintas instancias, se denominan variables de instancia.

- Métodos de clase
Los métodos de clase, por otro lado, se invocan para la clase en sí, en lugar de para una instancia. Se marcan con el decorador `@classmethod` y reciben un parámetro `cls` que apunta a la clase —y no a una instancia específica— cuando se llama al método. Un caso de uso común para los métodos de clase es crear y modificar estructuras de datos que contienen registros de todas las instancias de una clase. Normalmente, los programadores crean una lista dentro de la definición de la clase y métodos para agregar instancias de la clase a esa lista con el fin de mantener un registro de la misma.

- Métodos estáticos
Por último, los métodos estáticos, marcados con el decorador `@staticmethod`, no aceptan parámetros `self` ni `cls`. Se comportan como funciones normales, con la diferencia de que se pueden llamar directamente desde la clase. Es importante destacar que no es necesario instanciar la clase; los métodos simplemente residen en ella. Esto se debe a que las definiciones de clase son en sí mismas un objeto (es decir, una instancia de la clase base abstracta), lo que reduce la sobrecarga y permite encapsular las funciones de forma sencilla. Los programadores utilizan métodos estáticos cuando el método no necesita acceder a datos específicos de la instancia o la clase.

---

## Constructores y otros métodos especiales

- Creando la instancia de una clase:
    - En Python cuando se crea una instancia de una clase, se llama automáticamente al método especial constructor.
    - El constructor es lo que permite inicializar los atributos de la clase y todo lo necesario para que la instancia funcione correctamente.
    - En Python, el constructor se define mediante el método especial `__init__()`.
```Python
class Apple:
    def __init__(self):
        self.color = "red"
        self.flavor = "sweet"

honeycrisp = Apple()
print(honeycrisp.color)

# prints "red"
```

- Modificar variables
    - Si queremos dar más flexibilidad a nuestro constructor, podemos pasarle parámetros para modificar los valores de las variables de instancia.
```Python
class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

honeycrisp = Apple("red", "sweet")
fuji = Apple("red", "tart")
print(honeycrisp.flavor)
print(fuji.flavor)

# prints "sweet" and "tart"
```

- Otros métodos especiales
    - Al igual que el constructor `__init__`, los métodos especiales comienzan y terminan con un doble guion bajo, y esto se denomina método `dunder`.
    - La palabra "dunder" combina la "d" de double y la "under" de underscore.
    - Estos métodos se pueden "sobreescribir" para cambiar el comportamiento predeterminado de los objetos en Python.
    - Ejemplos:
        - `__str__`: Controla cómo se convierte un objeto a una representación de cadena para su salida. Cuando imprimes algo con print(), Python llama al método __str__() del objeto y muestra lo que este devuelve. En la mayoría de los casos, la salida predeterminada es simplemente el nombre de la clase y una ubicación de memoria.
        - `__len__`: Permite que la función len() devuelva un valor específico para un objeto. Por ejemplo, si tienes una clase que representa una colección de elementos, puedes definir el método `__len__()` para devolver el número de elementos en esa colección.
        - `__contains__`: Permite que la palabra clave `in` funcione con objetos de tu clase. Por ejemplo, si tienes una clase que representa un conjunto de elementos, puedes definir el método `__contains__()` para verificar si un elemento está presente en ese conjunto.
        - `__eq__`: Permite que los operadores de comparación, como `==`, funcionen con objetos de tu clase. Por ejemplo, si tienes una clase que representa un punto en un espacio bidimensional, puedes definir el método `__eq__()` para comparar dos puntos y determinar si son iguales.
```Python
class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

    def __str__(self):
        return "an apple which is {} and {}".format(self.color, self.flavor)

honeycrisp = Apple("red", "sweet")
print(honeycrisp)

# prints "an apple which is red and sweet"
```

---

## Métodos especiales
- En lugar de crear clases con valores vacíos o predeterminados, podemos establecer estos valores al crear la instancia. Esto garantiza que no se omita ningún valor importante y evita muchas líneas de código innecesarias. Para ello, utilizamos un método especial llamado constructor. A continuación, se muestra un ejemplo de una clase Apple con un método constructor definido.
```Python
class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

jonagold = Apple("red", "sweet")
print(jonagold.color)
```
- Además del método especial del constructor `__init__`, también existe el método especial `__str__`. Este método nos permite definir cómo se imprimirá una instancia de un objeto cuando se pase a la función `print()`. Si un objeto no tiene definido este método especial, utilizará la representación predeterminada, que imprimirá la posición del objeto en la memoria. No es muy útil. Aquí está nuestra clase `Apple`, con el método `__str__` añadido:
```Python
class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
    def __str__(self):
        return "This apple is {} and its flavor is {}".format(self.color, self.flavor)
```

---

## Instance Methods
- Los métodos son funciones que operan ​en los atributos de una instancia específica de una clase. 
- Para llamar parámetros propios de la clase en los diferentes métodos, se utiliza el parámetro `self`. Este parámetro hace referencia a la instancia de la clase y permite acceder a sus atributos y métodos.
- Ejemplo: `self.name` accede al atributo `name` de esa instancia específica del objeto de la clase.
- Para setear un atributo podemos hacerlo de 2 formas:
    1. Definiendo el atributo en el constructor `__init__` y luego modificándolo mediante un método de instancia.
    2. Definiendo el atributo directamente en un método de instancia, sin necesidad de declararlo en el constructor. Esto permite crear atributos de manera dinámica según las necesidades de la instancia.
- Las variables que tienen valores diferentes para distintas instancias ​de la misma clase se denominan variables de instancia

---

## Métodos como operadores especiales
- Los operadores especiales son símbolos o palabras clave específicos integrados que proporcionan un comportamiento especial al usarse con ciertos tipos de datos u objetos
- En tu clase, puedes definir métodos para implementar o sobrescribir el comportamiento estándar de los operadores de Python, creando así métodos como operadores especiales

- Diferentes tipos de operadores especiales:
    - Operadores aritméticos. Incluyen + (suma), - (resta), * (multiplicación), / (división) y ** (exponenciación).
    - Operadores de comparación. Incluyen == (igualdad), != (desigualdad), < (menor que) y >= (mayor o igual que).
    - Operadores lógicos. Incluyen and, or y not.
    - Operadores de asignación. Incluyen = (asignación simple), += (asignación de suma) y %= (asignación de módulo).
- Realizar operaciones especiales
    - Cada operador especial tiene un método `dunder` correspondiente que implementa la operación.
```Python
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def __add__(self, other):
        return self.area() + other.area()

triangle1 = Triangle(10, 5)
triangle2 = Triangle(6, 8)
print("The area of triangle 1 is", triangle1.area())
print("The area of triangle 2 is", triangle2.area())
print("The area of both triangles is", triangle1 + triangle2)

# The area of triangle 1 is 25.0 
# The area of triangle 2 is 24.0 
# The area of both triangles is 49.0
```

---

## Guía de estudio: Clases y métodos
- Definir clases y métodos:
```Python
class ClassName:
    def method_name(self, other_parameters):
        body_of_method
```
- Clases e instancias
    - Las clases definen el comportamiento de todas las instancias de una clase específica. En Python, el código que define una clase es, en sí mismo, un objeto; las clases se pueden usar sin instanciar un solo objeto, como cuando se utilizan métodos estáticos.
    - Recuerda que cada variable de una clase específica es una instancia u objeto.
    - En Python, los métodos `getter` y `setter` se utilizan para controlar el acceso a los atributos de un objeto. El método `getter` recupera el valor de un atributo, mientras que el método `setter` establece o cambia el valor del atributo, a menudo incluyendo algún tipo de validación o modificación de los datos antes de establecer el valor.
    - Puedes acceder a un atributo de una instancia, como `name`, llamando a `self.name` dentro de los métodos de la clase, o a `<instance>.name` fuera de la clase, donde `<instance>` es la instancia específica de la clase con la que estás trabajando. Los objetos pueden tener atributos, que almacenan información sobre el objeto.
    - Puedes hacer que los objetos realicen tareas llamando a sus métodos.
    - El primer parámetro de los métodos, `self`, representa la instancia actual.
    - Los métodos son similares a las funciones, pero solo se pueden usar dentro de una clase.
    - Puedes usar métodos de clase junto con una variable de clase para llevar un registro del número de instancias de una clase, incrementando la variable de clase cada vez que se crea una instancia en el método `__init__` de la clase.
- Métodos especiales
    - Los métodos especiales comienzan y terminan con __.
    - Los métodos especiales tienen nombres específicos, como __init__ para el constructor o __str__ para la conversión a cadena.
    - Los métodos __str__ y __repr__ permiten definir representaciones de cadena legibles y sin ambigüedades de los objetos, respectivamente.
    - Al definir métodos como __eq__, __ne__, __lt__, __gt__, __le__ y __ge__, se puede controlar cómo se comparan los objetos de la clase.

```Python
class ClassName:
    """Documentation for the class."""
    def method_name(self, other_parameters):
        """Documentation for the method."""
        body_of_method
        
def function_name(parameters):
    """Documentation for the function."""
    body_of_function


def my_function(x):
    """
    Sample usage:
    >>> my_function(“example input”)
    "example output"
    """
    

help(some_function)
```