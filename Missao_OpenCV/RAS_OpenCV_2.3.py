#Missao OpenCV
#Gabriel Nazario Goncalves

#Importação da biblioteca
import cv2

#Ler a imagem como função imread
#Primeiro argumento: Nome da imagem
imagem = cv2.imread('Missao_RAS.png')
#Varre todos os pixels da iamgem
for y in range(0, imagem.shape[0], 1): 
 for x in range(0, imagem.shape[1], 1): 
    imagem[y, x] = (0,(x*y)%256,0)#Pequena alteração na cor
cv2.imshow("Imagem modificada", imagem) #Mostra a imagem
cv2.waitKey(0) #Espera para fechar a guia
