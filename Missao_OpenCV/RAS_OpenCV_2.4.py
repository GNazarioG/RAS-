#Missao OpenCV
#Gabriel Nazario Goncalves

#Importação da biblioteca
import cv2

#Ler a imagem como função imread
#Primeiro argumento: Nome da imagem
imagem = cv2.imread('Missao_RAS.png')
#Varre todos os pixels da imagem
for y in range(0, imagem.shape[0], 10): #percorre linhas
    for x in range(0, imagem.shape[1], 10): #percorre colunas
         imagem[y:y+5, x: x+5] = (0,255,255) #Espacamento da aplicacao
cv2.imshow("Imagem modificada", imagem) #Mostra a imagem 
cv2.waitKey(0) #Espera para fechar a guia
