# Solicitudes de incorporación

## Introducción al módulo 4: Colaboración
- seguiremos explorando las herramientas de colaboración disponibles en Git
- Aprenderemos sobre herramientas que nos permiten enviar cambios a proyectos de los que no somos miembros ​, ayudarnos a mejorar la calidad de nuestro código, y ​vamos a seguir mejor nuestro trabajo
- GitHub Se usa en gran medida para proyectos de código abierto
- Estos son proyectos que permiten a cualquiera usar, copiar y modificar su código. 

---

## Una sencilla solicitud de incorporación de cambios en GitHub
- `Forking`: Es una forma de copiar el repositorio de un usuario y crear una copia en nuestra cuenta de GitHub. Esto nos permite hacer cambios en el proyecto sin afectar el repositorio original o de poder enviar cambios al proyecto original.
- `Pull Request`: Es una solicitud para que el propietario del repositorio original revise y considere los cambios que hemos hecho en nuestra copia del proyecto. Si el propietario acepta los cambios, estos se incorporan al proyecto original.

---

## Reseña: El flujo de trabajo típico de las solicitudes de incorporación de cambios en GitHub
- A continuación se muestra el código utilizado en los vídeos instructivos siguientes
```bash
git clone https://github.com/redquinoa/rearrange.git

cd rearrange
ls -l

git log

git checkout -b add-readme
git atom README.md 

git add README.md
git commit -m 'Add a simple README.md file'

git push -u origin add-readme
```

---

## El flujo de trabajo habitual de las solicitudes de incorporación de cambios en GitHub
- normalmente tendremos una copia local del repositorio ​en nuestra computadora y trabajaremos ​con el repositorio bifurcado como un control remoto
- Lo primero es hacer un `fork` del repositorio original en nuestra cuenta de GitHub. Esto nos permite hacer cambios en el proyecto sin afectar el repositorio original.
- Luego hacemo un `git clone` de nuestra copia del repositorio en nuestra computadora. Esto nos permite trabajar en el proyecto localmente.
- Después de hacer cambios en nuestra copia local del proyecto, podemos enviar esos cambios a nuestra copia del repositorio en GitHub usando `git push`.
- Luego en GitHub, podemos crear una `pull request` para solicitar que el propietario del repositorio original revise y considere los cambios que hemos hecho en nuestra copia del proyecto. Si el propietario acepta los cambios, estos se incorporan al proyecto original.

---

## Revisión: Actualización de una solicitud de incorporación de cambios existente
- A continuación se muestra el código utilizado en los vídeos instructivos siguientes
```bash
atom README.md

git commit -a -m 'Add more information to the README'

git push
```

---

## Actualización de una solicitud de incorporación de cambios existente
- Cuando enviamos una solicitud de extracción, ​es bastante común recibir algunos comentarios de ​los encargados del proyecto pidiendo algunas mejoras
- Para actualizar nuestra solicitud de incorporación de cambios, simplemente hacemos los cambios solicitados en nuestra copia local del proyecto y luego enviamos esos cambios a nuestra copia del repositorio en GitHub usando `git push`. Esto actualizará automáticamente la solicitud de incorporación de cambios existente con los nuevos cambios.
- Cada vez que miramos el diff ​generado por un commit o una cadena de commits, ​GitHub mostrará un color ​diff para los cambios que hemos realizado. ​Usará verde para ​nuevas líneas y rojo para las líneas que se eliminaron. 
- ​Si sólo una parte de la línea cambia, ​resaltará esa parte específica de la línea. ​En este caso, es un nuevo archivo, ​por lo que todas las líneas son adiciones.
- Debes revisar si el proyecto tiene un archivo CONTRIBUTING.md. Este archivo contiene información sobre cómo contribuir al proyecto, incluyendo las reglas de estilo de código, las pautas para enviar solicitudes de incorporación de cambios y cualquier otra información relevante para los colaboradores.

---

## Revisión: Aprobación de cambios
- A continuación se muestra el código utilizado en los vídeos instructivos siguientes
```bash
git rebase -i master

git show
git status
git log --graph --oneline --all -4
git push
git push -f
git log --graph --oneline --all -4
```

