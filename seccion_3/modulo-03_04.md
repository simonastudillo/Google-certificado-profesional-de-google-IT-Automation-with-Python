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