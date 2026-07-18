# Resolución de conflictos

## Reseña: El flujo de trabajo «Pull-Merge-Push»
- Los siguientes códigos se encuentran en el vídeo de la lección:
```bash
atom all_checks.py

git add -p
git commit -m 'Rename min_absolute to min_gb, use parameter names'
git push
git pull
git log --graph --oneline --all
git log -p origin/master

atom all_checks.py
git add all_checks.py 
git commit
git push
git log --graph --oneline
```

---

## El flujo de trabajo «Pull-Merge-Push»
- ¿y si cuando vamos a impulsar nuestros cambios, ​hay nuevos cambios en el repositorio remoto?
    - `git add -p` nos permite añadir cambios de manera interactiva, es decir, podemos elegir qué cambios añadir y cuáles no.
    - `git commit -m ''` nos permite añadir un mensaje de commit a nuestros cambios.
    - `git push` En este caso falla porque hay cambios en el remoto que no tenemos en nuestra copia local. Aparece un mensaje tipo `Updates were rejected because the remote contains work that you do not have locally...`
    - `git pull` nos permite traer los cambios del remoto a nuestra copia local y fusionarlos con nuestra rama local. En este caso no fue posible hacer un auto-merge, por lo que Git nos indica que debemos resolver los conflictos de manera manual.
    - `git log --graph --oneline --all` nos permite ver un gráfico de los commits de todas las ramas, incluyendo las ramas remotas.
    - `git log -p origin/master` nos permite ver los cambios de la rama remota master del remoto origin.
    - Editamos el archivo `all_checks.py` para resolver los conflictos, recuerda eliminar las marcas de conflicto `<<<<<<<`, `=======` y `>>>>>>>`.
    - `git add all_checks.py` nos permite añadir el archivo modificado a nuestro área de preparación.
    - `git commit` nos permite crear un nuevo commit con los cambios que hemos añadido al área de preparación.
    - `git push` nos permite enviar nuestros cambios al remoto.
    - `git log --graph --oneline` nos permite ver un gráfico de los commits de nuestra rama local, incluyendo los commits que hemos traído del remoto y los commits que hemos hecho nosotros. Ahora deberíamos ver que nuestra rama local y la rama remota están sincronizadas, es decir, apuntan al mismo commit.

---

## Reseña: Envío de ramas remotas
- Los siguientes códigos se encuentran en el vídeo de la lección:
```bash
git checkout -b refactor

atom all_checks.py
./all_checks.py 

git commit -a -m 'Create wrapper function for check_disk_full'
./all_checks.py 

git commit -a -m 'Iterate over a list of checks and messages to avoid code duplication'
./all_checks.py 

git commit -a -m 'Allow printing more than one error message'
git push -u origin refactor
```

---

## Envío de ramas remotas
- Siempre es recomendado crear una nueva rama para trabajar en un nuevo feature o bugfix, de esta forma podemos mantener nuestra rama master limpia y estable.
- `git checkout -b refactor` crea una nueva rama llamada refactor y nos cambia a esa rama.
- `atom all_checks.py` abre el archivo all_checks.py en el editor de texto Atom
- `git commit -a -m ''` nos permite añadir todos los cambios en los archivos rastreados y crear un nuevo commit con un mensaje.
- `git push -u origin refactor` nos permite enviar nuestra rama local refactor al remoto origin y establecer un seguimiento entre nuestra rama local y la rama remota.
    - `git push` envía los cambios de nuestra rama local al remoto.
    - `-u` establece un seguimiento entre nuestra rama local y la rama remota, de esta forma podemos usar `git push` y `git pull` sin especificar el remoto y la rama.
    - `origin` es el nombre del remoto al que estamos enviando nuestros cambios.
    - `refactor` es el nombre de la rama remota a la que estamos enviando nuestros cambios.

---

## Revisión: Reorganizar los cambios
- Los siguientes códigos se encuentran en el vídeo de la lección:
```bash
git checkout master

git pull

git log --graph --oneline --all

git checkout refactor

git rebase master

git log --graph --oneline

git checkout master

git merge refactor

git push --delete origin refactor

git branch -d refactor

git push
```

---

## Reorganizar los cambios
- Rebasing significa cambiar la confirmación base que se usa para nuestra rama.
- Si sólo una de las ramas tiene nuevos cambios cuando tratamos de fusionarlos, ​Git será capaz de avanzar rápidamente y aplicar los cambios.
- Pero si ambas ramas tienen nuevos cambios cuando tratamos de fusionar, ​Git creará una nueva confirmación de fusión para la fusión de tres vías.
- El problema con las fusiones de tres vías es que debido al historial dividido, ​es difícil para nosotros depurar cuando se encuentra un problema en nuestro código, y ​necesitamos entender dónde se introdujo el problema
- Al cambiar la base donde nuestros commits se dividen del historial de `branch`, ​podemos repetir los nuevos commits encima de la nueva base
- Esto permite a Git hacer una fusión rápida y mantener la historia lineal. 
- Cuando hagamos esto, ​Git intentará repetir nuestros commits después de la última confirmación en esa rama
- Esto funcionará automáticamente si los cambios se realizan en diferentes partes ​de los archivos, pero ​requerirá intervención manual si los cambios se realizaron en otros archivos
- `git checkout master` nos permite cambiar a la rama master.
- `git pull` nos permite traer los cambios del remoto a nuestra copia local y fusionarlos con nuestra rama local.
- `git log --graph --oneline --all` nos permite ver un gráfico de los commits de todas las ramas, incluyendo las ramas remotas.
- `git checkout refactor` nos permite cambiar a la rama refactor.
- `git rebase master` nos permite rebasar la rama actual sobre la rama master.
- `git log --graph --oneline` nos permite ver un gráfico de los commits de nuestra rama local, incluyendo los commits que hemos traído del remoto y los commits que hemos hecho nosotros.
- `git checkout master` nos permite cambiar a la rama master.
- `git merge refactor` nos permite fusionar la rama refactor con la rama master (introducir los cambios de la rama refactor en la rama master).
- `git push --delete origin refactor` nos permite eliminar la rama remota refactor del remoto origin.
- `git branch -d refactor` nos permite eliminar la rama local refactor.
- `git push` nos permite enviar nuestros cambios al remoto.

