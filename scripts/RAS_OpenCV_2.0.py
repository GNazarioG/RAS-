#Missao OpenCV
#Gabriel Nazario Goncalves

#Importação da biblioteca
import cv2

#Ler a imagem como função imread
#Primeiro argumento: Nome da imagem
imagem = cv2.imread('Missao_RAS.png')
#Procurar cor do pixel
(b, g, r) = imagem[250, 250] #veja que a ordem BGR e não RGB
print('O pixel (0, 0) tem as seguintes cores:')
print('Vermelho:', r, 'Verde:', g, 'Azul:', b)

#Resultado do terminal: 255,255,255 (RGB)
#Portanto, cor do pixel é branco