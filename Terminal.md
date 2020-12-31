

# Índice 📌

- [Administrando Paquetes](#Administrando-Paquetes)
  - [Pacman](#Pacman)
  - [Yay](#Yay)
- [Ranger](#ranger)
  
  # Administrando Paquetes
  
  ## Pacman
  
  Para eliminar un paquete y sus dependencias (siempre que no sean usadas por ningún otro paquete instalado): 
  ```
  pacman -Rs nombre_del_paquete
  ```
  Para listar todos los paquetes explícitamente instalados y no requeridos como dependencias: 
  ```
  pacman -Qet
  ```
  Para actualizar paquetes
  ```
  pacman -Syu
  ```
  
    ## Yay
    
  # Ranger
  
        i → Mostrar el archivo.
        r → Abrir archivo con el programa elegido.
        / → Buscar archivos (n | p saltar a la coincidencia siguiente / anterior).
        dd → Cortar archivo.
        yy → Copiar archivo.
        pp → Pegar archivo.
        ctrl + h → muestra archivos ocualtos.
        espacio → Seleccionar archivo actual.
        :rename → Renombrar archivo.
        :delete → Eliminar el archivo seleccionado.
        :mkdir → Crear un directorio.
        :touch → Crear un archivo.
        :rename → Renombrar archivo.

