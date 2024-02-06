import cv2
import mediapipe as mp
import time as time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
tipIds = [4, 8, 12, 16, 20]


while True:
   success, img = cap.read()
   img = cv2.flip(img, 1)

   imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

   results = hands.process(imgRGB)

   lmList = []

   lmimportant = [8,12,16,20]
   cv2.putText(img, f'BEDBOUD', (20,img.shape[0]-50),cv2.FONT_HERSHEY_PLAIN, 3, (200,200,200), 4)
   ptime = time.time()
   

   if results.multi_hand_landmarks:
      for handLms in results.multi_hand_landmarks:
         for id, lm in enumerate(handLms.landmark):
            # h, w, c = img.shape
            # cx, cy = int(lm.x * w), int(lm.y * h)
            # lmList.append([id, cx, cy])
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
            lmList.append([id,int(lm.x*img.shape[0]), int(lm.y*img.shape[1])])
            if(len(lmList)==21):
               # print(lmList)
               print(lmList[8])
               xx = lmList[8]
               print(xx)
               cv2.circle(img,(xx[1],xx[2]),1, (0,0,255), cv2.FILLED)
               i = 0
               if(lmList[4][1]<lmList[3][1]):
                  i=i+1
               for bruh in lmimportant:
                  if(lmList[bruh][2]< lmList[bruh-2][2]):
                     i = i+1
                  
               fingers = i
               cv2.putText(img, f'{i}', (30,100), cv2.FONT_HERSHEY_COMPLEX, 4, (0,0,0), 5)
               ctime = time.time()
               fps = 1/(ctime- ptime)
               ptime= ctime
               cv2.putText (img, f'FPS: {int(fps)}',(490,100), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0), 2)           


            
            

           


   cv2.imshow('Hand Tracker', img)
   if cv2.waitKey(5) & 0xff == 27:
      break