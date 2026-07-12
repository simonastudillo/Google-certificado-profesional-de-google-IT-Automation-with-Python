# scripting bash

## Revisión: Creando un script bash
- Los siguientes bloques de código se usarán en el próximo video:
```bash
#!/bin/bash
echo "Starting at: $(date)"
echo

echo "UPTIME"
uptime
echo

echo "FREE"
free
echo

echo "WHO"
who
echo

echo "Finishing at: $(date)"
```
```bash
./gather-information.sh 
Starting at: Mi 22. Mai 17:13:06 CEST 2019

UPTIME

 17:13:06 up 8 days,  1:34,  2 users,  load average: 0,00, 0,00, 0,00

FREE

              total        used        free      shared  buff/cache   available

Mem:        4037132      871336      253940       10032     2911856     2865984

Swap:       2097148        4364     2092784

WHO

user     :0           2019-05-14 15:39 (:0)

user     pts/1        2019-05-14 15:40 (192.168.122.1)

Finishing at: Mi 22. Mai 17:13:06 CEST 2019
```
```bash
#!/bin/bash

echo "Starting at: $(date)"; echo

echo "UPTIME"; uptime; echo

echo "FREE"; free; echo

echo "WHO"; who; echo

echo "Finishing at: $(date)"
```
```bash
./gather-information.sh 
Starting at: Mon 13 May 2019 02:52:11 PM CEST

UPTIME

 14:52:11 up 17 days,  2:35,  1 user,  load average: 0.70, 1.01, 1.16

FREE

              total        used        free      shared  buff/cache   available

Mem:       32912600    19966400     1003304      321672    11942896    12281516

Swap:      20250620      612352    19638268

WHO

user    tty7         2019-04-29 12:19 (:0)

Finishing at: Mon 13 May 2019 02:52:11 PM CEST
```

---

## Creando un script bash
- bash no es un lenguaje de programación, pero es un lenguaje de scripting que nos permite automatizar tareas en el sistema operativo.
- ​En su trabajo como especialista en TI, ​a veces necesita depurar un equipo que no se comporta correctamente. ​Hay muchos comandos que pueden decirle lo que está pasando allí para ​ayudarlo con su depuración
- El comando `ps` puede ayudar a ver qué procesos se están ejecutando en un sistema. El comando `df` puede ayudarlo a ver cuánto espacio en disco queda en un sistema. El comando `uptime` puede ayudarlo a ver cuánto tiempo ha estado funcionando un sistema.
- `$(date)` es un comando que devuelve la fecha y hora actuales, se pone dentro de `$()` para pasar el resultado de ese comando a la línea de comandos. En este caso, se pasa a `echo` para que se imprima en la pantalla.

---

## Revisión: Usando variables globales
- Los siguientes bloques de código se usarán en el próximo video:
```bash
example=hello
echo $example
# example=hello
```
```bash
#!/bin/bash

line="-------------------------------------------------"

echo "Starting at: $(date)"; echo $line

echo "UPTIME"; uptime; echo $line

echo "FREE"; free; echo $line

echo "WHO"; who; echo $line

echo "Finishing at: $(date)"
```
```bash
./gather-information.sh
Starting at: Mi 22. Mai 17:30:30 CEST 2019

-------------------------------------------------

UPTIME

 17:30:30 up 8 days,  1:51,  2 users,  load average: 0,00, 0,00, 0,00

-------------------------------------------------

FREE

              total        used        free      shared  buff/cache   available

Mem:        4037132      862132      444720       10032     2730280     2875336

Swap:       2097148        6156     2090992

-------------------------------------------------

WHO

user     :0           2019-05-14 15:39 (:0)

user     pts/1        2019-05-14 15:40 (192.168.122.1)

-------------------------------------------------

Finishing at: Mi 22. Mai 17:30:30 CEST 2019
```
```bash
echo *.py
# Cuando escribimos asterisco punto py [*.py], el intérprete de comandos lo convierte en una lista que contiene todos los nombres de archivo que terminan en py en el directorio actual.

echo c*
# Cuando escribimos c asterisco [c*], el intérprete de comandos lo convierte en una lista que contiene todos los nombres de archivo que comienzan con c en el directorio actual.

echo *
# Cuando escribimos asterisco [*], el intérprete de comandos lo convierte en una lista que contiene todos los nombres de archivo en el directorio actual.

echo ?????.py
# Cuando escribimos cinco signos de interrogación punto py [?????.py], el intérprete de comandos lo convierte en una lista que contiene todos los nombres de archivo que tienen cinco caracteres y terminan en py en el directorio actual.
```

