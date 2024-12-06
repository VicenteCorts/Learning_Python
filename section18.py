# Clase 158
# Los apartados con titulación comentada verde son los que se añaden para el nuevo proyecto:

import cv2, time

# Frame inicial para comparación
frame0=None

video=cv2.VideoCapture(0)

while True:
    check, frame = video.read()

    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Conversión a blureado del frame (hay que pasarle por parámetro: imagen, nivel de blur, desviación estándar -0-)
    gray=cv2.GaussianBlur(gray,(21,21),0)


    # Condicional para comprobar si existe el frame inicial de comparación. En la segunda iteración del bucle "frame0" ya tiene valor entonces no entra en este condicional
    if frame0 is None:
        # El frame inicial será la variable "gray" que toma el primer frame de la cámara y lo convierte en escala de grises
        frame0 = gray 
        continue

    # Calcular diferencia entre el frame0 y el frame actual
    delta_frame=cv2.absdiff(frame0, gray)

    # Calcular la diferencia entre los valores del frame gray y el delta frame. Si estos valores superan el 30 haremos que python los determine como movimiento:
    thresh_frame=cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]

    # hacer que el thresh_frame sea más "Smooth"
    thresh_frame=cv2.dilate(thresh_frame, None, iterations=2)

    # Creación de contornos para los objetos detectados en el dilated threshold frame
    (cnts,_) = cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Tomar contornos que tengan un ára superior a 1000 pixels
    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue

        # Cuando el área sea mayor a 1000 pixels crearemos el rectángulo
        (x, y, w, h) =cv2.boundingRect(contour)
        # Dibujando el rectángulo creado en el frame
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 3)

    cv2.imshow("Gray frame", gray)
    cv2.imshow("Delta frame", delta_frame) # para mostrar el video en deltaframe
    cv2.imshow("Threshhold frame", thresh_frame) # para mostrar el video en threshold, blanco y negro por siluetas
    cv2.imshow("Color", frame) # para ver la imagen en color y con el rectángulo de detección de movimiento

    key=cv2.waitKey(1)

    if key==ord('q'):
        break

video.release() 
cv2.destroyAllWindows
print("Webcam Off")