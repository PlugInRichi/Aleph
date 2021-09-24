# Secure Shell 

Secure Shell o SSH es un protocolo que permite a los usuarios controlar y modificar sus servidores remotos.


## Comandos básicos

Generar el par de llaves en el Host
    
    ssh-keygen -t rsa

El tipo de la clave se especifica mediante el parámetro -t y puede ser _rsa1_ para ssh v1 o _rsa, dsa_ para ssh v2

Compartir la llave pública
  
    ssh-copy-id username@remote_host
    
Otra alternativa a ssh-copy-id

    cat ~/.ssh/id_rsa.pub | ssh username@remote_host "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"


## Configuraciones ~/.ssh/config 

Permitir autenticación por archivo

    PasswordAuthentication yes



### Túnel SSH


    Host server_jump
      HostName server.dominio.mx
      Port 1818
      User richi
      IdentityFile ~/.ssh/id_rsa
    Host server_target
      HostName 192.168.20.29
      Port 22
      User richi
      IdentityFile ~/.ssh/id_rsa
      ProxyJump server_jump

  
 Con el tunel configurado podemos transferir nuestra llave pública de la siguiente manera
    
    ssh-copy-id server_target
    
 
Envío de archivos por tuneles
    
    scp host_file.zip server_target:path_file
