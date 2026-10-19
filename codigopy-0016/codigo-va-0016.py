# Importamos las librerias
import cv2
import matplotlib.pyplot as plt
import os
# ruta de la imagen
ruta_imagen = os.path.join(
    "img-original-0016",
    "tigre.jpg"
)
# Imagen
# Vamos a crear nuestra matriz principal
tigre = cv2.imread(ruta_imagen)
# print (tigre) muestra las matrices de la imagen
# Convertit de BGR a RGB color rojo COLOR_BGR2RGB
tigree = cv2.cvtColor(tigre, cv2.COLOR_BGR2RGB)
# cv2.imshow("tigre color 0016",tigre)
cv2.imshow("tigre color 0016",tigree)
cv2.waitKey(0) #tiempo de espera
cv2.destroyAllWindows() #destruye todas la ventana en memorias