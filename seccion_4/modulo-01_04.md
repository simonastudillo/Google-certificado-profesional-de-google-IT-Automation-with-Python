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