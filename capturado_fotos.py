import cv2 
import numpy as np
import os

# Para crear las carpetas de las imagenes como Positivas (p) y Negativas (n)
carpeta_positiva = 'p'
carpeta_negativa = 'n'
if not os.path.exists(carpeta_positiva):
  print("carpete creada {}".format(carpeta_positiva))
  os.makedirs(carpeta_positiva)

if not os.path.exists(carpeta_negativa):
  print("carpete creada {}".format(carpeta_negativa))
  os.makedirs(carpeta_negativa)

# Creamos el video streaming
capture = cv2.VideoCapture(0)

# Cordenadas para el rectangulo en pantalla
x1, y1, x2, y2 = 190, 80, 450, 398 

# Texto en pantalla 
msj = 'Imagen Guardada'
# fuente = cv2.FONT_ITALIC;

# Contadores para las imagenes que se guarden en las carpetas
count_img_p = 0
count_img_n = 0

while True:
  ret, frame = capture.read()
  if ret == False: break
  
  # Imaegn auxiliar para almacenar la imagen
  img_aux = frame.copy()
  # Dibjando el rectangulo en la pantalla
  cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 89, 32), 2)

  # Mostramos la imagen auxiliar y se cambia el tamanio para poder hacerlo mas pequeno
  imagen_copia = img_aux[y1:y2, x1:x2]
  imagen_copia = cv2.resize(imagen_copia, (38, 46))
  # Mostramos las imagens
  cv2.imshow('Frame', frame)
  cv2.imshow('Objeto', imagen_copia)

  k = cv2.waitKey(1)
  if k == 27: break

  # Grardamos las imagenes Positivas 
  if k == ord('s'):
    cv2.imwrite(carpeta_positiva+'/objeto_{}.jpg'.format(count_img_p), imagen_copia)
    print("Imagen Positiva Guardada como: {}/objeto_{}.jpg".format(carpeta_positiva, count_img_p))
    count_img_p += 1

  # Grardamos las imagenes Negativas
  if k == ord('n'):
    cv2.imwrite(carpeta_negativa+'/objeto_{}.jpg'.format(count_img_n), imagen_copia)
    print("Imagen Negativa Guardada como: {}/objeto_{}.jpg".format(carpeta_negativa, count_img_n))
    count_img_n += 1

capture.release()
cv2.destroyAllWindows()