<h1>¡ADIVINE QUIEN ES EL ARTISTA!</h1>

Este es un juego desarrollado en **Python** en donde el usuario tendra 3 intentos de adivinar quien es el Artista.
Para este juego se seleccionaron 6 Artistas de habla Hispana del sector Musical.

Descargalo y probalo!

<h1>CONOCIMIENTOS APLICADOS EN ESTE JUEGO:</h1>

<h2>Listas de diccionarios:</h2>
El código utiliza una lista de diccionarios llamada artistas. Cada diccionario representa a un artista con varias propiedades como nombre, profesión, nacionalidad, edad y sellos discográficos.

<h2>Módulo random:</h2>
Se importa el módulo random para seleccionar aleatoriamente un artista de la lista utilizando <code>random.choice()</code>.

<h2>Bucle while:</h2>
Se utiliza un bucle <code>while</code> para permitir que el jugador haga múltiples intentos para adivinar el nombre del artista.

<h2>Selección aleatoria de pistas:</h2>
Se selecciona aleatoriamente una pista sobre el artista que no haya sido mostrada antes utilizando <code>random.choice()</code> en combinación con una lista de comprensión.

<h2>Entrada del usuario:</h2>
Se utiliza la función <code>input()</code> para obtener la respuesta del usuario sobre el nombre del artista.

<h2>Método strip():</h2>
El método <code>strip()</code> se utiliza para eliminar espacios en blanco al principio y al final de la respuesta del usuario.

<h2>Condicionales if y else:</h2>
Se utilizan condicionales para verificar si la respuesta del usuario es correcta y proporcionar mensajes correspondientes.

<h2>Manipulación de listas:</h2>
Se utiliza una lista llamada pistas_mostradas para almacenar las pistas que ya se han mostrado.

<h2>Iteración sobre diccionarios:</h2>
Se itera sobre el diccionario del artista para mostrar pistas y comparar la respuesta del usuario con el nombre del artista.

<h2>Control de flujo:</h2>
Se utiliza el control de flujo para imprimir mensajes específicos según la situación, como el número de intentos restantes y si el jugador ha ganado o perdido el juego.
Este código aborda conceptos fundamentales de Python, como estructuras de datos, control de flujo, entrada/salida de usuario, manipulación de cadenas y el uso de módulos externos.
