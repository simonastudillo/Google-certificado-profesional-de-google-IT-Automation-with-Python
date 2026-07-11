# Otros conceptos de Test

## Black box vs White box
- `White box testing` (AKA clear-box or transparent testing): se basan en el conocimiento de los creadores de pruebas ​del software que se está probando para construir los casos de prueba.
- `Black box testing`: Las pruebas de caja negra se escriben con ​una conciencia de lo que se supone que debe hacer el programa, ​sus requisitos o especificaciones, ​pero no cómo lo hace
- Cada uno tiene sus ventajas:
    - Las pruebas de caja blanca son útiles ​porque un escritor de pruebas puede usar su conocimiento ​del código fuente para crear pruebas que ​cubran la mayoría de las formas en que el programa se comporta
    - Las pruebas de caja negra son útiles porque no se ​basan en el conocimiento de cómo funciona el sistema, esto significa que sus casos de prueba son ​menos propensos a estar sesgados por el código.
- Si el test se escribe antes que el código, se considera un enfoque de caja negra, ya que el test se basa en los requisitos y no en la implementación.
- Si el test se escribe después del código, se considera un enfoque de caja blanca, ya que el test se basa en la implementación y no en los requisitos.

---

## Otros tipos de test
- `Integration tests`: verifican que las interacciones entre los diferentes fragmentos ​de código en entornos integrados funcionan de la manera que esperamos
- `unit test`: no deben cruzar límites para ​hacer cosas como hacer una solicitud de red o integrarse con una API o base ​de datos, el objetivo de una prueba unitaria es verificar este tipo de interacciones y ​asegurarse de que todo el sistema funciona como se espera
- es ​posible que necesitemos crear un entorno de prueba independiente para nuestra prueba
- Estas pruebas generalmente requieren un poco más de trabajo en configurarse, ya que tendrá ​que asegurarse de que tiene las versiones de prueba de todos los sistemas relevantes.
- Pero podrían ayudar a detectar problemas que las pruebas unitarias no enviarán mensajes de texto, por lo que ​el esfuerzo adicional definitivamente vale la pena
- Por lo general, se escriben como parte de un proceso de depuración y solución de problemas ​para verificar que se ha corregido un problema o error una vez que se ha identificado
- Las pruebas de regresión son parte útil de un conjunto de pruebas porque aseguran ​que el mismo error no ocurra dos veces
- `smoke test`: a veces llamada prueba de verificación de construcción, ​obtener su nombre de un concepto que proviene de la prueba de equipos de hardware. ​Conecte la pieza de hardware dada y vea si empieza a salir humo de ella. 
    - Generalmente responden a la pregunta de: "¿El software se inicia y funciona lo suficiente como para que podamos probarlo más a fondo?"
- `load test`: Estas pruebas verifican que el sistema se comporta bien cuando está bajo una carga significativa, para realizar realmente estas pruebas tendrá que generar tráfico a nuestra aplicación ​simulando el uso típico del servicio