Este experimento se realiza con el fin de simular un monitor de microservicios de facturacion.
El experimento fue realizado en una maquina virtual con Linux instalado
Se uso la distribución KDE neon 5.22 https://neon.kde.org/

Se debe instalar el programa Nmap, el cual es un programa de código abierto que sirve para efectuar
rastreo de puertos. Se usa para evaluar la seguridad de sistemas informáticos, así como para descubrir
servicios o servidores en una red informática, para ello Nmap envía unos paquetes definidos a otros
equipos y analiza sus respuestas.

Para el experimento, NMAP se usara para hacer PING - ECHO y obtener el estado de salud de los microservicios
De igual forma se usa la instrucción "ps -e | grep xxxx" para saber si el servicio esta vivo

Para instalar nmap en linux usar

    sudo apt-get install nmap

Para poder ejecutar el experimento se deben seguir los siguientes instrucciones:

1. Se deben crear tres proyectos, uno asociado por cada microservicio
   Para el experimento se utilizo Visual Studio Code. Los microservicios son:

   * consultas - puerto asociado 5000
   * comandos - puerto asociado 5001
   * monitor - puerto asociado 5002

2. Instalar y ejecutar el microservicio comandos

    * Crear el entorno virtual "python3 -m venv venv"
    * Activar el entorno virtual "source venv/bin/activate"
    * Ingresar a la carpeta flaskr "cd flaskr"
    * Instalar las dependencias "pip install -r requirements.txt"
    * Ejecutar el microservicio "flask run -p 5000"

3. Instalar y ejecutar el microservicio consultas

    * Crear el entorno virtual "python3 -m venv venv"
    * Activar el entorno virtual "source venv/bin/activate"
    * Ingresar a la carpeta flaskr "cd flaskr"
    * Instalar las dependencias "pip install -r requirements.txt"
    * Ejecutar el microservicio "flask run -p 5001"

4. Instalar y ejecutar el microservicio monitor

    * Crear el entorno virtual "python3 -m venv venv"
    * Activar el entorno virtual "source venv/bin/activate"
    * Ingresar a la carpeta flaskr "cd flaskr"
    * Instalar las dependencias "pip install -r requirements.txt"
    * Ejecutar el microservicio "flask run -p 5002"
