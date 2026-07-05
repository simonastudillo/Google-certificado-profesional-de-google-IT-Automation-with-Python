# Proyecto final

## Introducción al proyecto final
- Hemos aprendido los conceptos básicos de la sintaxis de Python, incluidas las funciones ​, los condicionales y los bucles para-y-while
- Además, hemos aprendido a usar los tipos de datos más comunes, como números enteros, cadenas, ​listas y diccionarios
- Ahora vamos a reunir todos estos conocimientos para resolver ​problemas más divertidos y emocionantes
- En los próximos vídeos veremos cómo resolver un problema más complejo ​escribiendo un script desde cero
- Pensaremos en: Que datos necesitamos, como vamos a procesarlos y cómo vamos a mostrar los resultados

---

## Planteamiento del problema
- Imagina que es un especialista en TI que trabaja en una empresa mediana
- Su gerente quiere crear un informe diario que haga un seguimiento del uso de las máquina
- En concreto, quiere saber qué usuarios están conectados actualmente a qué ​máquinas
- En su empresa, hay un sistema que recopila todos los eventos que ocurren en ​las máquinas de la red. ​Entre los muchos eventos recopilados, registra cada vez que un usuario inicia o cierra sesión en ​una computadora. ​Con esta información, queremos escribir un script que genere un informe de ​qué usuarios han iniciado sesión en qué máquinas en ese momento.
- Antes de empezar a resolver ese problema, necesitamos saber qué información utilizaremos ​como entrada y qué información tendremos como salida
- Podemos resolver esto observando el resto del sistema en el que se ​alojará nuestro script
- En nuestro escenario de informe, la entrada es una lista de eventos. ​Cada evento es una instancia de la clase de eventos. ​Una clase de evento contiene la fecha en que ocurrió el evento, ​el nombre de la máquina en la que ocurrió, el usuario implicado y el tipo de evento
-  ​En este escenario, nos importa el tipo de evento de inicio y cierre de sesión
- Los atributos se denominan Date, User, Machine y Type
- Los eventos son: Login y Logout
- Nuestro script recibirá una lista de objetos de eventos y ​accederá a los atributos de los eventos. ​Luego usaremos esa información para saber si un usuario ha iniciado sesión actualmente en ​una máquina o no

- Output 
- ​Queremos generar un informe que enumere todos los nombres de las máquinas y, para ​cada máquina, una lista de los usuarios que han iniciado sesión actualmente
- Luego queremos que esta información se imprima en la pantalla
- es mejor centrarse primero en hacer que el programa funcione. ​Siempre puedes dedicar tiempo a hacer que el informe se vea bien más adelante
- Por ahora, simplifiquémoslo y optaremos por el enfoque de imprimir el ​nombre de la máquina seguido de todos los usuarios actuales separados por comas

---

## Reseña:  Investigación
- Los siguientes bloques de código se usarán en el próximo video:
```Python
numbers = [ 4, 6, 2, 7, 1 ]
numbers.sort()
print(numbers)

names = ["Carlos", "Ray", "Alex", "Kelly"]
print(sorted(names))
print(names)
print(sorted(names, key=len))
```

---

## Investigación
- Para averiguar qué usuarios han iniciado sesión actualmente en las máquinas, ​necesitamos comprobar cuándo iniciaron sesión y cuándo la cerraron
- ​Si un usuario ha entrado en una máquina y luego ha salido, ​ya no está conectado a ella. ​Pero si aún no ha salido, sigue conectado. 
- saber esto nos dice que para resolver esto correctamente, ​es vital que procesemos los eventos en orden cronológico
- Si no lo están, ​podemos obtener el evento de cierre de sesión antes que el evento de inicio de sesión correspondiente
- Y nuestro código puede hacer cosas impredecibles
- Investiga como ordenar listas en Python
    - sort(): Modifica la lista original y la ordena en su lugar
    - sorted(): Devuelve una nueva lista ordenada y deja la lista original sin cambios
- Se define usar la función sort()
- Debemos investigar como ordenar una lista basados en un atributo de los objetos que contiene
- La función sort() tiene un parámetro llamado key que nos permite especificar una función que se aplicará a cada elemento de la lista antes de compararlos
- Adicionalmente el parámetro key nos permite enviar una función como criterio, por ejemplo `len`
- Escribiremos una función llamada get_event_date que tomará un objeto de evento y devolverá su atributo Date

