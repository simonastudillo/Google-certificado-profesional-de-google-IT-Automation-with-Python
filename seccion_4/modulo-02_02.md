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

---

## Mantener los resultados locales
- Pero, ¿y si analizar el archivo lleva mucho ​tiempo incluso cuando se hace fuera del bucle? ​Recuerde que para que ​nuestros scripts lleguen a su objetivo más rápido, ​necesitamos evitar que nuestro ordenador haga un trabajo innecesario.
- Si el script se ejecuta con bastante regularidad, ​es común crear una caché local. 
- Así que si estamos analizando un archivo grande y ​guardando solo algunas piezas clave de información de él, ​podemos crear una caché para almacenar solo esa información, ​o si obtenemos alguna información a través de la red, ​podemos mantener una copia local del archivo ​para evitar descargarlo una y otra vez. 
- Tenemos que pensar en la frecuencia con la que vamos a actualizar ​la caché y qué sucede ​si los datos en la caché están desactualizados
- Si estamos buscando algunas estadísticas a largo plazo, ​podemos generar el caché una vez al día, ​y no será un problema. 
- Por ejemplo, si nuestra caché se basa en un archivo, ​podríamos almacenar la fecha de modificación de ​ese archivo cuando calculáramos la caché. ​Entonces solo vuelva a calcular la caché si ​la fecha de modificación del archivo ​es más reciente que la que habíamos almacenado. 
- ​Tenga en cuenta que las cachés no ​siempre necesitan ser estructuras elaboradas, ​almacenando mucha información con una lógica de tiempo de espera compleja. 
- ​A veces, pueden ser tan ​simples como tener una variable que almacena un ​resultado temporal en lugar de ​calcular este resultado cada vez que lo necesitamos. ​
- Ejemplo
    - supongamos que está generando un informe que imprime ​cuántos usuarios hay en ​cada uno de los diferentes grupos de la red.
    - ​Ahora, algunos de estos grupos pueden contener otros grupos en ​ellos y algunos grupos pueden incluso formar parte de varios grupos. 
    - Por ejemplo, el grupo de ingenieros de versiones de Java ​formaría parte del grupo de ingenieros de versiones ​y del grupo de desarrolladores de Java.
    - ​¿ Cómo podemos evitar contar usuarios únicos ​más de una vez si aparecen en varios grupos?
    - ​Podemos tener un diccionario con el grupo como ​la clave y la cantidad de usuarios como el valor.
    - ​De esta forma, solo necesitamos ​contar los miembros de un grupo una vez, ​y después de eso, simplemente usar el valor en el diccionario. 
- recuerde que querrá buscar ​estrategias que le permitan evitar realizar operaciones costosas. ​Primero, verifique si estas operaciones son necesarias en absoluto. ​Si lo son, vea si puede almacenar ​los resultados intermedios para evitar ​repetir la operación costosa más de lo necesario

---

