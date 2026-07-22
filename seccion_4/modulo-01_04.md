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