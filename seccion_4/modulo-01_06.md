# Repaso módulo 1

## Recapitulación del módulo 1: Conceptos de solución de problemas
- aprendimos los principios generales ​de depuración y solución de problemas
- Examinamos el proceso básico de resolver ​un problema técnico como obtener información, ​encontrar la causa raíz ​e implementar la corrección
- Aprendimos sobre un montón de ​herramientas y técnicas diferentes que podemos usar ​para entender mejor lo que está pasando ​con nuestros sistemas y nuestros programas, ​incluyendo cómo crear un caso de reproducción, ​cómo encontrar la causa raíz del problema ​y cómo lidiar con problemas ​que solo aparecen ocasionalmente
- aprendimos sobre el algoritmo de búsqueda binaria, ​y cómo podemos usarlo para biseccionar un problema ​y encontrar rápidamente la causa raíz de un problema técnico.
- Recuerde que los registros son su mejor amigo ​y use todos los recursos disponibles para usted, ​incluyendo buscar cosas en Internet ​y pedir ayuda a colegas o amigos

---

## Términos del glosario del curso 4, Módulo 1
- `binary search` (Búsqueda binaria): Algoritmo de búsqueda utilizado para encontrar un elemento específico en una lista o matriz ordenada dividiendo repetidamente el espacio de búsqueda por la mitad hasta que se encuentra el elemento deseado o se determina que está ausente
- `Bisection` (Bisección): Dividir en dos, también un comando Git
- `Debuggers` (Depuradores): Herramientas que siguen el código línea por línea, inspeccionan los cambios en las asignaciones de variables, interrumpen el programa cuando se cumple una condición específica, etc.
- `Debugging` (Depuración): El proceso de identificar, analizar y eliminar errores en el código real de un sistema en la aplicación
- `Linear search` (Búsqueda lineal): El proceso de buscar en cada línea de datos hasta localizar la entrada de datos deseada
- `Observer effect` (Efecto observador): La idea de que observar un fenómeno altera el fenómeno
- `System calls` (Llamadas al sistema): Las llamadas que los programas que se ejecutan en nuestro ordenador hacen al núcleo de ejecución
- `Troubleshooting` (Resolución de problemas): El proceso de resolver cualquier tipo de problema en el sistema que ejecuta la aplicación

---

## Module 1 challenge: Debug Python Scripts

1. How does debugging a script contribute to the quality and reliability of code and applications?
> Debugging helps you identify and rectify errors, enhancing code quality and application reliability

2. In the lab, where was the root cause of the issue located? 
>  Within the print statement

3. In the debugging process described, what is the purpose of replacing the original print statement with the following statement?

```python
# Original
print("hello " + name + ", your random number is " + number)
# Replacement
print("hello " + name + ", your random number is " + str(number))
```
> The purpose is to ensure the print statement correctly concatenates the name and random number with the appropriate data types.

3. Why is it important to reproduce an error when debugging scripts? Select all that apply
> To isolate the variables and conditions contributing to the error
> To document the problem for future reference
> To confirm that the issue is real and not a one-time occurrence

4. In the lab, what is the main issue with the script involving concatenating two different data points?
> The script uses incompatible data types for concatenation

4. Which of the following statements are true about adding two different data types directly in Python? 
> In Python, you cannot add two different data types directly.

5. What does the error message TypeError: Can't convert 'int' object to str implicitly tell you? 
> Something in the code is trying to concatenate a string and an integer

6. Question: In Python, what issue arises when trying to concatenate two different data types, such as a string and an integer, as seen in the provided code snippet?
> TypeError

6. You receive the following error message (TypeError: Can't convert 'int' object to str implicitly). What do you need to do to resolve this error? 
> Change the number into a string.

7. In the lab, you encountered an error message that indicates a problem with concatenating a string and an integer. To figure out the root cause of this bug, what step did you take next in the lab after successfully reproducing the error?
> Examined the code within the script

7. When you find an error, what should you do before trying to debug it? 
> Try and reproduce the error

8. When a bug is found in a software program during testing, what should you do?
> Document it and notify relevant team members

8. When a bug is found in a software program during testing, what is the best way to communicate it to the right individuals(s)? 
> Document it and notify relevant team members

9. Complete this sentence. In troubleshooting and debugging, a(n) ______________ type of problem is reproducible under the same set of conditions. 
> recurring

10. After a system update, a recurring error in the software you’re testing is no longer reproducible? What does this tell you? 
> The problem was a software issue. #bad

10. What can you infer if a recurring problem goes away when you change the system settings? 
> Something in the system settings was causing the problem.