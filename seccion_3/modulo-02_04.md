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