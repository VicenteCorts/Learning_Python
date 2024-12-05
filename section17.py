# Clase 151
'''
import cv2

# Cargar la imagen
img = cv2.imread("img/galaxy.jpg",0)

print(type(img))
print(img)
print(img.shape)
print(img.ndim)

resized_image=cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
cv2.imshow("Galaxy", resized_image)
cv2.imwrite("img/Galaxy_resized.jpg", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

'''
# Ejercicio de resize de imagenes Clase 152-153
import cv2
import glob
import os

folder = "img/152/"
images=glob.glob(folder + "*.jpg")

for image in images:
    img=cv2.imread(image,0)
    re=cv2.resize(img,(100,100))
    cv2.imshow("Hey",re)
    cv2.waitKey(400)
    cv2.destroyAllWindows()
    filename = os.path.basename(image)
    output_path = os.path.join(folder, "resized_" + filename)
    cv2.imwrite(output_path,re)
'''

# Clase 155
'''
# Importamos la librería
import cv2

# Creamos el objeto haarcascade
face_cascade=cv2.CascadeClassifier("img/haarcascade_frontalface_default.xml")

# Cargar imagen con cara frontal
img=cv2.imread("img/yo.jpg")
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # Convierte la imagen a escala de grises

# Método para aplicar haarcascade
faces=face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5)

# Dibujando la salida del método anterior en forma de rectángulo
for x, y, w, h in faces:
    img=cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 3)

print(type(faces))
print(faces)

re=cv2.resize(img, (int(img.shape[1]/1.5),int(img.shape[0]/1.5)))

cv2.imshow("Cara", re)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

# Clase 156
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
    # print(check)
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