---

## Reseña: Planificación
- Los siguientes bloques de código se usarán en el próximo video:
```Python
def current_users(events):
  events.sort(key=get_event_date)
  machines = {}
  for event in events:
    if event.machine not in machines:
      machines[event.machine] = set()
    if event.type == "login":
      machines[event.machine].add(event.user)
    elif event.type == "logout":
      machines[event.machine].remove(event.user)
  return machines

def generate_report(machines):
  for machine, users in machines.items():
    if len(users) > 0:
      user_list = ", ".join(users)
      print("{}: {}".format(machine, user_list))
```

---

## Planificación
- Sabemos que nuestra entrada será una lista ​de eventos y los ordenaremos por tiempo. ​Cada evento de esa lista incluirá un nombre de máquina y ​un nombre de usuario y ​nos indicará si el evento es un inicio de sesión o un cierre de sesión
- Queremos que nuestro script haga un seguimiento de los usuarios cuando ​inician y cierran sesión en las máquinas.
- Pensemos en lo que haremos para ​cada evento y veamos si ​podemos encontrar la mejor estrategia
- Cuando procesemos un evento, ​veremos que alguien ha interactuado con una máquina.
- Si se trata de un cierre de sesión, ​queremos eliminarlo del grupo ​de usuarios que han iniciado sesión en la máquina
- En ese escenario tiene sentido usar un conjunto de tipo `Set`
- Para saber a que máquina pertenece usaremos `dictionary`
- El `key` será el nombre de la máquina y el `value` será un conjunto de usuarios que han iniciado sesión actualmente en esa máquina
- Para cada evento que ​procesemos, revisaremos primero en el diccionario ​si la máquina ya está allí.
- Tenemos que comprobarlo porque podría ser ​la primera vez que ​procesemos un evento para esa máquina
- Si no está ahí, crearemos una nueva entrada. 
- Si es así, actualizaremos ​la entrada existente con ​la acción correspondiente al evento, ​lo que significa que agregaremos el usuario si ​el evento es un inicio de sesión o lo eliminaremos si es un cierre de sesión. 
- Una vez que hayamos terminado de procesar los eventos ​, queremos imprimir un informe con ​la información que generamos. 
- Esta es una tarea completamente independiente, ​por lo que debería ser una función independiente.
- Esta función recibirá ​el diccionario que generamos e imprimirá el informe.
- Es importante tener funciones independientes para ​procesar los datos e imprimirlos en la pantalla
- Esto se debe a que si queremos ​modificar la forma en que se imprime el informe, ​sabemos que solo necesitamos cambiar ​la función encargada de la impresión.
- ​O si encontramos un error en la forma en que procesamos los datos, ​solo necesitamos cambiar la función de procesamiento
- También nos permitiría usar ​la misma función de procesamiento de datos ​para generar un tipo diferente de informe, ​como generar un archivo PDF

---

## Reseña: Escribir el Script
- Los siguientes bloques de código se usarán en el próximo video:
```Python
def get_event_date(event):
	return event.date

def current_users(events):
    events.sort(key=get_event_date)
    machines = {}
    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()
        if event.type == "login":
            machines[event.machine].add(event.user)
        elif event.type == "logout":
            machines[event.machine].remove(event.user)
    return machines

def generate_report(machines):
    for machine, users in machines.items():
        if len(users) > 0:
            user_list = ",".join(users)
            print("{}: {}".format(machine, user_list))
```

---

