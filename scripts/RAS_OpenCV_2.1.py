#Missao OpenCV
#Gabriel Nazario Goncalves

#Importação da biblioteca
import cv2

#Ler a imagem como função imread
#Primeiro argumento: Nome da imagem
imagem = cv2.imread('Missao_RAS.png')
#Varre todos os pixeis da imagem
for y in range(0, imagem.shape[0]):
 for x in range(0, imagem.shape[1]):
    imagem[y, x] = (255,0,0) #Define a cor do pixel para azul (B,G,R)
cv2.imshow("Imagem modificada_2.1", imagem) #Mostra a imagem
#Espera pressionar qualquer tecla 
cv2.waitKey(0) 
