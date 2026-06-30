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