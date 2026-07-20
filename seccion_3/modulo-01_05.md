# Revisión módulo 1

## Resumen del Módulo 1: Introducción al control de versiones
- El flujo de trabajo que hemos examinado hasta ahora es muy simple, pero ya es útil para ​ayudándote a realizar un seguimiento de tus cambios
- Para las evaluaciones graduadas de este curso, utilizaremos la plataforma Qwiklabs online learning ​, que está impulsada por Google Cloud Console

---

## Glosario de términos
- `Commit`: Un comando para hacer ediciones a múltiples archivos y tratar esa colección de ediciones como un solo cambio
- `Commit files`: Una etapa en la que los cambios realizados en los archivos se almacenan de forma segura en una instantánea en el directorio Git
- `Commit message`: Un resumen y descripción con información contextual sobre las partes del código o configuración del cambio de commit
- `Diff`: Un comando para encontrar las diferencias entre dos archivos
- `DNS zone file`: Archivo de configuración que especifica las correspondencias entre las direcciones IP y los nombres de host de la red
- `Git`: Un sistema gratuito de control de versiones de código abierto disponible para su instalación en plataformas basadas en Unix, Windows y macOS
- `Git directory`: Una base de datos para un proyecto Git que almacena los cambios y el historial de cambios
- `Git log`: Registro que muestra los mensajes de confirmación
- `Git staging area`: Un archivo mantenido por Git que contiene toda la información sobre qué archivos y cambios van a ir en el siguiente commit
- `Modified files`: Una etapa en la que se han realizado cambios en un archivo, pero no se han almacenado o confirmado.
- `Patch`: Un comando que puede detectar que se han realizado cambios en el archivo y hará todo lo posible para aplicar los cambios
- `Repository`: Un sistema de organización de archivos que contiene proyectos de software independientes.
- `Source Control Management (SCM)`: Una herramienta similar al VCS para almacenar código fuente
- `Staged files`: Una etapa en la que los cambios en los archivos están listos para ser comprometidos
- `Tracked`: Se registran los cambios de un archivo
- `Untracked`: Los cambios de un archivo no se registran
- `Version Control Systems (VCS)`: Herramienta que permite probar el código de forma segura antes de publicarlo, permite que varias personas colaboren juntas en el mismo proyecto y almacena el historial del código y la configuración

---

## Qwiklabs guidelines and troubleshooting steps

---

## Qwiklabs assessment: Introduction to Git
- En este escenario, eres el líder de un proyecto en una empresa de TI. Tú y tu equipo trabajan en un proyecto enorme, compuesto por múltiples funcionalidades y módulos.
- Este proyecto evoluciona constantemente, por lo que tu equipo prevé numerosas revisiones de código.
- En este laboratorio, aprenderás a usar Git, un sistema de control de versiones distribuido.
- También descubrirás cómo conectarte a una instancia de máquina virtual, instalar Git y configurar tu información de usuario.
- A continuación, crearás un repositorio Git local, añadirás un archivo al repositorio y realizarás operaciones básicas como añadir y editar archivos, y confirmar cambios (commits).
- Qué harás:
1. Crear un repositorio Git.
2. Añadir archivos a este repositorio.
3. Editar los archivos.
4. Confirmar los cambios en el repositorio.

>[!WARNING]
> Debido a problemas con la plataforma Qwiklabs, no fue posible realizar laboratorio.

---

## Ejemplo: Introducción a Git
- Antes de instalar Git en tu VM Linux, necesitas asegurarte de que tienes un índice fresco de los paquetes disponibles. Para ello, ejecuta
```bash
sudo apt update
```
- Ahora, puedes instalar Git en tu máquina Linux usando apt ejecutando el siguiente comando:
```bash
sudo apt install git
```
- En caso de que se le pregunte, continúe pulsando Y.
- Comprueba la versión instalada de Git usando el siguiente comando:
```bash
git --version
```
- Crea un directorio para almacenar tu proyecto. Para ello, utilice el siguiente comando:
```bash
mkdir my-git-repo
```
- Ahora navega al directorio que has creado.
```bash
cd my-git-repo
```
- A continuación, inicialice un nuevo repositorio utilizando el siguiente comando:
```bash
git init
```
- Git utiliza un nombre de usuario para asociar los commits con una identidad. Para ello utiliza el comando git config. Para configurar el nombre de usuario de Git usa el siguiente comando:
```bash
git config --global user.name "Name"
```
- Sustituye Nombre por tu nombre. Cualquier futura confirmación que envíes a GitHub desde la línea de comandos estará representada por este nombre. Puedes usar git config incluso para cambiar el nombre asociado a tus commits de Git. Esto sólo afectará a los commits futuros y no cambiará el nombre utilizado para los commits pasados.

