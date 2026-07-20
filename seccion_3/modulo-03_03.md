# Secure shell y API Keys

## Que es un Secure Shell (SSH)
- Secure Shell (SSH) es un protocolo robusto para conectarse a servidores de forma remota.
- En el ámbito del acceso remoto a servidores, la seguridad es cada vez más importante para proteger su información.
- Secure Shell se utiliza principalmente para iniciar sesión en servidores Linux, servidores Unix y ciertos equipos de red, como enrutadores.
- Alternativas
    - Telnet: Expone los comandos que escribes, incluidas las contraseñas, a cualquier persona en la red que cuente con las herramientas adecuadas. Si bien el protocolo TLS (Transport Layer Security) cifra los datos dentro de los navegadores web, SSH protege los datos en sesiones de terminal interactivas o transferencias de archivos. Este cifrado garantiza que la información confidencial permanezca protegida durante la comunicación.
    - VPN: Las VPN también ofrecen cifrado, pero otorgan acceso a redes completas después de la conexión. SSH se rige por el principio de mínimo privilegio, restringiendo a los usuarios a hosts específicos y mejorando así la seguridad.
    - VNC o GoToMyPC: Estos se centran en interfaces gráficas de usuario y experiencias de escritorio, que pueden no ser compatibles con la mayoría de los servidores Linux que operan sin entornos de escritorio.
- SSH funciona mediante dos componentes clave: el servidor SSH y el cliente SSH.
- El servidor SSH, ubicado en el servidor de destino, establece conexiones de red seguras, realiza la autenticación mutua e inicia sesiones de inicio de sesión o transferencias de archivos cifradas.
- Por otro lado, el cliente SSH establece una conexión con el servidor SSH, garantizando una interacción segura. El cliente realiza solicitudes, como «iniciar sesión» o «copiar este archivo».
- En el protocolo SSH, una credencial de acceso se conoce como clave SSH.
- Cumple una función similar a la de los nombres de usuario y las contraseñas, aunque los administradores de sistemas y los usuarios avanzados suelen utilizar las claves para automatizar procedimientos y lograr el inicio de sesión único.
- Mostrar la huella digital de una clave SSH es una forma útil de verificar que se está utilizando la clave correcta y que la clave del servidor remoto no ha sido manipulada.
- Para mostrar la huella digital de una clave SSH, puede utilizar la herramienta de línea de comandos ssh-keygen.

---

## El protocolo SSH
- El protocolo de red Secure Shell, generalmente abreviado como «SSH», permite el acceso seguro a un ordenador a través de una red no segura.
- Que es un protocolo?
    - Un protocolo es un conjunto de reglas que definen cómo deben comunicarse dos elementos entre sí.
    - En el caso de los protocolos informáticos, estos suelen publicarse como estándares abiertos para que cualquier protocolo pueda implementarse en diversos productos.
    - El hecho de que estos protocolos estén disponibles para todos significa que cualquier máquina o red que implemente un protocolo determinado debería poder comunicarse sin problemas con cualquier otro dispositivo que lo admita.
- ¿Cómo protege SSH la red?
    - Funciona mediante el principio de cifrado de clave pública.
    - Tanto el cliente como el servidor generan una clave de cifrado robusta para los datos que se transmiten entre ellos.
    - Esta clave se divide por la mitad: el cliente conserva una parte y el servidor la otra.
- En SSH, las claves se dividen en una clave pública (la parte pública de la clave de cifrado del servidor) y una clave privada, que se almacena únicamente en el servidor.
- De esta forma, el equipo del usuario puede cifrar un mensaje con la clave pública, pero solo el servidor conectado puede descifrarlo, ya que solo la clave privada del servidor permite hacerlo correctamente.
- Así, si alguien interceptara el tráfico de red, no podría leerlo porque no tiene la clave privada del servidor.
- Con SSH, tanto las pulsaciones de teclas como las respuestas del servidor son completamente seguras.

