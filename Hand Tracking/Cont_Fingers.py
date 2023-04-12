#Missao Hand Tracking
#Gabriel Nazario Goncalves

# Importacao de biblioteca openCV e mediapipe
# OpenCV: Edição da imagem capturada 
# Mediapipe: Biblioteca usada para o mapeamento da mao
import cv2
import mediapipe as mp

video = cv2.VideoCapture(0)

hand = mp.solutions.hands
Hand = hand.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils

while True:
    check,img = video.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = Hand.process(imgRGB)
    handsPoints = results.multi_hand_landmarks
    #A-Altura da img; L-largura da img; _ -desconsidera a coordenada z
    a,l,_ = img.shape
    pontos = []
    if handsPoints:
        for points in handsPoints:
            mpDraw.draw_landmarks(img,points,hand.HAND_CONNECTIONS)
            for id,cord in enumerate(points.landmark):
                cx,cy = int(cord.x*l), int(cord.y*a)
                pontos.append((cx,cy))

        dedos = [8,12,16,20]
        contador = 0
        if points:
            if pontos[1][0] < pontos[0][0]:
                if pontos[4][0] < pontos[3][0]:
                    contador +=1
            else:
                if pontos[4][0] > pontos[3][0]:
                    contador +=1
            
            for x in dedos:
                if pontos[x][1] < pontos[x-2][1]:
                    contador +=1
        cv2.putText(img,str(contador),(107,112),cv2.FONT_HERSHEY_SIMPLEX,4,(0,0,0),20)
        cv2.putText(img,str(contador),(107,112),cv2.FONT_HERSHEY_SIMPLEX,4,(0,0,255),5)

    cv2.imshow("Imagem",img)
    cv2.waitKey(1)