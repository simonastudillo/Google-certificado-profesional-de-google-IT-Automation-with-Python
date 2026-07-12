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