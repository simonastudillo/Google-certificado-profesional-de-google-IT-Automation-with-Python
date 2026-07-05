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