# Leyendo y escribiendo archivos CSV

## Qué es un archivo CSV?
- `Parsing`: Analizar el contenido de un archivo para estructurar correctamente los datos.
- `HTML`: Lenguaje de marcado utilizado para crear páginas web.
- `JSON`: Formato de intercambio de datos ligero y fácil de leer para humanos.
- `CSV`: Formato de archivo que almacena datos tabulares en texto plano, donde cada línea representa un registro y los valores están separados por comas.
- Un archivo CSV es similar a una hoja de cálculo, donde cada línea representa un registro y los valores están separados por comas.
- A veces es más util una csv o hoja de calculo para procesar y analizar datos.

---

## Reseña: Leyendo archivos CSV
- Los siguientes bloques de código se usarán en el próximo video:
```Python
import csv
 f = open("csv_file.txt")
 csv_f = csv.reader(f)
 for row in csv_f:
     name, phone, role = row
     print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))
f.close()
#Name: Sabrina Green, Phone: 802-867-5309, Role: System Administrator

#Name: Eli Jones, Phone: 684-3481127, Role: IT specialist

#Name: Melody Daniels, Phone: 846-687-7436, Role: Programmer

#Name: Charlie Rivera, Phone: 698-746-3357, Role: Web Developer
```

---

## Leyendo archivos CSV
- `CSV` (Comma-Separated Values), cada registros está separado por una coma y cada línea representa un registro.
- Debemos importar el módulo `csv` para poder leer archivos CSV en Python.
- Al aplicar la función `csv.reader()` a un archivo abierto, podemos iterar sobre cada línea del archivo y acceder a los valores de cada registro.
- Luego podemos descomponer cada línea en variables individuales y procesarlas según sea necesario.
- Recuerda cerrar el archivo después de leerlo para liberar recursos del sistema.

---

## Reseña: Generando archivos CSV
- Los siguientes bloques de código se usarán en el próximo video:
```Python
import csv

hosts = [["workstation.local", "192.168.25.46"],["webserver.cloud", "10.2.5.6"]]
with open('hosts.csv', 'w') as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)
```

---

## Generando archivos CSV
- Para generar un archivo CSV, debemos importar el módulo `csv` y abrir un archivo en modo escritura.
- Luego, podemos crear un objeto `writer` utilizando la función `csv.writer()`, que nos permitirá escribir filas en el archivo CSV.
- Podemos utilizar el método `writerows()` para escribir múltiples filas a la vez, pasando una lista de listas que contenga los datos que deseamos escribir.
- La variable writer es ahora ​una instancia de una clase de escritor CSV
- Hay dos funciones que podemos usar: `writerow()`, ​que escribiremos una fila a la vez; ​y `writerows()`, que escribiremos todas juntas

---

## Reseña: Leyendo y escribiendo archivos CSV con diccionarios
- Los siguientes bloques de código se usarán en el próximo video:
```Python
#the following command should be used in the terminal
cat software.csv 
#Output name,version,status,users
#MailTree,5.34,production,324
#CalDoor,1.25.1,beta,22
#Chatty Chicken,0.34,alpha,4

with open('software.csv') as software:
    reader = csv.DictReader(software)
    for row in reader:
      print(("{} has {} users").format(row["name"], row["users"]))
# output:
#MailTree has 324 users
#CalDoor has 22 users
#Chatty Chicken has 4 users
```
- Aquí el código crea una lista de diccionarios con los datos que queremos almacenar. 
- Primero definimos la lista de claves que queremos escribir en el archivo, luego abrimos el archivo para escritura. 
- A continuación, creamos el DictWriter pasando las claves que habíamos identificado previamente, y luego llamamos a dos métodos diferentes en el escritor.
- El método writeheader() creará la primera línea del CSV basándose en las claves que le pasamos, y el método writerows() convertirá la lista de diccionarios en líneas en ese archivo.

---

## Leyendo y escribiendo archivos CSV con diccionarios
- Es común que la primera línea de un archivo CSV contenga los nombres de las columnas, que se pueden usar como claves para acceder a los valores de cada registro.
- La función `csv.DictReader()` nos permite leer un archivo CSV y acceder a los valores de cada registro utilizando las claves definidas en la primera línea del archivo.
- Este lector convierte cada fila de los datos de un archivo CSV en un diccionario.
- Tambien podemos usar la función `csv.DictWriter()` para escribir datos en un archivo CSV utilizando diccionarios.
- Al crear un objeto `DictWriter`, debemos pasar una lista de claves que representen los nombres de las columnas en el archivo CSV.

```Python
users = [{"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"}, 
{"name": "Eli Jones", "username": "eli", "department": "IT support"}, 
{"name": "Melody Daniels", "username": "melody", "department": "IT development" }]

keys = ["name", "username", "department"]

with open('by_department.csv', 'w') as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)
```