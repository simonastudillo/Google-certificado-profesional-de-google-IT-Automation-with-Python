# Strings

## Introducción estructuras básicas
- Anteriormente cubrimos
    - elementos básicos de la sintaxis de Python
    - definir funciones
    - cómo hacer que su computadora actúe de ​manera diferente en función de los condicionales
    - cómo hacer que realice operaciones ​repetidamente usando while y para bucles y recursión
    - aprenderemos un montón de ​nuevas habilidades muy útiles ​para añadir a tu caja de herramientas de programación. 
    - Revisaremos algunos tipos de datos que proporciona ​el lenguaje Python para ayudarnos a ​resolver problemas comunes con nuestros scripts.
    - En particular, ​profundizaremos en los strings, las listas y los diccionarios

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
- La indexación de strings permite acceder a caracteres individuales dentro de un string.
- Esto se logra utilizando corchetes y la posición, o índice, del carácter deseado.
- Es importante recordar que Python comienza los índices en 0.
- Por lo tanto, para acceder al primer carácter de un string, se utiliza el índice [0].
- Si se intenta acceder a un índice mayor que la longitud del string, se produce un error de índice (IndexError).
- Esto se debe a que se intenta acceder a un elemento inexistente.
- También se puede acceder a los índices desde el final del string hacia el principio utilizando valores negativos.
- El índice [-1] permite acceder al último carácter del string, y el índice [-2] al penúltimo.

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

  ---

## Crear nuevos strings
- Los strings son inmutables, lo que significa que no se pueden cambiar después de haber sido creados.
- Para modificar un string debemos crear un nuevo string que contenga los cambios deseados.
- podemos usar la indexación y el slicing para crear un nuevo string a partir de un string existente.
- Luego de crear un nuevo string, podemos asignarlo a la misma variable para reemplazar el string original.
- `index()` es un método de string que devuelve el índice de la primera aparición de un substring dentro del string.
- Es decir busca un substring dentro de un string y devuelve la primera posición donde se encuentra. 
- Si el substring no se encuentra, se produce un error de valor (ValueError).
- El operador `in` se puede usar para verificar si un substring está presente dentro de un string.
- Devuelve True si el substring está presente, y False si no lo está.

---

## Métodos basicos de strings
- `index()` es un método de string que devuelve el índice de la primera aparición de un substring dentro del string.
- Ejemplo:
```Python
animals = "lions tigers and bears"
animals.index("g")

animals = "lions tigers and bears"
animals.index("bears")
```

- `in()` es un operador que se puede usar para verificar si un substring está presente dentro de un string.
- Ejemplo:
```Python
animals = "lions tigers and bears"
"horses" in animals

animals = "lions tigers and bears"
"tigers" in animals
```

---

## Reseña: Más métodos de strings
- Los siguientes bloques de código se usarán en el próximo video:
```Python
"Mountains".upper()
"Mountains".lower()

answer = "YES"
if answer.lower() == "yes":
  print("User said yes")

" yes ".strip()

" yes ".strip()
" yes ".lstrip()
" yes ".rstrip()

"The number of times e occurs in this string is 4".count("e")

"Forest".endswith("rest")

"Forest".isnumeric()
"12345".isnumeric()

int("12345") + int("54321")

" ".join(["This", "is", "a", "phrase", "joined", "by", "spaces"])
"...".join(["This", "is", "a", "phrase", "joined", "by", "triple", "dots"])

"This is another example".split()
```

---

## Más métodos de strings
- `upper()` es un método de string que devuelve un nuevo string con todos los caracteres en mayúsculas.
- `lower()` es un método de string que devuelve un nuevo string con todos los caracteres en minúsculas.
- `strip()` es un método de string que devuelve un nuevo string con los espacios en blanco al principio y al final eliminados. Tambien elimina las tabulaciones y saltos de línea al principio y al final del string.
- `lstrip()` es un método de string que devuelve un nuevo string con los espacios en blanco al principio eliminados.
- `rstrip()` es un método de string que devuelve un nuevo string con los espacios en blanco al final eliminados.
- `count()` es un método de string que devuelve el número de veces que un substring aparece en el string.
- `endswith()` es un método de string que devuelve True si el string termina con el substring especificado, y False si no lo hace.
- `isnumeric()` es un método de string que devuelve True si todos los caracteres en el string son dígitos, y False si no lo son.
- `join()` es un método de string que toma una lista de strings y las une en un solo string, separadas por el string que llama al método.
- `split()` es un método de string que toma un string y lo divide en una lista de strings, utilizando el string que llama al método como delimitador. Si no se especifica un delimitador, se utiliza cualquier espacio en blanco como delimitador.

