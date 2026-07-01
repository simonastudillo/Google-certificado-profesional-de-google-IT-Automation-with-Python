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