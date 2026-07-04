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

