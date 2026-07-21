# Entender el problema

## "No funciona"
- Cuando se trabaja con usuarios, ​es bastante común recibir informes de fallas ​que simplemente se reducen a: «No funciona». 
- Qué información es útil o ​no puede depender del problema
- Preguntas útiles:
    - ¿ Qué intentabas hacer?
    - ​¿ Qué pasos seguiste?
    - ¿ Cuál fue el resultado esperado?
    - ¿ Cuál fue el resultado real?
- Debemos considerar ​primero las explicaciones más simples y evitar ​saltar a soluciones complejas o que consumen mucho tiempo ​a menos que realmente tengamos que hacerlo
- Debemos identificar los pasos que permitan eliminar la mayor cantidad de causas posibles del problema, para poder centrarnos en la causa raíz.
- Es importante que antes de comenzar a intentar resolver el problema, nos aseguremos de que entendemos lo que el usuario estaba intentando hacer y cuál era el resultado esperado. Esto nos ayudará a identificar la causa raíz del problema y a encontrar una solución más rápidamente.

---

## Creación de una caja de reproducción
- `Reproduction case`: Es una forma de verificar si el problema está presente o no, y de aislar la causa raíz del problema.
- Hay casos donde el problema no se puede reproducir, y en esos casos debemos recopilar toda la información posible sobre el entorno del usuario y las condiciones en las que ocurrió el problema.
- Esto se logra mirando los registros: pueden ser de accesos, errores o de eventos, dependiendo del tipo de problema que estemos tratando de resolver.
- Directorios de errores:
    - Linux: /var/log/
    - MacOS: /Library/Logs/
    - Windows: Event Viewer
- Muchas veces los logs contienen información útil sobre el problema, como mensajes de error, advertencias o información sobre el estado del sistema en el momento en que ocurrió el problema.

---

## Encontrar la causa
- Entender la causa raíz del problema es escencial para poder encontrar una solución efectiva de largo plazo.
- Debemos generar una teoría sobre lo que podría estar causando el problema y luego probar esa teoría para ver si es correcta.
- En caso de que la teoría no sea correcta, debemos generar una nueva teoría y probarla nuevamente.
- Siempre que sea posible, debemos probar nuestras teorías en un entorno de prueba antes de aplicarlas en el entorno de producción, para evitar causar más problemas.
- `iotop`: Es una herramienta de depuración de procesos y memoria que permite ver qué procesos están utilizando más recursos del sistema, como CPU, memoria o disco. Esto puede ayudarnos a identificar procesos que podrían estar causando problemas de rendimiento o bloqueos en el sistema.
- `iostat`: Es una herramienta de depuración de procesos y memoria que permite ver qué procesos están utilizando más recursos del sistema, como CPU, memoria o disco. Esto puede ayudarnos a identificar procesos que podrían estar causando problemas de rendimiento o bloqueos en el sistema.
- `vmstat`: Es una herramienta de depuración de procesos y memoria que permite ver qué procesos están utilizando más recursos del sistema, como CPU, memoria o disco. Esto puede ayudarnos a identificar procesos que podrían estar causando problemas de rendimiento o bloqueos en el sistema.
- `iftop`: Es una herramienta de depuración de red que permite ver qué procesos están utilizando más ancho de banda de red. Esto puede ayudarnos a identificar procesos que podrían estar causando problemas de rendimiento o bloqueos en la red.
- `rsync`: Es una herramienta para sincronizar archivos y directorios entre dos ubicaciones. Podemos usar el flag `-bwlimit` para limitar el ancho de banda utilizado por `rsync`, lo que puede ayudarnos a evitar problemas de rendimiento o bloqueos en la red.
- `nice`: Es una herramienta que permite cambiar la prioridad de un proceso en ejecución. Podemos usar `nice` para aumentar o disminuir la prioridad de un proceso, lo que puede ayudarnos a evitar problemas de rendimiento o bloqueos en el sistema.

---

## Problemas intermitentes
- Los problemas intermitentes son aquellos que ocurren de manera aleatoria y no se pueden reproducir de manera consistente.
- Para estos casos, siempre que se pueda añade información de depuración al código fuente del programa para que se pueda obtener más información sobre lo que está haciendo el programa en el momento en que ocurre el problema.
    - Por ejemplo podemos agregar que información se envía a un archivo de registro, o que información se imprime en la consola.
