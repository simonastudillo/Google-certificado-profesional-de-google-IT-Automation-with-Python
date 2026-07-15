# Usando Git

## Reseña: Primeros passo con Git
- Esta lectura contiene el código utilizado en los vídeos siguientes:
```bash
git config --global user.email "me@example.com"
git config --global user.name "My name"

mkdir checks
cd checks
git init

ls -la

ls -l

ls -l .git/

cp ../disk_usage.py .
ls -l

git add disk_usage.py 
git status

git commit
```

---

## Primeros pasos con Git
- Lo primero es indicar a Git quienes somos, para ello usamos los siguientes comandos:
```bash
git config --global user.email "me@example.com"
git config --global user.name "My name"
```
- Luego podemos crear un nuevo directorio para nuestro proyecto y entrar en él
- una vez dentro del directorio, podemos inicializar un nuevo repositorio Git con el comando `git init`
- Usamos el comando `ls -la` para listar todos los archivos y carpetas, incluyendo los ocultos, y podemos ver que se ha creado un nuevo directorio llamado `.git`, que contiene toda la información del repositorio
- Podemos usar el comando `ls -l .git/` para ver los archivos y carpetas dentro del directorio `.git`, y podemos ver que contiene varios archivos y carpetas que Git utiliza para rastrear los cambios en nuestro proyecto
- `Working tree` o `árbol de trabajo` es el directorio donde trabajamos con nuestros archivos y carpetas, y es donde hacemos cambios en nuestro proyecto
- `Staging area` o `área de preparación` es donde preparamos los cambios que queremos confirmar en nuestro repositorio, y es donde usamos el comando `git add` para agregar archivos a la zona de preparación
- `git status` nos permite ver el estado de nuestro repositorio, incluyendo los archivos que han sido modificados, los archivos que están en la zona de preparación y los archivos que no están siendo rastreados por Git
- `git commit` nos permite confirmar los cambios que hemos preparado en la zona de preparación, y nos pedirá que ingresemos un mensaje de confirmación que describa los cambios realizados

---

## Reseña: Tracking files
- Esta lectura contiene el código utilizado en los vídeos siguientes:
```bash
cd checks
ls -l

git status

atom disk_usage.py 
git status

git commit -m 'Add periods to the end of sentences.'

git status
```