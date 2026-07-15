# Sistemas de control de versiones

## ¿Qué es el control de versiones?
- Un sistema de control de versiones (VCS) realiza un seguimiento de los cambios que realizamos en nuestros archivos
- Nos permite recuperar versiones anteriores de nuestros archivos y ver quién modificó qué y cuándo.
- podemos editar varios archivos y tratar esa colección ​de ediciones como un solo cambio, lo que comúnmente se conoce como `commit`
- Los `commit` van acompañados de un mensaje que describe los cambios realizados, lo que nos permite entender el historial de cambios en nuestro proyecto.
- Los archivos suelen separarse en repositorios, que son contenedores de archivos y carpetas que contienen el historial de cambios de esos archivos.

---

## Control de versiones y automatización
- incluso si trabajas solo en un proyecto, el control de versiones puede ayudarte a automatizar tareas como la creación de copias de seguridad, la gestión de versiones y la colaboración con otros desarrolladores.
- Se recomienda siempre usar un VCS para cualquier proyecto de software, incluso si es un proyecto personal o de pequeña escala.
- Ejemplo: supongamos que ha almacenado el archivo de zona DNS ​para su empresa en un VCS y, en caso de que no lo recuerde, ​un archivo de zona DNS es un archivo de configuración que especifica ​las asignaciones entre direcciones IP ​y nombres de host en su red
- Cuando actualice la información de zona, ​siempre use buenos mensajes explicativos de confirmación. 
- Si comete un error, puede volver a una versión anterior del archivo de zona y restaurar la configuración correcta.

---

## ¿Qué es Git?
- Git es un VCS creado en 2005 por Linus Torvalds
- Linus lo creó originalmente para ayudar a administrar la tarea de desarrollar ​el kernel Linux
- ​Git puede funcionar como un programa independiente como servidor y como cliente. ​Esto significa que puede usar Git en una sola máquina sin siquiera tener ​una conexión de red. ​O puede usarlo como servidor en una máquina donde desea alojar su repositorio
- Los clientes Git pueden comunicarse con los servidores Git a través de la red usando HTTP, ​SSH o el propio protocolo especial de Git
- ​Puedes usarlo para proyectos pequeños con como un desarrollador o ​grandes proyectos con miles de colaboradores
- Puedes usarlo para rastrear el trabajo privado que puedes guardar para ti mismo o puedes compartir ​tu trabajo con otros alojando un código en servidores públicos como Github, Gitlab u ​otros
- Al buscar información en línea, puede notar que el sitio web oficial de Git ​se llama git-scm.com
- `SCM` significa "gestión de código fuente", que es otro término para VCS.

---

## Más información sobre Git
- [https://git-scm.com/doc](https://git-scm.com/doc)
- [https://www.mercurial-scm.org/](https://www.mercurial-scm.org/)
- [https://subversion.apache.org/](https://subversion.apache.org/)
- [https://en.wikipedia.org/wiki/Version_control](https://en.wikipedia.org/wiki/Version_control)

---

## Instalación de Git
- En la mayoría de los sistemas operativos, Git viene instalado, para saber si lo tienes instalado, abre una terminal y escribe el siguiente comando:
```bash
git --version
```
- En caso de que no lo tengas instalado, puedes descargarlo desde el sitio web oficial de Git: [https://git-scm.com/downloads](https://git-scm.com/downloads)

---

## Instalación de Git en Windows (opcional)
- Entramos a la página oficial de Git: [https://git-scm.com/downloads](https://git-scm.com/downloads)
- Descargamos el instalador para Windows y lo ejecutamos
- Aceptamos los términos, aceptamos la ubicación de instalación, luego habilitamos la opción de revisar a diario si hay actualizaciones y aceptamos
- En la siguiente ventana, dejamos las opciones por defecto y aceptamos
- Luego seleccionamos el editor de texto que queremos usar con Git, por ejemplo, Visual Studio Code y aceptamos
- Seleccionamos la opción de usar Git desde la línea de comandos agregar al PATH y aceptamos
- Seleccionamos la opción de usar OpenSSL y aceptamos
- Seleccionamos la primera opción de configuración de line ending
- Seleccionamos la opción por defecto del emulador de terminal
- No seleccionamos ninguna opción de configuración adicional y aceptamos
- Finalmente, hacemos clic en instalar y esperamos a que finalice la instalación