---

## Reseña: Otro ejemplo de rebasamiento
- Los siguientes códigos se encuentran en el vídeo de la lección:
```bash
atom all_checks.py
git commit -a -m 'Add a simple network connectivity check'

git fetch
git rebase origin/master

git rebase origin/master
git add health_checks.py 

git rebase --continue
git log --graph --oneline

git push
```

---

## Otro ejemplo de rebasamiento
- Un ejemplo común es ​rebasar los cambios en la rama maestra ​cuando alguien más también hizo ​cambios y queremos mantener la historia lineal.
- Esta es una ocurrencia bastante común ​cuando estás trabajando en un cambio que es pequeño ​lo suficientemente como para no necesitar una rama separada y ​tus colaboradores acaban de suceder ​para hacer un `commit` al mismo tiempo.
- `atom all_checks.py` abre el archivo all_checks.py en el editor de texto Atom.
- `git commit -a -m ''` nos permite añadir todos los cambios en los archivos rastreados y crear un nuevo commit con un mensaje.
- `git fetch` nos permite traer los cambios del remoto a nuestra copia local, pero no los fusiona con nuestra rama local.
- `git rebase origin/master` nos permite rebasar la rama actual sobre la rama master del remoto origin. En este caso, Git nos indica que hay conflictos que debemos resolver de manera manual.
- `git add health_checks.py` nos permite añadir el archivo modificado a nuestro área de preparación.
- `git rebase --continue` nos permite continuar con el rebasamiento después de resolver los conflictos.
- `git log --graph --oneline` nos permite ver un gráfico de los commits de nuestra rama local, incluyendo los commits que hemos traído del remoto y los commits que hemos hecho nosotros.
- `git push` nos permite enviar nuestros cambios al remoto.

---

## Buenas prácticas para la colaboración
- Sincroniza siempre las ramas antes de comenzar cualquier trabajo
    - Antes de crear una nueva rama, asegúrate de que tu rama local esté actualizada con la rama remota correspondiente.
    - Una vez la rama este actualizada, puedes crear una nueva rama para trabajar en tu feature o bugfix.
- Evita hacer cambios muy grandes en una sola rama
    - Si estás trabajando en un feature o bugfix que requiere muchos cambios, considera dividirlo en varias ramas más pequeñas.
    - Esto facilita la revisión de código y reduce la probabilidad de conflictos al fusionar.
- Evita mezclar cambios no relacionados en un commit
    - Cada commit debe representar un cambio lógico y coherente en el código.
    - Esto facilita la revisión de código y la identificación de problemas en el futuro.
- Si tenemos una rama para features o bugfixes, actualiza de forma constante tu rama con los cambios de la rama master
    - Esto reduce la probabilidad de conflictos al fusionar y mantiene tu rama actualizada con los últimos cambios.
- Si necesitas tener más de 1 versión activa de tu proyecto, considera usar ramas para cada versión
    - La rama principal para el desarrollo activo, y ramas separadas para cada versión estable.
- No uses rebase en ramas compartidas con otros colaboradores
    - El rebase reescribe el historial de commits, lo que puede causar problemas si otros colaboradores están trabajando en la misma rama.
    - Si necesitas rebasar, hazlo en tu rama local antes de compartirla con otros colaboradores.
- Escriba buenos mensajes de commit
    - Los mensajes de commit deben ser claros y descriptivos, indicando qué cambios se realizaron y por qué.
    - Esto facilita la revisión de código y la identificación de problemas en el futuro.
    - Recuerda que puedes agregar un parrafo adicional en el mensaje de commit para explicar más a fondo los cambios realizados.

---

## Guía de estudio: Resolución de conflictos
- En Git, los conflictos de fusión, o conflictos que se producen cuando las ramas fusionadas tienen commits que compiten entre sí, no son infrecuentes cuando se trabaja con un equipo de desarrolladores o cuando se trabaja con software de código abierto
- Consejos para resolver conflictos de fusión
    - Tras ejecutar Git merge, aparecerá un mensaje informando de que se ha producido un conflicto en el archivo.
    - Lee los mensajes de error que implican que no puedes enviar tus cambios locales a GitHub, especialmente los cambios remotos con Git pull.
    - Utiliza la línea de comandos o GitHub Desktop para empujar el cambio a tu rama en GitHub después de hacer un clon local del repositorio para todos los demás tipos de conflictos de fusión.
    - Antes de fusionar cualquier commit a la rama maestra, envíalo a un repositorio remoto para que los colaboradores puedan ver el código, probarlo e informarte de que está listo para fusionarse.
    - Utiliza el comando Git rebase para reproducir los nuevos commits sobre la nueva base y, a continuación, fusiona de nuevo la rama de características con la principal.