- El protocolo SSH se usa comúnmente para iniciar sesión en servidores de forma remota.
- Si bien se usa principalmente para iniciar sesión en servidores Linux y Unix, también se usa para cifrar transferencias de archivos y para iniciar sesión en algunos equipos de red, como enrutadores.
- La mayoría de los clientes SSH no se conectarán si su clave privada no está protegida de otros usuarios
Además de proporcionar una shell de inicio de sesión segura en un servidor remoto, SSH se puede usar para otras funciones, entre ellas:
    - Transferencia de archivos entre cliente y servidor con SCP (Protocolo de Copia Segura) o SFTP (Protocolo de Transferencia Segura de Archivos);
    - Reenvío de puertos de red del servidor al cliente, o "tunelización".
    - Reenviar su inicio de sesión a otro servidor detrás de un cortafuegos, a veces denominado «servidor intermedio» o «servidor bastión».
    - Ejecutar aplicaciones con interfaz gráfica de usuario (GUI) en un servidor, pero mostrarlas en un cliente local.

---

## Configurando SSH
- Los puertos de computadora son puntos de inicio y fin de una conexión de red, definidos por software.
- Al usar Secure Shell (SSH), el cliente se conecta al servidor a través del puerto 22 (por defecto).
- Una vez establecida la conexión, el servidor envía su clave pública al cliente.
- A continuación, el cliente y el servidor negocian un conjunto de reglas de cifrado, denominado algoritmo de cifrado, compatible con ambas máquinas.
- Cuando ambas máquinas coinciden en el algoritmo de cifrado, el servidor inicia una sesión de inicio de sesión para el usuario.
- Configuración de un cliente SSH
    - Las instrucciones de configuración de SSH serán diferentes dependiendo de su sistema operativo y de la implementación de SSH
- Generar su par de claves
    - En primer lugar, necesitarás generar tu par de claves pública/privada
    - La primera vez que se conecte a un servidor determinado utilizando SSH, el servidor almacenará una copia de su clave pública en su máquina
    - Esto sólo debe hacerse una vez, ya que el mismo par de claves puede utilizarse para conectarse a cualquier número de hosts remotos.
    - Podemos crear una ejecutando el comando `ssh-keygen -t rsa -b 2048` en la terminal de nuestro sistema operativo.
        - `ssh-keygen` es la herramienta de línea de comandos que se utiliza para generar, administrar y convertir claves de autenticación para SSH.
        - `-t rsa` especifica el tipo de clave a crear, en este caso RSA.
        - `-b 2048` especifica el tamaño de la clave en bits, en este caso 2048 bits, que es un tamaño de clave seguro y ampliamente utilizado.
- OpenSSH le preguntará WHERE para guardar las claves generadas. Tenga en cuenta que creará un directorio oculto llamado .ssh en su directorio personal. Aquí puede aceptar los valores predeterminados.
- SSH también le pedirá una contraseña para proteger su clave
- Mucha gente elige no usar una frase de contraseña porque si la introduce aquí, se le pedirá que la introduzca cada vez que se use su clave.
- Sin embargo, si está en una máquina que no es segura, alguien que obtenga acceso a ese ordenador también tendrá acceso a todos los sistemas que utilicen esa clave.
- Si añade una frase de contraseña a su clave SSH para mayor seguridad, puede guardarla en un agente SSH, que es un programa que gestiona claves SSH
- Una vez que haya establecido su frase de contraseña o rechazado la opción, OpenSSH generará un par de claves públicas/privadas aleatorias y las guardará
- Conexión por primera vez
    - Ahora que tienes un par de claves, puedes conectarte a un host. La forma más básica del comando para conectarse es `ssh <usuario>@<host>`:
        - `<usuario>` es el nombre de usuario en el host remoto al que desea conectarse.
        - `<host>` es la dirección IP o el nombre de dominio del host remoto al que desea conectarse.
    - Cuando se conecta a un servidor por primera vez, SSH imprimirá la huella digital de la clave del servidor remoto y confirmará que realmente desea conectarse.
    - Es posible que se le pida que introduzca la contraseña de la cuenta en el host remoto. Una vez hecho esto, se almacenará una copia de tu clave pública en el host y no tendrás que volver a introducir la contraseña
