# Revisión del módulo

## Qué es Quiklabs?
- Qwiklabs es un ​entorno de aprendizaje en línea que lo guía a través de ​escenarios reales y reales que puede ​encontrar como especialista en TI
- Qwiklabs trabaja con Google Cloud Console ​para activar y crear máquinas virtuales.
- Este software simula todo el hardware necesario ​para el sistema operativo que se ​ejecuta dentro de la máquina
- Las máquinas virtuales se han convertido en un elemento básico en muchos ​departamentos de TI, ya que nos permiten ​crear nuevas computadoras virtuales bajo demanda
- Si, por ejemplo, quieres usar ​software que solo esté disponible en un sistema operativo específico, ​es más fácil crear una máquina virtual nueva, usar ​software y, a continuación, ​eliminar la máquina virtual una vez que hayas terminado. 
- Cuando el laboratorio termine, ​Qwiklabs destruirá esta máquina virtual. ​De esta forma, cualquier CPU, memoria ​y almacenamiento que haya utilizado la máquina virtual se devuelve ​al conjunto de recursos disponibles del proveedor.

---

## Directrices y pasos para la resolución de problemas de Qwiklabs
- Cómo usar Qwiklabs

1. Acceda al laboratorio directamente a través de Coursera (no a través del catálogo de Qwiklabs). Si no accede a los laboratorios directamente a través de Coursera, no recibirá una calificación.
2. Acepte el código de honor de Coursera y haga clic en «Abrir aplicación».
3. Inicie sesión. Si es la primera vez que usa Qwiklabs, se le pedirá que cree una cuenta o inicie sesión con Google. Una vez que haya completado este paso, no tendrá que hacerlo para los siguientes laboratorios.
4. Seleccione el botón «Iniciar laboratorio» para comenzar.
5. Espere a que el laboratorio se cargue. Los laboratorios de Qwiklabs se ejecutan en un entorno interactivo en la nube y tardan un tiempo en cargarse, a menudo varios minutos. Además, puede experimentar algunas demoras cuando se inicien los entornos simulados de Linux y Windows.
6. Tenga en cuenta el tiempo asignado para el laboratorio. A menos que se indique lo contrario, tendrá 90 minutos para completar cada tarea de Qwiklabs. Si no terminas el laboratorio en el tiempo asignado, tendrás que reiniciarlo desde el principio.
7. Si te sientes cómodo/a, permite que Qwiklabs y el navegador tengan acceso de lectura al portapapeles de tu ordenador. Esto te permitirá copiar y pegar comandos del laboratorio en el entorno virtual que estás utilizando en Qwiklabs.
8. No selecciones el botón "Finalizar laboratorio" hasta que hayas completado todos los pasos y el laboratorio haya estado en ejecución durante al menos 5 minutos. De lo contrario, los laboratorios sin calificar podrían no marcarse como completados y los laboratorios calificados podrían no recibir una calificación.
9. Utiliza el navegador adecuado. Asegúrate de que tu navegador de internet esté actualizado. Qwiklabs requiere la última versión de Google Chrome, Mozilla Firefox, Safari o Microsoft Edge. Si tu navegador está desactualizado o no es compatible con Qwiklabs, podrías tener problemas. Si tu navegador está actualizado y usas uno de los navegadores mencionados anteriormente, pero sigues teniendo problemas, intenta reiniciarlo o borrar la caché y las cookies. También puedes usar el modo incógnito, que impide que tu navegador almacene cookies y otros datos temporales.
10. Utiliza una conexión a internet estable. Si tienes problemas para iniciar o completar Qwiklabs, es posible que tu conexión a internet sea demasiado lenta o inestable. Algunos indicios de una conexión inestable son que los laboratorios se congelen, dificultad para conectarse a máquinas virtuales o la imposibilidad de escribir o introducir comandos en el entorno del laboratorio.

---

## Qwiklabs assessment: Handling files
Para este laboratorio, imagina que eres un especialista en TI en una empresa mediana. El departamento de Recursos Humanos de tu empresa quiere que averigües cuántas personas hay en cada departamento. Debes escribir un script de Python que lea un archivo CSV con la lista de empleados de la organización, cuente cuántas personas hay en cada departamento y genere un informe con esta información. El resultado de este script será un archivo de texto plano. Te guiaremos paso a paso durante todo el laboratorio.
```Python
#!/usr/bin/env python3
import csv

def read_employees(csv_file_location):
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')
   
    employee_list = []
    for data in employee_file:
        employee_list.append(dict(data))
    return employee_list

def process_data(employee_list):
    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data['Department'])
    department_data = {}
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)
    return department_data

def write_report(dictionary, report_file):
    with open(report_file, "w+") as f:
        for k in sorted(dictionary):
            f.write(str(k) + ':' + str(dictionary[k]) + '\n')
        f.close()


employee_list = read_employees('/home/student/data/employees.csv')
print(employee_list)

dictionary = process_data(employee_list)
print(dictionary)

write_report(dictionary, '/home/student/test_report.txt')
```

