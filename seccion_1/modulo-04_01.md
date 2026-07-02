# Strings

## Introducción estructuras básicas
- Anteriormente cubrimos
    - elementos básicos de la sintaxis de Python
    - definir funciones
    - cómo hacer que su computadora actúe de ​manera diferente en función de los condicionales
    - cómo hacer que realice operaciones ​repetidamente usando while y para bucles y recursión
    - aprenderemos un montón de ​nuevas habilidades muy útiles ​para añadir a tu caja de herramientas de programación. 
    - Revisaremos algunos tipos de datos que proporciona ​el lenguaje Python para ayudarnos a ​resolver problemas comunes con nuestros scripts.
    - En particular, ​profundizaremos en las cadenas, las listas y los diccionarios

---

## Reseña: Qué es un string?
- Los siguientes bloques de código se usarán en el próximo video:
```Python
name = "Sasha"
color = 'Gold'

place = "Cambridge'
#This will throw an error

pet = ""

name = "Sasha"
color = 'Gold'
print("Name: " + name + ", Favorite color: " + color)

"example" * 3

pet = "loooooooooooooooooooooooooooooooong cat"
len(pet)
```

---

## Qué es un string?
- String: es un tipo de dato que representa una secuencia de caracteres.
- Un string se puede definir usando comillas simples ('), comillas dobles (") nunca se deben mezclar.
- Los strings pueden contener letras, números, símbolos y espacios.
- Los strings se pueden concatenar usando el operador +.
- Los strings se pueden repetir usando el operador *.
- Los strings tienen una longitud que se puede obtener usando la función len().