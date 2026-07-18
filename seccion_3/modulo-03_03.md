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