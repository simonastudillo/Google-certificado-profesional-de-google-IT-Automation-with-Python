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