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