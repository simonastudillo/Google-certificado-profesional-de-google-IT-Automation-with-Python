# Solicitudes de incorporación

## Introducción al módulo 4: Colaboración
- seguiremos explorando las herramientas de colaboración disponibles en Git
- Aprenderemos sobre herramientas que nos permiten enviar cambios a proyectos de los que no somos miembros ​, ayudarnos a mejorar la calidad de nuestro código, y ​vamos a seguir mejor nuestro trabajo
- GitHub Se usa en gran medida para proyectos de código abierto
- Estos son proyectos que permiten a cualquiera usar, copiar y modificar su código. 

---

## Una sencilla solicitud de incorporación de cambios en GitHub
- `Forking`: Es una forma de copiar el repositorio de un usuario y crear una copia en nuestra cuenta de GitHub. Esto nos permite hacer cambios en el proyecto sin afectar el repositorio original o de poder enviar cambios al proyecto original.
- `Pull Request`: Es una solicitud para que el propietario del repositorio original revise y considere los cambios que hemos hecho en nuestra copia del proyecto. Si el propietario acepta los cambios, estos se incorporan al proyecto original.

---

## Reseña: El flujo de trabajo típico de las solicitudes de incorporación de cambios en GitHub
- A continuación se muestra el código utilizado en los vídeos instructivos siguientes
```bash
git clone https://github.com/redquinoa/rearrange.git

cd rearrange
ls -l

git log

git checkout -b add-readme
git atom README.md 

git add README.md
git commit -m 'Add a simple README.md file'

git push -u origin add-readme
```

---

## El flujo de trabajo habitual de las solicitudes de incorporación de cambios en GitHub
- normalmente tendremos una copia local del repositorio ​en nuestra computadora y trabajaremos ​con el repositorio bifurcado como un control remoto
- Lo primero es hacer un `fork` del repositorio original en nuestra cuenta de GitHub. Esto nos permite hacer cambios en el proyecto sin afectar el repositorio original.
- Luego hacemo un `git clone` de nuestra copia del repositorio en nuestra computadora. Esto nos permite trabajar en el proyecto localmente.
- Después de hacer cambios en nuestra copia local del proyecto, podemos enviar esos cambios a nuestra copia del repositorio en GitHub usando `git push`.
- Luego en GitHub, podemos crear una `pull request` para solicitar que el propietario del repositorio original revise y considere los cambios que hemos hecho en nuestra copia del proyecto. Si el propietario acepta los cambios, estos se incorporan al proyecto original.