#Missao OpenCV
#Gabriel Nazario Goncalves

#Importação da biblioteca
import cv2

#Ler a imagem como função imread
#Primeiro argumento: Nome da imagem
#Segundo argumento: Definição de Cor
imagem = cv2.imread('Missao_RAS.png',cv2.IMREAD_COLOR)

#Imprime no terminal as dimensoes da imagem escolhida
#largura da imagem
print('Largura em pixels: ', end='')
print(imagem.shape[1]) 
#altura da imagem
print('Altura em pixels: ', end='')
print(imagem.shape[0]) 
#Definição de cor
print('Qtde de canais: ', end='')
print(imagem.shape[2]) 

#Nome da aba da imagem
cv2.imshow("Nome da janela", imagem)
#Espera pressionar qualquer tecla 
cv2.waitKey(0) 

#Escreve na pasta, a imagem que foi visualizada com nome "Saida"
cv2.imwrite("saida.jpg", imagem)