---

## Métodos avanzados de strings
- El método `lower` devuelve un string con todos los caracteres convertidos a minúsculas. 
- El método `upper` devuelve un string en mayúsculas. 
- Estos se aplican a un string usando la notación de punto, como por ejemplo: `"this is a string".upper()`. Esto devolvería el string "THIS IS A STRING". 
- Esto puede ser muy útil al verificar la entrada del usuario, ya que podría escribir todo en minúsculas, todo en mayúsculas o incluso una combinación de ambas.

- Puedes usar el método `strip` para eliminar los espacios en blanco que rodean un string.
- Los espacios en blanco incluyen espacios, tabulaciones y saltos de línea.
- También puedes usar los métodos `lstrip` y `rstrip` para eliminar los espacios en blanco solo del lado izquierdo o derecho del string, respectivamente.

- El método `count` se puede usar para obtener la cantidad de veces que aparece una substring en un string.
- Esto puede ser útil para saber cuántos caracteres tiene un string o para contar cuántas veces aparece una palabra determinada en una oración o párrafo.

- Si desea comprobar si un string termina con una substring dada, puede usar el método `endswith`.
- Este devolverá `True` si la substring se encuentra al final del string y `False` en caso contrario.

- El método `isnumeric` permite comprobar si un string está compuesto únicamente por números.
- Si el string contiene solo números, este método devolverá `True`.
- Podemos usarlo para comprobar si un string contiene números antes de pasarla a la función `int()` para convertirla a un entero, evitando así un error.

- También podemos usar el método `join` para concatenar strings.
- Este método se aplica a un string que se utilizará para unir una lista de strings.
- Este método recibe como parámetro una lista de strings que se van a unir y devuelve un nuevo string compuesto por cada uno de los strings de la lista unidos mediante el string inicial.
- Por ejemplo, `join(["This","is","a","sentence"])` devolvería el string "This is a sentence".

- El método `split` es el inverso del método `join`.
- Este método nos permite dividir un string en una lista de strings.
- Por defecto, divide por cualquier carácter de espacio en blanco.
- También se puede dividir por cualquier otro carácter pasando un parámetro.

---

## Reseña: Formatear strings
- Los siguientes bloques de código se usarán en el próximo video:
```Python
name = "Manny"
number = len(name) * 3
print("Hello {}, your lucky number is {}".format(name, number))

name = "Manny"
print("Your lucky number is {number}, {name}.".format(name=name, number=len(name)*3))

price = 7.5
with_tax = price * 1.09
print(price, with_tax)
print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax))

def to_celsius(x):
  return (x-32)*5/9

for x in range(0,101,10):
  print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))
```

---

## Formatear strings
- Hay una mejor forma de unir strings que la concatenación usando el operador +.
- Podemos usar el método `format` para insertar valores en un string.
- La función `format` toma los valores que se pasan como argumentos y los inserta en el string en las posiciones indicadas por llaves `{}`.
- No importa si el valor es un string, un número o cualquier otro tipo de dato, `format` lo convertirá a string automáticamente.
- Podemos usar llaves con nombres para indicar qué valor se debe insertar en cada posición.
- También podemos usar llaves con números para indicar qué valor se debe insertar en cada posición.
Ejemplo:
```Python
def student_grade(name, grade):
	return "{} received {}% on the exam".format(name, grade)

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))
```
- La función `format` también nos permite formatear números de diferentes maneras.
- Podemos usar `:.2f` para formatear un número como un float con dos decimales (`.2f` significa "float con 2 decimales").
- Podemos usar `:>3` para alinear un número a la derecha con un ancho de 3 caracteres (`>3` significa "alinear a la derecha con un ancho de 3 caracteres").
- Podemos usar `:<3` para alinear un número a la izquierda con un ancho de 3 caracteres (`<3` significa "alinear a la izquierda con un ancho de 3 caracteres").

