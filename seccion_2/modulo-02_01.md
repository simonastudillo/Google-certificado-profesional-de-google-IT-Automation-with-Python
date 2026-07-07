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