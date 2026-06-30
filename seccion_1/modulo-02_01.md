# Expresiones y variables

## Introducción a la sintaxis básica de Python
- cada lenguaje de programación ​tiene una sintaxis específica, ​que necesitamos aprender para ​poder decirle a la computadora qué hacer.
- profundizaremos en ​algunos componentes básicos de la sintaxis de Python
    - Varibales
    - Expresiones
    - Funciones
    - Bloques condicionales
- Cuando te sumerjas en la programación en Python, ​aprenderás a formular declaraciones ​de código que la computadora pueda entender
- La clave para ser bueno en la programación es ​practicar, practicar y practicar

---

## Explorando la sintaxis de Python
- Python es un lenguaje de programación flexible, usando en muchos campos, incluyendo el desarollo de software, Machine learning y analisis de datos.
- La sintaxis de Python incluye palabras que representan objetos y comandos.
- La mejor forma de aprender la sintaxis y semantica de Python es escribiendo código y ejecutándolo.
- Variables: Representan data almacenada como strings, tuplas, diccionarios, listas y objetos.
- Keywords: Palabras especiales que están reservadas para propósitos específicos.
```Python
int
not
or
for
while
return
```
- Operadores: Simbolos que representan operaciones en objetos y variables.
```Python
+
-
*
/
**
%
//
>
<
==
```
- Expresiones: Una combinación de numberos, simbolos y variables que representan un valor y retornan un resultado.
- Funciones: Un groupo de sentencias relacionadas para realizar una tarea específica y retornar un resultado.
```Python
def to_celsius(x):
   '''Convert Fahrenheit to Celsius'''
   return (x-32) * 5/9


to_celsius(75)
```
- Bloques condicionales: Sección de código que se ejecuta solo si se cumple una condición específica.
```Python
number = -4


if number > 0:
   print('Number is positive.')
elif number == 0:
   print('Number is zero.')
else:
   print('Number is negative.')
```
- Convenciones y reglas para nombrar variables y funciones:
    - No usar palabras reservadas de Python
    - No usar espacios en blanco
    - No usar caracteres especiales
    - No empezar con un número
    - Usar nombres descriptivos y significativos
    - Usar snake_case para variables y funciones, esto significa que se deben separar las palabras con guiones bajos.
    - Usa la guía oficial de estilo de Python, PEP 8, para escribir código limpio y legible. [link](https://peps.python.org/pep-0008/)

### The Zen of Python
```txt
Beautiful is better than ugly.

Explicit is better than implicit.

Simple is better than complex.

Complex is better than complicated.

Flat is better than nested.

Sparse is better than dense.

Readability counts.

Special cases aren't special enough to break the rules.

Although practicality beats purity.

Errors should never pass silently.

Unless explicitly silenced.

In the face of ambiguity, refuse the temptation to guess.

There should be one—and preferably only one—obvious way to do it.

Although that way may not be obvious at first unless you're Dutch.

Now is better than never.

Although never is often better than *right* now.

If the implementation is hard to explain, it's a bad idea.

If the implementation is easy to explain, it may be a good idea.

Namespaces are one honking great idea -- let's do more of those!
```

---

## Revisión: Tipos de datos
- Int: Representa números enteros, positivos o negativos, sin decimales.
```Python
print(7+8)
```
- String: Representa texto, que puede incluir letras, números y símbolos.
```Python
print("hello "+ "world")
```
- Errores: Representa errores en el código, que pueden ser de sintaxis o de ejecución.
    - Este ejemplo falla porque estamos intentando sumar un número entero con un string, lo cual no es permitido en Python.
```Python
print(7+"8")
#this will throw an error
```
- Obtener el tipo de dato de una variable usando la función type()
```Python
print(type("a")) # <class 'str'> - Indica que es un string
print(type(2)) # <class 'int'> - Indica que es un número entero
print(type(2.5)) # <class 'float'> - Indica que es un número decimal
``` 

---

## Tipos de datos
- String: Texto encerrado entre comillas simples o dobles.
- Integer: Números enteros, positivos o negativos, sin decimales.
- Float: Números decimales, positivos o negativos.
- Por lo general, el equipo no sabe cómo mezclar diferentes tipos de datos. 
    - Por ejemplo, no podemos sumar un número entero con un string, ya que son tipos de datos diferentes.
- Lea los errores detenidamente, comprenda lo que le dicen y, a ​continuación, utilice ese nuevo conocimiento para ayudarlo a corregir el error
- Si no estás seguro del tipo de dato de una variable, puedes usar la función type() para averiguarlo.

---

## Categorizar: Nombrar variables

---

## Anotando variables por tipo
- Las anotaciones de tipo son una forma de indicar el tipo de dato que se espera que tenga una variable.
- Reduce las posibilidades de errores y ayuda a documentar el código para otros usuarios.
- Como hacerlo: Debes usar el símbolo de dos puntos (:) seguido del tipo de dato esperado después del nombre de la variable.
```Python
name: str = "Betty"
age: int = 34
```

>[!TIP]
> Si una función espera una lista de números, anotala como `List[int]`, no solo `List`. Ser específico con tus tipos ayuda a encontrar posibles errores antes de que ocurran.

- Tipos dinámicos
    - Muchos lenguajes requieres declarar el tipo, en Python no es obligatorio.
    - Una de las ventajas de Python es que las variables pueden cambiar de tipo.
```Python
x = 5 # x es un entero
x = "Hello" # x ahora es un string
```
- Tipado dinámico puede ayudar a acelerar el desarrollo, pero también puede llevar a errores si no se tiene cuidado.
- Python infiere el tipo de dato de una variable en tiempo de ejecución, lo que significa que no es necesario declarar el tipo de dato al crear la variable.
- Comentarios del tipo: Otra forma de documentar el tipo de dato esperado de una variable es usar comentarios.
```Python
caption = "Picard" # type: str
```

### Cómo afectan al rendimiento
- Cada vez que una librería es importada, se necesita más capacidad computacional.
- Tipo de dato es poco común en usuarios de Python en ciencia de datos, pero es muy útil para desarrolladores de software.
- En programación orientada a objetos, las anotaciones de tipo son útiles para definir la interfaz de una clase y sus métodos.

>[!TIP]
> Se estrategico con las anotaciones de tipo. Esto puede añadir complejidad innecesaria.

---

## Reseña: Expresiones, números y conversiones de tipo
```Python
print(7+8.5) # 15.5 - Python convierte automáticamente el entero 7 a un float para realizar la operación.
print("a"+"b"+"c") # abc - Python concatena los strings.
print("This " + "is " + "pretty " + "neat!") # This is pretty neat! - Python concatena los strings.

base = 6
height = 3
area = (base*height)/2
print("The area of the triangle is: " + str(area))  # The area of the triangle is: 9.0 - Python convierte el float area a un string para poder concatenarlo con el resto del mensaje.
```

--- 

## Expresiones, números y conversiones de tipo
- Python puede transformar automáticamente un tipo de dato en otro cuando es necesario, esto se llama conversión de tipo implícita.
- Es por esto que podemos sumar un número entero con un número decimal y obtener un resultado decimal.
- Conversión Explícita: Podemos convertir un tipo de dato en otro usando funciones como int(), float() y str().

### Practica escribiendo expresiones y conversiones de tipo.
- En este escenario, tenemos un directorio con 5 archivos. Cada archivo tiene un tamaño diferente: 2048, 4357, 97658, 125 y 8. Completa los espacios para calcular el tamaño promedio de los archivos haciendo que Python sume todos los valores por ti, y luego asigna la variable files al número de archivos. Finalmente, muestra un mensaje que diga "El tamaño promedio es: " seguido del número resultante. Recuerda usar la función str() para convertir el número en una cadena.
```Python
total:int = 2048 + 4357 + 97658 + 125 + 8
files:int = 5
average:float = total / files
print("The average size is:" + str(average))
```

---

## Conversión de tipo implícita y explícita
- Conversión de tipo implícita: Python convierte automáticamente un tipo de dato en otro cuando es necesario.
- Conversión de tipo explícita: Podemos convertir un tipo de dato en otro usando funciones como int(), float() y str().