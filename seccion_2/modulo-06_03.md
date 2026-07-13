# Conceptos avanzados de bash

## Revisión: While loops en script bash
- Los siguientes bloques de código se usarán en el próximo video:
```bash
n=1
while [ $n -le 5 ]; do
  echo "Iteration number $n"
  ((n+=1))
done
Iteration number 1
Iteration number 2
Iteration number 3
Iteration number 4
Iteration number 5
```
```python
import sys
import random

value = random.randint(0, 3)
print("Returning: " + str(value))
sys.exit(value)
# Returning: 1
```
```bash
#!/bin/bash

n=0
command=$1
while ! $command && [ $n -le 5 ]; do
        sleep $n
        ((n+=1))
        echo "Retry #$n"
done;
Returning: 1
Retry #1
Returning: 3
Retry #2
Returning: 1
Retry #3
Returning: 0
```