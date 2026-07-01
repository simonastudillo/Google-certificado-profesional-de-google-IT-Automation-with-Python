# For loops

## Reseña: Qué es un bucle for?
- Los siguientes bloques de código se usarán en el próximo video:
```Python
for x in range(5):
    print(x)
```

```Python
friends = ['Taylor', 'Alex', 'Pat', 'Eli']
for friend in friends:
    print("Hi " + friend)
```

```Python
values = [ 23, 52, 59, 37, 48 ]
sum = 0
length = 0
for value in values:
    sum += value
    length += 1

print("Total sum: " + str(sum) + " - Average: " + str(sum/length))
```