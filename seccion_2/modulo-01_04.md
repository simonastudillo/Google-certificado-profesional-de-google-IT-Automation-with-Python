# Tareas automáticas a través de la programación

## Beneficios de la automatización
- Considere la automatización como un multiplicador de fuerza de TI.
- Es​una herramienta que puede aumentar la eficacia de ​un equipo de TI sin necesidad de ​aumentar la cantidad de miembros del equipo.
- La escalabilidad significa que cuando ​se agrega más trabajo a un sistema, ​el sistema puede hacer lo que sea necesario para completar el trabajo
- Otro beneficio sutil pero muy útil ​de la automatización es la centralización de los errores
- Lo que significa que si encuentra un error en un script, ​puede corregir el error de una vez por todas, ​lo que no es el caso de los ​errores cometidos por humanos

---

## Peligros de la automatización
- Cuando la automatización se implementa sin un diseño cuidadoso, ​puede causar algunos problemas graves
- Cualquier tarea o proceso que automaticemos conlleva una compensación
    - ¿El tiempo y el esfuerzo necesarios para ​escribir el script valen la pena por los posibles beneficios de la automatización?
- [time_to_automate < (time_to_perform * amount_of_time_done)]
- Ejemplo: 
    - La automatización de la tarea demora `1 hora` de programación.
    - La tarea manual demora `5 minutos` por día.
    - Eso significa que después de `12 días`, la automatización habrá ahorrado tiempo.
    - Eso es `60 minutos/5 minutos por día = 12 días`
    - En este caso, la automatización es una buena idea, ya que el tiempo de programación es mucho menor que el tiempo que se ahorrará.
- Ejemplo 2:
    - La automatización de la tarea demora `10 horas` de programación.
    - La tarea manual demora `5 minutos` por día.
    - Eso significa que después de `120 días`, la automatización habrá ahorrado tiempo.
    - Eso es `600 minutos/5 minutos por día = 120 días`
    - En este caso, la automatización no es una buena idea, ya que el tiempo de programación es demasiado largo en comparación con el tiempo que se ahorrará.
- Un tiempo alto de automatización es peligroso en el sentido de que en ese tiempo podría haber ocurrido un cambio en el proceso que haga que el script ya no funcione correctamente.
- Por lo general, la decisión de ​automatizar o no no es tan sencilla.
    - ​Si una tarea es compleja y se realiza con poca frecuencia, ​puede parecer que la automatización ​es más difícil de lo que vale la pena.
    - ​Pero ten en cuenta que, una vez que una ​tarea se automatiza, cualquiera puede realizarla.
    - ​Puede resultar muy útil automatizar una ​tarea compleja y propensa a errores si es ​fundamental que la tarea se realice correctamente, ​incluso si no se ejecuta con tanta frecuencia
- Principio de Pareto: El 80% de los efectos provienen del 20% de las causas. En el contexto de la automatización, esto significa que una pequeña cantidad de tareas puede generar la mayor parte del valor. Por lo tanto, es importante identificar y priorizar las tareas que tendrán el mayor impacto cuando se automatizan.
- Bit-rot: Se refiere a la degradación de un sistema o software con el tiempo debido a la falta de mantenimiento, actualizaciones o cambios en el entorno.
- ¿Cómo podemos evitar estos fracasos silenciosos? ​Puede crear un método de notificación ​en sus sistemas automatizados.
- lo peor del fracaso de la automatización ​es cuando la automatización tiene éxito, ​pero realiza una acción incorrecta.
- Para esta clase de fallos más sutiles, ​podemos utilizar pruebas periódicas para comprobar ​el comportamiento de sus sistemas automatizados.
- podríamos programar una restauración regular de los datos de ​la base de datos de ventas y, a continuación, comprobar que ​los datos restaurados son los ​que esperaba que se respaldaran