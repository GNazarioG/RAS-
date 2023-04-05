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
    #Redefine os novos pixels com base no resto da divisao
    imagem[y, x] = (x%256,y%256,x%256) 
cv2.imshow("Imagem modificada_2.2", imagem) #Mostra a imagem
cv2.waitKey(0) #Espera para fechar a imagem modificada
