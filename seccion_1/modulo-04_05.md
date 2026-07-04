# Repaso del módulo

## Resumen de las estructuras básicas
- Vimos strings, listas, tuplas y diccionarios.
- Como estos nuevos tipos nos ayudan a resolver problemas de manera más eficiente.
- Práctica, cada vez se hará más fácil de entender y de aplicar.

---

## En palabras de Marga: Mi guion más desafiante

-- 

## Glosario de términos
-  `Dictionaries` (Diccionarios): Un tipo de dato que se utiliza para organizar elementos en colecciones, con la forma de pares clave-valor.
- `List comprehensions` (Comprensión de listas): Crean nuevas listas a partir de secuencias o rangos.
- `string` (Cadena de caracteres): Un tipo de dato que se utiliza para representar un fragmento de texto. Son secuencias de caracteres e inmutables.
- `tuplas` (Tuplas): Secuencias de elementos de cualquier tipo que son inmutables y se escriben entre paréntesis en lugar de corchetes.

---

## Guía de estudio: Módulo 4
- Conocimientos:
    - Cómo mostrar una lista con las claves de un diccionario de Python.
    - Cómo determinar el rango de índices de una cadena.
    - Cómo determinar el contenido de una lista después de usar el método `.insert()`.
    - Cómo reemplazar una palabra específica en una oración por la misma palabra en mayúsculas.
    - Cómo usar un diccionario para contar la frecuencia de las letras en una cadena.
- Operadores, métodos y funciones:
    - .upper()
    - .lower()
    - .split()
    - .format()
    - .isnumeric()
    - .isalpha()
    - .replace()
    - string index [ ]
    - len()
- Métodos de Comprensión de listas
    - .reverse()
    - .extend()
    - .insert()
    - .append()
    - .remove()
    - .sort()
    - list comprehensions [ ]
    - list comprehensions [ ] with if condition
- Métodos de Diccionarios
    - .items()
    - .update()
    - .keys()
    - .values()
    - .copy()
    - dictionary[key]
    - dictionary[key] = value 
- Habilidades
    - Separa los valores numéricos de los valores de texto en una cadena usando `.split()`.
    - Itera sobre los elementos de una cadena.
    - Comprueba si un elemento contiene letras con `.isalpha()`.
    - Asigna los elementos de la cadena resultante a nuevas variables.
    - Elimina los espacios en blanco adicionales usando `.strip()`.
    - Dale formato a una cadena usando `.format()` y los marcadores de posición de variables `{}`.
    - Utilice la función len() para medir una cadena de texto.
    - Invierte el orden de una lista usando el método .reverse().
    - Combina dos listas usando el método .extend().
    - Utiliza una comprensión de lista [ ] como atajo para crear una nueva lista a partir de un rango.
    - Incluye un cálculo con un bucle for en un rango con dos parámetros (límite inferior, límite superior + 1).
    - Utilice una comprensión de lista [ ] con un bucle for y una condición if.
    - Recorre las claves y los valores de un diccionario.
    - Devuelve las claves y los valores en una cadena formateada usando la función `.format()`.
    - Crea una copia del diccionario.
    - Recorre los valores del nuevo diccionario.
    - Modifica cada valor del nuevo diccionario, manteniendo las mismas claves.

--- 

## Module 4 challenge: Strings, Lists, and Dictionaries
1. Fill in the blank to complete the “first_character” function. This function should return the first character of any string passed in.  Complete the string operation needed in this function so that input like "Hello, World" will produce the output "H".
```python
def first_character(string):
    # Complete the return statement using a string operation.
    return string[0] 


print(first_character("Hello, World")) # Should print H
print(first_character("Python is awesome")) # Should print P
print(first_character("Keep going")) # Should print K
```

2. Complete the for loop and string method needed in this function so that a function call like "alpha_length("This has 1 number in it")" will return the output "17". This function should:
    - accept a string through the parameters of the function;
    - iterate over the characters in the string;
    - determine if each character is a letter (counting only alphabetic characters; numbers, punctuation, and spaces should be ignored);
    - increment the counter;
    - return the count of letters in the string.
```python
def alpha_length(string):
    character = ""
    count_alpha = 0
    # Complete the for loop sequence to iterate over "string".
    for char in string: 
        # Complete the if-statement using a string method. 
        if char.isalpha():
            count_alpha += 1  
    return count_alpha
 
print(alpha_length("This has 1 number in it")) # Should print 17
print(alpha_length("Thisisallletters")) # Should print 16
print(alpha_length("This one has punctuation!")) # Should print 21
```

3. Consider the following scenario about using Python lists: 
    - A professor gave his two assistants, Jaime and Drew, the task of keeping an attendance list of students in the order they arrive in the classroom. Drew was the first one to note which students arrived, and then Jaime took over. After the class, they each entered their lists into the computer and emailed them to the professor. The professor wants to combine the two lists into one, in the order of each student's arrival. Jaime emailed a follow-up, saying that her list is in reverse order. 
    - Complete the code to combine the two lists into one in the order of: the contents of Drew's list, followed by Jaime’s list in reverse order, to produce an accurate list of the students as they arrived. This function should: 
    - accept two lists through the function’s parameters;
    - reverse the order of “list1”; 
    - combine the two lists so that “list2” comes first, followed by “list1”;
    - return the new list. 
