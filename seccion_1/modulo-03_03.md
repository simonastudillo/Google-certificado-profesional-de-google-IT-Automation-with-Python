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

---

## Recursos adicionales sobre recursión
```Python
def recursive_function(parameters):
    if base_case_condition(parameters):
        return base_case_value
    recursive_function(modified_parameters)
```
- [wikipedia: Recursion](https://en.wikipedia.org/wiki/Recursion)
- [Search Google for recursion](https://www.google.com/search?q=recursion)

---

## Test your knowledge: Recursion
1. What is recursion used for?
> Recursion is used to call a function from inside the same function.

2. Which of these activities are good use cases for recursive programs? Check all that apply.
> Going through a file system collecting information related to directories and files.
> Managing permissions assigned to groups inside a company, when each group can contain both subgroups and users.

3. Fill in the blanks to make the is_power_of function return whether the number is a power of the given base. Note: base is assumed to be a positive number. Tip: for functions that return a boolean value, you can return the result of a comparison.
```Python
def is_power_of(number, base):
 # Base case: when number is smaller than base.
    if number < base:
        # If number is equal to 1, it's a power (base**0).
        return number == 1

    # Recursive case: keep dividing number by base.
    return is_power_of(number / base, base)


print(is_power_of(8,2))     # Should be True
print(is_power_of(64,4))    # Should be True
print(is_power_of(70,10))   # Should be False
```

4. Recursion is a process where a function calls itself one or more times with modified values to accomplish a task. This technique can be particularly effective when solving complex problems that can be broken down into smaller, simpler problems of the same type. In the provided code, the count_users function uses recursion to count the number of users that belong to a group within a company's system. It does this by iterating through each member of a group, and if a member is another group, it recursively calls count_users to count the users within that subgroup. However, there is a bug in the code! Can you spot the problem and fix it?
```Python
def count_users(group):
  count = 0
  for member in get_members(group):
    if is_group(member):
      count += count_users(member)
    else:
      count +=1
  return count


print(count_users("sales")) # Should be 3
print(count_users("engineering")) # Should be 8
print(count_users("everyone")) # Should be 18
```

5. In the while loops practice quiz, you were asked to write a function to calculate the sum of all positive numbers between 1 and n. Rewrite the function using recursion instead of a while loop. Remember that when n is less than 1, the function should return 0 as the answer.
```Python
def sum_positive_numbers(n):
    if n < 1:
        return 0
    return n + sum_positive_numbers(n-1)


print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15
```