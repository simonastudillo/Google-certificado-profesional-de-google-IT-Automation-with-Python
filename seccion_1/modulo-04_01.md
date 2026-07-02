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

---

## Reseña: Las partes de un string
- Los siguientes bloques de código se usarán en el próximo video:
```Python
name = "Jaylen"
print(name[1])

name = "Jaylen"
print(name[0])

name = "Jaylen"
print(name[5])
print(name[6])

text = "Random string with a lot of characters"
print(text[-1])
print(text[-2])

color = "Orange"
color[1:4]

fruit = "Pineapple"
print(fruit[:4])
print(fruit[4:])
```

---

## Las partes de un string
- Indexación de strings: cada carácter en un string tiene un índice, que es un número entero que indica la posición del carácter en el string. El primer carácter tiene un índice de 0, el segundo carácter tiene un índice de 1, y así sucesivamente.
- Los índices negativos se pueden usar para acceder a los caracteres desde el final del string. El último carácter tiene un índice de -1, el penúltimo carácter tiene un índice de -2, y así sucesivamente.
- Intentar acceder a un índice que no existe en el string producirá un error llamado IndexError.
- Slice: Un porción de un string se puede obtener usando la sintaxis de slice.
- La sintaxis de slice es: string[inicio:fin], donde inicio es el índice del primer carácter que se desea incluir en el slice, y fin es el índice del primer carácter que se desea excluir del slice.
- Si inicio se omite, se asume que es 0. Si fin se omite, se asume que es la longitud del string.
- Si fin se omite, se asume que es la longitud del string.

---

## Indexación de strings y slicing
- La indexación de cadenas permite acceder a caracteres individuales dentro de una cadena.
- Esto se logra utilizando corchetes y la posición, o índice, del carácter deseado.
- Es importante recordar que Python comienza los índices en 0.
- Por lo tanto, para acceder al primer carácter de una cadena, se utiliza el índice [0].
- Si se intenta acceder a un índice mayor que la longitud de la cadena, se produce un error de índice (IndexError).
- Esto se debe a que se intenta acceder a un elemento inexistente.
- También se puede acceder a los índices desde el final de la cadena hacia el principio utilizando valores negativos.
- El índice [-1] permite acceder al último carácter de la cadena, y el índice [-2] al penúltimo.

---

## Practice: Work with index values
1. Tap to match each code example to the characters it extracts: 
> "Security"[2:4] - "cu"
> "Security"[0] - "S"
> "Security"[1] - "e"
> "Security"[2:5] - "cur"

2. Tap to match each code example to the characters it extracts:
> str_var = “ip address“ str_var[0] - "i"
> str_var = “ip address“ str_var[1] - "p"
> str_var = “ip address“ str_var[5:7] - "dr"
> str_var = “ip address“ str_var[3:6] - "add"

3. Tap to match each code example to the characters it extracts:
> "system".index("e") - 4
> "system".index("y") - 2
> "system".index("s") - 0
> "system".index("t") - 3

---

## Reseña: Crear nuevos strings
- Los siguientes bloques de código se usarán en el próximo video:
```Python
message = "A kong string with a silly typo"
message[2] = "l"
#This will throw an error

message = "A kong string with a silly typo"
new_message = message[0:2] + "l" + message[3:]
print(new_message)

message = "This is a new message"
print(message)
message = "And another one"
print(message)

pets="Cats & Dogs"
pets.index("&")
pets.index("C")
pets.index("Dog")
pets.index("s")

pets="Cats & Dogs"
pets.index("x")
#This will throw an error

pets="Cats & Dogs"
"Dragons" in pets
"Cats" in pets

def replace_domain(email, old_domain, new_domain):
  if "@" + old_domain in email:
    index = email.index("@" + old_domain)
    new_email = email[:index] + "@" + new_domain
    return new_email
  return email
  ```