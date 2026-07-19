# Gestión de proyectos

## Gestión de la colaboración
- Aunque las herramientas como GitHub facilitan la colaboración, siempre será necesario coordinarse con los demás miembros del equipo para asegurarse de que todos estén en la misma página.
- Por ejemplo al trabajar en una refactorización, es importante que el resto del equipo sepa para que no estén trabajando en la misma parte del código al mismo tiempo. Esto puede causar conflictos y retrasos en el proyecto.
- Parte importante de esto es la documentación, tanto en el código, commit y una documentación más amplia del proyecto.
- De esta forma, los miembros del equipo pueden entender rápidamente lo que está sucediendo y cómo contribuir al proyecto.
- Si eres un mantenedor de un proyecto, es importante que entiendas cada código que se envía a tu proyecto.
- Esto es por seguridad y por facilidad de mantenimiento. Si no entiendes el código, no podrás mantenerlo ni arreglarlo si algo sale mal.
- Una herramienta útil para esto son las `issues track`.

---

## Revisión: Problemas de seguimiento
- A continuación se muestra el código utilizado en los vídeos instructivos siguientes
```bash
cd health-checks/
atom README.md

git commit -a

git push
```

---

## Problemas de seguimiento
- Los `issues trackers` son una herramienta de gestión de proyectos que nos permite crear y asignar tareas, hacer un seguimiento de los errores y las solicitudes de funciones, y mantenernos organizados.
- `Bugzilla` es un ejemplo de un `issue tracker` que se utiliza para realizar un seguimiento de los errores y las solicitudes de funciones en proyectos de software.
- `GitHub Issues` es otro ejemplo de un `issue tracker` que se utiliza para realizar un seguimiento de los errores y las solicitudes de funciones en proyectos de software.
- Se pueden crear desde la página del mismo repositorio, es importante que envíes todal información que tienes sobre como se generó el problema, incluso un paso a paso de como reproducirlo, esto ayudará a los desarrolladores a entender el problema y a encontrar una solución más rápidamente.
- `GitHub Issues` usa ids únicos para issues y pull requests, lo que permite a los desarrolladores referirse a ellos fácilmente en el código y en la documentación. Puedes indicar que un issue está relacionado con un pull request usando palabras clave como `fixes #123` o `closes #456`, lo que cerrará automáticamente el issue cuando se fusione el pull request.
- También se pueden cerrar issues desde comentarios en commit usando palabras clave como `fixes #123` o `closes #456`.

---

## Integración continua
- `Continuous Integration system (CI)` consiste en un conjunto de prácticas de desarrollo de software que requieren que los desarrolladores integren su código en un repositorio en pequeños incrementos de manera frecuente, lo que permite detectar errores rápidamente y mejorar la calidad del software. Tambien es necesaria la implementación de pruebas automatizadas para garantizar que el código funciona correctamente y no introduce errores en el sistema.
- ​Una vez que tengamos nuestro código automáticamente construido y probado, ​el siguiente paso de automatización es la `implementación continua` (`continuous deployment` o `CD`) ​que a veces se llama entrega continua.
- La implementación continua significa ​el nuevo código se implementa a menudo. ​El objetivo es evitar los lanzamientos ​con muchos cambios entre dos versiones de ​un proyecto y en su lugar hacer ​actualizaciones incrementales con solo unos pocos cambios a la vez.
- `Jenkins` es un ejemplo de una herramienta de integración continua que se utiliza para automatizar la construcción, prueba y despliegue de aplicaciones de software.
- Permite a los desarrolladores integrar su código en un repositorio compartido y ejecutar pruebas automatizadas para detectar errores rápidamente.
- `Github Actions` es otro ejemplo de una herramienta de integración continua que se utiliza para automatizar la construcción, prueba y despliegue de aplicaciones de software.
- `Pipelines` especifican los pasos que ​debe ejecutar para obtener el resultado que desea. Esto puede ser tan simple como ejecutar un script de prueba o tan complejo como compilar, probar y desplegar un proyecto completo.
- `artofacts` utilizado para describir ​cualquier archivo que se genere como parte de la canalización. Esto normalmente incluye las versiones compiladas ​del código, pero puede incluir ​otros archivos generados como PDF para ​la documentación o paquetes específicos del sistema operativo ​para una fácil instalación. 
- Así que dos cosas a recordar, primero, ​asegúrese de que las entidades autorizadas ​para los servidores de prueba no son ​las mismas entidades autorizadas ​para implementar en los servidores de producción. 
- De esta manera, si hay ​algún tipo de compromiso en el pipeline, ​su servidor de producción no se ve afectado.
- En segundo lugar, siempre tenga un plan para recuperar ​su acceso en caso de que su pipeline se vea comprometida
- Estas configuraciones se suelen escribir en un archivo de configuración de tipo YAML, que describe los pasos que se deben ejecutar y las condiciones para cada paso.

