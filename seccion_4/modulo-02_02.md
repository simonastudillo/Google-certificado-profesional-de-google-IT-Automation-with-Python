# Código lento

## Escribir código eficaz
- Siempre debemos comenzar ​escribiendo código claro que haga lo que debería y ​solo tratar de hacerlo más rápido si ​nos damos cuenta de que no es lo suficientemente rápido.
- Si tarda 10 minutos en escribir ​un script que se ejecutará en cinco segundos ​y 20 minutos en escribir un script que ​hará lo mismo pero tarda tres segundos, ​¿hace la diferencia?
- Si lo ejecuta una vez al día, ​la diferencia de dos segundos definitivamente no ​justificará los 10 minutos adicionales de trabajo. 
- Pero si va a ejecutar el mismo script para ​los 500 equipos de su red, ​esa pequeña diferencia significa que tomará ​15 minutos menos ejecutar todo el script
- Intentar optimizar cada ​segundo de un script probablemente no valga la pena. 
- Si queremos que nuestro código termine más rápido, ​necesitamos hacer que nuestro ordenador funcione menos, ​y para hacerlo, ​tendremos que evitar hacer un trabajo que realmente no es necesario. 
- Los más comunes incluyen ​almacenar datos que ya se calcularon para ​evitar volver a calcularlos, utilizando ​las estructuras de datos correctas para ​el problema y reorganizar ​el código ​para que el equipo pueda permanecer ocupado mientras espera ​información de fuentes lentas ​como disco o a través de la red.
- `Profiler` es una herramienta que nos permite ​ver qué partes de nuestro código ​están consumiendo más tiempo y recursos.
- `gprof` es un ejemplo de `Profiler` que nos permite ​ver qué partes de nuestro código ​están consumiendo más tiempo y recursos.
- `cProfile` es otro ejemplo de `Profiler` que nos permite ​ver qué partes de nuestro código ​están consumiendo más tiempo y recursos para programas escritos en Python.
- `Expensive actions` son aquellas que consumen mucho tiempo y recursos, como acceder a un disco duro o a través de la red.

---

## Utilizar las estructuras de datos adecuadas
- Tener una buena comprensión de ​las estructuras de datos disponibles para nosotros puede ayudarnos a ​evitar operaciones costosas innecesarias ​y a crear scripts eficientes.
- Las listas son secuencias de elementos. ​Podemos añadir, eliminar ​o modificar los elementos en ellos. ​Podemos iterar a través ​de toda la lista para operar en cada uno de los elementos
- Las listas son una estructura de datos que es ​rápida para agregar o eliminar elementos al final. ​Pero agregar o eliminar elementos en el medio puede ser ​lento porque todos los elementos ​que siguen deben reposicionarse.
- En los diccionarios ​agregamos datos asociando un valor a una clave. ​Luego, recuperamos un valor buscando una clave específica.
- La parte del mapa en esos nombres proviene de ​cómo estamos creando un mapeo entre una clave y un valor. 
- La parte Hash proviene ​del hecho de que para hacer que la estructura sea eficiente, ​se usa ​internamente una función hash para decidir cómo se almacenarán los elementos.
- La característica principal de esta estructura ​es que es súper rápida para buscar llaves. ​Una vez que tenemos nuestros datos almacenados en un diccionario, ​podemos encontrar el valor asociado a ​una clave en una sola operación. 
- ​Entonces, como regla general, ​si necesita acceder a los elementos por posición ​o siempre iterará a través de todos los elementos, ​use una lista para almacenarlos. ​
- si necesitamos ​buscar los elementos usando una clave, ​usaremos un diccionario.
- Otra cosa que podríamos evitar es ​crear copias de las estructuras que tenemos en la memoria, es decir generar más de una variable con el mismo valor. ​Si estas estructuras son grandes ​, puede ser bastante caro crear esas copias. ​Por lo tanto, deberíamos verificar si la copia ​es realmente necesaria. 

---

## Bucles caros
- Los bucles son los que hacen que nuestras computadoras hagan las cosas repetidamente. ​Son una herramienta extremadamente útil ​y evitemos el trabajo repetitivo, ​pero tenemos que utilizarlos con precaución.
- En particular, tenemos que pensar en ​qué acciones vamos a hacer dentro del bucle, ​y cuando sea posible, evitar hacer acciones costosas.
- ​Si realiza una operación costosa dentro de un bucle, ​multiplica el tiempo que tarda en hacer ​la operación costosa por ​la cantidad de veces que repite el bucle.
- Siempre que tenga un bucle en su código, ​asegúrese de verificar qué acciones está haciendo ​y vea si hay operaciones que puede ​sacar del bucle para hacerlas solo una vez.
- ​En lugar de hacer una llamada de red para cada elemento, ​haga una llamada antes del bucle.
- ​En lugar de leer desde el disco para cada elemento, ​lea todo antes del bucle. 
- Incluso si las operaciones realizadas ​dentro del bucle no son especialmente caras, ​si estamos revisando ​una lista de mil elementos y solo necesitamos cinco de ellos, ​estamos perdiendo tiempo en elementos que no necesitamos.
- Otra cosa que debe recordar sobre los bucles es ​salir del bucle ​una vez que encuentre lo que estaba buscando.
- `Break` es una palabra clave que nos permite salir de un bucle antes de que termine. ​Si estamos buscando un elemento en una lista, ​una vez que lo encontramos, podemos salir del bucle y ahorrar tiempo.