# Proyecto_LightsOut.
El proyecto se trata del videojuego Lights Out creado con Python, este programa se ejecuta y funciona dentro de una terminal como: cmd o powershell de Windows.

## Autores
- Fajardo Sepulveda Kevin Yovanni
- Salcido Peralta Jorge Manuel

## Información para la ejecución del videojuego.
Para ejecutar este programa primero es necesario descargar Python en el equipo, puedes descargar el instalador en la página oficial de Python <a src="https://www.python.org/downloads/">https://www.python.org/downloads/</a>, después hacer lo siguiente:
- Se debe descargar los 3 archivos (comandos_consola.py, impresiones.py y light.py) y colocarlos dentro de una misma carpeta.
- Abrir una terminal (preferiblemente la aplicación "Terminal" de Windows).
- Ir a la ruta donde se encuentran guardados los 3 archivos en la terminal, ejemplo: cd C:\Users\usuario\Documents\LightOut>.
- Poner en pantalla completa y reducir lo máximo posible el zoom de la terminal.
- Ejecutar el archivo principal "light.py" en la terminal de la siguiente manera: Python light.py.

## Información del programa.
Una vez ejecutado el videojuego obtendremos el siguiente resultado en la terminal.

<img width="1913" height="628" alt="image" src="https://github.com/user-attachments/assets/e111840d-0032-464b-9eea-b351da773ae0" />

Se trata del menú de inicio del videojuego, donde podemos seleccionar una dificultad entre fácil, intermedio y difícil.
Para seleccionar una dificultad se utiliza las siguientes teclas:
- W: Mover hacia arriba
- S: Mover hacia abajo
- Enter: Confirmar dificultad

Dependiendo de la dificultad elegida, el videojuego tendrá un tablero con un mayor o menor cantidad de luces.
- Fácil.
  <img width="1920" height="497" alt="image" src="https://github.com/user-attachments/assets/83fbb8dd-efef-4928-9025-458c164c188a" />

- Intermedio.
  <img width="1920" height="700" alt="image" src="https://github.com/user-attachments/assets/7444d82c-5a4a-4e3e-a706-64bb673f3754" />

- Difícl.
  <img width="1920" height="694" alt="image" src="https://github.com/user-attachments/assets/a1753ba3-cd30-466d-9c8d-86924498648a" />

## Explicación del videojuego
El videojuego consiste en apagar todas las luces, en este caso, cerrar todos los ojos. <br>
Al seleccionar un ojo y presionarlo, este cambiara de estado, es decir, si el ojo se encontraba abierto entonces se cerrará y viceversa, pero también, los ojos que se encuentren alrededor del ojo seleccionado (sin contar los ojos de las esquinas) cambiaran de estado al presionar el ojo seleccionado, por lo que se tiene que pensar bien que ojos presionar.

<img width="839" height="474" alt="image" src="https://github.com/user-attachments/assets/32edad70-1f05-4576-a212-13f3f09520c3" />
<img width="823" height="487" alt="image" src="https://github.com/user-attachments/assets/d8dfae9c-5012-4ee3-9e2f-5b2bfd5e3aed" />

Una vez que se haya logrado cerrar todos los ojos, el videojuego te felicitará por ganar y terminará el juego.
<img width="828" height="500" alt="image" src="https://github.com/user-attachments/assets/bc68976c-77f0-4ffc-94cd-7e584e42ef64" />

## Controles
Las teclas para jugar son las siguientes:
- W: Mover selección hacia arriba.
- A: Mover selección hacia la izquierda.
- S: Mover selección hacia abajo.
- D:  Mover selección hacia la derecha.
- Enter: Realizar la alternación de las luces (apagar o encender las luces).
- Backspace: Pedir al programa una ayuda (Marca de un color la luz que debes cambiar).
- Q: Detener el programa.


