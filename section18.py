# Clase 158-159
# Los apartados con titulación comentada verde son los que se añaden para el nuevo proyecto:

import cv2, time, pandas
# importamos datetime
from datetime import datetime 

# Frame inicial para comparación
frame0=None

# Variable de lista vacía para rellenar con el valor de "status"
status_list=[None, None]

# Variable DataFrame de panda para recoger los datos de la lista times
df=pandas.DataFrame(columns=["Start","End"])

# Variable para guardar tiempos de cambios de status
times=[]

video=cv2.VideoCapture(0)

while True:
    check, frame = video.read()

    # Variable para analizar el movimiento
    status=0

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

        # Si el programa detecta algo con una variación cuya area sea mayor a 1000 pixeles cambiamos la variable status:
        status=1

        # Cuando el área sea mayor a 1000 pixels crearemos el rectángulo
        (x, y, w, h) =cv2.boundingRect(contour)
        # Dibujando el rectángulo creado en el frame
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 3)

    # Rellenando la variable status_list con los valores de la variable status
    status_list.append(status)

    ########################
    # AÑADIDO EN CLASE 175 # -> para evitar colapsar la memoria, y hacer que al imprimir status_list solo nos muestre los dos últimos valores
    ########################
    status_list=status_list[-2:]

    # Condicional para anexar tiempos a la lista times cuando un objeto es detectado
    if status_list[-1]==1 and status_list[-2]==0:
        times.append(datetime.now())

    # Condicional para anexar tiempos a la lista times cuando un objeto deja de ser detectado
    if status_list[-1]==0 and status_list[-2]==1:
        times.append(datetime.now())

    #cv2.imshow("Gray frame", gray)
    #cv2.imshow("Delta frame", delta_frame) # para mostrar el video en deltaframe
    #cv2.imshow("Threshhold frame", thresh_frame) # para mostrar el video en threshold, blanco y negro por siluetas
    cv2.imshow("Color", frame) # para ver la imagen en color y con el rectángulo de detección de movimiento

    key=cv2.waitKey(1)

    if key==ord('q'):
        # Añadir tiempo final si el progrmaa se cierra con objeto en pantalla (haciendo que no genere tiempo de cierre)
        if status==1:
            times.append(datetime.now())
        break
    
# Imprimimos la variable status_list al finalizar
print(status_list)
# Imprimimos la variable times al finalizar
print(times)

# Bucle para iterar (tantas veces como valores tenga la lista times, con un step de 2 - valores de 2 en 2-) por la lista times e incluir los datos en la variable DataFrame
for i in range(0, len(times),2):
    new_row=pandas.DataFrame({"Start":[times[i]], "End":[times[i+1]]})
    df=pandas.concat([df, new_row], ignore_index=True)

# Creación del archivo CSV
df.to_csv("downloads/Times.csv")

video.release() 
cv2.destroyAllWindows
print("Webcam Off")