## Escribir el Script
- Empecemos definiendo ​la función de ayuda que usaremos para ordenar la lista.
- Usaremos la función simple como ​parámetro de la función de ordenación para ordenar la lista
- Ahora estamos listos para empezar a codificar nuestra función de procesamiento, ​a la que llamaremos `current_users`
- Dentro de la función, primero ordenaremos nuestros eventos usando ​el método sort y pasando ​la función que acabamos de crear como clave. 
- antes de empezar a iterar por nuestra lista de eventos, ​necesitamos crear el diccionario donde ​almacenaremos los nombres y usuarios de una máquina
- A continuación, queremos comprobar si ​la máquina afectada por este evento está en el diccionario. ​Si no lo está, la añadiremos con un conjunto vacío como valor
- para los eventos de inicio de sesión, ​queremos añadir el usuario a la lista, ​y para los eventos de cierre de sesión, ​queremos eliminar el usuario de la lista
- Para ello, vamos a utilizar los métodos add y remove, ​que añaden y eliminan elementos de un conjunto
- Una vez que hayamos terminado de iterar por la lista de eventos, ​el diccionario contendrá todas las máquinas que hemos visto como claves
- crearemos una nueva función llamada `generate_report`
- En nuestro informe, queremos iterar ​sobre las claves y valores del diccionario. ​Para ello, utilizaremos el método items que devuelve ​tanto la clave como el valor de cada par del diccionario. 
- antes de imprimir nada, ​queremos asegurarnos de no imprimir ​ninguna máquina en la que no haya nadie conectado
- Para evitarlo, le decimos al ordenador que sólo imprima ​cuando el conjunto de usuarios tenga más de cero elementos
- Ahora, hemos dicho antes que queremos imprimir ​el nombre de la máquina seguido de ​los usuarios conectados a la máquina separados por comas.
- ​Generemos la cadena de usuarios logueados para ​esa máquina usando el método join.
- ​Ahora, podemos generar la cadena que queremos usando el método format.

---

## Reseña: Uniendo las piezas
- Los siguientes bloques de código se usarán en el próximo video:
```Python
def get_event_date(event):
  return event.date

def current_users(events):
  events.sort(key=get_event_date)
  machines = {}
  for event in events:
    if event.machine not in machines:
      machines[event.machine] = set()
    if event.type == "login":
      machines[event.machine].add(event.user)
    elif event.type == "logout":
      machines[event.machine].remove(event.user)
  return machines

def generate_report(machines):
  for machine, users in machines.items():
    if len(users) > 0:
      user_list = ", ".join(users)
      print("{}: {}".format(machine, user_list))

class Event:
  def __init__(self, event_date, event_type, machine_name, user):
    self.date = event_date
    self.type = event_type
    self.machine = machine_name
    self.user = user

events = [
  Event('2020-01-21 12:45:46', 'login', 'myworkstation.local', 'jordan'),
  Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
  Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
  Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
  Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
  Event('2020-01-23 11:24:35', 'login', 'mailserver.local', 'chris'),
]

users = current_users(events)
print(users)

generate_report(users)
```

---

## Unir las piezas
- Se crea un ejemplo de la clase Event y se crea una lista de eventos
- Se llama a la función current_users con la lista de eventos y se imprime el diccionario resultante
- Se llama a la función generate_report con el diccionario resultante y se imprime el informe en la pantalla
- El resultado final: 2 máquinas con usuarios conectados y 1 máquina sin usuarios conectados
- Luego en el reporte se imprimen las 2 máquinas con usuarios conectados y no se imprime la máquina sin usuarios conectados

---

## Lab: Unir las piezas
```Python
def get_event_date(event):
  return event.date

def current_users(events):
  events.sort(key=get_event_date)
  machines = {}
  for event in events:
    if event.machine not in machines:
      machines[event.machine] = set()
    if event.type == "login":
      machines[event.machine].add(event.user)
    elif event.type == "logout" and event.user in machines[event.machine]:
      machines[event.machine].remove(event.user)
  return machines

def generate_report(machines):
  for machine, users in machines.items():
    if len(users) > 0:
      user_list = ", ".join(users)
      print("{}: {}".format(machine, user_list))

class Event:
  def __init__(self, event_date, event_type, machine_name, user):
    self.date = event_date
    self.type = event_type
    self.machine = machine_name
    self.user = user

events = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'logout', 'mailserver.local', 'chris'),
]

users = current_users(events)
print(users)

generate_report(users)
```

---

## Python en acción
- Felicidades por tu avance, aprendiste a:
1. Identificar un problema
2. Investigar las formas de solucionarlo
3. Planificar la mejor estrategía para llevarlo a cabo, como se hace y como estructurar el código
4. Escribir el código y resolver el problema
5. Ejecutar y verificar que el código funciona correctamente

- El problema y solución
Imagina este escenario: Cada mes, recibes una hoja de cálculo con cientos de nuevos empleados. Se te pide que crees cuentas de usuario para todos ellos en un servidor Linux. El formato de la hoja de cálculo es el siguiente:
```
username,password,real_name

amanda,,Amanda Alonso

ian,,Ian Ortega

eugene,,Eugene Konya

[...]
```
Observa que el campo de contraseña está vacío en todos los registros. Esto significa que debes generar contraseñas aleatorias para cada usuario y luego crear sus cuentas. También necesitas guardar las contraseñas generadas en un nuevo archivo CSV para poder comunicárselas a los nuevos empleados.

