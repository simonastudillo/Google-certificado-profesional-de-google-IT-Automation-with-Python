# Conceptos avanzados de bash

## Revisión: While loops en script bash
- Los siguientes bloques de código se usarán en el próximo video:
```bash
n=1
while [ $n -le 5 ]; do
  echo "Iteration number $n"
  ((n+=1))
done
Iteration number 1
Iteration number 2
Iteration number 3
Iteration number 4
Iteration number 5
```
```python
import sys
import random

value = random.randint(0, 3)
print("Returning: " + str(value))
sys.exit(value)
# Returning: 1
```
```bash
#!/bin/bash

n=0
command=$1
while ! $command && [ $n -le 5 ]; do
        sleep $n
        ((n+=1))
        echo "Retry #$n"
done;
Returning: 1
Retry #1
Returning: 3
Retry #2
Returning: 1
Retry #3
Returning: 0
```

---

## While loops en script bash
- En bash tambien se pueden crear `while loops` y `for loops`.
- podemos usar operadores de comparación para evaluar condiciones, por ejemplo:
  - `-eq` igual a
  - `-ne` diferente de
  - `-lt` menor que
  - `-le` menor o igual que
  - `-gt` mayor que
  - `-ge` mayor o igual que
- En bash usamos `$1` para acceder al primer argumento pasado a un script bash, `$2` para acceder al segundo argumento, y así sucesivamente.

---

## Revisión: For loops en script bash
- Los siguientes bloques de código se usarán en el próximo video:
```bash
cat fruits.sh
#!/bin/bash
for fruit in peach orange pear; do
    echo "I like $fruit!"
done
```
```bash 
./fruits.sh 
I like peach!
I like orange!
I like pear!
```
- El código anterior itera sobre una lista de frutas y para cada fruta, imprime un mensaje indicando que le gusta esa fruta.
```bash
cd old_website/
/old_website$ ls -l
total 0
-rw-r--r-- 1 user user 0 May 24 10:19 about.HTM
-rw-r--r-- 1 user user 0 May 24 10:20 contact.HTM
-rw-r--r-- 1 user user 0 May 24 10:20 footer.HTM
-rw-r--r-- 1 user user 0 May 24 10:20 header.HTM
-rw-r--r-- 1 user user 0 May 24 10:19 index.HTM
```
```bash
/old_website$ basename index.HTM .HTM
index
```
```bash
#!/bin/bash

for file in *.HTM; do
        name=$(basename "$file" .HTM)
        mv "$file" "$name.html" 
done
```
- Este script itera sobre todos los archivos que terminan con `.HTM` en el directorio actual, y para cada archivo, obtiene el nombre base (sin la extensión `.HTM`) y luego renombra el archivo a tener la extensión `.html`.
```bash
/old_website$ chmod +x rename.sh
/old_website$ ./rename.sh 
mv about.HTM about.html
mv contact.HTM contact.html
mv footer.HTM footer.html
mv header.HTM header.html
mv index.HTM index.html
```
```bash
/old_website$ ./rename.sh 
/old_website$
/old_website$ ls -l
-rw-r--r-- 1 user user  0 May 24 10:19 about.html
-rw-r--r-- 1 user user  0 May 24 10:20 contact.html
-rw-r--r-- 1 user user  0 May 24 10:20 footer.html
-rw-r--r-- 1 user user  0 May 24 10:20 header.html
-rw-r--r-- 1 user user  0 May 24 10:19 index.html
-rwxr-xr-x 1 user user 90 May 24 10:40 rename.sh
```

---

## For loops en script bash
- En bash enumeramos elementos de una lista usando `for loops`.
- A diferencia de Python donde podemos iterar sobre una lista de elementos, en bash iteramos sobre una lista de palabras separadas por espacios.
- `basename` es un comando que se usa para obtener el nombre base de un archivo, eliminando la ruta y la extensión del archivo.
- la linea `name=$(basename "$file" .HTM)` obtiene el nombre base del archivo `$file` eliminando la extensión `.HTM`, y lo asigna a la variable `name`.
- Es buena idea antes de ejecutar un script de cambio de nombre, permisos o similares, primero ejecutar el script con un `echo` en el comando que realiza la acción, para asegurarnos de que el script hace lo que esperamos.
- Ejemplo `echo mv "$file" "$name.html"` en lugar de `mv "$file" "$name.html"` para ver qué archivos se renombrarán antes de ejecutar el script.

---

## Revisión: Interacción avanzada de comandos
- Los siguientes bloques de código se usarán en el próximo video:
```bash
tail /var/log/syslog
May 24 10:17:01 ubuntu.local CRON[257236]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)
May 24 10:18:41 ubuntu.local rsyslogd: -- MARK --
May 24 10:25:19 ubuntu.local systemd[1]: Reloading.
```
```bash
tail /var/log/syslog | cut -d' ' -f5-
CRON[257236]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)
rsyslogd: -- MARK --
systemd[1]: Reloading.
```
```bash
cut -d' ' -f5- /var/log/syslog | sort | uniq -c | sort -nr | head
41 systemd[1]: Starting Network Manager Script Dispatcher Service...
41 systemd[1]: Started Network Manager Script Dispatcher Service.
41 systemd[1]: NetworkManager-dispatcher.service: Succeeded.
41 nm-dispatcher: req:1 'dhcp4-change' [ens3]: start running ordered scripts...
41 nm-dispatcher: req:1 'dhcp4-change' [ens3]: new request (1 scripts)
41 dhclient[757]: DHCPREQUEST for 192.168.122.103 on ens3 to 192.168.122.1 port 67 (xid=0x3a5ff7ed)
41 dhclient[757]: DHCPACK of 192.168.122.103 from 192.168.122.1 (xid=0xedf75f3a)
41 dbus-daemon[592]: [system] Successfully activated service 'org.freedesktop.nm_dispatcher'
41 dbus-daemon[592]: [system] Activating via systemd: service name='org.freedesktop.nm_dispatcher' unit='dbus-org.freedesktop.nm-dispatcher.service' requested by ':1.15' (uid=0 pid=599 comm="/usr/sbin/NetworkManager --no-daemon " label="unconfined")
9 systemd[1]: Started Run anacron jobs.
```
```bash
#!/bin/bash

for logfile in /var/log/*log; do
    echo "Processing: $logfile"
    cut -d' ' -f5- $logfile | sort | uniq -c | sort -nr | head -5
done
```
- Este script itera sobre todos los archivos de registro en el directorio `/var/log/` que terminan con `.log`, y para cada archivo, imprime los cinco mensajes más frecuentes en el archivo de registro.
```bash
Processing: /var/log/user.log
    23 system-updater[199481]: DEBUG Command exited with status: 0
    19 system-updater[46682]: DEBUG Command exited with status: 0
    16 system-updater[175060]: DEBUG Command exited with status: 0
    11 /usr/bin/lock: called by /bin/bash for . uid 0, euid 0.
    11 network-manager-dhclient-hooks: Dispatching run of '/etc/dhcp/dhclient-exit-hooks.d/hostname' ...

Processing: /var/log/Xorg.0.log

    87 Printing DDC gathered Modelines:
    87 Modeline "1920x1080"x0.0  141.00  1920 1936 1952 2104  1080 1083 1097 1116 -hsync -vsync (67.0 kHz eP)
    87 EDID vendor "AUO", prod id 5949
    78 vendor "AUO", prod id 5949
    78 DDC gathered Modelines:
```