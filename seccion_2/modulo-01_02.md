# Preparándonos para Python

## Introducción al módulo 1: Preprarándonos para Python
- Tener Python a tu alcance como ​esto te permite entender cómo ejecutar programas Python, ​cómo instalar módulos adicionales de Python, ​y cómo se integra todo
- Para poner esto en práctica a lo largo del curso, ejecutaremos scripts de Python en ​una máquina Linux remota utilizando laboratorios rápidos.

---

## Familiarizándose con el sistema operativo
- El sistema operativo es ​un software que administra ​todo lo que ocurre en la computadora.
- Lee, escribe y borra archivos del disco duro
- Controla cómo comienzan los procesos, ​cómo interactúan entre sí ​y cómo terminan eventualmente
- Gestiona cómo se ​asigna la memoria a los diferentes procesos, ​cómo se envían y reciben los paquetes de red ​y cómo cada programación puede ​acceder a los diferentes componentes de hardware
- Un sistema operativo tiene dos partes principales: ​el núcleo (Kernel) y el espacio de usuario
    - Kernel: El núcleo es el núcleo principal de un sistema operativo. ​Se comunica directamente con nuestro hardware ​y administra los recursos de nuestro sistema.
    - Espacio de usuario: El espacio de usuario es básicamente ​todo lo que está fuera del núcleo. ​Son cosas con las que interactuamos directamente, ​como los programas del sistema y la interfaz de usuario.
- ​Los principales sistemas operativos que utilizan TI en la actualidad son ​Windows, macOS y Linux
    - Windows: Windows es un sistema operativo desarrollado por Microsoft. ​Es el sistema operativo más utilizado en el mundo, ​y es muy popular entre los usuarios domésticos y las empresas.
    - macOS: macOS es un sistema operativo desarrollado por Apple. ​Es el sistema operativo que se ejecuta en las computadoras Mac, ​y es muy popular entre los diseñadores gráficos y los desarrolladores de software.
    - Linux: Linux es un sistema operativo de código abierto que se utiliza ampliamente en servidores y sistemas embebidos. ​Es muy popular entre los desarrolladores y los administradores de sistemas debido a su flexibilidad y seguridad.
- Distribuciones de linux comúnes: Ubuntu, Debian, RedHat.
- Otros sistemas operativos:
    - Chrome OS: Chrome OS es un sistema operativo desarrollado por Google, su nucleo se basa en el kernel de Linux pero es de código cerrado.
    - Android: Android es un sistema operativo basado en Linux desarrollado por Google. ​Es el sistema operativo más utilizado en dispositivos móviles, como teléfonos inteligentes y tabletas.
    - Unix: Unix es un sistema operativo desarrollado ​en los años 70 por Bell Labs. ​Después de su lanzamiento original, ​el sistema operativo pasó por un montón de ​versiones diferentes y diferentes ​compañías lanzaron variantes del mismo. 
- Las ideas fundamentales de cómo funciona Linux en la ​actualidad se basan en los principios de Unix
- Python es un lenguaje de programación que puede funcionar en cualquier sistema operativo.

---

## Preprando tu computador para Python
- Es recomendable aprender a instalar y desinstalar software en tu computadora, te permite un mayor control, confianza y seguridad sobre tu entorno de desarrollo.
- Para verificar si tienes instalado Python en tu computadora, abre una terminal y escribe el siguiente comando:
    - `python3 --version` o `python --version`
- En este curso trabajaremos con Python 3, que es la versión más reciente y recomendada de Python.
- Podemos usar módulos externos para un montón ​de tareas como generar PDFs, ​servir páginas web, crear archivos comprimidos, ​interactuar con el correo electrónico, y un montón de cosas más
- Cuando los desarrolladores escriben un módulo de Python ​que creen que otros podrían encontrar útil, ​lo publican en PyPI, ​también conocido como el Python Package Index.
- ​Podemos navegar por este repositorio de ​módulos Python para encontrar el módulo que necesitamos. 

---

