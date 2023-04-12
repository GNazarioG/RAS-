#Missao Hand Tracking
#Gabriel Nazario Goncalves

# Importacao de biblioteca openCV e mediapipe
# OpenCV: Edição da imagem capturada 
# Mediapipe: Biblioteca usada para o mapeamento da mao
import cv2
import mediapipe as mp

# Capitura da camera
video = cv2.VideoCapture(0)

# Configuracao da leitura das maos
hand = mp.solutions.hands
Hand = hand.Hands(max_num_hands=1) # Uma mao por vez
mpDraw = mp.solutions.drawing_utils

while True:
    check,img = video.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) # Converter BGR/RGB
    results = Hand.process(imgRGB)
    handsPoints = results.multi_hand_landmarks
    # A-Altura da img; L-largura da img; _ -desconsidera a coordenada z
    a,l,_ = img.shape
    # Cria array com par de cords
    pontos = []
    if handsPoints:
        for points in handsPoints:
            #Mapeia e enumera pontos
            mpDraw.draw_landmarks(img,points,hand.HAND_CONNECTIONS)
            for id,cord in enumerate(points.landmark):
                cx,cy = int(cord.x*l), int(cord.y*a)
                pontos.append((cx,cy))

        dedos = [8,12,16,20]
        contador = 0
    # Codificacao dos numeros
        if points:
            # SINAL 1 
            if pontos[8][1] < pontos[6][1]: #Dedo indicador
                if pontos[12][1] > pontos[10][1]: #Dedo medio
                    if pontos[16][1] > pontos[14][1]: #Dedo anelar
                        if pontos[20][1] > pontos[18][1]: #Dedo minimo
                            if pontos[1][0] < pontos[0][0]: #Polegar
                                if pontos[4][0] > pontos[3][0]: #Mao Esquerda
                                    contador = 1
                            else:
                                if pontos[4][0] < pontos[3][0]: #Mao Direita
                                    contador = 1
            # SINAL 2  
            if pontos[8][1] < pontos[6][1]: #Dedo indicador
                if pontos[12][1] < pontos[10][1]: #Dedo medio
                    if pontos[16][1] > pontos[14][1]: #Dedo anelar
                        if pontos[20][1] > pontos[18][1]: #Dedo minimo
                            if pontos[1][0] < pontos[0][0]: #Polegar
                                if pontos[4][0] > pontos[3][0]: #Mao Esquerda
                                    contador = 2
                            else:
                                if pontos[4][0] < pontos[3][0]: #Mao Direita
                                    contador = 2
            # SINAL 3  
            if pontos[8][1] < pontos[6][1]: #Dedo indicador
                if pontos[12][1] < pontos[10][1]: #Dedo medio
                    if pontos[16][1] < pontos[14][1]: #Dedo anelar
                        if pontos[20][1] > pontos[18][1]: #Dedo minimo
                            if pontos[1][0] < pontos[0][0]: #Polegar
                                if pontos[4][0] > pontos[3][0]: #Mao Esquerda
                                    contador = 3
                            else:
                                if pontos[4][0] < pontos[3][0]: #Mao Direita
                                    contador = 3
            # SINAL 4
            if pontos[8][1] < pontos[6][1]: #Dedo indicador
                if pontos[12][1] < pontos[10][1]: #Dedo medio
                    if pontos[16][1] < pontos[14][1]: #Dedo anelar
                        if pontos[20][1] < pontos[18][1]: #Dedo minimo
                            if pontos[1][0] < pontos[0][0]: #Polegar
                                if pontos[4][0] > pontos[3][0]: #Mao Esquerda
                                    contador = 4
                            else:
                                if pontos[4][0] < pontos[3][0]: #Mao Direita
                                    contador = 4
            # SINAL 5
            if pontos[8][1] < pontos[6][1]: #Dedo indicador
                if pontos[12][1] < pontos[10][1]:  #Dedo medio
                    if pontos[16][1] < pontos[14][1]: #Dedo anelar
                        if pontos[20][1] < pontos[18][1]: #Dedo minimo
                            if pontos[1][0] < pontos[0][0]: #Polegar
                                if pontos[4][0] < pontos[3][0]: #Mao Esquerda
                                    contador = 5
                            else:
                                if pontos[4][0] > pontos[3][0]: #Mao Direita
                                    contador = 5
            # SINAL 6
            if pontos[8][1] > pontos[6][1]: #Dedo indicador
                if pontos[12][1] > pontos[10][1]: #Dedo medio
                    if pontos[16][1] > pontos[14][1]: #Dedo anelar
                        if pontos[20][1] < pontos[18][1]: #Dedo minimo
                            if pontos[1][0] < pontos[0][0]: #Polegar
                                if pontos[4][0] > pontos[3][0]: #Mao Esquerda
                                    contador = 6
                            else:
                                if pontos[4][0] < pontos[3][0]: #Mao Direita
                                    contador = 6
            # SINAL 7
            if pontos[8][1] > pontos[6][1]: #Dedo indicador
                if pontos[12][1] > pontos[10][1]: #Dedo medio
                    if pontos[16][1] > pontos[14][1]: #Dedo anelar
                        if pontos[20][1] < pontos[18][1]: #Dedo minimo
                            if pontos[1][0] < pontos[0][0]: #Polegar
                                if pontos[4][0] < pontos[3][0]: #Mao Esquerda
                                    contador = 7
                            else:
                                if pontos[4][0] > pontos[3][0]: #Mao Direita
                                    contador = 7
            # SINAL 8
            if pontos[8][1] < pontos[6][1]: #Dedo indicador
                if pontos[12][1] > pontos[10][1]: #Dedo medio
                    if pontos[16][1] > pontos[14][1]: #Dedo anelar
                        if pontos[20][1] < pontos[18][1]: #Dedo minimo
                            if pontos[1][0] < pontos[0][0]: #Polegar
                                if pontos[4][0] < pontos[3][0]: #Mao Esquerda
                                    contador = 8
                            else:
                                if pontos[4][0] > pontos[3][0]: #Mao Direita
                                    contador = 8
            # SINAL 9
            if pontos[8][1] < pontos[6][1]: #Dedo indicador
                if pontos[12][1] < pontos[10][1]: #Dedo medio
                    if pontos[16][1] > pontos[14][1]: #Dedo anelar
                        if pontos[20][1] < pontos[18][1]: #Dedo minimo
                            if pontos[1][0] < pontos[0][0]: #Polegar
                                if pontos[4][0] > pontos[3][0]: #Mao Esquerda
                                    contador = 9
                            else:
                                if pontos[4][0] < pontos[3][0]: #Mao Direita
                                    contador = 9
            # SINAL 10
            if pontos[8][1] < pontos[6][1]: #Dedo indicador
                if pontos[12][1] > pontos[10][1]: #Dedo medio
                    if pontos[16][1] > pontos[14][1]: #Dedo anelar
                        if pontos[20][1] < pontos[18][1]: #Dedo minimo
                            if pontos[1][0] < pontos[0][0]: #Polegar
                                if pontos[4][0] > pontos[3][0]: #Mao Esquerda
                                    contador = 10
                            else:
                                if pontos[4][0] < pontos[3][0]: #Mao Direita
                                    contador = 10
        # Colocar numero na imagem
        cv2.putText(img,str(contador),(20,107),cv2.FONT_HERSHEY_SIMPLEX,4,(0,0,0),20)
        cv2.putText(img,str(contador),(20,107),cv2.FONT_HERSHEY_SIMPLEX,4,(0,0,255),5)

    # Janela
    cv2.imshow("Sinal_Fingers",img)
    cv2.waitKey(1)