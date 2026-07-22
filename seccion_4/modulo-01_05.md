# Actividades de Qwiklabs

## Directrices y pasos para la resolución de problemas de Qwiklabs

---

## Evaluación de Qwiklabs: Depuración de scripts de Python
Imagina que uno de tus compañeros ha escrito un script de Python que no se ejecuta correctamente. Te pide ayuda para depurarlo. En este laboratorio, investigarás por qué falla el script y aplicarás los pasos de resolución de problemas que ya hemos aprendido para obtener información, encontrar la causa raíz y solucionar el problema.

Ten en cuenta que hay un cuestionario calificado después de este laboratorio. Debes completar el laboratorio antes de realizar el cuestionario. El cuestionario evaluará tu comprensión de los conceptos y procedimientos clave vistos en el laboratorio.

Aquí tienes algunas sugerencias para prepararte:
1. Presta mucha atención a las instrucciones y explicaciones proporcionadas durante la sesión de laboratorio.
2. Participa activamente en las actividades del laboratorio y toma notas.
3. Repasa tus notas del laboratorio antes de realizar el cuestionario.

---

## Ejemplar: Depurar scripts de Python
- En el laboratorio anterior se nos pide depurar un script de Python que no se ejecuta correctamente.
- El script es `~/scripts/greetings.py`
- Se asignan los permisos de ejecución y se ejecuta el script con el comando `./greetings.py`.
- Nos pregunta un nombre correctamente pero falla al darnos el número de la suerte
- Al revisar el error, nos indica que no puede concatenar un entero con una cadena de texto.
- Al revisar el contenido nos encontramos que el formar el string para el print, la variable `number` es un entero y no se hizo la transformación a string, por lo que al concatenar con el texto, nos da el error.
- La solución es transformar la variable `number` a string con la función `str()`, de esta manera: `print("Hello " + name + ", your lucky number is " + str(number))`.
- Hacemos el cambio, ejecutamos nuevamente el script y nos da el resultado esperado.
