# Revisión módulo 3

## Resumen del módulo 3: trabajando con remotos
- Primero, hablamos de lo que GitHub es ​y cómo se ve la interacción básica ​con el servicio
- Luego discutimos cómo los repositorios remotos ​y la naturaleza distribuida de ​Git permiten a muchos colaboradores desarrollar ​un proyecto de forma independiente.
- Aprendimos cómo extraer datos ​desde repositorios remotos, ​empujar nuestros cambios locales a ellos, ​y también resolver conflictos que aparecen cuando ​nuestras sucursales locales y remotas están dessincronizadas
- El uso y la comprensión de VCS es ​una habilidad valiosa y versátil para ​cada especialista de TI y un ​que te diferenciará de la multitud

---

## Glosario de términos
- `Application Programming Interface (API) key` (Clave de Interfaz de programación de aplicaciones (API)): Es un token de autenticación que llama a una API, a la que se llama para identificar a la persona, programador o programa que intenta acceder a un sitio web
- `Computer protocols` (Protocolos informáticos): Directrices publicadas como estándares abiertos para que cualquier protocolo dado pueda implementarse en varios productos
- `Distributed` (Distribuidos): Cada desarrollador tiene una copia de todo el repositorio en su máquina local
- `GitHub` (GitHub): Un servicio de alojamiento de repositorios Git basado en la web, que permite a los usuarios compartir y acceder a repositorios en la web y copiarlos o clonarlos en un ordenador local
- `Merge` (Fusión): Operación que fusiona la rama origen/master en una rama master local
- `Private key` (Clave privada): Clave criptográfica secreta y segura que debe mantenerse confidencial y protegida y que se utiliza para descifrar los datos que se han cifrado con la clave pública correspondiente
- `Public Key` (Clave pública): Estructura criptográfica de seguridad empleada frecuentemente para establecer una comunicación segura mediante el cifrado de datos o para validar la autenticidad de una firma digital
- `Rebase` (Rebase): Se cambia el commit base que se utiliza para una rama
- `Remote branch` (Rama remota): Git utiliza ramas de sólo lectura para mantener copias de los datos almacenados en el repositorio remoto
- `Remote repositories` (Repositorios remotos): Repositorios que permiten a los desarrolladores contribuir a un proyecto desde sus propias estaciones de trabajo haciendo cambios en las copias locales del proyecto independientemente unos de otros
- `Secure Shell (SSH)` (Secure Shell (SSH)): Protocolo robusto para conectarse a servidores de forma remota
- `SSH client` (Cliente SSH): Establece una conexión con el servidor SSH, garantizando una interacción segura, en la que el cliente realiza solicitudes de acceso
- `SSH key` (Clave SSH): Una credencial de acceso
- `SSH protocol` (Protocolo SSH): Estándar utilizado habitualmente para acceder a servidores de forma remota según el principio de cifrado de clave pública
- `SSH server` (Servidor SSH): Establece conexiones de red seguras, se somete a autenticación mutua e inicia sesiones de inicio de sesión o transferencias de archivos cifradas

---

## Qwiklabs assessment: Introduction to Github
En este laboratorio, practicarás los conceptos básicos de la interacción con GitHub. Practicarás cómo configurar una cuenta, iniciar sesión, crear un repositorio, realizar cambios en tu máquina local y enviarlos al repositorio remoto. Usaremos estas operaciones de Git para compartir cambios entre el repositorio remoto y el local, y viceversa.

Qué harás:
1. Crear una cuenta de GitHub
2. Crear un repositorio de Git
3. Clonar el repositorio para crear una copia local en tu máquina
4. Añadir un archivo al repositorio
5. Crear una o varias instantáneas del repositorio local
6. Enviar las instantáneas a la rama principal (master)

---

## Ejemplar: Introducción a GitHub
En el laboratorio anterior, practicaste los conceptos básicos de la interacción con GitHub. Practicaste la configuración de una cuenta, el inicio de sesión, la creación de un repositorio, la realización de cambios en el equipo local, y el envío de cambios al repositorio remoto. Hemos utilizado estas operaciones Git para compartir los cambios desde el repositorio remoto al repositorio local y viceversa.

Este ejemplo es un recorrido por la actividad anterior de Qwiklab, incluyendo instrucciones detalladas y soluciones. Puede utilizar este ejemplo si no pudo completar el laboratorio o si necesita orientación adicional para realizar las tareas del laboratorio. También puede consultar este ejemplo para prepararse para el cuestionario calificado de este módulo.

