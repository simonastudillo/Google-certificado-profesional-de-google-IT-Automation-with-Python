# Introducción a Git y GitHub

- Módulo 1: Introducción al control de versiones
1. [Introducción al curso](modulo-01_01.md)
2. [Antes del control de versiones](modulo-01_02.md)
3. [Sistemas de control de versiones](modulo-01_03.md)
4. [Usando Git](modulo-01_04.md)
5. [Revisión módulo 1](modulo-01_05.md)
- Módulo 2: Uso local de Git
1. [Interacción avanzado con Git](modulo-02_01.md)
2. [Deshacer cosas](modulo-02_02.md)
3. [Ramificación y fusión](modulo-02_03.md)
4. [Revisión módulo 2](modulo-02_04.md)
- Módulo 3: Trabajar con mandos a distancia
1. [Trabajando con remotos](modulo-03_01.md)
2. [Usando un repositorio remoto](modulo-03_02.md)
3. [Secure shell y API Keys](modulo-03_03.md)
4. [Resolución de conflictos](modulo-03_04.md)
5. [Revisión módulo 3](modulo-03_05.md)
- Módulo 4: Colaboración
1. [Solicitudes de incorporación](modulo-04_01.md)
2. [Revisiones de código](modulo-04_02.md)
3. [Gestión de proyectos](modulo-04_03.md)
4. [Módulo 4 repaso](modulo-04_04.md)
5. [Resumen del curso](modulo-04_05.md)

## Skills
- Integración Continua
- Gestión de la Configuración de Software
- Instalación de Software
- Seguimiento de Incidencias
- Control de Versiones
- Revisión de Código
- Control de Versiones de Software
- Software Colaborativo
- Interfaz de Línea de Comandos
- GitHub
- Git (Sistema de Control de Versiones)

## Resumen de sección

### Módulo 1: Introducción al control de versiones (5 archivos)

**Temas:** VCS (Version Control Systems), `diff` y `patch`, Git, configuración inicial (`git config`), `git init`, `git add`, `git commit`, `git status`, `git log`, working tree vs staging area vs .git directory, ciclo de vida de archivos (modified, staged, committed).

**Puntos importantes:**
- Un VCS rastrea cambios en archivos, permite revertir a versiones anteriores y facilita la colaboración.
- `diff -u` compara archivos línea por línea; `patch` aplica esos cambios a un archivo.
- `git config --global user.name` y `user.email` son necesarios antes de empezar.
- Tres estados de archivos: modified (modificado), staged (en preparación), committed (confirmado).
- `git commit` crea una instantánea con un mensaje descriptivo (resumen de ≤50 caracteres + descripción de ≤72 caracteres por línea).

**Lo más difícil:**
- Escribir mensajes de commit claros y estructurados.

### Módulo 2: Uso local de Git (4 archivos)

**Temas:** `git commit -a`, `git log -p`/`--stat`, `git show`, `git diff`/`git diff --staged`, `git add -p`, `git rm`, `git mv`, `.gitignore`, `git checkout`, `git reset HEAD`, `git commit --amend`, `git revert`, `git branch`, `git checkout -b`, `git merge`, fast-forward vs three-way merge, conflictos de fusión.

**Puntos importantes:**
- `git commit -a` omite el staging area solo para archivos ya trackeados.
- `git log -p` muestra el diff de cada commit; `git show <id>` muestra un commit específico.
- `git rm` y `git mv` eliminan y renombran archivos respectivamente, preparando el cambio automáticamente.
- `.gitignore` excluye archivos/patrones del rastreo.
- `git checkout <file>` descarta cambios sin stage; `git reset HEAD <file>` los quita del staging area.
- `git commit --amend` modifica el último commit (solo si no se ha compartido).
- `git revert <commit>` crea un nuevo commit que deshace los cambios del commit indicado.
- Ramas: `git branch` crea/listar/eliminar; `git checkout -b` crea y cambia; `git merge` fusiona.
- Fast-forward merge (historial lineal) vs three-way merge (crea commit de fusión).
- Conflictos: Git marca con `<<<<<<<`, `=======`, `>>>>>>>`; se resuelven editando, haciendo `git add` y `git commit`.

**Lo más difícil:**
- Diferenciar `git revert` (seguro para público) vs `git reset` (peligroso en compartido).
- Resolver conflictos de fusión manualmente, especialmente con archivos grandes.
- Entender fast-forward vs three-way merge y cuándo ocurre cada uno.

### Módulo 3: Trabajar con mandos a distancia (5 archivos)

**Temas:** GitHub, `git clone`, `git push`, `git pull`, `git fetch`, `git remote -v`, `git branch -r`, SSH (`ssh-keygen`, clave pública/privada), API keys, flujo pull-merge-push, `git rebase`, `git push --delete`, buenas prácticas de colaboración.

**Puntos importantes:**
- GitHub es un servicio de alojamiento de repositorios Git con características adicionales (issues, wikis, PRs).
- `git clone` crea una copia local; `git push` envía cambios; `git pull` = `git fetch` + `git merge`.
- `git remote -v` muestra las URL de fetch y push del remoto.
- SSH: `ssh-keygen -t rsa -b 2048` genera un par de claves; la pública se agrega a GitHub para autenticación sin contraseña.
- Las API keys son tokens de autenticación para servicios externos.
- `git rebase` reescribe la base de la rama para mantener un historial lineal, evitando commits de fusión.
- Buenas prácticas: sincronizar antes de trabajar, commits pequeños y atómicos, no rebaser ramas compartidas.

**Lo más difícil:**
- Entender `git rebase` vs `git merge` y cuándo usar cada uno.

### Módulo 4: Colaboración (5 archivos)

**Temas:** Forking, Pull Requests, `git rebase -i` (squash/fixup), `git push -f`, code reviews, issues trackers (Bugzilla, GitHub Issues), CI/CD (Jenkins, GitHub Actions), pipelines, artefactos, GitHub Projects.

**Puntos importantes:**
- Fork: copia de un repositorio en tu cuenta de GitHub para hacer cambios sin afectar el original.
- Pull Request: solicitud al propietario del repositorio original para revisar y fusionar cambios.
- `git rebase -i` permite squash (combinar mensajes) o fixup (descartar mensaje) de commits.
- Code review: revisión por pares para detectar errores, mejorar estilo y compartir conocimiento.
- Issues trackers: permiten crear, asignar y dar seguimiento a tareas, errores y solicitudes de funciones.
- CI/CD: integración continua (build + test automáticos) y despliegue continuo (actualizaciones incrementales frecuentes).
- GitHub Projects: tableros Kanban integrados con issues y pull requests.

**Lo más difícil:**
- Entender el flujo completo: fork → clone → rama → cambios → push → PR → review → merge.
- Usar `git rebase -i` correctamente (squash vs fixup) y forzar push (`git push -f`) con precaución.
- Diferenciar CI (pruebas automáticas) de CD (despliegue automático) y cómo se complementan.