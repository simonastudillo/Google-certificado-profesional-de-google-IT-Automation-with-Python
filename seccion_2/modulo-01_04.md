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

---

## Ejemplo practico de automatización
- Usemos el módulo shutil y ​la función de uso del disco para comprobar el espacio en disco disponible actualmente.
- podemos usar otro módulo llamado psutil: esta función recibe un intervalo de segundos y ​devuelve un porcentaje promedio de uso en ese intervalo
- Ejemplo: [example-s2-m1-04.py](../ejercicios/example-s2-m1-04.py)
- Ejemplo 2: [doctor_my_pc.py](../ejercicios/doctor_my_pc.py)

---

## ¿Merece la pena el tiempo invertido?
- Las empresas investigan si la automatización de procesos o tareas ahorra tiempo de trabajo (y, por tanto, dinero), ofrece un Retorno de la inversión (ROI) suave, o ambas cosas
- Si merece la pena, el proceso automatizado ahorrará tiempo de trabajo a la empresa, beneficios de ROI blando, o ambos.
- ROI blando
    - El ROI blando a través de la automatización es difícil de medir porque, normalmente, no hay cifras o datos concretos que lo respalden. Las métricas de ROI blando incluyen la mejora de:
        - La colaboración en equipo
        - La moral del equipo
        - La motivación de los empleados
        - La satisfacción de los empleados
- Time_to_automate < (time_to_perform * amount_of_times_done)

>[!TIP]
> observe que tiene dos medidas de tiempo. Antes de introducir los valores en la fórmula, convierte 10 horas en minutos.
> Multiplica 10 por 60 para convertir 10 horas en minutos. Obtendrás 600 minutos.
> Cuando introduces tus valores en la fórmula anterior, obtienes: 600 < 40x
> x representa el número de semanas, así que puedes sustituirlo por x en la fórmula.
> Luego, divide ambos lados por 40 para obtener: 15 semanas.

---

## Ponga a prueba sus conocimientos: Automatización

1. At a manufacturing plant, an employee spends several minutes each hour noting uptime and downtime for each of the machines they are running. Which of the following ideas would best automate this process?
> Add an analog Internet of Things (IoT) module to each machine, in order to detect their power states, and write a script that records uptime and downtime, reporting hourly

2. One important aspect of automation is forensic value. Which of the following statements describes this term correctly?
> It is important for automated processes to leave extensive logs so when errors occur, they can be properly investigated.

3. An employee at a technical support company is required to collate reports into a single file and send that file via email three times a day, five days a week for the next four weeks, on top of his other duties. It takes him about 15 minutes each time. He has discovered a way to automate the process, but it will take him about 10 hours to code the automation script. Which of the following equations will help them decide whether it's worth automating the process?
> if [10 hours to automate < (15 minutes * 60 times)] then automate

4. A company is looking at automating one of their internal processes and wants to determine if automating a process would save labor time this year. The company uses the formula [time_to_automate < (time_to_perform * amount_of_times_done)] to decide whether automation is worthwhile. The process normally takes about 10 minutes every week. The automation process itself will take 40 hours total to complete. Using the formula, how many weeks will it be before the company starts saving time on the process?
> 2400/ 10 = 240 weeks

5. Which of the following are valid methods to prevent silent automation errors? (Check all that apply)
> Regular consistency checks
> Email notifications about errors
> Internal issue tracker entries