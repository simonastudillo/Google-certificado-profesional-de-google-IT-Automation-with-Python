# Escribiendo y leyendo archivos

## Programando con archivos
- Como especialista en ​TI, es probable que necesite manipular ​mucho archivos y directorios en una computadora
- Los sistemas de archivos generalmente se organizan en ​una estructura de árbol con directorios ​y archivos anidados bajo sus padres
- `Absolute path` es la ruta completa a un archivo o directorio desde la raíz del sistema de archivos
- `Relative path` es la ruta a un archivo o directorio desde el directorio de trabajo actual
- ​Las rutas relativas son un acceso directo que puede ​utilizar para que no tenga que escribir la ruta completa del archivo

---

## Reseña: Leyendo archivos
- Los siguientes bloques de código se usarán en el próximo video:
```Python
file = open("spider.txt")
print(file.readline())
print(file.readline())
print(file.read())
file.close()

file = open("spider.txt")
print(file.readline())
print(file.readline())
print(file.read())
file.close()
with open("spider.txt") as file:
    print(file.readline())
```
- El método readline() lee una línea del archivo y la devuelve como una cadena.
- El método read() lee el archivo completo y lo devuelve como una cadena.
- El método close() cierra el archivo.
- Finalmente, la línea que utiliza la instrucción `with` para abrir el archivo spider.txt está en modo de lectura.
- La palabra clave `as` asigna el objeto de archivo a la variable `file`.
- El bloque de código dentro de la instrucción `with` se ejecutará y, a continuación, el archivo se cerrará automáticamente.

---

## Leyendo archivos
- En la programación, trabajamos con archivos todo el tiempo.
- En el método open, estamos pasando la ruta relativa del archivo spider.txt, que está en el mismo directorio que nuestro script de Python.
- El sistema operativo busca el archivo y verifica los permisos de lectura.
- Luego nos da un `file descriptor`, que es un objeto que representa el archivo abierto.
- Este es un token generado por el sistema operativo ​que permite a los programas realizar más operaciones con el archivo
- El método readline() lee una línea del archivo y la devuelve como una cadena.
- A diferencia del método read(), que lee todo el archivo, readline() solo lee una línea a la vez.
- ​Es una buena idea cerrar los archivos ​después de haberlos abierto por algunas razones.
- ​En primer lugar, cuando un archivo está abriendo el script, el ​sistema de archivos generalmente lo bloquea y por lo tanto ningún ​otro programa o scripts ​puede usarlo hasta que haya terminado
- En segundo lugar, hay un número limitado de descriptores de archivos ​que puede crear antes de que el ​sistema de archivos se quede sin ellos
- En tercer lugar, dejar archivos abiertos colgando ​puede conducir a condiciones de carrera que ocurren ​cuando varios procesos intentan modificar y leer desde ​un recurso al mismo tiempo y pueden ​causar todo tipo de comportamientos inesperados
- Para no olvidar cerrar un archivo podemos usar la instrucción `with` para abrir un archivo. Esto asegura que el archivo se cierre automáticamente cuando el bloque de código dentro de la instrucción `with` haya terminado de ejecutarse.

---

## Reseña: Iterando sobre archivos
- Los siguientes bloques de código se usarán en el próximo video:
```Python
with open("spider.txt") as file:
    for line in file:
        print(line.upper())

with open("spider.txt") as file:
    for line in file:
        print(line.strip().upper())

# Here strip is used to remove the newline character, and we get the output without empty lines.
file = open("spider.txt")
lines = file.readlines()
file.close()
lines.sort()
print(lines)

# output:
# THE ITSY BITSY SPIDER CLIMBED UP THE WATERSPOUT.
# DOWN CAME THE RAIN
# AND WASHED THE SPIDER OUT.
# OUT CAME THE SUN
# AND DRIED UP ALL THE RAIN
# AND THE ITSY BITSY SPIDER CLIMBED UP THE SPOUT AGAIN.
```

---

## Iterando sobre archivos
- Cuando Python lee el archivo línea por línea, ​la variable de línea siempre tendrá ​un nuevo carácter de línea al final.
- Podemos usar un método de string llamado strip() para eliminar el carácter de nueva línea al final de cada línea.
- Otra forma en que podemos trabajar con el contenido del archivo ​es leer las líneas del archivo en una lista
- Para hacer eso, abrimos ​el archivo y usamos el método.readlines
- En general Python usa el caracter `\` para indicar caracteres no imprimibles, como el carácter de nueva línea (`\n`).
- Para archivos pequeños es factible usar readlines() para leer todo el archivo en memoria, pero para archivos grandes es mejor iterar sobre el archivo línea por línea.

---

## Reseña: Escribiendo archivos
- Los siguientes bloques de código se usarán en el próximo video:
```Python
with open("novel.txt", "w") as file:
    file.write("It was a dark and stormy night")
```
- La instrucción `with open()` crea un objeto de archivo y lo asigna a la variable `file`.
- La función `open()` recibe dos argumentos: el nombre del archivo y el modo.
- En este caso, el modo es `w`, que significa "escribir".
- Esto le indica a la función `open()` que cree un archivo nuevo si no existe, o que sobrescriba el archivo existente si ya existe.
- El método `write()` del objeto de archivo recibe una cadena como argumento y la escribe en el archivo. En este caso, la cadena es "It was a dark and stormy night".

---

## Escribiendo archivos
- Los archivos pueden abrirse en varios modos, esto es como un permiso sobre archivo
- El modo `r` (readonly) es el modo de lectura, que es el valor predeterminado si no se especifica ningún modo.
- El modo `w` (write) es el modo de escritura, que crea un archivo nuevo si no existe, o sobrescribe el archivo existente si ya existe.
- El modo `a` (append) es el modo de anexado, que agrega contenido al final del archivo si ya existe, o crea un archivo nuevo si no existe.
- El modo `r+` (read and write) es el modo de lectura y escritura, que permite leer y escribir en el archivo.
- Recuerda siempre revisar el modo en el que estás abriendo un archivo antes de escribir en él, para evitar sobrescribir accidentalmente un archivo existente.
- La función `write()` devuelve el número de caracteres escritos en el archivo.

---

## Guía de estudio: Leyendo y escribiendo archivos
- Abrir un archivo o un objeto similar a un archivo para leer o escribir es uno de los pasos fundamentales para un programador de Python.
- Por ejemplo, es posible que desee leer un archivo .csv y convertirlo a formato JSON. O tal vez desee seleccionar datos de una base de datos y escribirlos en un archivo de salida.
- Leer un archivo:
```Python
# mode rt = read text
with open("sample_data/declaration.txt", "rt") as textfile:
 for line in textfile:
   print(line)
```
- Escribir un archivo:
```Python
# mode wt = write text
with open("sample_data/declaration.txt", "wt") as textfile:
    textfile.write("It was a dark and stormy night")
```
- Encoding: 
    - Python distingue entre el modo binario («b») y el modo texto («t»).
    - Por defecto, los archivos se abren en modo texto, lo que significa que se leen y escriben cadenas de texto codificadas en una codificación específica.
    - Si no se especifica la codificación, la predeterminada depende de la plataforma.
    - Esto implica que se llama a `locale.getencoding()` para obtener la codificación de la configuración regional actual.
    - Si necesita abrir el texto con una codificación específica, debe especificarla.
```Python
f = open('workfile', 'w', encoding="utf-8") 
```

>[!TIP]
> Recuerda siempre cerrar un archivo después de abrirlo, para liberar recursos del sistema y evitar errores.
> El función `with` es una forma conveniente de asegurarse de que un archivo se cierre automáticamente después de que se haya terminado de usar.