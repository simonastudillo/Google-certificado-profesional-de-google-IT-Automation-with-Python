# Usando un repositorio remoto

## Que es un remote
- Un remote es un repositorio remoto hace referencia a un repositorio que no se encuentra en nuestra máquina local, sino en un servidor remoto.
- Puede ser en GitHub, Bitbucket, GitLab o un servidor privado.
- Un servidor Git alojado localmente puede ejecutarse en ​casi cualquier plataforma, incluyendo Linux, ​Mac OS o Windows.
- Junto con las ramas de desarrollo locales como master, ​Git mantiene copias de los commits que se han enviado ​al repositorio remoto y branches separadas
- Si alguien ha actualizado un repositorio desde ​la última vez que sincronices tu copia local, ​Git te dirá que es hora de hacer una actualización
- Si tiene sus propios cambios locales ​cuando extrae el código del repositorio remoto, ​es posible que necesite corregir los conflictos de fusión ​antes de poder empujar sus propios cambios. 
- Git admite una variedad de formas ​de conectarse a un repositorio remoto. ​Algunos de los más comunes son el uso de los protocolos HTTP, ​HTTPS y SSH y sus correspondientes URL. 
- HTTP se utiliza generalmente ​para permitir el acceso de sólo lectura a un repositorio. ​En otras palabras, permite a las personas clonar el contenido de ​su repositorio sin dejar que le empujen nuevos contenidos. ​Por el contrario, HTTPS y SSH, ​proporcionan métodos para autenticar a los usuarios ​para que pueda controlar quién obtiene permiso para presionar.

---

## Revisión: Trabajando con remotos
- Los siguientes códigos se encuentran en el vídeo de la lección:
```bash
cd health-checks/
git remote -v

git remote show origin
git branch -r

git status
```

---

## Trabajando con remotos
- Podemos usar el comando `git remote -v` para ver los remotos configurados en nuestro repositorio local, y el comando `git remote show <remote>` para ver información detallada sobre un remoto específico.
- Por cada remoto veremos 2 URL, una para fetch y otra para push, la URL de fetch es la que se usa para traer cambios del remoto a nuestra copia local, y la URL de push es la que se usa para enviar cambios de nuestra copia local al remoto.
- Cada vez que operamos con controles remotos, Git usa ramas remotas ​para mantener copias de los datos almacenados en el repositorio remoto
- Podríamos echar un vistazo a las ramas remotas que ​nuestro repositorio de Git está rastreando actualmente ejecutando `git branch -r`. 
- Si usamos `git status` aparece algo del estilo `origin/master` que indica que nuestra rama local master está rastreando la rama remota master del remoto origin.

---

## Revisión: Trabajando con remotos
- Los siguientes códigos se encuentran en el vídeo de la lección:
```bash
cd health-checks/
git remote show origin

git fetch

git log origin/master

git status

git merge origin/master

git log
```

---

## Trabajando con remotos
- Siempre podríamos usar el sitio web de GitHub ​para navegar por los cambios que se enviaron
- Sin embargo siempre es importante saber hacerlo desde la línea de comandos, de esta forma, no importa que plataforma usemos, siempre podremos trabajar con Git desde la línea de comandos.
- `git remote show origin` nos muestra información detallada sobre el remoto origin, incluyendo las ramas remotas que está rastreando nuestra copia local.
- `git fetch` descarga los cambios del remoto origin a nuestra copia local, pero no los fusiona con nuestra rama local.
- `git log origin/master` nos permite ver los commits de la rama remota master del remoto origin.
    - Aquí podemos ver `origin/master` indica el último commit al que apunta la rama remota master del remoto origin.
    - `origin/HEAD` indica el último commit del remoto origin, y `HEAD` indica el último commit.
    - `HEAD -> master` indica el último commit al que apunta nuestra rama local master.
- `git merge origin/master` fusiona los cambios de la rama remota master del remoto origin con nuestra rama local master.