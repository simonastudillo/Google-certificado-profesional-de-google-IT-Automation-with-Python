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