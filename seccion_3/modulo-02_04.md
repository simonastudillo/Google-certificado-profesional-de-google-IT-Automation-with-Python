# Revisión módulo 2

## Resumen del módulo 2: Uso de Git localmente
- Aprendimos sobre cómo interactuar con Git.
- ​Comenzamos con algunos comandos avanzados, ​como omitir el `staging area`, obtener información adicional sobre nuestros `commit`, y ​poder eliminar y renombrar archivos en nuestro repositorio
- Después de eso, nos adentramos en uno de los principales conceptos de control de versiones, ​la capacidad de deshacer las cosas
- Finalmente vimos el uso de ramas, que nos permite trabajar en diferentes características o correcciones de errores de manera independiente, sin afectar el código principal del proyecto

---

## Glosario de términos
- Branch: Un puntero a una confirmación específica, que representa una línea de desarrollo independiente en un proyecto.
- Commit ID: Un identificador junto a la palabra "confirmación" en el registro.
- Fast-forward merge: Una fusión en la que todas las confirmaciones de la rama seleccionada también se encuentran en la rama que se está fusionando.
- Head: Indica la parte superior de la rama que se está utilizando.
- Master: La rama predeterminada que Git crea al inicializar un nuevo repositorio; se usa comúnmente para colocar las partes aprobadas de un proyecto.
- Merge conflict: Ocurre cuando se realizan cambios en la misma parte del mismo archivo y Git no sabe cómo fusionarlos.
- Rollback: El proceso de revertir los cambios realizados en el software a un estado anterior.
- Three-way merge: Una fusión en la que se toman instantáneas de las puntas de las dos ramas con el ancestro común más reciente, la confirmación anterior a la divergencia.

---

## Qwiklabs assessment: Merge branches in Git
En este laboratorio, usarás tus conocimientos de Git y el historial de commits para clonar un repositorio existente y realizar algunos cambios. También pondrás a prueba lo aprendido sobre cómo revertir commits después de cambios erróneos para corregir un script en el repositorio y ejecutarlo para obtener el resultado correcto.

Qué harás:
1. Verificar el estado y el historial de un repositorio Git existente
2. Crear una rama
3. Modificar el contenido de la rama
4. Revertir los cambios
5. Fusionar la rama

---

## Ejemplo: Fusión de ramas en Git
- Ejemplo del laboratorio de Qwiklabs: Merge branches in Git
- Se detecta error en el script `food_question.py`.
- Usamos comando como `git log`, `git status` y `git branch` para conocer el estado del repositorio y la rama en la que estamos trabajando.
- Antes de trabajar configuramos nuestro nombre de usuario y correo electrónico con los comandos `git config user.name "Your Name"` y `git config user.email "email"`
- Creamos la rama `improve-output` y nos cambiamos a ella con el comando `git checkout -b improve-output`
- Modificamos el script `food_count.py` para agregar un print adicional, lo ejecutamos para verificar su funcionamiento
- Agregamos los cambios al área de preparación con `git add food_count.py` y realizamos un commit con `git commit -m `
- Usamos `git log` para detectar en que commit se encuentra el error del archivo `food_question.py` y revertimos el commit con `git revert <commit-id>` para deshacer los cambios realizados en el commit incorrecto
- Ejecutamos el script `food_question.py` para verificar que el error se haya corregido
- Finalmente, nos cambiamos a la rama `master` y fusionamos la rama `improve-output` con el comando `git merge improve-output` para integrar los cambios realizados en la rama de mejora al código principal del proyecto.
- Verificamos con `git status` y `git log`