---

## Usando variables globales
- establecemos ​estas variables usando el signo igual
- Cuando queremos acceder al valor de una variable en bash, ​necesitamos prefijo el nombre de la ​variable con el signo de dólar.
- ejemplo: `$example` devuelve el valor de la variable `example`.
- No se puede dejar un espacio antes o después del signo igual cuando se establece una variable. Por ejemplo, `example = hello` no funcionará, pero `example=hello` sí funcionará.
- En los script bash, tambien podemos definir variables globales que se pueden usar en cualquier parte del script.
- Por ejemplo podemos crear la variable global `line` y usarla en varias partes del script para imprimir una línea de guiones. 
- `globs` : es una forma de referirse a los patrones que se usan para hacer coincidir nombres de archivo. 
    - `*`: coincide con cualquier número de caracteres, incluidos cero caracteres.
    - `?`: coincide con un solo carácter.

---

## Revisión: Ejecutar condicionales en bash
- Los siguientes bloques de código se usarán en el próximo video:
```bash
cat check_localhost.sh 
#!/bin/bash

if grep "127\.0\.0\.1" /etc/hosts; then

	echo "Everything ok"

else

	echo "ERROR! 127.0.0.1 is not in /etc/hosts"

fi
```
```bash
./check_localhost.sh 
# 127.0.0.1	localhost
```

---

## Ejecutar condicionales en bash
- La lógica de `exit status` de 0 y 1 de un comando es utilizada por el operador if en bash
- Si el comando utilizado en el operador if devuelve un `exit status` de 0, entonces el bloque de código dentro del if se ejecutará.
- Si el comando utilizado en el operador if devuelve un `exit status` de 1, entonces el bloque de código dentro del else se ejecutará.
- En bash no es obligatorio usar sangría como en Python, sin embargo es una buena práctica usarla para mejorar la legibilidad del código.
- En bash para ejecutar un bloque de código dentro de un if, else o elif, se debe usar la palabra clave `then` después de la condición.
- Ejemplo: `if grep "127\.0\.0\.1" /etc/hosts; then` indica que si el comando `grep` devuelve un `exit status` de 0, entonces se ejecutará el bloque de código dentro del if.
- Para finalizar un bloque de código dentro de un if, else o elif, se debe usar la palabra clave `fi` al final del bloque de código.
- `test` es un comando que se puede usar para evaluar expresiones condicionales en bash.
- Ejemplo: `test -f /etc/hosts` devuelve un `exit status` de 0 si el archivo `/etc/hosts` existe, y un `exit status` de 1 si no existe.
- Ejemplo 2: Podemos usar `[]` en lugar de `test` para evaluar expresiones condicionales en bash. Por ejemplo, `[ -f /etc/hosts ]` devuelve un `exit status` de 0 si el archivo `/etc/hosts` existe, y un `exit status` de 1 si no existe.

---

## Recursos para script bash
- [https://ryanstutorials.net/bash-scripting-tutorial/](https://ryanstutorials.net/bash-scripting-tutorial/)
- [https://linuxconfig.org/bash-scripting-tutorial-for-beginners](https://linuxconfig.org/bash-scripting-tutorial-for-beginners)
- [https://www.shellscript.sh](https://www.shellscript.sh)
