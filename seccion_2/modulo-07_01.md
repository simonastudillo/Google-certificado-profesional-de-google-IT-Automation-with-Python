# Prepararse para el proyecto final

## Introducción a su proyecto final
- Hemos aprendido acerca de administrar archivos y directorios, ​leer y escribir archivos de texto y archivos ​CSV usando expresiones regulares, ​entender cómo interactúa el sistema con nuestros programas, ​ejecutar comandos del sistema ​y escribir pruebas automatizadas por nombrar algunos
- Tambien hemos aprendido a usar bash

---

## Escribir un script desde cero
- El primer paso para manejar ​cualquier proyecto de codificación es ​comprender completamente la declaración del problema
- Esto incluye; deletrear lo que hay ​que hacer e identificar cuáles ​son las entradas dadas y las salidas deseadas para ese programa que necesitamos escribir
- Luego se recomienda hacer algunas investigaciones
- Esto significa descrubir cómo podemos abordar el problemas con las herramientas proporcionadas por la biblioteca estándar de Python y otras bibliotecas de terceros
- Queremos evitar reinventar la rueda
- La investigación incluye buscar la documentación de módulos, clases y funciones que necesitamos usar y crear, ver ejemplos de la documentación.
- En tercer lugar, debemos planificar
- Esto significa pensar en qué ​tipos de datos son útiles para nuestra solución, ​el orden de operaciones que necesitamos realizar ​y cómo todas las piezas se han ​unido para formar nuestra solución
- Por último, debemos escribir el código y probarlo
- Este paso incluye escribir el código, hacer pruebas manuales y automatizadas, depurar el código y refactorizarlo para mejorar la legibilidad y la eficiencia
- Dentro de lo posible, debemos tambien agregar documentación y comentarios para que otros puedan entender nuestro código

---

## Planteamiento del problema del proyecto
- uno de ​los servidores utilizados por su empresa ​ejecuta un servicio llamado ticky
- Este servicio es un sistema interno de ticketing utilizado por ​muchos equipos diferentes de ​la empresa para gestionar su trabajo
- El servicio registra un montón de eventos en syslog, ​tanto cuando se ejecuta correctamente como ​cuando encuentra errores
- Los desarrolladores del servicio están pidiendo ​su ayuda para obtener ​información de esos registros, ​para comprender mejor cómo se está ​utilizando el software y cómo mejorarlo
- Las líneas de registro siguen un patrón similar a esto
```bash
May 27 11:45:40 ubutu.local ticky: INFO: Created ticket [#1234] (username)
Jun 1 11:06:48 ubutu.local ticky: ERROR: Connection to DB failed (username)
```
- Cuando el servicio se ejecuta correctamente, ​registra un mensaje de información en syslog, ​indicando lo que ha hecho, ​el nombre de usuario y el número de ticket relacionado con el evento
- Si el servicio encuentra un problema, ​inicia sesión en el mensaje de error en el syslog, ​indicando qué estaba mal y el ​nombre de usuario que desencadenó la acción ​que causó el problema.
- Se necesitan 2 reportes:

1. una clasificación ​de errores generados por el sistema: una lista de todos los mensajes de error registrados ​y cuántas veces se encontró cada uno de ellos, ​sin tener en cuenta los usuarios involucrados, deben ordenarse por el error más común ​al error menos común
2. una estadística de uso para el servicio: Esto significa, una lista de todos los usuarios que han utilizado el sistema ​, incluyendo cuántos mensajes de información y ​cuántos mensajes de error han generado, este informe debe ordenarse por nombre de usuario.

- Para visualizar los datos de estos informes, ​desea generar un par de páginas web que ​serán servidas por un servidor web que se ejecute en el equipo. ​Para hacer esto, puede hacer uso de un script que ​ya está en el sistema llamado csv_ to_html.py
- Este script convierte los datos de un archivo CSV ​en un archivo HTML que contiene una tabla con los datos
- A continuación, coloque los archivos en el directorio ​que utiliza el servidor web para mostrar las páginas web
- El objetivo es tener un script que pueda ​hacer todo el trabajo necesario de forma automática, ​todos los días sin ninguna interacción del usuario
- recomendamos dividir la tarea para ​que cada pieza pueda escribirse y probarse por separado

---

## Ayuda para la investigación y la planificación
- Se recomienda usar expresiones regulares para extraer la información de los registros, ya que los registros siguen un patrón específico.
- Podemos usar la web [gregx101.com](https://regex101.com/) para probar nuestras expresiones regulares y asegurarnos de que funcionan correctamente.
- para contar y ordenar la información podemos usar diccionarios y listas en Python, y luego usar la función `sorted()` para ordenar los resultados.
- Podemos tener 2 diccionarios: uno para los errores y otro para los usuarios, donde las claves serán los mensajes de error o los nombres de usuario, y los valores serán el número de ocurrencias.
- Una vez que tengamos los datos contados y ordenados, podemos escribirlos en archivos CSV usando el módulo `csv` de Python.
- Luego tenemos que pasar esos archivos CSV al script `csv_to_html.py` para generar los archivos HTML.
- Se recomienda hacer esta tarea con bash, ya que tiene una sintaxis simple y es muy útil para automatizar tareas en Linux como mover archivos.