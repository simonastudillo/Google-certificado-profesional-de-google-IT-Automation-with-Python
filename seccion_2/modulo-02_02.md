# Rutas de archivo

## Rutas de archivo
- `File path` es la ubicación de un archivo en el sistema de archivos.
- `Relative file path` es la ubicación de un archivo en relación con el directorio de trabajo actual.
- `Absolute file path` es la ubicación completa de un archivo en el sistema de archivos, comenzando desde la raíz del sistema de archivos.
- Hay que evitar tanto como sea posible el uso de rutas absolutas, ya que estas pueden cambiar dependiendo del sistema operativo y la ubicación del proyecto.
- Error común: Confundir la ruta de donde se llama a un función y donde está ubicado el script que se está ejecutando.
- Por ejemplo, si se ejecuta un script desde un directorio diferente al que se encuentra el script, la ruta relativa puede no funcionar como se espera.

---

## Reseña: Cómo escribir rutas de archivo en código
- Los siguientes bloques de código se usarán en el próximo video:
```Python
#Windows file directory
C:\my-directory\target-file.txt
#Windows file directory written in Python
C:/my-directory/target-file.txt.
#Windows file directory
C:\\my-directory\\target-file.txt
#CWD command: 
os.getcwd()
#CWD command for external files:
outputs['current_directory_before'] = os.getcwd()
```

---

## Escribiendo rutas de archivo en código
- La estructura específica de la ruta del archivo depende del sistema operativo que utilices para el código.
- En Windows, las rutas de archivo utilizan barras invertidas (`\`) para separar los directorios, mientras que en macOS y Linux, se utilizan barras diagonales (`/`).
- En Python, se pueden utilizar barras diagonales (`/`) para escribir rutas de archivo, independientemente del sistema operativo, ya que Python las interpreta correctamente.
- Comando `cwd` (current working directory) devuelve la ruta del directorio de trabajo actual, que es el directorio desde el cual se ejecuta el script de Python.
- Obtener y configurar el directorio actual es solo ​una de las formas de usar rutas de archivo en Python para hacer referencia a archivos externos
- También puedes listar archivos y ​directorios para encontrar la ruta de archivo ​que necesitas usando este código `outputs['files_and_directories'] = os.listdir()`
- Tambien puedes acceder a la rutas de los archivos a través de variables de entorno: `outputs['path_env'] = os.environ.get('PATH')`
- Recuerda:
    - Piensa en las rutas de archivos como ubicaciones
    - Usa el `/` para separar directorios en rutas de archivo
    - Usa el comando `cwd` para obtener la ruta del directorio de trabajo actual y usar rutas relativas para acceder a archivos externos