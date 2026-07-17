# Ramificación y fusión

## Que es un branch?
- En Git, una rama en ​, el nivel más básico es ​solo un puntero a un commit particular.
-  representa ​una línea independiente de desarrollo en un proyecto. ​del cual el compromiso al que apunta es ​el último eslabón de una cadena de historia en desarrollo
- La rama predeterminada que Git crea para usted ​cuando un nuevo repositorio inicializado se llama main (antiguamente master).
- Puedes fusionarte de nuevo en la rama maestra, ​cuando tengas algo que te guste, ​o descartar tus cambios sin impacto negativo ​si no funcionan
- En Git, las ramas se usan todo el tiempo, ​como parte del flujo de trabajo de desarrollo normal. 
- Se recomienda siempre crear una nueva rama para cada nueva función o corrección de errores en la que esté trabajando.
- Una vez que se completa la función o corrección de errores, puede fusionar la rama de nuevo en la rama principal (main) y eliminar la rama temporal.

---

## Revisión: Creando nuevas ramas (branches)
- Los siguientes códigos se encuentran en el vídeo de la lección:
```bash
cd checks/
git branch

git branch new-feature
git branch

git checkout new-feature

git checkout -b even-better-feature
```

---

## Creando nuevas ramas (branches)
- Podemos usar el comando `git branch` para crear, editar, eliminar y listar ramas.
- `git branch <branch-name>`: Crea una nueva rama con el nombre especificado.
- `git branch`: Lista todas las ramas en el repositorio, con un asterisco (*) junto a la rama actual.
- `git checkout <branch-name>`: Cambia a la rama especificada.
- `git checkout -b <branch-name>`: Crea una nueva rama con el nombre especificado y cambia a ella inmediatamente.
- `git switch <branch-name>`: Cambia a la rama especificada.
- `git switch -c <branch-name>`: Crea una nueva rama con el nombre especificado y cambia a ella inmediatamente.
- `git log -2`: Si estamos en otra rama, podemos ver el log y notar que el último commit es diferente al de la rama principal (main). Esto se debe a que cada rama tiene su propio historial de commits, lo que permite trabajar en diferentes características o correcciones de errores de manera independiente.

>[!NOTE]
> Ya no se recomienda el uso de `git checkout` para cambiar de rama, ya que puede ser confuso.
> En su lugar se recomienda usar `git switch <branch-name>` para cambiar de rama y `git switch -c <branch-name>` para crear y cambiar a una nueva rama.

---

## Revisión: Trabajando con ramas (branches)
- Los siguientes códigos se encuentran en el vídeo de la lección:
```bash
cd checks
git status

ls -l

git checkout master
git log -2

ls -l

git branch

git branch -d new-feature 

git branch

git branch -d even-better-feature 
```

---

## Trabajando con ramas (branches)
- Recuarda que cambiar de rama cambia el contenido de tu directorio de trabajo para reflejar el estado de la rama a la que te has cambiado.
- Los archivos se cambiarán a la versión que estaba en la rama, otros se crearan y otros se eliminarán según el estado de la rama a la que te has cambiado.
- `git branch -d <branch-name>`: Elimina la rama especificada. Solo se puede eliminar una rama si no tiene cambios sin fusionar en otra rama-
- Si la rama tiene cambios sin fusionar, Git mostrará un mensaje de error y no permitirá eliminar la rama. En ese caso, puedes usar `git branch -D <branch-name>` para forzar la eliminación de la rama, pero ten en cuenta que esto puede resultar en la pérdida de cambios no fusionados.

---

## Revisión: Fusionando ramas (merging branches)
- Los siguientes códigos se encuentran en el vídeo de la lección:
```bash
git branch

git merge even-better-feature 

git log
```

---