---

## Confirmación de cambios
- no deberías reescribir el historial ​cuando se hayan publicado las confirmaciones. ​Eso se debe a que alguien más ya puede haber sincronizado ​ese repositorio con esos contenidos.
- Esta regla no se aplica con solicitudes de forks, ​ya que normalmente solo tú has clonado tu bifurcación del repositorio
- Cuando llamamos a una rebase interactiva, ​se abre un editor de texto con una lista de ​todos los commits seleccionados ​desde el más antiguo hasta el más reciente. 
- Cambiando la primera palabra de cada línea, ​podemos seleccionar lo que queremos hacer con los commits.
- ​Tenemos dos opciones para combinar commits, ​squash y fix up.
- ​En ambos casos, el contenido del `commit` seleccionado se fusiona ​en la confirmación anterior de la lista.
- ​La diferencia es lo que sucede con los mensajes de `commit`.
- ​Cuando elegimos squash, ​los mensajes de `commit` se agregan juntos y un editor ​se abre para permitirnos hacer los cambios necesarios.
- ​Cuando elegimos fix up, ​se descarta el mensaje de `commit` para esa confirmación.
- ​Después de guardar y cerrar el editor, ​Git reescribirá el historial de confirmaciones y nos permitirá continuar con la rebase.
- ​Si no hay conflictos, ​la rebase se completará y podremos enviar los cambios a nuestra bifurcación del repositorio en GitHub.
- Al intentar hacer un `push` después de una rebase, es posible que recibamos un error que nos indique que nuestro historial local está detrás del remoto. 
- En este caso, debemos usar la opción `-f` para forzar el `push` y sobrescribir el historial remoto con nuestro historial local reescrito.

---

## Guía de estudio: bifurcaciones y solicitudes de incorporación de cambios en Git
- GitHub es una plataforma de código abierto para la colaboración y el intercambio de conocimientos, que permite a los usuarios explorar el código creado por otros. 
- Las pull requests permiten informar a otros colaboradores de los cambios realizados en una rama de Git
- Al hacer pull requests, puedes discutir y evaluar los cambios propuestos antes de implementarlos en la rama principal.
- es importante tener en cuenta que antes de realizar cualquier cambio en el código original, GitHub crea una bifurcación (o una copia del proyecto), lo que permite que los cambios sean confirmados a la copia de la bifurcación, incluso si los cambios no pueden ser enviados a la otra repositorio. 
- Puede fusionar pull requests conservando las confirmaciones. A continuación se muestra una lista de opciones de fusión de pull requests que puede utilizar al fusionar pull requests.
    - Fusionar commits. Todas las confirmaciones de la rama de características se añaden a la rama base en una confirmación de fusión utilizando la opción -- no-ff.
    - Aplastar y combinar confirmaciones. Múltiples confirmaciones de una pull request son aplastadas, o combinadas en una sola confirmación, usando la opción fast-forward. Se recomienda que cuando se fusionen dos ramas, los pull requests se aplasten y fusionen para evitar la probabilidad de conflictos debido a la redundancia.
    - Mensaje de fusión para una fusión squash. GitHub genera un mensaje de confirmación por defecto, que puedes editar. Este mensaje puede incluir el título de la solicitud, su descripción o información sobre las confirmaciones.
    - Rebase y fusión de confirmaciones. Todas las confirmaciones de la rama temática se añaden a la rama base individualmente sin una confirmación de fusión.
    - Fusiones indirectas. GitHub puede fusionar una pull request automáticamente si la rama principal se fusiona directa o indirectamente en la rama base de forma externa.

---

## Test your knowledge: Pull requests
1. What is the difference between using squash and fixup when rebasing?
> Squash combines the commit messages into one. Fixup discards the new commit message.

2. What is a pull request?
> A request sent to the owner and collaborators of the target repository to pull your recent changes.

3. Under what circumstances is a new fork created?
> When you want to experiment with changes without affecting the main repository.

4. What combination of command and flags will force Git to push the current snapshot to the repo as it is, possibly resulting in permanent data loss?
> git push -f

5. When using interactive rebase, which option is the default, and takes the commits and rebases them against the branch we selected?
> pick