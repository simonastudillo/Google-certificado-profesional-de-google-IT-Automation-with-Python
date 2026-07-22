# La búsqueda binaria es un problema

## ¿Qué es la búsqueda binaria?
- `Búsqueda lineal`: es un algoritmo de búsqueda que recorre una lista de elementos uno por uno hasta encontrar el elemento deseado o llegar al final de la lista. Su complejidad es O(n).
- `Búsqueda binaria`: es un algoritmo de búsqueda que divide repetidamente una lista ordenada en mitades hasta encontrar el elemento deseado o determinar que no está presente. Su complejidad es O(log n).

>[!INFO]
> La búsqueda binaria requiere que la lista esté ordenada. Si la lista no está ordenada, primero debemos ordenarla antes de aplicar la búsqueda binaria.

---

## Búsqueda lineal y binaria (Opcional)
- Búsqueda lineal en Python:
```python
def linear_search(list, key):
    """If key is in the list returns its position in the list,
       otherwise returns -1."""
    for i, item in enumerate(list):
        if item == key:
            return i
    return -1
```
- Búsqueda binaria en Python:
```python
def binary_search(list, key):
    """Returns the position of key in the list if found, -1 otherwise.

    List must be sorted.
    """
    left = 0
    right = len(list) - 1
    while left <= right:
        middle = (left + right) // 2
        
        if list[middle] == key:
            return middle
        if list[middle] > key:
            right = middle - 1
        if list[middle] < key:
            left = middle + 1
    return -1
```

---

## Aplicación de la búsqueda binaria a la resolución de problemas
- `Bisecting`: es un enfoque de resolución de problemas que utiliza la búsqueda binaria para encontrar la causa raíz de un problema. Consiste en dividir el problema en mitades y probar cada mitad hasta encontrar la causa del problema.
- Un ejemplo sería cuando un programa falla, le solicitamos al usuario que envíe los archivos de configuración.
    - Luego copiamos la mitad de los archivos de configuración y ejecutamos el programa.
    - Si el programa funciona correctamente, sabemos que la causa del problema está en la otra mitad de los archivos de configuración.
    - Luego copiamos la mitad de los archivos restantes y ejecutamos el programa nuevamente.
    - Repetimos este proceso hasta que encontramos el archivo de configuración que causa el problema.
    - Por último podríamos copiar parte del archivo de configuración que causa el problema y ejecutar el programa nuevamente para ver si podemos encontrar la línea específica que causa el problema.
- Git tambien tiene una herramienta de `bisecting` que nos permite encontrar el commit que introdujo un error en el código fuente de un proyecto.

---

## Revisión: Encontrar datos no válidos
- Esta lectura contiene el código utilizado en los vídeos sigueintes
```bash
/import_data$ cat contacts.csv | ./import.py --server test
# Import Error


/import_data$ wc -l contacts.csv 



/import_data$ head -15 contacts.csv 



/import_data$ tail -20 contacts.csv 


/import_data$ head -50 contacts.csv | ./import.py --server test
# Import Error

/import_data$ head -50 contacts.csv | head -25 | ./import.py --server test


/import_data$ head -50 contacts.csv | tail -25 | ./import.py --server test
# Import Error

/import_data$ head -50 contacts.csv | tail -25 | head -13 | ./import.py --server test


/import_data$ head -50 contacts.csv | tail -25 | tail -12 | head -6 | ./import.py --server test
# Import Error

/import_data$ head -50 contacts.csv | tail -25 | tail -12 | head -6 | head -3 


/import_data$ cat contacts.csv | ./import.py --server test
```

---

## Encontrar datos no válidos
- Ejemplo: Tenemos un programa que lee datos de un archivo CSV, los procesa ​y luego los importa en una base de datos.
- Uno de los usuarios del sistema nos dice que el archivo que intentan importar ​falla con un error de importación oscuro
- En el ejemplo se usa el flag de `--server test` para que el programa se ejecute en un entorno de prueba y no afecte a la base de datos real.
- `wc -l contacts.csv` nos permite contar el número de líneas en el archivo CSV, lo que nos da una idea de cuántos registros hay en el archivo.
    -`wc` es una herramienta de línea de comandos que cuenta el número de líneas, palabras y caracteres en un archivo.
    - `-l` es una opción de `wc` que cuenta solo el número de líneas en el archivo.
- `head -15 contacts.csv` nos permite ver las primeras 15 líneas del archivo CSV, lo que nos da una idea de cómo se ve el archivo y qué tipo de datos contiene.
    - `head` es una herramienta de línea de comandos que muestra las primeras líneas de un archivo.
    - `-15` es una opción de `head` que muestra solo las primeras 15 líneas del archivo.