---

## String formateados
- Puedes usar el método `format` para concatenar strings de formas diferentes y poderosas
- Puedes simplmente usar las llaves `{}` para indicar dónde quieres que se inserten los valores.
- También puedes usar llaves con nombres para indicar qué valor se debe insertar en cada posición, algo como `{name}` y `{number}`.
- Recuerda que usas este método debes nombrar los parámetros que pasas a la función `format` con los mismos nombres que usas en las llaves.
- También puedes usar llaves con números para indicar qué valor se debe insertar en cada posición, algo como `{0}` y `{1}`.
- Además para los números puedes usar `:.2f` para formatear un número como un float con dos decimales, `:>3` para alinear un número a la derecha con un ancho de 3 caracteres, y `:<3` para alinear un número a la izquierda con un ancho de 3 caracteres. 

---

## Guía de referencia para strings
- `len(string)`: devuelve la longitud del string.
```Python
print(len("abcde"))         # prints 5
```

- `for character in string`: itera sobre cada carácter en el string.
```Python
for c in "abcde":  print(c)                  # prints "a", then "b", then "c", etc.
```

- `if substring in string`: verifica si un substring está presente en el string.
```Python
print("abc" in "abcde")     # prints True
print("def" in "abcde")     # prints False
```

- `string[index]`: devuelve el carácter en la posición `index` del string.
```Python
print("abcde"[2])           # prints "c"
print("abcde"[-1])          # prints "e"
```

- `string[start:end]`: devuelve un slice del string desde `start` hasta `end` (excluyendo `end`).
```Python
print("abcde"[0:2])         # prints "ab"
print("abcde"[2:])          # prints "cde"
```

- `string.lower()`: devuelve un nuevo string con todos los caracteres en minúsculas.
```Python
print("AaBbCcDdEe".lower())             # prints "aabbccddee"
```

- `string.upper()`: devuelve un nuevo string con todos los caracteres en mayúsculas.
```Python
print("AaBbCcDdEe".upper())             # prints "AABBCCDDEE"
```

- `string.lstrip()`: devuelve un nuevo string con los espacios en blanco al principio eliminados.
```Python
print("   Hello   ".lstrip())           # prints "Hello   "
```

- `string.rstrip()`: devuelve un nuevo string con los espacios en blanco al final eliminados.
```Python
print("   Hello   ".rstrip())           # prints "   Hello"
```

- `string.strip()`: devuelve un nuevo string con los espacios en blanco al principio y al final eliminados.
```Python
test = "How much wood would a woodchuck chuck"
print(test.count("wood"))               # prints 2
```

- `string.isnumeric()`: devuelve True si todos los caracteres en el string son dígitos, y False si no lo son.
```Python
print("12345".isnumeric())              # prints True
print("-123.45".isnumeric())            # prints False
```

- `string.isalpha()`: devuelve True si todos los caracteres en el string son letras, y False si no lo son.
```Python
print("xyzzy".isalpha())                # prints True
```

- `string.split(delimiter)`: divide el string en una lista de strings usando el delimitador especificado, por defecto divide por cualquier espacio en blanco.
```Python
print(test.split())    # prints ['How', 'much', 'wood', 'would', 'a', 'woodchuck', 'chuck']
```

- `string.replace(old, new)`: devuelve un nuevo string con todas las apariciones de `old` reemplazadas por `new`.
```Python
print(test.replace("wood", "plastic"))  # prints "How much plastic would a plasticchuck chuck"
```

- `delimiter.join(list_of_strings)`: une una lista de strings en un solo string, separadas por el delimitador especificado.
```Python
print("-".join(test.split()))           # prints "How-much-wood-would-a-woodchuck-chuck"
```

---

