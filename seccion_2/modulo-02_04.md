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