---

## Integración de Git y GitHub
- Git es una aplicación cliente/servidor desconectada.
- Esto significa que los repositorios se mantienen en un servidor y se copian a tu máquina local
- Algunas operaciones de Git, como git push o git pull, sincronizarán tu copia con el repositorio remoto.
- Integración de Git y GitHub
    - Puedes utilizar HTTPS o SSH con el cliente Git de línea de comandos para interactuar con GitHub
    - Los métodos de autenticación difieren dependiendo de si estás utilizando HTTPS o SSH.
- Autenticación HTTPS
    - Línea de comandos con HTTPS
        - Cuando hagas push a un repositorio de GitHub sobre HTTPS, o clones un repositorio privado, Git te pedirá tu nombre de usuario y contraseña de GitHub.
        - Si no quieres introducir tu nombre de usuario y contraseña cada vez, puedes almacenarlos en un archivo llamado .netrc en tu directorio home
        - Asegúrate de que el archivo no es legible por nadie más, o Git podría ignorarlo.
    - Línea de comandos HTTPS con token
        - En lugar de almacenar tu contraseña en texto plano en el archivo .netrc, puedes generar un token de acceso personal y utilizarlo en lugar de tu contraseña
        - Consulta [Gestión de tus credenciales](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)
    - Gestor de credenciales Git
        - Git Credential Manager (GCM) es una herramienta que almacena de forma segura tus contraseñas y las suministra a Git sin tu intervención
        - Funciona en Linux, macOS y Windows, y también admite la autenticación de múltiples factores.
    - Autenticación SSH
        - Para utilizar SSH con GitHub, primero debes generar un par de claves SSH en tu máquina local y agregar la clave pública a tu cuenta de GitHub
        - Una vez que hayas agregado la clave pública a tu cuenta de GitHub, puedes utilizar la clave privada para autenticarte con GitHub sin necesidad de introducir tu nombre de usuario y contraseña cada vez que hagas push o pull.

---

## Herramientas de gestión de proyectos de GitHub
- Además de servir como repositorio de tu código y de realizar un seguimiento de los cambios que se producen en él a lo largo del tiempo, GitHub también incluye herramientas que te ayudarán a gestionar tu proyecto de software.
- Proyectos de GitHub
    - GitHub Projects es una herramienta flexible para el seguimiento y la gestión del trabajo en GitHub
    - Puedes utilizar Proyectos para crear una hoja de cálculo adaptable, un tablero de tareas y una hoja de ruta que se integre con tus incidencias y pull requests
    - Con los proyectos de GitHub, puedes filtrar, ordenar y agrupar tus incidencias y pull requests, y personalizarlos para adaptarlos al flujo de trabajo de tu equipo
    - Los proyectos se pueden crear en un repositorio, y luego se les pueden añadir incidencias.
- Incidencias de GitHub
    - GitHub Issues es una parte de GitHub Projects, y proporciona una manera de realizar un seguimiento de las tareas que tienes que completar.
    - Una incidencia puede ser un error, una petición de funcionalidad o una tarea de mantenimiento (como actualizar una biblioteca a la última versión).
    - Las incidencias pueden ir acompañadas de descripciones y textos detallados, así como de capturas de pantalla y fragmentos de código. Las incidencias pueden discutirse, comentarse, asignarse a personas y etiquetarse.
- Gestión de proyectos tradicional
    - También puedes ver las incidencias abiertas en un formato de gestión de proyectos más tradicional, con estado, asignados, estimaciones y mucho más
    - Esto se hace desde la misma pestaña de proyectos, puedes generar nuevas pestañas con diferentes formatos de visualización, como por ejemplo un tablero Kanban, que te permite ver el estado de las incidencias y su progreso a lo largo del tiempo.

---

## Herramientas adicionales
- [Ética del bricolaje en código abierto](https://arp242.net/diy.html)
- [Vincular una pull request a una incidencia](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue)
- [Establecer directrices para los colaboradores del repositorio](https://help.github.com/en/articles/setting-guidelines-for-repository-contributors)
- [¿Qué es CI/CD? Explicación de la integración continua y la entrega continua](https://www.infoworld.com/article/3271126/what-is-cicd-continuous-integration-and-continuous-delivery-explained.html)
- [¿Qué es CICD? Qué es importante y cómo hacerlo bien](https://stackify.com/what-is-cicd-whats-important-and-how-to-get-it-right/)
- [Tutorial de Travis CI](https://docs.travis-ci.com/user/tutorial/)
- [Etapas de construcción](https://docs.travis-ci.com/user/build-stages/)
 