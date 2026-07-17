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