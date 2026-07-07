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