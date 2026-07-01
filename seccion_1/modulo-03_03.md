# Recursión (opcional)

## Reseña: Que es la recursión
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