- Creamos un repositorio en Git con nuestra cuenta de GitHub y lo clonamos en la máquina del laboratorio.
- En mi caso primero creé una clave SSH para poder conectarme a GitHub desde la máquina del laboratorio
- Añadí la clave pública a mi cuenta de GitHub y la clave privada la dejé en la máquina del laboratorio
- Luego hice un git clone del repositorio que creé en GitHub para tener una copia local en la máquina del laboratorio
- Se edita archivo README.md y se hace un commit con los cambios realizados
- Se hace un push de los cambios al repositorio remoto en GitHub
- En la segunda parte se crea un archivo llamado `example.py`
- Se guarda y se crea el commit respectivo
- Luego se crea un archivo en GitHub llamado `test.py` y se hace un commit de este archivo
- Se intenta hacer un `push origin main` desde la máquina del laboratorio, pero no se puede porque el repositorio remoto tiene cambios que no están en la copia local
- Se hace un `git pull origin main` para traer los cambios del repositorio remoto a la copia local
- Como hay conflictos de fusión, se resuelven los conflictos y se hace un commit de la resolución de los conflictos
- Luego se hace un `push origin main` para enviar los cambios de la copia local al repositorio remoto en GitHub

---

## Module 3 challenge: Introduction to GitHub
1. Which of the following steps are involved in creating a Github account? Select all that apply
> Providing a valid email address
> Choosing a password
> Choosing a username

1. What command is used to clone a Git repository onto your local machine?
> git clone

2. If you create a private repository on Github, what will you need to clone the repo via HTTPS?
> Your Github username and your password #bad
> Your Github username and your personal access token

2. When creating a new repository on Github, what will selecting private repository access allow others to do?
> Choosing private means you choose who can see and commit to the repository. 

3. What happens when the git clone command is used? Select all that apply. 
> It initializes a .git directory. 
> It creates a new directory with the same name as the repository.
> It creates a working copy of the latest version. 

3. How can you create a Personal Access Token? 
> In the Developer settings of your Github account

4. What does the command git add do? 
> Adds content from the working directory into the staging area for the next commit

4. After you have created a local repository and a remote repository, which one should you use first for adding new content?
> Either repository #bad
> The local repository ?

4. After you set a Github username, any future commits you push to GitHub from the command line will be represented by this name. What happens if you change the name associated with your Git commits?
> This will only affect future commits and won't change the name used for past commits.

5. Which of the following commands will clone a repository named 'project' from a remote server named 'server'.?
> git clone server/project

5. What will the command git status show?
> The different states of files in your working directory and staging area

6. Git uses the term “commit”. In more common terms, how would you describe a commit?
> Git commit is like making a copy of your work. #bad
> Git commit is like saving your work. ?

6. Every commit has an associated commit message. What is a commit message?
> A log message from the user describing the changes

7. What does the command git commit do? Select all that apply.
> It stores the current contents of the index in a new commit. 
> It captures a snapshot of the project's currently staged changes. 
> It stores the commit message for this new commit.

7. Which of the following commands will create a snapshot of the current state of the repository in Git?
> git commit

8. After you have committed changes, you can push the committed changes from your local repository to a remote repository on the main branch by using which of the following commands? 
> git push origin main

8. You have added files on a remote repository, which aren’t yet present on your local repository. You need to fetch and download content from the remote repository and update the local repository to match that content. What is the command you will use?
> git pull origin main

9. Recently, you added files on a remote repository, but those files aren’t yet present on your local repository. What will happen if you try to push something from the local repository to the remote repository?
> Your attempt will return an error.

9. Recently, you added files to a remote repository, but not the local repository. Now you want to push changes from the local repository to the remote one. What do you need to do?
> Pull the current snapshot/commit in the remote repository to the local repository, update the local repository from the remote repository, then push the changes from the local repository to the remote one. 

9. Recently, you added files to a remote repository, but not the local repository. Now you want to pull these changes from the remote repository to the local one. What command do you use to pull the current snapshot/commit in the remote repository to the local repository? 
> git pull origin main

10. You can check the changes made to the local README.md file on the remote repository on 
Github . What should you select for more details related to a commit?
> The commit message. #bad
> The commit ID ?

10. What is the git pull command used for? 
> To fetch and download content from a remote repository and update the local repository to match that content.