- `tail -20 contacts.csv` nos permite ver las últimas 20 líneas del archivo CSV, lo que nos da una idea de cómo se ve el final del archivo y qué tipo de datos contiene.
    - `tail` es una herramienta de línea de comandos que muestra las últimas líneas de un archivo.
    - `-20` es una opción de `tail` que muestra solo las últimas 20 líneas del archivo.
- Probamos enviando los primeros 50 registros del archivo CSV al programa de importación, lo que nos permite ver si el error ocurre en los primeros registros o más adelante en el archivo.
    - Esto lo hacemos con el comando `head -50 contacts.csv | ./import.py --server test`.
    - En el ejemplo, al ejecutar este comando el programa da error.
- Probamos con la primera mitad de los 50 registros, lo que nos permite ver si el error ocurre en la primera mitad o en la segunda mitad de los primeros 50 registros.
    - Esto lo hacemos con el comando `head -50 contacts.csv | head -25 | ./import.py --server test`.
    - Aquí concatenamos el uso de `head` para obtener los primeros 50 registros y luego los primeros 25 de esos 50 registros.
    - En el ejemplo, al ejecutar este comando el programa funciona correctamente.
- Usamos `head` y `tail` obtener la segunda mitad de los primeros 50 registros, lo que nos permite ver si el error ocurre en la segunda mitad de los primeros 50 registros.
    - Esto lo hacemos con el comando `head -50 contacts.csv | tail -25 | ./import.py --server test`.
    - Aquí concatenamos el uso de `head` para obtener los primeros 50 registros y luego `tail` para obtener los últimos 25 de esos 50 registros.
    - En el ejemplo, al ejecutar este comando el programa da error.
- Al comando anterior le agregamos otro `head` para obtener la primera mitad de los últimos 25 registros, lo que nos permite ver si el error ocurre en la primera mitad o en la segunda mitad de los últimos 25 registros.
    - Esto lo hacemos con el comando `head -50 contacts.csv | tail -25 | head -13 | ./import.py --server test`.
    - Aquí concatenamos el uso de `head` para obtener los primeros 50 registros, luego `tail` para obtener los últimos 25 de esos 50 registros y luego `head` para obtener los primeros 13 de esos 25 registros.
    - En el ejemplo, al ejecutar este comando el programa funciona correctamente.
- Ahora probamos con `tail -13` en lugar de `head -13` para obtener la segunda mitad de los últimos 25 registros, lo que nos permite ver si el error ocurre en la segunda mitad de los últimos 25 registros.
    - Esto lo hacemos con el comando `head -50 contacts.csv | tail -25 | tail -12 | head -6 | ./import.py --server test`.
    - Aquí concatenamos el uso de `head` para obtener los primeros 50 registros, luego `tail` para obtener los últimos 25 de esos 50 registros, luego `tail` para obtener los últimos 12 de esos 25 registros y luego `head` para obtener los primeros 6 de esos 12 registros.
    - En el ejemplo, al ejecutar este comando el programa da error.
- Volvemos a ejecutar el comando añadiendo un último `head` para obtener la primera mitad de los últimos 6 registros, lo que nos permite ver si el error ocurre en la primera mitad o en la segunda mitad de los últimos 6 registros.
    - Esto lo hacemos con el comando `head -50 contacts.csv | tail -25 | tail -12 | head -6 | head -3`.
    - Aquí concatenamos el uso de `head` para obtener los primeros 50 registros, luego `tail` para obtener los últimos 25 de esos 50 registros, luego `tail` para obtener los últimos 12 de esos 25 registros, luego `head` para obtener los primeros 6 de esos 12 registros y luego `head` para obtener los primeros 3 de esos 6 registros.
    - En el ejemplo, al ejecutar este comando el programa falla, por lo que hemos encontrado los 3 registros que contienen datos no válidos. Ahora podemos abrir el archivo CSV y corregir los datos en esos registros para que el programa de importación funcione correctamente.
- Ejecutamos el comando anterior pero sin enviarlo al programa de importación, para ver cuáles son los 3 registros que contienen datos no válidos.
    - Esto lo hacemos con el comando `head -50 contacts.csv | tail -25 | tail -12 | head -6 | head -3`.
    - Podemos ver que hay un registro que contiene una coma (`,`) en lugar de un punto para un nombre.
    - Esto generaba el problema en el CSV, dando a entender que había un campo más de los que realmente había, y por lo tanto el programa de importación fallaba.

---

## Test your knowledge: Binary searching a problem
1. You have a list of computers that a script connects to in order to gather SNMP traffic and calculate an average for a set of metrics. The script is now failing, and you do not know which remote computer is the problem. How would you troubleshoot this issue using the bisecting methodology?
> Run the script with the first half of the computers.

