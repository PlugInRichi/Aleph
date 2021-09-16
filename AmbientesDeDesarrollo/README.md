# Ambientes de desarrollo

Seguramente en algún momento te ha ocurrido que al compartir código con un colega el programa no carga correctamente o surgen errores de ejecución. El típico "en mi máquina sí funcionaba :( ".

Utiliza ambientes de desarollo pueden ahorrarnos muchos dolores de cabeza especialmente cuando trabajamos en un mismo servidor donde coexisten diferentes versiones de una misma librería, frameworks o bases de datos y cada una es impresindible para alguno de los proyectos que ahí se ejecutan.

## PyEnv
Una manera simple de gestionar las dependencias de tu proyecto es utilizando entornos virtuales, muy útiles para encapsular dependencias de tal manera que estén disponibles únicamente para el proyecto en el que se requieren y no para todo el sistema.

Uno de los paquetes más usados para realizar entornos virtuales es conocido como _virtualenv_, sim embargo yo prefiero _pyenv_ debido a que nos permite administrar las versiones de Python, Anaconda.


Instalación (ArchLinux)

    sudo pacman -S pyenv
    yay -S pyenv-virtualenv
  Adicionalmente tendrás que agregar en tu archivo .bashrc
 
     eval "$(pyenv init -)"
     eval "$(pyenv virtualenv-init -)"


Gestionar diferentes versiones de python requiere instalarlas en el sistema operativo:

    pyenv install 3.6.0

Actualizar la versión instalada

    pyenv rehash

Crear un ambiente virtual con una versión específica

    pyenv virtualenv 3.6.0 minIA

Activar el ambiente

	pyenv activate