## Guía de referencia para formatear strings
- La mayoría de los programas necesitan, tarde o temprano, proporcionar algún tipo de resultado o información al usuario.
- Dar formato al resultado facilita su lectura.
- Por ejemplo, imagina que trabajas en un mercado de agricultores y necesitas generar recibos para tus clientes.
- Debes pesar los productos, calcular el precio total de cada uno (peso por precio por libra) y luego añadir el impuesto sobre las ventas al subtotal.
- Tu primer intento podría verse así:
```Python
# Here are the items in the customer's basket. Each item is a tuple
# of (item name, weight, price per pound).
#
basket = [
    ("Peaches", 3.0, 2.99),
    ("Pears", 5.0, 1.66),
    ("Plums", 2.5, 3.99)
]


# Calculate the total price for each item (weight times price per pound)
# and add them up to get a subtotal.
#
subtotal = 0.00
for item in basket:
  fruit, weight, unit_price = item
  subtotal += (weight * unit_price)


# Now calculate the sales tax and total bill.
#
tax_rate = 0.06625  # 6.625% sales tax in New Jersey
tax_amt = subtotal * tax_rate
total = subtotal + tax_amt


# Print the receipt for the customer.
#
print("Subtotal:", subtotal)
print("Sales Tax:", tax_amt)
print("Total:", total)
```
- Si ejecutamos el código veremos algo como
> Subtotal: 27.245
> Sales Tax: 1.8049812500000002
> Total: 29.049981250000002

- Sin embargo sería mejor que luzca como un recibo real.
> Subtotal: $27.25
> Sales Tax: $1.80
> Total: $29.05

- Para lograr esto, usamos el método `format`.
```Python
fruit = "peaches"
weight = 3.0
per_pound = 2.99


output = "You are buying {} pounds of {} at {} per pound.".format(weight, fruit, per_pound)
print(output)

output = "{1} are {2} per pound, and you have {0} pounds of {1}.".format(weight, fruit, per_pound)
print(output)

output = "{fruit} are {price} per pound, and you have {weight} pounds of {fruit}.".format(weight=weight, fruit=fruit, price=per_pound)
print(output)
```
> You are buying 3.0 pounds of peaches at 2.99 per pound
> Peaches are 2.99 per pound, and you have 3.0 pounds of peaches
> Peaches are 2.99 per pound, and you have 3.0 pounds of peaches

- Para el prime ejemplo podríamos modificar la salida de esta forma
```Python
# Print the receipt for the customer. The format string ":10,.2f" 
# works as follows:
#   - ":10" makes the output 10 characters wide.
#   - "," inserts thousands separators between groups of digits.
#   - ".2" limits the output to two digits after the decimal.
#   - "f" tells Python to expect a floating-point number.
#
print("Subtotal:     ${:10,.2f}".format(subtotal))
print("Sales Tax:    ${:10,.2f}".format(tax_amt))
print("Total:        ${:10,.2f}".format(total))
```
> Subtotal:      $     27.25
> Sales Tax:     $      1.80
> Total:         $     29.05

- Formatear strings usando literales de cadena (f-strings)
- La función de literales de cadena formateados, añadida en Python 3.6, aún no se usa mucho.
- Una cadena literal formateada o f-string es una cadena que comienza con 'f' o 'F' antes de las comillas.
- Estas cadenas pueden contener marcadores de posición {} mediante expresiones similares a las que se usan para las cadenas del método format().
- La diferencia importante entre las f-strings y el método format() es que las f-strings toman el valor de las variables del contexto actual, en lugar de tomar los valores de los parámetros.
```Python
name = "Micah"
print(f'Hello {name}')
# Hello Micah

item = "Purple Cup"
amount = 5
price = amount * 3.25
print(f'Item: {item} - Amount: {amount} - Price: {price:.2f}')
# Item: Purple Cup - Amount: 5 - Price: 16.25
```

- Para más información visita la documentación oficial de Python sobre [f-strings](https://docs.python.org/3/reference/lexical_analysis.html#f-strings).

- Antigua forma de formatear strings
- El método format() se introdujo en Python 2.6.
- Antes de eso, se podía usar el operador % (módulo) para obtener un resultado similar.
- Aunque este método ya no se recomienda para código nuevo, es posible que lo encuentres en el código de otra persona.
- Así es como se ve:
```Python
"base string with %s placeholder" % variable
```
- El operador % (módulo) devuelve una copia de la cadena donde los marcadores de posición indicados por % seguidos de una expresión de formato se reemplazan por las variables que aparecen después del operador.
- Para reemplazar más de un valor, debe proporcionarlos como una tupla.
- La expresión de formato debe coincidir con el tipo de valor.
```Python
"base string with %d and %d placeholders" % (value1, value2)
```