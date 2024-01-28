import random

artistas = [
    {"nombre": "Karol G", "Profesion": "Cantante, compositora, actriz y empresaria", "Nacionalidad": "Colombiana", "edad": 32, "Sellos discográficos": "Interscope Records y Universal Music Latin Entertainment"},
    {"nombre": "Bad Bunny", "Profesion": "Cantante, compositor, productor y luchador profesional", "Nacionalidad": "Puertoriqueño", "edad": 29, "̣Sellos discográficos": "Hear This Music y Rimas Entertainment"},
    {"nombre": "Tiago PZK", "Profesion": "Cantante y compositor", "Nacionalidad": "Argentino", "edad": 22, "Sello Discográfico": "Warner Music Latina"},
    {"nombre": "Nicky Jam", "Profesion": "Cantante, compositor y productor", "Nacionalidad": "Estadounidense", "edad": 42, "Sellos discográficos": "Pina Records, Sony Music Latin y muchos más"},
    {"nombre": "Maria Becerra", "Profesion": "Cantante, compositora y ex-youtuber", "Nacionalidad": "Argentina", "Edad": 23, "Sellos discográficos": "300 Entertainment y Warner Music Latina"},
    {"nombre": "Nicki Nicole", "Profesion": "Cantante, rapera y compositora", "Nacionalidad": "Argentina", "Edad": 23, "Sellos discográficos": "Dale Play Records y Sony Music Latin"}
]

artista = random.choice(artistas)
intentos = 3

# Lista para almacenar las pistas ya mostradas
pistas_mostradas = []

print("Bienvenido al juego de adivinar quién es.")
print("Tienes que adivinar el nombre de un artista que he elegido al azar.")
print("Te daré algunas pistas sobre el artista, y tendrás", intentos, "intentos para adivinar su nombre.")
print("Empecemos.")

while intentos > 0:
    # Seleccionar una pista que no se haya mostrado antes y que no sea el nombre
    pista, valor = random.choice([(key, value) for key, value in artista.items() if key != "nombre" and key not in pistas_mostradas])

    # Agregar la pista a la lista de pistas mostradas
    pistas_mostradas.append(pista)

    print("Pista:", pista.capitalize(), ":", valor)

    respuesta = input("¿Quién es? ").strip().lower()

    if respuesta == artista["nombre"].lower():
        print("¡Correcto! Has adivinado el nombre de", artista["nombre"] + ". ¡Eres un experto!")
        break
    else:
        intentos -= 1
        print("Lo siento, esa no es la respuesta correcta.")

        if intentos > 0:
            print("Te quedan", intentos, "intentos. ¡Sigue intentándolo!")
        else:
            print("Te has quedado sin intentos. Has perdido el juego.")
            print("La respuesta correcta era", artista["nombre"] + ". Mejor suerte la próxima vez.")