Esta tarea no es difícil, pero consume mucho tiempo si creas las contraseñas y cuentas para los cientos de nuevos empleados una por una. La solución es automatizar esta tarea con Python.

- El script
Para ayudar a organizar todos los datos, crear cuentas para los nuevos empleados y generar contraseñas para cada nuevo usuario, primero debe importar algunas bibliotecas estándar de Python.
- `import csv` - Esta biblioteca proporciona funciones para leer y escribir archivos CSV.
- `import secrets` - Esta biblioteca proporciona funciones para generar contraseñas aleatorias seguras.
- `import subprocess` - Esta biblioteca proporciona funciones para ejecutar comandos del sistema operativo desde Python, además permite usar el comando `useradd` para crear cuentas de usuario en un sistema Linux.
- `from pathlib import Path` - Esta biblioteca proporciona funciones para trabajar con rutas de archivos y directorios de manera más sencilla y legible.

- Comencemos
- Antes de comenzar usemos el comando `cwd = Path.cwd()` para obtener el directorio de trabajo actual
- Luego usemos a `with` y la `keyword` `as`. El uso de `with` nos ayuda a manejar recursos y `as` crea un alias para el recurso que quieres llamar.
```Python
with open(cwd / "data/users_in.csv", "r") as file_input, open(cwd / "data/users_out.csv", "w") as file_output:
```
- La librería `csv`se encarga de leer y parsear al entrada desde el fichero.
- Luego puedes usar un `DictReader`, de esta forma cada fila del archivo CSV se convertirá en un diccionario.
```Python
    reader = csv.DictReader(file_input)
```
- La entrada para el script esta listo, ahora necesitamos crear la salida.
- Crea el `DictWriter` y usa los mismo campos de la entrada para crear la salida. Luego escribe el encabezado en el archivo de salida.
```Python
    writer = csv.DictWriter(file_output, fieldnames=reader.fieldnames)
    writer.writeheader()
```
- Ahora puedes crear un log para revisar cada fila
```Python
    for user in reader:
        print(user)
```
- Despues del loop, usa la librería de `secrets`,  genera una contraseña aleatoria de 8 bits, equivalente a 16 caracteres en total. 
- Luego ejecuta `/sbin/useradd` para crear cada usuario
- Usar el parámetro `check=True` para asegurarte de que si el comando falla, se lanzará una excepción y podrás manejarla adecuadamente.
```Python
        user["password"] = secrets.token_hex(8)
        useradd_cmd = ["/sbin/useradd",
                       "-c", user["real_name"],
                       "-m",
                       "-G", "users",
                       "-p", user["password"],
                       user["username"]]
        subprocess.run(useradd_cmd, check=True)
```
- Por último , escribe la fila en el archivo de salida
```Python
        writer.writerow(user)
```

---

## Diálogo con el entrenador: Planificación para soluciones Python eficientes
- En este diálogo, exploraremos cómo aplicar técnicas de planificación a necesidades comunes de programación.
- Esto es lo que cubriremos:
- Comprender la importancia de planificar antes de empezar a programar.
- Diferenciar entre el método `.sort()` y la función `sorted()` de Python.
- Mejorar la eficiencia del código planificando la solución de forma eficaz.