- `Haisenbug`: Es un tipo de error que desaparece o se comporta de manera diferente cuando se intenta depurarlo. Esto puede ocurrir debido a la naturaleza del error, como errores de sincronización en programas multihilo, o debido a la forma en que se está depurando el programa, como agregar instrucciones de depuración que cambian el comportamiento del programa. Este nombre proviene de la palabra "Heisenberg", en referencia al principio de incertidumbre de Heisenberg, que establece que no se puede conocer con precisión tanto la posición como la velocidad de una partícula al mismo tiempo. De manera similar, un Haisenbug puede cambiar su comportamiento cuando se intenta observarlo o depurarlo.
- Es cierto que muchas veces podemos resolver los problemas intermitentes simplemente reiniciando el sistema, pero esto no nos ayuda a entender la causa raíz del problema y puede llevar a que el problema vuelva a ocurrir en el futuro.

---

## Revisión: Guión intermitentemente fallido
- Los siguientes códigos se encuentran en el vídeo de la lección:
```bash
/meeting_reminder$ ./meeting_reminder.sh
```
```bash
#!/bin/bash

meeting_info=$(zenity --forms \
    --title 'Meeting' --text 'Reminder information' \
    --add-calendar 'Date' --add-entry 'Title' \
    --add-entry 'Emails' \
    2>/dev/null)
if [[ -n "$meeting_info" ]]; then
    python3 send_reminders.py "$meeting_info"
fi
```
```python
def main():
    if len(sys.argv) < 2:
        return usage()

    try:
        date, title, emails = sys.argv[1].split('|')
        message = message_template(date, title)
        send_message(message, emails)
        print("Successfully sent reminders to:", emails)
    except Exception as e:
        print("Failure to send email", file=sys.stderr)
    except Exception as e:
       print("Failure to send email: {}".format(e), file=sys.stderr)
```
```bash

meeting_info=$(zenity --forms \
    --title 'Meeting' --text 'Reminder information' \
    --add-calendar 'Date' --add-entry 'Title' \
    --add-entry 'Emails' \
    --forms-date-format='%Y-%m-%d' \
    2>/dev/null)
echo $meeting_info
if [[ -n "$meeting_info" ]]; then
    python3 send_reminders.py "$meeting_info"
fi
```
```python
def dow(date):
    dateobj = datetime.datetime.strptime(date, r"%Y-%m-%d")
    return dateobj.strftime("%A")
```

---

## Guión intermitentemente fallido
- Ejemplo: Un colega recientemente desarrolló una pequeña aplicación ​para enviar recordatorios de reuniones a las personas de la empresa, ​porque alguien se olvidaba de aparecer. ​El equipo de ventas fue el primero en ​probar la aplicación la semana pasada, y funcionó bien. ​Pero esta semana, otro usuario está tratando de enviar ​un recordatorio de reunión y el programa ​continúa terminando con un error. ​Dado que el colega que desarrolló la aplicación ​está al otro lado del Atlántico, ​el usuario está pidiendo ​nuestra ayuda para averiguar qué está pasando
- Primero, intentemos ejecutar el programa ​nosotros mismos y verifiquemos si podemos reproducir el problema
- Se nos presenta una ventana donde ​podemos introducir la fecha de la reunión, ​el título de la reunión ​y las personas a las que queremos enviar el recordatorio. ​El recordatorio de reunión que el usuario estaba ​intentando enviar fue para el 13 de enero ​y el título era Revisión de producción. 
- Vamos a tratar de recordar que el equipo de ventas ​envió la semana pasada que había funcionado bien. ​En ese caso, el recordatorio había sido enviado para el ​7 de enero y el título era Sales All Hands. ​Una vez más, me enviaré esto ​a mí mismo para evitar que la gente abarque recordatorios. ​Sí. En este caso, ​el programa envió correctamente el recordatorio. 
- ¿ Qué parámetro cree que tiene la culpa? ¿ ​El título o la fecha? Podría ser cualquiera. ​Pero apuesto a que es la fecha. ​Intentémoslo una vez más con ​el 13 de enero como fecha y Ventas All Hands como título. ​Otro fracaso. ​Así que tenemos un caso de reproducción. 
- Cuando intentamos enviar el recordatorio de la reunión del ​13 de enero, ​recibimos el mensaje de error. ​Pero si tratamos de enviar el mismo recordatorio ​para el 7 de enero, funciona bien. ​Ahora, el siguiente paso es ​encontrar la causa raíz del problema.
- en general, cuando las fechas están involucradas en un fallo, ​el problema se debe a cómo se formatean las fechas. ​En algunos países, las fechas se ​escriben con el mes primero y el segundo día.
- Abriremos el script meeting_reminder.sh, ​que es un script escrito en Bash. ​Vemos que este script está llamando a ​un programa llamado Zenity. ​Zenity es la aplicación que muestra la ventana para ​seleccionar la fecha, el título y los correos electrónicos. ​La salida generada por Zenity se ​almacena en una variable llamada meeting_info, ​que luego se pasa como un parámetro al ​script send_reminders.py, Python 3. ​A continuación, este script envía los correos electrónicos. 
- Modificamos el script para agregar un echo de la variable meeting_info, para que podamos ver qué información se está pasando al script de Python. 
- Al ejecutar vemos que la fecha usa el formato de mes/día/año, que es el formato predeterminado en los Estados Unidos
- Ahora revisamos el script de Python para buscar más información
- Vemos que la función main separa las variable con un splot, luego llama a la función message_template para crear el mensaje y luego llama a la función send_message para enviar el mensaje.
- Modificamos el print para imprimir la excepción que se está produciendo, para que podamos ver qué está causando el error.
- Al ejecutar recibimos el error que la fecha entregada no hace match con el formato esperado, que es %d/%m/%Y.
- Ahora modificamos el script de Bash para agregar el flag --forms-date-format='%Y-%m-%d' a la llamada a Zenity, para que la fecha se entregue en el formato esperado por el script de Python.
- Por último, modificamos el script de Python modificando la función dow para que use el formato %Y-%m-%d al analizar la fecha.