## Configuración del entorno en Windows (opcional)
- Por lo general, Windows no viene con Python preinstalado, por lo que es posible que tengamos que instalarlo manualmente.
- Para instalar, se recomienda descargar la última versión de Python desde el sitio web oficial de Python (https://www.python.org/downloads/).
- Al instalar asegurate de marcar la opción "Add Python to PATH" para que puedas ejecutar Python desde la línea de comandos.
- Compryeba ejecutando el comando `python --version` en la terminal de Windows (CMD o PowerShell) para verificar que Python se haya instalado correctamente.
- Para verificar si tienes un módulo instalado, puedes usar el comando `pip show <nombre_del_módulo>`. Si el módulo está instalado, verás información sobre él; si no, no se mostrará nada.
- En caso de que no lo tengas instalado, puedes instalarlo usando el comando `pip install <nombre_del_módulo>`.
- Podemos hacer una prueba rápida para verifiar si tenemos el módulo `requests` instalado:
```Python
import requests

response = requests.get('https://www.google.com')
print(len(response.text))
```

---

## Configuración del entorno en MacOS (opcional)
- Por lo general, macOS viene con Python preinstalado, pero puede que no sea la versión más reciente. Para verificar la versión de Python instalada, abre una terminal y ejecuta el comando `python3 --version`.
- En MacOS, podemos usar Homebrew para instalar y gestionar paquetes de software o descargar desde la web
- Descargalo desde la web oficial de Python (https://www.python.org/downloads/) y sigue las instrucciones de instalación.
- Sigue las instrucciones de instalación, es posible que necesites permisos de administrador para completar la instalación.
- Para comprobar ejecuta el comando `python3 --version` en la terminal para verificar que Python se haya instalado correctamente.
- Usemos el módulo `Arrow` para verificar si tenemos el módulo instalado, ejecuta el siguiente comando `pip3 show arrow`. Si el módulo está instalado, verás información sobre él; si no, no se mostrará nada.
- Si no lo tienes instalado ejecutamos el comando `pip3 install arrow` para instalarlo.
- Comprobamos que el módulo se haya instalado correctamente ejecutando el siguiente código en la terminal:
```Python
import arrow

date = arrow.get('2024-01-01', 'YYYY-MM-DD')
date = date.shift(weeks=+6)
print(date.format('DD MM YYYY'))
```

---

## Configuración del entorno en Linux (opcional)
- Por lo general, Linux viene con Python preinstalado, pero puede que no sea la versión más reciente. Para verificar la versión de Python instalada, abre una terminal y ejecuta el comando `python3 --version`.
- En linux, podemos usar el gestor de paquetes de nuestra distribución para instalar y gestionar paquetes de software. Por ejemplo, en Ubuntu podemos usar `apt`, `yum` o `dnf` dependiendo de la distribución.
- Para instalar Python en Ubuntu, ejecuta el siguiente comando en la terminal:
```bash
sudo apt update
sudo apt install python3
```
- Usarémos el módulo `Pill` para verificar si tenemos el módulo instalado.
- Para instalarlo ejecutamos el comando `sudo apt install python3-pil`
- Comprobamos que el módulo se haya instalado correctamente ejecutando el siguiente código en la terminal:
```Python
import PIL.Image

image = PIL.Image.open('path/to/image.jpg')
print(image.size)
print(image.format)
```
- En casos de que una librería no esté disponible en el gestor de paquetes de nuestra distribución, podemos usar `pip` para instalarla.
- Instalamos `pip` en Ubuntu ejecutando el siguiente comando:
```bash
sudo apt update
sudo apt install python3-pip
```
- Usarémos el módulo `pandas` para verificar si tenemos el módulo instalado, ejecuta el siguiente comando `pip3 show pandas`. Si el módulo está instalado, verás información sobre él; si no, no se mostrará nada.
- Si no lo tienes instalado ejecutamos el comando `pip3 install pandas` para instalarlo.
- Comprobamos que el módulo se haya instalado correctamente ejecutando el siguiente código en la terminal:
```Python
import pandas
visitors = [1234, 6424, 9345, 8464, 2345]
errors = [23, 45, 33, 45, 76]
df = pandas.DataFrame({'visitors': visitors, 'errors': errors}, index=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
print(df)

df["errors"].mean()
```