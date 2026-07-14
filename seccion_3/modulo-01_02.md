# Antes del control de versiones

## Introducción al módulo 1: Control de versiones
- ​Imagina que tu equipo ha agregado una nueva funcionalidad ​a un script que examina el bienestar ​de todas las computadoras de las que eres responsable.
- La nueva verificación examina que el firmware de tu computadora, ​conocido también como UEFI, ​este actualizado a la última versión
- Cuando despliegas esto, ​de repente te das cuenta que ​la mitad de las computadoras dicen estar dañadas.
- ​Después de algunas revisiones, descubres que ​la revisión necesita tener en cuenta ​los diferentes modelos de las computadoras
- Puede que te sientas tentado a hacer un arreglo rápido del código, ​enviarlo de inmediato a las máquinas que han sido afectadas, ​especialmente si el problema parece fácil de arreglar
- Pero es más habitual que ​los arreglos rápidos incluyan errores ​porque no nos tomamos el tiempo ​para probar el nuevo código correctamente
- Podemos usar VCS para revertir el código a una versión anterior estable
- Luego podemos arreglar el código y probarlo antes de enviarlo a las computadoras afectadas

---

## Conservación de copias históricas
- Si sentías que algunas de las cosas que se eliminaron un día, ​podrían tener que añadirse más adelante. ​Así que cada vez que estabas a punto eliminar una parte significativa, ​hacías una copia de todo, por si acaso. 
- Si algo de esto te suena familiar, ya has trabajado en la forma más primitiva ​de un control de versiones, manteniendo copias históricas.
- Decimos que esto es primitivo, porque es muy manual y no muy detallado
- Primero, necesitas recordar hacer la copia.
- ​Segundo, generalmente haces una copia de todo el archivo, ​incluso si sólo estas cambiando una pequeña parte. 
- Y tercero, incluso si envías los cambios por correo a tus colegas, ​puede ser difícil averiguar al final, quién hizo qué y, lo más importante, ​por qué lo hicieron. 