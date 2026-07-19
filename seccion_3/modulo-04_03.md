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