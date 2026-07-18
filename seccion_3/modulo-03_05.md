# Revisión módulo 3

## Resumen del módulo 3: trabajando con remotos
- Primero, hablamos de lo que GitHub es ​y cómo se ve la interacción básica ​con el servicio
- Luego discutimos cómo los repositorios remotos ​y la naturaleza distribuida de ​Git permiten a muchos colaboradores desarrollar ​un proyecto de forma independiente.
- Aprendimos cómo extraer datos ​desde repositorios remotos, ​empujar nuestros cambios locales a ellos, ​y también resolver conflictos que aparecen cuando ​nuestras sucursales locales y remotas están dessincronizadas
- El uso y la comprensión de VCS es ​una habilidad valiosa y versátil para ​cada especialista de TI y un ​que te diferenciará de la multitud

---

## Glosario de términos
- `Application Programming Interface (API) key` (Clave de Interfaz de programación de aplicaciones (API)): Es un token de autenticación que llama a una API, a la que se llama para identificar a la persona, programador o programa que intenta acceder a un sitio web
- `Computer protocols` (Protocolos informáticos): Directrices publicadas como estándares abiertos para que cualquier protocolo dado pueda implementarse en varios productos
- `Distributed` (Distribuidos): Cada desarrollador tiene una copia de todo el repositorio en su máquina local
- `GitHub` (GitHub): Un servicio de alojamiento de repositorios Git basado en la web, que permite a los usuarios compartir y acceder a repositorios en la web y copiarlos o clonarlos en un ordenador local
- `Merge` (Fusión): Operación que fusiona la rama origen/master en una rama master local
- `Private key` (Clave privada): Clave criptográfica secreta y segura que debe mantenerse confidencial y protegida y que se utiliza para descifrar los datos que se han cifrado con la clave pública correspondiente
- `Public Key` (Clave pública): Estructura criptográfica de seguridad empleada frecuentemente para establecer una comunicación segura mediante el cifrado de datos o para validar la autenticidad de una firma digital
- `Rebase` (Rebase): Se cambia el commit base que se utiliza para una rama
- `Remote branch` (Rama remota): Git utiliza ramas de sólo lectura para mantener copias de los datos almacenados en el repositorio remoto
- `Remote repositories` (Repositorios remotos): Repositorios que permiten a los desarrolladores contribuir a un proyecto desde sus propias estaciones de trabajo haciendo cambios en las copias locales del proyecto independientemente unos de otros
- `Secure Shell (SSH)` (Secure Shell (SSH)): Protocolo robusto para conectarse a servidores de forma remota
- `SSH client` (Cliente SSH): Establece una conexión con el servidor SSH, garantizando una interacción segura, en la que el cliente realiza solicitudes de acceso
- `SSH key` (Clave SSH): Una credencial de acceso
- `SSH protocol` (Protocolo SSH): Estándar utilizado habitualmente para acceder a servidores de forma remota según el principio de cifrado de clave pública
- `SSH server` (Servidor SSH): Establece conexiones de red seguras, se somete a autenticación mutua e inicia sesiones de inicio de sesión o transferencias de archivos cifradas

---

## Qwiklabs assessment: Introduction to Github
En este laboratorio, practicarás los conceptos básicos de la interacción con GitHub. Practicarás cómo configurar una cuenta, iniciar sesión, crear un repositorio, realizar cambios en tu máquina local y enviarlos al repositorio remoto. Usaremos estas operaciones de Git para compartir cambios entre el repositorio remoto y el local, y viceversa.

Qué harás:
1. Crear una cuenta de GitHub
2. Crear un repositorio de Git
3. Clonar el repositorio para crear una copia local en tu máquina
4. Añadir un archivo al repositorio
5. Crear una o varias instantáneas del repositorio local
6. Enviar las instantáneas a la rama principal (master)

---

## Ejemplar: Introducción a GitHub
En el laboratorio anterior, practicaste los conceptos básicos de la interacción con GitHub. Practicaste la configuración de una cuenta, el inicio de sesión, la creación de un repositorio, la realización de cambios en el equipo local, y el envío de cambios al repositorio remoto. Hemos utilizado estas operaciones Git para compartir los cambios desde el repositorio remoto al repositorio local y viceversa.

Este ejemplo es un recorrido por la actividad anterior de Qwiklab, incluyendo instrucciones detalladas y soluciones. Puede utilizar este ejemplo si no pudo completar el laboratorio o si necesita orientación adicional para realizar las tareas del laboratorio. También puede consultar este ejemplo para prepararse para el cuestionario calificado de este módulo.

- Creamos un repositorio en Git con nuestra cuenta de GitHub y lo clonamos en la máquina del laboratorio.
- En mi caso primero creé una clave SSH para poder conectarme a GitHub desde la máquina del laboratorio
- Añadí la clave pública a mi cuenta de GitHub y la clave privada la dejé en la máquina del laboratorio
- Luego hice un git clone del repositorio que creé en GitHub para tener una copia local en la máquina del laboratorio
- Se edita archivo README.md y se hace un commit con los cambios realizados
- Se hace un push de los cambios al repositorio remoto en GitHub
- En la segunda parte se crea un archivo llamado `example.py`
- Se guarda y se crea el commit respectivo
- Luego se crea un archivo en GitHub llamado `test.py` y se hace un commit de este archivo
- Se intenta hacer un `push origin main` desde la máquina del laboratorio, pero no se puede porque el repositorio remoto tiene cambios que no están en la copia local
- Se hace un `git pull origin main` para traer los cambios del repositorio remoto a la copia local
- Como hay conflictos de fusión, se resuelven los conflictos y se hace un commit de la resolución de los conflictos
- Luego se hace un `push origin main` para enviar los cambios de la copia local al repositorio remoto en GitHub