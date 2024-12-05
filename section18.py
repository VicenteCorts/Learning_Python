# Clase 158
# Importamos Librerías
import cv2, time

# Crear objeto video - el número indica qué cámara actuará- al tener solo una, marcamos el primer índice: 0
video=cv2.VideoCapture(0)

# Variable para contar frames (por curiosear)
a=1

# Bucle While para pasar de formato imagen (frame) a video (bucle de frames)
while True:
    # Contando frames
    a = a + 1
    # Revisión de los frames que captura la webcam
    check, frame = video.read()
    print(check)
    print(frame) # Por defecto es el primer frame que la cámara captura
    # Imagen en gris (tests)
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Ralentizar la ejecución del script para comprobar si la webcam se activa
    # time.sleep(3)

    # Mostrar Captura de Video
    cv2.imshow("Capturing", gray)

    # Liberar/Parar la webcam y las ventanas de testing de captura
    key=cv2.waitKey(1)
    if key==ord('q'):
        break

video.release() 
cv2.destroyAllWindows
print("Webcam Off")
print("Total de frames: {}".format(a))