```python
def combine_lists(list1, list2):


  combined_list = [] # Initialize an empty list variable
  list1.reverse() # Reverse the order of "list1"
  list2 += list1 # Combine the two lists 
  combined_list = list2
  return combined_list  
  
Jaimes_list = ["Alma", "Chika", "Benjamin", "Jocelyn", "Oakley"]
Drews_list = ["Minna", "Carol", "Gunnar", "Malena"]


print(combine_lists(Jaimes_list, Drews_list))
# Should print ['Minna', 'Carol', 'Gunnar', 'Malena', 'Oakley', 'Jocelyn', 'Benjamin', 'Chika', 'Alma']
```

4. Fill in the blank to complete the squares() function. This function should use a list comprehension to create a list of squared integers (using either the expression n*n or n**2). The function receives two variables and should return the list of squares that occur between the start and end variables inclusively (meaning the range should include both the “start” and “end” values). Complete the list comprehension in this function so that input like squares(2, 3) will produce the output [4, 9].
```python
def squares(start, end):
    return [n**2 for n in range(start, end + 1)] # Create the required list comprehension.


print(squares(2, 3)) # Should print [4, 9]
print(squares(1, 5)) # Should print [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

5. Fill in the blanks to complete the car_listing() function. This function accepts a car_prices dictionary. It should iterate through the keys (car models) and values (car prices) in that dictionary. For each item pair, the function should format a string so that a dictionary entry like "Kia Soul":19000 will print "A Kia Soul costs 19000 dollars.". Each new string should appear on its own line. Be sure to include the period at the end of each sentence.
```python
def car_listing(car_prices):
  result = ""
  # Complete the for loop to iterate through the key and value items 
  # in the dictionary.
  for car, price in car_prices.items():
    result += f"A {car} costs {price} dollars.\n" # Use a string method to format the required string. 
  return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))

# Should print:
# A Kia Soul costs 19000 dollars.
# A Lamborghini Diablo costs 55000 dollars.
# A Ford Fiesta costs 13000 dollars.
# A Toyota Prius costs 24000 dollars.
```

6. Consider the following scenario about using Python dictionaries: 
    - Tessa and Rick are hosting a party. Together, they sent out invitations, and collected the responses in a dictionary, with names of their friends and the number of guests each friend will be bringing. 
    - Complete the function so that the “check_guests” function retrieves the number of guests (value)  the specified friend “guest” (key) is bringing. This function should:
    - accept a dictionary “guest_list” and a key “guest” variable passed through the function parameters;
    - print the values associated with the key variable.
```python
def check_guests(guest_list, guest):
  return guest_list.get(guest) # Return the value for the given key


guest_list = { "Adam":3, "Camila":3, "David":5, "Jamal":3, "Charley":2, "Titus":1, "Raj":6, "Noemi":1, "Sakira":3, "Chidi":5}


print(check_guests(guest_list, "Adam")) # Should print 3
print(check_guests(guest_list, "Sakira")) # Should print 3
print(check_guests(guest_list, "Charley")) # Should print 2
```

7. Complete the function so that input like "This is a sentence." will return a dictionary that holds the count of each letter that occurs in the string: {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}. This function should:
    - accept a string “text” variable through the function’s parameters;
    - iterate over each character the input string to count the frequency of each letter found, (only letters should be counted, do not count blank spaces, numbers, or punctuation; keep in mind that Python is case sensitive);
    - populate the new dictionary with the letters as keys, ensuring each key is unique, and assign the value for each key with the count of that letter;
    - return the new dictionary.
```python
def count_letters(text):
  # Initialize a new dictionary.
  dictionary = {} 
  # Complete the for loop to iterate through each "text" character and 
  # use a string method to ensure all letters are lowercase.
  for char in text.lower():
    # Complete the if-statement using a string method to check if the
    # character is a letter.
    if char.isalpha():
      # Complete the if-statement using a logical operator to check if 
      # the letter is not already in the dictionary.
      if dictionary.get(char) is None: 
           # Use a dictionary operation to add the letter as a key
           # and set the initial count value to zero.
           dictionary[char] = 0
      # Use a dictionary operation to increment the letter count value 
      # for the existing key.
      dictionary[char] += 1
  return dictionary

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}
```

8. What do the following commands return when country = Luxembourg?
```python
print(country[3:6])
print(country[-5])
print(country[8:])
# Should print:
# emb
# b
# rg
```

9. What does the list "music_genres" contain after these commands are executed?
```python
music_genres = ["rock", "pop", "country"]
music_genres.append("blues")
```
> ['rock', 'pop', 'country', 'blues']

10. What do the following commands return?
```python
teacher_names = {"Math": "Aniyah Cook", "Science": "Ines Bisset", "Engineering": "Wayne Branon"}
teacher_names.values()
```
> dict_values(['Aniyah Cook', 'Ines Bisset', 'Wayne Branon