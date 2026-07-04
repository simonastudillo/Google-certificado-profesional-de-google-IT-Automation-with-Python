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