# Clase 69-72
def frase (cadena):
    interrogacion = ("qué", "cómo", "cuándo", "quién", "por qué")
    mayus = cadena.capitalize()
    if cadena.startswith(interrogacion):
        return "¿{}?". format(mayus)
    else:
        return "{}.".format(mayus)

result = []

while True:
    user_imput = input("Escribe algo: ")
    if user_imput == "/end":
        break
    else:
        result.append(frase(user_imput))

print(" ".join(result))