- Configuración de un servidor SSH
    - El componente del servidor SSH, llamado "demonio", suele estar instalado por defecto en Linux y Unix
    - En Linux, el archivo de configuración del servidor suele estar en /etc/ssh/sshd_config y rara vez es necesario modificarlo.
    - Las versiones posteriores de MacOS también tienen un cliente SSH de línea de comandos ya instalado. Para una implementación gratuita de SSH para Windows, Mac y Unix, consulte [Putty](https://www.putty.org/).

>[!TIP]
> Puedes utilizar el mismo par de claves privada/pública en todas las máquinas que controles. Así, si tienes dos portátiles y una tableta, puedes copiar tu par de claves en todos ellos. Esto puede ahorrarte algunos pasos al iniciar sesión desde otros dispositivos.

---

## Claves API
- Una clave de Interfaz de programación de aplicaciones (API) es un token de autenticación que permite llamar a una API
- Una aplicación pasa una clave API a la API, que luego es llamada para identificar a la persona, el programador o el programa que intenta acceder a un sitio web
- La clave API suele ser generada aleatoriamente por la aplicación y debe enviarse en cada llamada a la API. Sirve como identificador distintivo y ofrece un token seguro para la autenticación.
- Autenticación y autorización
    - Las claves API pueden utilizarse tanto para la autenticación, asegurándose de que usted es quien dice ser, como para la autorización, decidiendo a qué API se le permite llamar.
    - Con la autenticación de proyectos (autenticación de aplicaciones o sitios), las claves API ayudan a identificar el proyecto o la aplicación que realiza la llamada
    - Al autorizar con claves de API, también se está asegurando de que la llamada a la API es correcta. La autorización también comprobará que la clave de API que se está utilizando en el proyecto está disponible.
- Cómo se utilizan
    - El uso de las API depende de cada una de ellas. Con la mayoría de las API, es necesario enviar la clave API con cada solicitud. Puede enviarse de varias formas:
    - tipo GET: `GET https://myapp.com/api/users/list?apikey=12345678`
    - Encabeza GET: `GET https://myapp.com/api/users/listX-API-Key: 12345678`
    - POST: `POST https://myapp.com/api/auth{ “token”: “12345678” }`

---

## Cuándo utilizar claves API
- La gestión del acceso y la salvaguarda de los recursos es donde entran en juego las claves API
- Para qué se pueden utilizar las claves API
    - Para bloquear el tráfico anónimo: Puede ayudar a proteger su API de abusos y garantizar que sólo los usuarios autorizados puedan acceder a ella.
    - Para controlar el número de llamadas realizadas a su API: Puede ayudar a evitar que su API se sobrecargue y garantizar que esté disponible para todos los usuarios autorizados.
    - Para identificar patrones de uso: Puede utilizarse para mejorar su API y asegurarse de que satisface las necesidades de sus usuarios.
    - Para filtrar los registros por clave de API: Puede ayudarle a solucionar problemas con su API y a identificar qué usuarios utilizan más su API.
- Para qué no puede utilizar claves de API
    - Identificar usuarios individuales: Las claves API no identifican usuarios individuales; identifican proyectos enteros.
    - Autorización segura: Sólo deben utilizarse para identificar y controlar el acceso a una API.
    - Identificar a los creadores de un proyecto: la infraestructura de servicios no proporciona un método para buscar proyectos directamente a partir de claves de API.

---

## Claves públicas frente a claves privadas
- En un mundo tecnológico en rápida evolución, es más importante que nunca establecer políticas de seguridad en toda la organización que salvaguarden la valiosa información y los activos de datos
- La criptografía asimétrica se basa en claves públicas y privadas para mantener la seguridad y confidencialidad de los datos frente a los peligros.
- ¿Qué es una clave pública?
    - Una clave pública se emplea con frecuencia para establecer una comunicación segura mediante el cifrado de datos o para validar la autenticidad de una firma digital
    - La seguridad está garantizada porque la clave pública procede de una autoridad certificadora de confianza, que expide certificados digitales que verifican la identidad y la clave del propietario
- ¿Qué es una clave privada?
    - Una clave privada es una clave secreta y segura que debe mantenerse confidencial y protegida
    - Su función consiste en descifrar y crear firmas digitales que garanticen la integridad y autenticidad de los datos.
    - Es la contrapartida de la clave pública y se comparte para descifrar la información codificada.
- ¿Cómo funcionan juntas las claves pública y privada?
    - Las claves públicas y privadas trabajan juntas para garantizar que la comunicación segura, el cifrado de datos, las firmas digitales y los intercambios de claves tengan lugar de forma segura a través de diversos canales de comunicación. Este proceso abarca:
        1. Generación de claves
        2. Intercambio de claves
        3. Cifrado de datos
        4. Transmisión de datos
        5. Descifrado de datos