# Trabajando con remotos

## Introducción a GitHub
- En este módulo, aprenderemos un montón de ​cosas nuevas relacionadas con GitHub y los repositorios remotos
- Primero hablaremos de qué es GitHub y por qué es importante, ​y luego nos sumergiremos en cómo trabajar ​con GitHub y otros repositorios remotos
- Ser capaz de utilizar repositorios remotos ​nos permite colaborar eficazmente con los demás
- Nuestros colaboradores pueden estar sentados en las mismas oficinas que nosotros, ​o pueden estar a miles de kilómetros de distancia en ​un continente diferente trabajando a una hora diferente del día. 
- Usar un sistema de control de versión como Git nos permite ​incorporar el trabajo de diferentes personas ​sin importar dónde estén o cuándo estén trabajando

---

## Que es GitHub
- ​Distribuido significa que cada desarrollador tiene una copia de todo el repositorio ​en su máquina local
- Cada copia es un par de los demás. ​Pero podemos alojar una de estas copias en un servidor y ​luego usarla como repositorio remoto para las otras copias
- Esto nos permite sincronizar el trabajo entre copias a través de este servidor
- GitHub es un servicio de alojamiento de repositorio Git basado en la web
- Además de la funcionalidad de control de versiones de Git, ​GitHub incluye características adicionales como seguimiento de errores, wikis y administración de tareas
- Otros servicios de alojamiento de repositorios Git incluyen Bitbucket y GitLab
- GitHub proporciona acceso gratuito a un servidor Git para repositorios públicos y ​privados. ​Limita el número de colaboradores para los repositorios privados gratuitos, y ​ofrece un servicio de repositorio privado ilimitado por una cuota mensual
- Sin embargo, una palabra de precaución sobre cómo puede administrar estos repositorios. ​Si los hackers obtienen información sobre la infraestructura de TI de su organización, ​pueden usarla para intentar entrar en su red
- Así que asegúrese de tratar esta información como confidencial
- Para un trabajo real de configuración y desarrollo, debe usar un servidor Git seguro y ​privado, y limitar a las personas autorizadas a trabajar en él. 

---

## Revisión: Interacción básica con GitHub
- Los siguientes códigos se encuentran en el vídeo de la lección:
```bash
git clone https://github.com/redquinoa/health-checks.git

cd health-checks/
ls -l

git commit -a -m "Add one more line to README.md"

git push

git config --global credential.helper cache

git pull
```

---

## Interacción básica con GitHub
- creamos una cuenta, luego creamos un repositorio y lo clonamos en nuestra máquina local
- Podemos dejarlo privado o publico, adicionalmente podemos seleccionar opciones como agregar un archivo README, un archivo .gitignore y una licencia
- Usamos el comando `git clone` para crear una copia local del repositorio remoto, github solicitará nuestras credenciales de usuario y contraseña.
- Una vez que tenemos una copia local, podemos hacer cambios en los archivos y luego usar `git commit` para guardar esos cambios en nuestra copia local
- Para enviar esos cambios al repositorio remoto, usamos el comando `git push`
- Para no tener que ingresar nuestras credenciales cada vez que hacemos un push, podemos crear una clave SSH y agregarla a nuestra cuenta de GitHub, de esta forma reconoce nuestra máquina y no nos pedirá credenciales cada vez que hagamos un push
- otra opción es usar el comando `git config --global credential.helper cache` para almacenar nuestras credenciales en caché durante un tiempo determinado