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