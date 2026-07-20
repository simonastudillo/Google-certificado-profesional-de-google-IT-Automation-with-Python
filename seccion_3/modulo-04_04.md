#  Módulo 4 repaso

## Recapitulación del módulo 4: Colaboración
- Hemos comprobado muchas herramientas para una mejor colaboración a través de GitHub
- Miramos el flujo de trabajo típico para solicitudes de extracción, cómo actualizar y ​cambios de squash
- Aprendimos cómo las revisiones de código mejoran nuestro código ayudándonos a detectar errores, errores tipográficos y ​otros problemas

---

## Glosario de términos del curso 3, módulo 4
- `CI/CD` (CI/CD): Nombre que recibe todo el sistema de integración continua y despliegue continuo
- `Code review` (Revisiones del código): La reunión deliberada y metódica de otros programadores para examinar el código de los demás en busca de errores para aumentar la calidad del código y reduce la cantidad de errores
- `Continuous Deployment (CD)` (Despliegue continuo (DC)): El código nuevo se despliega a menudo después de haberse compilado y probado automáticamente
- `Continuous Integration (CI)` (Integración continua (IC)): Un sistema que construirá y probará automáticamente nuestro código cada vez que haya un cambio
- `Fixup` (Arreglar): La decisión de descartar los mensajes de commit para ese commit
- `Fork` (Bifurcación): Una forma de crear una copia del repositorio dado para que pertenezca a nuestro usuario
- `Indirect merges` (Fusiones indirectas): GitHub puede fusionar un pull request automáticamente si la rama de cabecera se fusiona directa o indirectamente en la rama base de forma externa
- `Bug tracker` (Seguimiento de incidencias): Un rastreador que muestra las tareas que hay que hacer, el estado en el que se encuentran y quién está trabajando en ellas
- `Merge commits` (Fusión de confirmaciones): Todos los commits de la rama de características se añaden a la rama base
- `Pipelines` (Canalizaciones): Los pasos específicos que deben ejecutarse para obtener el resultado deseado
- `Pull request` (Solicitud de extracción): Procedimiento por el que se examina el código nuevo antes de fusionarlo para crear una rama o rama maestra.
- `Squash commits` (Combinar commits): La decisión de añadir mensajes de confirmación juntos y un editor se abre para hacer los cambios necesarios

---

## Evaluación de Qwiklabs: Enviar commits locales a GitHub
Para este proyecto, necesitarás hacer un fork de un repositorio existente, corregir un error en un script, enviar tu commit a GitHub, y crear un pull request con tu commit.

Lo que harás
1. Crear otro repositorio
2. Confirmar los cambios en tu propia bifurcación y crear pull requests al repositorio original
3. Familiarízate con las revisiones de código y asegúrate de que tu corrección funciona correctamente en tu sistema antes de crear el pull request
4. Describa su pull request

---

## Ejemplo: Enviar commits locales a GitHub
- En el laboratorio anterior hicimos un fork del repositorio de [google](https://github.com/google/it-cert-automation-practice)
- Configuramos git con nuestro nombre de usuario y correo electrónico, además en mi caso agregue mi clave SSH a mi cuenta de GitHub
- Luego clonamos el repositorio a nuestra máquina local y creamos una rama improve-username-behavior
- Modificamos el script `/Course3/Lab4/validations.py`
- En primera instancia se pide agregar pruebas al script
- Se hace la modificación, se cambian los permisos al script y se ejecuta para verificar que funciona correctamente
- Falla según lo esperado, por lo que se agrega una nueva validación para que el nombre el usuario no comience con puntos ni guiones bajos
- Se ejecuta nuevamente el script y ahora funciona correctamente
- Se genera un commit indicando que se cierra el issue #1 y se hace push a la rama improve-username-behavior
- Luego en github se crea un pull request para que el propietario del repositorio original pueda revisar los cambios y fusionarlos en la rama principal

---

## Diálogo de Coach: Colaboración con Git y GitHub
