# Recursión (opcional)

## Reseña: Qué es la recursión
- Los siguientes bloques de código se usarán en el próximo video:
```Python
def factorial(n):
  if n < 2:
    return 1
  return n * factorial(n-1)
```

```Python
def factorial(n):
  print("Factorial called with " + str(n))
  if n < 2:
    print("Returning 1")
    return 1
  result = n * factorial(n-1)
  print("Returning " + str(result) + " for factorial of " + str(n))
  return result

factorial(4)
```

---

## Qué es la recursión
- Además de `for` y `while`, Python tiene otra forma de repetir código: la recursión.
- La ​recursión es la aplicación repetida ​del mismo procedimiento a un problema más pequeño. 
- La recursión nos permite abordar ​problemas complejos al reducir ​el problema a uno más simple.
- En programación, la recursión es una forma de realizar ​una tarea repetitiva haciendo que una función se llame a sí misma
- Una función recursiva se llama a sí misma normalmente con ​un parámetro modificado hasta ​que alcanza una condición específica. ​Esta afección se denomina caso base. 

---

## Reseña: Recursión en acción en un contexto IT
- Los siguientes bloques de código se usarán en el próximo video:
```Python
def factorial(n):
  if n < 2:
    return 1
  return n * factorial(n-1)

factorial(1000)

#this will produce an error
```

---

## Recursión en acción en un contexto IT
- Digamos que necesitas escribir una herramienta que recorra un montón de directorios ​de tu ordenador y calcule cuántos archivos contiene cada uno.
- Al listar los ficheros dentro de un directorio, podrías encontrar subdirectorios dentro de ellos, ​y querrías contar los ficheros en esos subdirectorios también.
- El caso base sería un directorio sin subdirectorios. 
- Para este caso, la función sólo devolvería la cantidad de ficheros.
- El caso recursivo sería llamar a la función recursiva para ​cada uno de los subdirectorios contenidos.
- ​El valor de retorno de una llamada a una función dada sería la suma de todos los ficheros de ese ​directorio más todos los ficheros de los subdirectorios contenidos. 

- Pongamos que tu software de gestión de grupos te permite crear grupos que tienen tanto ​usuarios como otros grupos como miembros, y ​quieres listar todos los usuarios humanos que forman parte de un grupo dado.
- En este caso se utilizaría una función recursiva para recorrer los grupos
- ​El caso base sería un grupo que sólo incluye usuarios, listando todos ellos. 
- ​El caso recursivo significaría recorrer todos los grupos contenidos, listar ​todos los usuarios en ellos, y luego listar cualquier usuario contenido en el grupo actual. ​
- En Python, por defecto, ​puedes llamar a una función recursiva 1000 veces hasta alcanzar el límite

>[!NOTE]
> Es importante señalar que en algunos lenguajes, ​hay una cantidad máxima de llamadas recursivas que se pueden utilizar