# Revisiones de código

## ¿Qué son las revisiones de código?
- GitHub y otros servicios de alojamiento de repositorios ofrecen herramientas para ​haciendo revisiones de código en su plataforma
- Hacer una revisión de código significa revisar el código de otra persona, la documentación o la configuración ​y verificar que todo tiene sentido y ​sigue los patrones esperados
- El objetivo de una revisión de código es mejorar el proyecto asegurándose de que ​los cambios sean de alta calidad. 
- También nos ayuda a asegurarnos de que los contenidos son fáciles de entender.
- ​Que el estilo sea consistente con el proyecto general.
- ​Y que no olvidemos ningún caso importante.Las revisiones ​aumentaron el número de ojos que han comprobado el código. 
- Si estamos escribiendo documentación, nuestro revisor puede ayudarnos a detectar errores tipográficos y ​cosas que no están totalmente claras
- las revisiones de código no se trata de que seamos buenos o ​malos codificadores, se trata de mejorar nuestro código.
- Al recibir comentarios, podemos seguir mejorando nuestras técnicas de código. 

---

## El flujo de trabajo de revisión de código
- El revisor podría decir que todo está bien y que nuestros cambios son aprobados, pero ​normalmente encontrarán algo que necesita mejorar.
- ​Así que agregarán comentarios a nuestros cambios explicando lo que hay que arreglar y cómo. 
- Cuando obtengamos la revisión, los comentarios los abordarán solucionando nuestros errores tipográficos, ​agregando cualquier prueba faltante y así sucesivamente
- Después de abordar un comentario, podemos marcarlo como resuelto para que ​sepamos que ha sido atendido. 
- Si hay algo que no estamos seguros de cómo hacer o ​creemos que un enfoque diferente podría ser mejor, podemos responder al comentario y ​pedir a nuestro revisor más información sin marcar el comentario como resuelto.
- ​Una vez que todos los comentarios hayan sido resueltos y nuestro espectador esté satisfecho con los resultados, ​aprobarán el cambio y podremos fusionarlo
- Es común que las revisiones de código ​incluyan varios comentarios sobre el estilo del código. ​Para evitar un montón de ida y vuelta, es una buena idea referirse a una guía de estilo que ​explica el estilo de codificación preferido para el proyecto

---

## Reseña: Cómo realizar revisiones de código
- A continuación se muestra el código utilizado en los vídeos instructivos siguientes
```bash
atom README.md

git commit -a --amend

git status

git push -f
```

---

## Cómo realizar revisiones de código
- Basado en el mismo ejemplo del módulo anterior, se nos pide cambiar el archivo README.md para agregar más información sobre el proyecto.
- Se solicita agregar más ejemplos y cambiar de tamaño el título usando `##` en lugar de `#`.
- Recuerda que el comando `git commit -a --amend` nos permite modificar el último commit, agregando los cambios que hemos hecho en el archivo README.md.
- Después de hacer los cambios, podemos usar `git push -f` para forzar la actualización de nuestra solicitud de incorporación de cambios existente con los nuevos cambios. Esto actualizará automáticamente la solicitud de incorporación de cambios existente con los nuevos cambios.

---

## Más información sobre las revisiones de código
- Unas normas de codificación coherentes son esenciales para los proyectos a gran escala, ya que garantizan la legibilidad y la facilidad de mantenimiento
- Las guías de estilo de Google son un ejemplo destacado de cómo establecer y respetar estas normas en distintos equipos.
- Las revisiones del código también son esenciales para producir código de calidad
- Guías de estilo de Google
    - Todos los proyectos importantes de código abierto incluyen una Guía de estilo, que es un conjunto de normas para escribir código para ese proyecto.
    - Cuando todo el código de una enorme base de código se escribe de la misma manera, resulta considerablemente más sencillo de entender.
    - Puedes ver el estilo de codificación de Google [aquí](https://github.com/google/styleguide)
- Revisión del código
    - La revisión del código, también conocida como revisión por pares, es la reunión deliberada y metódica de otros programadores para examinar el código de los demás en busca de errores
    - La revisión del código puede acelerar y simplificar el proceso de desarrollo de software, a diferencia de otras técnicas
    - Las revisiones entre iguales también ahorran tiempo y dinero, sobre todo porque detectan defectos que podrían colarse en las pruebas, la producción y los portátiles de los usuarios finales.
- Estrategias habituales de revisión del código
    - Programación en pareja: Este método de creación de software pone a los ingenieros codo con codo, trabajando juntos en el mismo código. La Programación en pareja es una de las características definitorias de la Programación extrema (XP). Parece integrar la revisión del código directamente en el proceso de programación y es una técnica fantástica para que los ingenieros senior orienten a los miembros junior del equipo
    - El hilo de correo electrónico: Con la estrategia del hilo de correo electrónico, se envía un archivo a los compañeros de trabajo correspondientes a través del correo electrónico en cuanto se prepara un determinado fragmento de código para su revisión, de modo que puedan revisarlo individualmente
    - Por encima del hombro: Una de las formas más antiguas, sencillas y naturales de participar en la revisión de código por pares es la técnica por encima del hombro, que resulta más cómoda para la mayoría de los ingenieros que la programación en parejas de XP. Cuando tu código esté completo, pide a un compañero de trabajo que lo evalúe mientras le explicas por qué lo has creado así.
    - Herramientas asistidas: Las herramientas de revisión de código basadas en software, algunas de las cuales se basan en navegadores o se integran perfectamente en una serie de marcos de desarrollo IDE y SCM comunes, son la última forma de revisión de código. Las herramientas de software permiten que las revisiones se realicen de forma asíncrona y no local, enviando notificaciones al programador original cuando llegan nuevas revisiones.
    - Revisiones pull request: Un pull request (PR) es un procedimiento en el que se examina el código nuevo antes de fusionarlo para crear una rama o rama maestra en GitHub. Antes de fusionar una solicitud de extracción, las revisiones dan a los colaboradores la oportunidad de comentar las modificaciones sugeridas en la solicitud, aceptar los cambios o solicitar cambios adicionales. Los administradores del repositorio pueden ordenar que cada pull request sea aceptada antes de ser fusionada.
- Cinco consejos para la revisión de pull requests
    - Sea selectivo con los revisores: Es importante seleccionar un número razonable de revisores para una pull request. 
    - Revisiones puntuales: Lo ideal es que las revisiones se completen en las dos horas siguientes al envío de la pull request. 
    - Comentarios constructivos: Los comentarios deben ser constructivos y explicar qué hay que cambiar y, lo que es más importante, por qué se sugieren esos cambios. 
    - Descripción detallada de la solicitud: El pull request debe incluir una descripción detallada que cubra los cambios realizados en la rama de características en comparación con la rama de desarrollo, los requisitos previos, las instrucciones de uso, los cambios de diseño con comparaciones con maquetas y cualquier nota adicional que los revisores deban tener en cuenta
    - Rebasados interactivos: Los cambios interactivos permiten a los desarrolladores modificar commits individuales sin saturar el historial de commits con cambios redundantes o no relacionados. 

---

## Test your knowledge: Code reviews
1. When should we respond to comments from collaborators and reviewers?
> Always

2. What is a nit?
> A trivial comment or suggestion

3. Select common code issues that might be addressed in a code review. (Check all that apply)
> Using unclear names
> Forgetting to handle a specific condition
> Forgetting to add tests

4. If we've pushed a new version since we've made a recent change, what might our comment be flagged as?
> Outdated

5. What are the goals of code review? (Check all that apply)
> Make sure that the contents are easy to understand
> Ensure consistent style
> Ensure we don't forget any important cases