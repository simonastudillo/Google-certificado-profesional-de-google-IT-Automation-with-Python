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

---

## Module 4 challenge: Push local commits to Github
1. Why is it important to push your local changes to the main project? Select all that apply.
> It allows you to coordinate work with teammates.
> It helps you avoid tracking divergent lines of development.

1. Consider you have made some changes to your local copy of a Git repository. What happens to the remote repository? 
> The remote repository remains unchanged until you push your changes

2. Why is git status the first command in the process to commit your changes? 
> It shows the states of the files in your working directory and staging area.

3. What are the best practices for writing a commit message? Select all that apply.
> Include an appended line that tells GitHub which issue to close.
> Describe what the commit does and why it was made. 

3. Why is it important to include a descriptive message with each commit to a Version Control System? 
> To help other developers understand the changes

4. Which of the following can be achieved using GitHub's Pull Request feature? Select all that apply.
> Propose changes to someone else's code
> Request reviews from your peers
> Merge changes from another branch
> Preview changes before merging them

4. What is the primary purpose of a pull request in Git?
> To propose changes and initiate a discussion before merging them into a branch.

5. What is the purpose of the "Merge" button in a Git pull request on platforms like GitHub or GitLab?
> To finalize the pull request, merge the changes into the target branch, and close the pull request.

6. What is the main benefit of using pull requests in Git? 
> To propose changes, facilitate code review, and ensure quality before merging them into the target branch.

6. You have received feedback on a pull request you created and need to make changes. What is the correct method to update your pull request? 
> Push the changes to your branch and they will automatically update the pull request

7. What does a code review in GitHub involve? 
> Evaluating the quality of the code and suggesting improvements

8. You're reviewing a colleague's code on GitHub and you find a significant issue. What is the best way to provide feedback? 
> Leave a comment on the code with a respectful, constructive suggestion

9. Which of the following statements are true about the 'Request changes' option in GitHub code reviews?
> It allows you to suggest specific changes to the code

9. Why is it important to review code before merging it into the master branch?
> To find and fix potential bugs and ensure the code aligns with the project's standards

10. What happens when you fork a repository?
> A duplicate of the original repository is created in your GitHub account.

10. When forking a repository, what does the phrase “upstream repository” mean? 
> The original repository from which the fork was created

---

## IT skills in action
- vamos a poner en práctica tus conocimientos en un escenario real que engloba las lecciones que has aprendido.
- Imagina que formas parte de un equipo de TI responsable de desarrollar y gestionar un proyecto de software
- Tu equipo está utilizando Git para el control de versiones, colaborando en las tareas de codificación y asegurando el éxito del proyecto. Recorramos el proceso paso a paso.
- Pasos del proyecto
1. Antes del Control de versión: Antes de sumergirte en el código, asegúrate de que tu equipo está alineado con el alcance, los objetivos y las responsabilidades del proyecto.
2. Sistemas de control de versiones: Elija Github como su sistema de control de versiones para realizar un seguimiento de los cambios, colaborar de manera efectiva y mantener un historial de su proyecto.
3. Uso de Git: Comience por iniciar un repositorio de Github, confirmando su código inicial, y utilizando git status y git log para gestionar y realizar un seguimiento de los cambios.
4. Interacción avanzada con Git: Utiliza comandos avanzados como git diff para visualizar los cambios, git stash para ocultar temporalmente los cambios y git tag para marcar hitos significativos.
5. Deshacer cosas: Utiliza git reset y git revert para deshacer cambios y corregir errores de forma controlada.
6. Crear ramas y fusionarlas: Crea ramas para el desarrollo de características con git branch, cambia de rama con git checkout y fusiona los cambios con git merge.
7. Secure Shell y claves API: Garantizar la seguridad mediante el uso de claves SSH y la gestión de datos sensibles como claves API correctamente.
8. Resolver conflictos: Resuelve los conflictos que surgen al fusionar ramas usando git merge o pull requests.
9. Pull requests: Abre pull requests para proponer cambios, revisar código y discutir modificaciones con tu equipo.
10. Revisiones de código: Participar en revisiones de código para mantener la calidad del código, identificar mejoras y garantizar las mejores prácticas.
11. Gestión de proyectos: Organiza tu proyecto utilizando tableros de proyecto, hitos y problemas para seguir el progreso y priorizar las tareas.

- Ponerlo todo junto: Imagina que tienes que añadir una nueva funcionalidad a tu proyecto: un sistema de autenticación de usuarios. Así es como aplicarías tus habilidades:
1. Antes del control de versiones: En colaboración con el equipo de desarrollo y las partes interesadas, define el alcance y las prioridades de la función. FROM the business requirements you develop user stories from which the team can build out tasks. Revise las tareas creadas por su equipo y discuta los resultados esperados.
2. Sistemas de control de versiones: Se crea una rama para el sistema de autenticación en el repositorio existente de la aplicación, que ya se encuentra en Github. Su equipo utiliza esta nueva rama para empezar a trabajar en las tareas asociadas a la solicitud de funcionalidad. Todo el progreso se controla en tiempo real y se documenta con comentarios en Github.
3. Interacción avanzada con Git: Se utiliza Git diff para ver y comparar los cambios de código y mirar hacia atrás en la historia de los cambios. Cuando sea necesario se puede utilizar git diff para comparar ramas enteras como la característica se hace más robusto. A medida que te acercas a completar la característica, creas etiquetas para marcar los hitos del desarrollo. Cuando se acerque el lanzamiento de la característica, puedes utilizar un hito para compartir el progreso con las partes interesadas.
4. Deshacer cosas: A medida que te encuentras con problemas, tienes hitos estables que sabes que puedes restaurar. Puedes guardar los cambios pendientes o deshacerlos de forma segura utilizando los comandos de Git. utiliza el comando `git stash` para guardar temporalmente los cambios que aún no están listos para ser confirmados. Utiliza `git stash pop` para recuperar los cambios guardados cuando estés listo para continuar trabajando en ellos. 
5. Bifurcación  y fusión:  Tu equipo se asegura de seguir el ritmo de la bifurcación y la fusión de cambios. El equipo prueba sus cambios en la rama de características para evitar introducir problemas o errores en la rama principal.
6. Resolución de conflictos: Así surgen conflictos de código durante la fusión, se intenta automatizarla. Cuando surgen conflictos más profundos, se reúne al equipo y se abordan en colaboración.
7. Pull requests y revisiones de código: Uno de los miembros del equipo abre una solicitud de extracción para su rama de características. Por fin ha llegado el momento de fusionar nuestra función con la rama principal. Se ejecutan pruebas automatizadas con el código en cuestión y su equipo programa una revisión del código. Usted se prepara para recopilar y hacer un seguimiento de los comentarios.
8. Revisión del código: Todas las partes interesadas participan en las revisiones del código. Miembros del equipo se dirigen al grupo y revisan sus aportaciones al código. También se revisan las pruebas y las métricas. El equipo colabora para abordar los comentarios y garantizar un código de alta calidad.
9. Gestión de proyectos: A lo largo del proyecto, e incluso después de que hayan concluido los esfuerzos de desarrollo, se sigue haciendo un seguimiento del progreso de la función mediante tableros de proyecto, hitos y problemas. El desarrollo es iterativo y su equipo seguirá trabajando en las funciones a medida que reciba comentarios y solicitudes de las partes interesadas.