Vamos a configurar tu dirección de correo electrónico para asociarla a tus commits de Git.
```bash
git config --global user.email "user@example.com"
```
- Sustituye user@example.com por tu email-id. Cualquier confirmación futura que envíes a GitHub estará asociada a esta dirección de correo electrónico. Incluso puedes utilizar git config para cambiar el correo electrónico del usuario asociado a tus commits de Git.
- Vamos a crear un archivo de texto llamado README. Para ello utilizaremos el editor nano.
- Escribe cualquier texto dentro del archivo, o puedes usar el siguiente texto:
```markdown
This is my first repository.
```
- Guarda el archivo presionando Ctrl-o, tecla Enter y Ctrl-x.
- Git es ahora consciente de los archivos en el proyecto. Podemos comprobar el estado utilizando el siguiente comando:
```bash
git status
```
- Este comando muestra el estado del árbol de trabajo. También muestra los cambios que han sido puestos en escena, los cambios que no han sido puestos en escena, y los archivos que no son seguidos por Git.
```bash
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	
    README

nothing added to commit but untracked files present (use "git add" to track)
```
- Ahora puedes ver el archivo que has creado, README, en la sección Archivos no rastreados. Git aún no está rastreando los archivos. Para rastrear los archivos, tenemos que confirmarlos añadiéndolos al área de preparación.
- Ahora vamos a añadir el archivo a la zona de preparación utilizando el siguiente comando:
```bash
git add README
```
- Este comando añade cambios desde el árbol de trabajo a la zona de preparación, es decir, recoge y prepara los archivos para Git antes de confirmarlos. En otras palabras, actualiza el índice con el contenido actual que se encuentra en el árbol de trabajo para preparar el contenido que se prepara para la siguiente confirmación.
- Ahora puedes ver el estado del árbol de trabajo usando el comando: git status. Esto muestra ahora el archivo README en verde, es decir, el archivo está ahora en el área de preparación y aún no ha sido confirmado.
```bash
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
	
    new file:   README
```
- Sin embargo, git add no afecta seriamente al repositorio porque los cambios no se registran hasta que se confirman.
- Ahora confirmemos los cambios. Un commit en Git es equivalente al término Guardar.
- Confirma los cambios usando el siguiente comando:
```bash
git commit
```
- Esto abre un editor, pidiéndote que escribas un mensaje de confirmación. Cada confirmación tiene un mensaje de confirmación asociado. Un mensaje de confirmación es un mensaje de registro del usuario describiendo los cambios.
- Introduzca el mensaje de confirmación de su elección o puede utilizar el siguiente texto:
```bash
This is my first commit!
```
- Una vez introducido el mensaje de confirmación, guárdelo pulsando Ctrl-o y la tecla Intro. Para salir pulse Ctrl-x.
- El comando git commit captura una instantánea de los cambios realizados en el proyecto, es decir, almacena el contenido actual del índice en una nueva confirmación junto con el mensaje de confirmación.
- ¡Has confirmado con éxito tu archivo!
- Ahora vamos a re-edit el archivo de nuevo para entender mejor el proceso. Abre el archivo README usando el editor nano.
```bash
nano README
```
- Ahora añada otra línea de descripción para su repositorio debajo de la línea introducida anteriormente. Añada la descripción de su elección o puede utilizar el siguiente texto:
```markdown
A repository is a location where all the files of a particular project are stored.
```
- Guarde y salga del editor pulsando Ctrl-o, tecla Enter y Ctrl-x.
- Ahora, repitamos el proceso anterior. ASÍ COMO se mencionó anteriormente, siempre puede comprobar el estado de su repositorio utilizando:
```bash
git status
```
- Para entender la diferencia, compárelo con el escenario anterior en el que añadió el nuevo fichero al repositorio.
```bash
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	
    modified:   README

no changes added to commit (use "git add" and/or "git commit -a")
```
- Git rastrea los cambios y muestra que el fichero ha sido modificado. Puede ver los cambios realizados en el archivo utilizando el siguiente comando:
```bash
git diff README
```
- Puede ver las diferencias entre el fichero antiguo y el nuevo. Las nuevas adiciones se indican con texto de color verde y un signo + al principio de la línea. Las sustituciones/eliminaciones se indican con texto en color rojo y un signo - al principio de la línea.
- Ahora, añadiremos estos cambios al área de preparación.
```bash
git add README
```
- Vea el estado del repositorio usando el siguiente comando:
```bash
git status
```
- Git muestra ahora el mismo fichero en texto de color verde. Esto significa que los cambios están listos para ser confirmados.
- Vamos a confirmar el archivo ahora introduciendo el mensaje de confirmación con el propio comando, a diferencia de la confirmación anterior.
```bash
git commit -m "This is my second commit."
```
- El comando git log muestra el historial de confirmaciones del repositorio. Muestra todos los commits del repositorio representados por un único ID de commit en la parte superior de cada commit. También muestra el autor, fecha y hora y el mensaje de confirmación asociado a las confirmaciones.
- También tiene varias opciones para limitar la salida de este comando. La salida puede filtrarse basándose en el último número de confirmaciones, autor, mensaje de confirmación, etc.

