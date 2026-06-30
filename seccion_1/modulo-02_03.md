# Condicionales

## Reseña: Comparando cosas
- Estos son los ejemplos usados en el siguiente video:
```Python
print(10>1)
#True
print("cat" == "dog")
#False
print (1 != 2)
#True

print(1 < "1")
#Will return a type error

print(1 == "1")
#False

print("Yellow" > "Cyan" and "Brown" > "Magenta")
#False

print(25 > 50 or 1 != 2)
#True

print(not 42 == "Answer")
#True
```

---

## Comparando cosas
- Python puede comparar cosas
    - Si algo es pequeño o grande que otra cosa
- Booleanos: True o False
- Operadores de comparación: `==`, `!=`, `<`, `>`, `<=`, `>=`
    - `==` es igual a
    - `!=` es diferente a
    - `<` es menor que
    - `>` es mayor que
    - `<=` es menor o igual que
    - `>=` es mayor o igual que
- En Python podemos comparar números, strings y booleanos
- Operadores lógicos: `and`, `or`, `not`
    - `and` devuelve True si ambos son True
    - `or` devuelve True si al menos uno es True
    - `not` devuelve True si el valor es False y viceversa