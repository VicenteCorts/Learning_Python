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










