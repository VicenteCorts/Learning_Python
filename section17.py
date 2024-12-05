# Clase 151
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