---

## Ejemplo: Manejo de archivos
- En el laboratorio de Qwiklabs, se creo el usuario `student`
- Existían 2 directorios: `data` y `scripts`
- Debemos crear un script llamado `generate_report.py` en el directorio `scripts` que lea un archivo CSV con la lista de empleados de la organización, cuente cuántas personas hay en cada departamento y genere un informe con esta información.
- Para esto importamos el módulo `csv` y creamos 3 funciones: `read_employees()`, `process_data()` y `write_report()`.
- `read_employees()` lee el archivo CSV y devuelve una lista de diccionarios, donde cada diccionario representa un empleado.
- `process_data()` toma la lista de empleados y devuelve un diccionario donde las claves son los nombres de los departamentos y los valores son el número de empleados en cada departamento.
- `write_report()` toma el diccionario generado por `process_data()` y escribe un informe en un archivo de texto.
- Se usaron las funciones de dialecto de `csv` para manejar los espacios en blanco y asegurar que el archivo CSV se lea correctamente.
- Se utilizó el valor de retorno de la función `read_employees()` para obtener la lista de empleados, luego se pasó esa lista a `process_data()` para obtener el conteo de empleados por departamento, y finalmente se pasó ese diccionario a `write_report()` para generar el informe en un archivo de texto.

---

## Glosario módulo 2
- `Absolute path` (Ruta absoluta): Ruta completa al recurso en el sistema de archivos.
- `Comma separated values (CSV)` (Valores separados por comas): Formato de datos muy común que se utiliza para almacenar datos como segmentos de texto separados por comas.
- `Dialects` (Dialectos): Reglas que definen la estructura de un archivo CSV.
- `File systems` (Sistemas de archivos): Métodos y estructuras que se utilizan para organizar y controlar el almacenamiento y el acceso a los datos.
- `Mode` (Modo): Formato que controla las acciones que se pueden realizar con un archivo recién abierto.
- `Qwiklabs`: Entorno de aprendizaje en línea o máquina virtual para simular escenarios del mundo real.
- `Reader objects` (Objetos lectores): Objeto que representa un elemento o entidad dentro de una escena que necesita ser renderizado en pantalla.
- `Relative path` (Ruta relativa): Parte de una ruta que indica la ubicación del recurso en relación con el directorio de trabajo actual.
- `Virtual machine (VM)` (Máquina virtual): Ordenador simulado mediante software.
- `Writer objects` (Objetos escritores): Capacidad para escribir datos en un archivo CSV.

---

## Resumen del Módulo 2: Gestión de archivos con Python
- Comprobamos cómo leer y escribir tanto en textos como en ​archivos CSV y cómo administrar ​archivos y directorios con Python
- Tenga en cuenta que los archivos son una de ​las formas más importantes de almacenar ​y transmitir información en TI

---

## Module 2 challenge: Handling Files
1. What is a characteristic of a CSV file?
> Data in each row is separated by a special character.

2. You and your colleagues frequently work in a folder containing thousands of automatically generated files. One day you discover that you cannot write to any of the files in the folder. What is a likely cause of this?
> Someone wrote a script that used open() to write to all the files and forgot to close them.

3. On a Windows file system, C:\Users\Home\Documents\report.docx is an example of what kind of file path?
> Absolute path

4. Why is the os module useful when working in Python?
> It allows you to interact with the operating system using Python, regardless of whether that operating system is Windows, Mac, Linux, or something else.

5. What happens if you use the open() function in write mode ('w') on an existing file?
> The old contents will be deleted as soon as the file is opened.

6. Imagine you're reading a text file line by line in Python. The file contains data like names, but each name has an extra blank line appended after it. Which of the following modifications to the code would most effectively remove these extra blank lines while keeping the names intact?
> Apply the strip() method on each line before storing it in a list.

7. Imagine you're working in a terminal on a Linux system. You want to create a new directory named project_data within your current working directory. Which command achieves this?
> mkdir project_data

8. What is the primary function of the line reader = csv.DictReader(software.csv)?
> It creates a dictionary reader object to iterate over rows in the software.csv file, treating each row as a dictionary.

9. Imagine you're working in a terminal on a Linux or Unix-based system. You have a file named employees.csv and want to display its contents. Which of the following commands would achieve this?
> cat employees.csv

10. In Python's csv module, what's the primary benefit of registering a dialect like empDialect with csv.register_dialect as shown in the code snippet: csv.register_dialect('empDialect', skipinitialspace=True, strict=True)?
> It allows you to define custom parsing behavior (like removing leading spaces) for CSV files without explicitly specifying the parameters every time you use the csv module.