2. The find_item function uses binary search to recursively locate an item in a list, returning True if found, False otherwise. Something is missing from this function. Can you spot what it is and fix it? Add debug lines where appropriate to help you narrow down the problem.
```python
def find_item(list, item):
  list.sort()
 #Returns True if the item is in the list, False if not.
  if len(list) == 0:
   return False


 #Is the item in the center of the list?
  middle = len(list)//2
  if list[middle] == item:
   return True


 #Is the item in the first half of the list?
  if item < list[middle]:
   #Call the function with the first half of the list
   return find_item(list[:middle], item)
  else:
   #Call the function with the second half of the list
   return find_item(list[middle+1:], item)


  return False


#Do not edit below this line - This code helps check your work!
list_of_names = ["Parker", "Drew", "Cameron", "Logan", "Alex", "Chris", "Terry", "Jamie", "Jordan", "Taylor"]


print(find_item(list_of_names, "Alex")) # True
print(find_item(list_of_names, "Andrew")) # False
print(find_item(list_of_names, "Drew")) # True
print(find_item(list_of_names, "Jared")) # False
```

3. The binary_search function returns the position of key in the list if found, or -1 if not found. You want to make sure that it's working correctly, so you need to place debugging lines to let you know each time that the list is cut in half, whether you're on the left or the right. You do not want to print anything when the key is located.
For example, the command binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3) performs these steps:
1. It determines that the key, 3, is in the left half of the list and prints "Checking the left side". 
2. It then determines that 3 is in the right half of the new list and prints "Checking the right side".
3. Finally, it returns the value of 2, which is the position of the key in the list.

Add commands to the code to print out "Checking the left side" or "Checking the right side" in the appropriate places.  
```python
def binary_search(list, key):
	list.sort() # Binary search starts with a sorted list
	left = 0 # The first value of the list
	right = len(list) - 1 # The last value of the list


	while left <= right:
		middle = (left + right) // 2


		if list[middle] == key:
			print("Middle element")
			return middle
		elif list[middle] > key:
			# Add debug statement here
            print("Checking the right side")
			right = middle - 1
		else:
			# Add debug statement here
            print("Checking the left side")
			left = middle + 1
	return -1

print(binary_search([10, 2, 9, 6, 7, 1, 5, 3, 4, 8], 1)) # 0
#print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)) # 4
#print(binary_search([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 7)) # 3
#print(binary_search([1, 3, 5, 7, 9, 10, 2, 4, 6, 8], 10)) # 9
#print(binary_search([5, 1, 8, 2, 4, 10, 7, 6, 3, 9], 11)) # -1
```

4. When trying to find an error in a log file or output to the screen, what command can we use to review, say, the first 10 lines?
> head

5. The best_search function compares linear_search and binary_search functions to locate a key in the list, returns how many steps each method took, and which method is the best for that situation. The list does not need to be sorted, as the binary_search function sorts it before proceeding (and uses one step to do so). Here, linear_search and binary_search functions both return the number of steps that it took to either locate the key or determine that it's not in the list. If the number of steps is the same for both methods (including the extra step for sorting in binary_search), then the result is a tie. Fill in the blanks to make this work.
```python
def linear_search(list, key):
   #Returns the number of steps to determine if key is in the list


   #Initialize the counter of steps
   steps=0
   for i, item in enumerate(list):
       steps += 1
       if item == key:
           break
   return steps


def binary_search(list, key):
   #Returns the number of steps to determine if key is in the list


   #List must be sorted:
   list.sort()


   #The Sort was 1 step, so initialize the counter of steps to 1
   steps=1


   left = 0
   right = len(list) - 1
   while left <= right:
       steps += 1
       middle = (left + right) // 2
      
       if list[middle] == key:
           break
       if list[middle] > key:
           right = middle - 1
       if list[middle] < key:
           left = middle + 1
   return steps


def best_search(list, key):
   steps_linear = linear_search(list, key)
   steps_binary = binary_search(list, key)
   results = "Linear: " + str(steps_linear) + " steps, "
   results += "Binary: " + str(steps_binary) + " steps. "
   if (steps_linear < steps_binary):
       results += "Best Search is Linear."
   elif (steps_binary < steps_linear):
       results += "Best Search is Binary."
   else:
       results += "Result is a Tie."


   return results


print(best_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1))
#Should be: Linear: 1 steps, Binary: 4 steps. Best Search is Linear.


print(best_search([10, 2, 9, 1, 7, 5, 3, 4, 6, 8], 1))
#Should be: Linear: 4 steps, Binary: 4 steps. Result is a Tie.


print(best_search([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 7))
#Should be: Linear: 4 steps, Binary: 5 steps. Best Search is Linear.


print(best_search([1, 3, 5, 7, 9, 10, 2, 4, 6, 8], 10))
#Should be: Linear: 6 steps, Binary: 5 steps. Best Search is Binary.


print(best_search([5, 1, 8, 2, 4, 10, 7, 6, 3, 9], 11))
#Should be: Linear: 10 steps, Binary: 5 steps. Best Search is Binary.
```