>[!NOTE]
> Se copió el contenido completo de este ejemplo de laboratorio de Qwiklabs ya que no se puedo realizar el laboratorio por problemas antes mencionados

---

## Module 1 challenge: Introduction to Git
1. What do you need to do before you install Git on your Linux VM?
> Make sure that you have a fresh index of the packages available to you.

1. Which of the following best describes Git? 
> Version control system

1. What is Git primarily used for? 
> Version control

2. What will the command mkdir my-git-repo return?
> A directory named my-git-repo

2. What is the first step to create a new repository in Git? 
> Initialize a new repository using git init

2. The git init command has several functions. Which of the following is one of them?
> To convert an existing, unversioned project to a Git repository

3. The git config command has several functions. Which of the following is one of them?
> To change the user email associated with future Git commits

3. What is the purpose of the git config command? 
> To configure global or repository-specific settings

3. What command will display changes that have been staged, changes that haven't been staged, and files that aren't tracked by Git? 
> git status

4. What does the git commit command do in Git?
> Saves the staged changes to the local repository 

4. What is the best description of a repository from the choices below? 
> A repository is a location where all the files of a particular project are stored.

5. What will the command nano README return?
> A text file named README

5. Which of the following is a way to verify that Git has been correctly installed on your machine?
> Run git --version in the terminal

6. When viewing the status of files of the project, where are the files listed that Git is not yet tracking? 
> Under “Untracked files”

6. What is the first step to install Git on a Linux machine? 
> Run sudo apt install git in the terminal

6. When viewing the status of files of the project, where are the files listed have been moved to the staging area using the git add command? 
> Under “Changes to be committed”

7. What effect does the git add command have on the repository?
> It changes the status of the repository #bad

7. What effect does the git add command have on the repository? 
> No real effect

7. What is the command for moving files to the staging area? 
> git add

8. What is the result of using the git commit command? Select all that apply
> It changes the status of the repository. #bad
> A snapshot is captured of the project's currently staged changes.
> It stores the current contents of the index in a new commit along with the commit message.

8. After you enter a commit message, how do you save that message?
> Press Ctrl-o and Enter key. 

9. What command would you use to add the commit message “Revisions complete” at the same time you enter a git commit command?
> git commit -m "Revisions complete"

9. After you have made a commit, what command can you use to look at the changes?
> git diff

10. What command will allow you to view all the commits?
> git log

10. When using the -m flag to add the commit message at the same time you enter a git commit command, what happens if multiple -m flags are given to the command?
> The first commit message is saved. #bad
> The commit message values are concatenated as separate paragraphs.