> Coach: Great! Imagine you're tasked with organizing a list of computer serial numbers for a new IT project. Before you even write a single line of code, what is the very first critical step in the planning phase, and why is it essential?
> Me: We need to verify the information we have and how we want the final information to be displayed, so we can plan the next steps.
> Coach: That's a good start! You've touched on understanding the desired output. To elaborate a bit, why is it so important to thoroughly understand the problem and the information you have before you even think about writing code?
> Me: It's important to know what data we'll have available to sort, filter, and verify if validations are needed, and what the most efficient way to do it might be. If we write code without knowing what data is coming in, it's very likely to fail and we'll have to modify the code.
> Coach: Excellent! You've highlighted the crucial point that understanding the input data and potential validations helps prevent errors and rework, leading to more efficient code. Now, let's move on to Linking Planning to Effective Coding. How does identifying the inputs and outputs help you write clearer code?
> Me: It helps us identify steps; we can do it first on paper or in words. If we need to use a field to filter or if it should have different behavior, knowing what that field will be called is vital.
> Coach: That's a great way to put it! Planning on paper or in words helps you map out the logic and anticipate how different data fields will be used. This clarity directly contributes to writing code that is easier to understand and maintain. Now, thinking about organizing those serial numbers, how would planning help you choose the right Python sorting method, and what are some differences between .sort() and sorted()?
> Me: The difference between .sort() and .sorted() is that the former modifies the current list, while the latter generates a new list with the data already sorted. In this case, we could use .sort() unless we need to compare the input data against the sorted data.
> Coach: Good work! You've accurately described the main difference between .sort() and sorted() and even considered a scenario for when to use .sort(). To expand your knowledge, can you think of a situation where using the key argument with either of these sorting methods would be beneficial?
> Me: Of course, we can sort them using the key argument and thus sort by category, by type, department or some other data that comes in the entry; it could even be sorted by date of age if it has one
> Coach: That's a perfect explanation! Using the key argument allows for much more flexible sorting based on specific criteria like category, type, or even a custom function. This shows a solid understanding of how to tailor sorting to your specific needs. Now, let's move on to Summarizing Planning and Efficiency. How does the planning phase, coupled with a solid understanding of Python tools like sorting methods, collectively work towards creating a reliable and efficient script?
> Me: Planning is fundamental to knowing what we have to do, what we are doing, and what we still need to do; knowing the limits of what a function should handle at a micro level and its importance at a macro level
> Coach: You're doing a great job! You clearly understand the essential steps for planning an efficient coding solution. Your explanation highlights how planning provides a roadmap, ensuring you're aware of the scope and purpose of your code at both micro and macro levels. This foresight is key to building reliable and efficient scripts. Good job, you have completed all the topics for our session. Up next - view your feedback.

- During today's session covering how to apply planning techniques to common coding needs, we focused on understanding the importance of planning before coding, differentiating between Python's .sort() and sorted() methods, and improving code efficiency through effective planning.
- Your strengths:
- You accurately identified the importance of understanding the problem and input data to prevent errors and rework.
- You clearly articulated the difference between .sort() and sorted() and provided a good example of when to use the key argument for flexible sorting.
- Keep up the good work!

---

## Module 5 challenge: Final Project
1. A software engineer is tasked with developing a new feature for a popular web application. The feature involves a complex algorithm that requires a significant amount of coding. The engineer is tempted to start writing the code from scratch, but their manager suggests taking a different approach. What is the manager’s recommendation based on?
> The manager believes that the engineer should spend some time researching the problem to identify if a similar problem has been solved before.

2. Based on the following code, what is the correct output?
```Python
numbers = [ 3, 5, 4, 8, 1 ]

numbers.sort()

print(numbers)
```
> 1, 3, 4, 5, 8

3. Which method is used to sort a list without creating a new list?
> The sort() method 

4. You want to sort the following list in descending order. What is the correct code to use to do this?
```Python
numbers = [ 4, 6, 2, 7, 1 ]
```
> numbers.sort(reverse = True)

5. What is the purpose of the argument key=len in a Python script?
> To sort a list of strings based on their length. 

6. A system administrator is managing a network of computers. Each computer has a set of users who are currently logged in. The administrator wants to be able to quickly look up the current users of a given computer. Which data structure is the most efficient for storing the current users of each computer?
> A dictionary 

7. A programmer is tasked with developing a program that processes events and prints the associated data to the screen. The programmer is unfamiliar with the most efficient approach to accomplish this task. What should the programmer do?
> Create 2 separate functions to process the events and print the associated data to the screen.

8. What does the following code snippet do?
```Python
if event.type == "login":

 machines[event.machine].add(event.user)
```
> It checks if the event type is “login” and if so, adds the user to the list of logged-in users for a specified machine. 

9. A programmer is designing a grading script for a teacher. The teacher needs to assign grades to students based on different student assessment scores. The programmer needs to create a script that will execute code block A if condition 1 is true but will execute code block B if condition 1 is false and condition 2 is true. What type of statement should the programmer use to evaluate condition 2?
> elif statement

10. Take a look at the code snippet below. What is the purpose of the generate_report function?
```Python
def generate_report(machines):
 for machine, users in machines.items():
    if len(users) > 0:
        user_list = ", ".join(users)
        print("{}: {}".format(machine, user_list))
```
> To generate a report that lists all the machines and the users logged into each machine.