---

## Test your knowledge: Understanding the problem

1. When a user reports that an "application doesn't work," what is an appropriate follow-up question to gather more information about the problem?
> What should happen when you open the app?

2. What is a heisenbug?
> The observer effect.

3. The compare_strings function is supposed to compare just the alphanumeric content of two strings, ignoring upper vs lower case and punctuation. But something is not working. Fill in the code to try to find the problems, then fix the problems. Your goal is to search for the character “-” but - is typically reserved for ranges. Find a work-around that enables you to compare the two strings.
```python
import re
def compare_strings(string1, string2):
 #Convert both strings to lowercase
 #and remove leading and trailing blanks
 string1 = string1.lower().strip()
 string2 = string2.lower().strip()


 #Ignore punctuation
 punctuation = r"[.?!,;:\-']" # Escape the hyphen to avoid range error




 string1 = re.sub(punctuation, r"", string1)
 string2 = re.sub(punctuation, r"", string2)


 #DEBUG CODE GOES HERE
 print(string1 == string2)


 return string1 == string2


print(compare_strings("Have a Great Day!", "Have a great day?")) # True
print(compare_strings("It's raining again.", "its raining, again")) # True
print(compare_strings("Learn to count: 1, 2, 3.", "Learn to count: one, two, three.")) # False
print(compare_strings("They found some body.", "They found somebody.")) # False
```

4. How do we verify if a problem is still persisting or not?
> Attempt to trigger the problem again by following the steps of our reproduction case

5. The datetime module supplies classes for manipulating dates and times, and contains many types, objects, and methods. You've seen some of them used in the dow function, which returns the day of the week for a specific date. We'll use them again in the next_date function, which takes the date_string parameter in the format of "year-month-day", and uses the add_year function to calculate the next year that this date will occur (it's 4 years later for the 29th of February during Leap Year, and 1 year later for all other dates). Then it returns the value in the same format as it receives the date: "year-month-day".

Can you find the error in the code? Is it in the next_date function or the add_year function? How can you determine if the add_year function returns what it's supposed to? Add debug lines as necessary to find the problems, then fix the code to work as indicated above.   
```python
import datetime
from datetime import date

def add_year(date_obj):
  try:
    new_date_obj = date_obj.replace(year = date_obj.year + 1)
  except ValueError:
    # This gets executed when the above method fails, 
    # which means that we're making a Leap Year calculation
    new_date_obj = date_obj.replace(year = date_obj.year + 4)
  return new_date_obj

def next_date(date_string):
  # Convert the argument from string to date object
  date_obj = datetime.datetime.strptime(date_string, r"%Y-%m-%d")
  next_date_obj = add_year(date_obj)

  # Convert the datetime object to string, 
  # in the format of "yyyy-mm-dd"
  next_date_string = next_date_obj.strftime("%Y-%m-%d")
  return next_date_string

today = date.today()  # Get today's date
print(next_date(str(today))) 
# Should return a year from today, unless today is Leap Day

print(next_date("2021-01-01")) # Should return 2022-01-01
print(next_date("2020-02-29")) # Should return 2024-02-29
```