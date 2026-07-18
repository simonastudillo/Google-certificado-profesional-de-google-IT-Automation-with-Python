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