## Fusionando ramas (merging branches)
- `Merging` es el proceso de tomar los cambios de una rama y aplicarlos a otra. En Git, esto se hace mediante el comando `git merge`.
- `git merge <branch-name>`: Fusiona la rama especificada en la rama actual. Esto aplica los cambios de la rama especificada a la rama actual, creando un nuevo commit de fusión si es necesario.
- Git tiene 2 formas de fusionar ramas: Fast-forward y Three-way merge.
- `Fast-forward merge` ocurre cuando la rama que se está fusionando es una extensión directa de la rama actual. En este caso, Git simplemente mueve el puntero de la rama actual hacia adelante para incluir los cambios de la rama fusionada.
- `Three-way merge` ocurre cuando las ramas han divergido y tienen cambios independientes. Tambien cuando se han realizado cambios en la rama actual que no están presentes en la rama que se está fusionando. En este caso, Git crea un nuevo commit de fusión que combina los cambios de ambas ramas.

---

## Revisión: Resolviendo conflictos (merge conflicts)
- Los siguientes códigos se encuentran en el vídeo de la lección:
```bash
atom free_memory.py

git commit -a -m 'Add comment to main()'

git checkout even-better-feature 

git commit -a -m 'Print everything ok'

git checkout master

git merge even-better-feature 

git status

git add free_memory.py
git status

git commit

git log --graph --oneline
```

---

## Resolviendo conflictos (merge conflicts)
- De vez en cuando, ​podríamos encontrar que ambas ramas ​que estamos tratando de fusionar ​tienen ediciones en la misma parte del mismo archivo.
- Esto dará como resultado algo llamado conflicto de fusión.
- Cuando tenemos un conflicto de fusión, Git necesitará un poco de ayuda para averiguar qué hacer.
- Al ocurrir un conflicto de fusión, Git marcará el archivo en conflicto y detendrá el proceso de fusión.
- Mostrará un mensaje de error indicando que hay un conflicto de fusión y que debemos resolverlo antes de continuar.
- Para resolver un conflicto de fusión, debemos abrir el archivo en conflicto y decidir qué cambios queremos conservar.
- Los cambios en conflicto estarán marcados con `<<<<<<<` (cambios en la rama actual), `=======` y `>>>>>>>` (cambios en la rama que se está fusionando).
- Luego agregar el archivo resuelto a la zona de preparación con `git add <archivo>` y confirmar los cambios con `git commit`.
- Tambien puedes usar `git merge --abort` para abortar el proceso de fusión y volver al estado anterior a la fusión, si decides que no quieres continuar con la fusión.

>[!NOTE]
> Debes eliminar las marcas de conflicto y hacer los cambios necesarios para resolver el conflicto. 
> Git no eliminará automáticamente las marcas de conflicto ni decidirá qué cambios conservar.

- `git log --graph --oneline`: Muestra un gráfico del historial de commits, lo que nos permite ver cómo se han fusionado las ramas y cómo se han resuelto los conflictos.
    - `--graph`: Muestra un gráfico ASCII del historial de commits, lo que nos permite ver cómo se han fusionado las ramas y cómo se han resuelto los conflictos.
    - `--oneline`: Muestra cada commit en una sola línea, lo que nos permite ver más commits en la pantalla y facilita la lectura del historial de commits.

---

## Guía de estudio: Ramas y fusiones de Git
- `git branch`: Se puede utilizar para listar, crear o eliminar sucursales.
- `git branch <name>`: Se puede utilizar para crear una nueva rama en su repositorio.
- `git branch -d <nombre>`: Se puede usar para eliminar una rama del repositorio.
- `git branch -D <nombre>`: Fuerce la eliminación de una rama.
- `git checkout <rama>`: Cambia tu rama de trabajo actual.
- `git checkout -b <nueva-rama>`: Crea una nueva rama y la convierte en tu rama de trabajo actual.
- `git merge <rama>`: Combina los cambios de una rama con los de otra.
- `git merge --abort`: Solo se puede usar después de conflictos de fusión. Este comando abortará la fusión e intentará volver al estado anterior.
- `git log --graph`: Muestra un gráfico ASCII del historial de confirmaciones y fusiones.
- `git log --oneline`: Muestra cada confirmación en una sola línea.