## Script lento con bucle costoso
- Ejemplo:
    - Script de ejemplos pasados que tenía problemas con fecha.
    - Los desarrolladores están pidiendo ​nuestra ayuda para averiguar cómo ​podemos hacer que el programa sea más rápido
    - ​Primero, necesitaremos reproducir ​el problema y averiguar qué significa lento en este caso. 
    - Un usuario nos dijo que el problema es ​visible cuando la lista de destinatarios es larga.
    - Es posible que recuerde que la aplicación tiene dos partes.
    - ​Un script de shell que aparece ​una ventana donde podemos introducir los datos ​del recordatorio y un script de Python ​que prepara el correo electrónico y lo envía. 
    - La parte que es lenta es el envío de los correos electrónicos. ​Así que no interactuaremos con la ventana emergente en absoluto.
    - Mediremos la velocidad del script usando el comando time.
    - `time ./send_reminders.py "2020-01-13|Example|test1"
    - Cuando llamamos a time, ejecuta el comando que ​le pasamos e imprime el tiempo que tardó ejecutarlo.
    - ​Hay tres valores diferentes. ​Real, usuario y sys.
        - ​Real es la cantidad de tiempo real ​que tardó en ejecutar el comando. Este valor a veces se denomina ​hora del reloj de pared porque es ​cuánto tiempo ​mediría un reloj colgado en la pared sin importar lo que esté haciendo el equipo
        - Usuario es el tiempo dedicado a realizar ​operaciones en el espacio de usuario
        - Sys es el tiempo dedicado a realizar operaciones a nivel de sistema.
    - Muy bien. Vemos que ​esta vez con 9 correos tardó 0.296 segundos en enviar el correo electrónico.
    - ​Eso todavía no es mucho, pero ​parece que está tomando más tiempo con una lista más larga de correos electrónicos.
    - Siempre podríamos mirar el código y ver ​si encontramos operaciones costosas que podamos mejorar. ​Pero en este caso queremos usar un generador de perfiles para ​obtener algunos datos sobre lo que está pasando.
    - Usaremos `pprofile3` para generar un perfil de nuestro script. ​Este generador de perfiles imprimirá un informe ​que nos mostrará qué funciones ​están consumiendo más tiempo y recursos.
    - `pprofile3 -f callgrind -o profile.out ./send_reminders.py "2020-01-13|Example|test1,test2,test3,test4,test5,test6,test7,test8,test9"`
        - ​El parámetro -f le dice al generador de perfiles que genere un informe en formato callgrind, que es un formato que podemos usar con herramientas de visualización como KCachegrind o QCachegrind.
        - El parámetro -o le dice al generador de perfiles que guarde el informe en un archivo llamado profile.out.
    - usaremos KCachegrind para ver el informe `kcachegrind profile.out`
    - En la mitad inferior derecha vemos un gráfico de llamadas, ​que nos dice que la función principal es ​llamar a la función de envío de mensajes una vez. 
    - Esta función llama a la función de plantilla de mensaje, ​la función get name ​y la función send message nueve veces cada una.
    - El gráfico también nos indica ​cuántos microsegundos se gastan en cada una de estas llamadas. 
    - Podemos ver que la mayor parte del tiempo ​se gasta en la función get name
    - Así que vemos que la función get name abre ​un archivo CSV y luego pasa por todo el archivo comprobando si ​el primer campo de la línea coincide con el nombre del correo electrónico ​y cuando ese es el caso ​establece el valor de la variable de nombre.
    - Hay un par de cosas que ​están mal con esta función. 
    - Primero, una vez que encuentra el elemento en ​la lista, debe salir inmediatamente del bucle. 
    - Pero incluso si arreglamos que todavía abriría ​el archivo y lo leería para cada dirección de correo electrónico. ​Esto puede ser muy lento si el archivo tiene muchas líneas.
    - Podemos leer el archivo una vez ​y almacenar los valores que nos importan en ​un diccionario y luego usar ​ese diccionario para las búsquedas
    - Cambiaremos la función get name ​y la convertiremos en una función de lectura de nombres ​que procesará el archivo CSV y ​almacenará los valores que queremos en el diccionario de nombres.
    - ​Para cada línea almacenará el correo electrónico como ​la clave y los nombres como los valores. ​
    - Ahora tenemos que cambiar la forma en que se ​llama a esto en la función de enviar mensaje. ​Vemos que la función get name ​se llama una vez por correo electrónico.
    - ​Para aplicar nuestro cambio debemos llamar a ​la función de nombres de lectura antes del ​bucle for para que lo hagamos solo una vez. 

---

## Más sobre la mejora de nuestro código
- El desarrollo de software es un componente clave de las tecnologías de la información, ya que implica la creación y el mantenimiento de aplicaciones que permiten a los usuarios de ordenadores resolver problemas y realizar tareas. 
- La comprensión del desarrollo de software le permitirá identificar y abordar los problemas con rapidez, idear soluciones eficaces y establecerse como un socio de confianza en su organización
- Perfiles
    - La creación de perfiles de software es una técnica de diagnóstico utilizada para analizar en tiempo real la utilización de los recursos de las aplicaciones y supervisarlas.
    - Este proceso implica examinar métricas de rendimiento clave como la utilización de la CPU, el consumo de memoria y el uso de espacio en disco
    - Esto se hace evaluando el tiempo y los recursos que consume. Permite medir la velocidad del código en comparación con una línea de base e incluso con software o productos de la competencia.
    - En Python, el benchmark se realiza a través del módulo Timeit. Éste mide el tiempo de ejecución de tus segmentos de código, ayudándote a identificar posibles cuellos de botella mediante la realización de mini pruebas comparativas para funciones individuales. De este modo, puedes mejorar la eficiencia de tu aplicación y optimizar el código.
    - Las herramientas de perfilado, como Flat, Call-graph y Input-sensitive, forman parte integral de la depuración
    - La importancia de la creación de perfiles va más allá del desarrollo de software. También es útil en el desarrollo de arquitectura informática y compiladores
    - Los perfiles desempeñan un papel esencial no sólo en el desarrollo de software, sino también en el panorama informático más amplio
    - La creación de perfiles ayuda a los ingenieros de software a diseñar aplicaciones eficientes y eficaces mediante la supervisión y el análisis del uso de recursos en tiempo real.