import cv2
import mediapipe as mp
import pyautogui
import time 

mp_hands= mp.solutions.hands
hands= mp_hands.Hands()

cap= cv2.VideoCapture(0)
while True:
    ret, frame= cap.read()
    if not ret:
        break
    frame= cv2.flip(frame,1)
    
    rgb=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    result= hands.process(rgb)
    
    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:
            fingers=0
            if hand.landmark[4].x<hand.landmark[3].x:
                fingers+=1
                
            if hand.landmark[8].x<hand.landmark[6].x:
                fingers+=1
                
                
            if hand.landmark[12].x<hand.landmark[10].x:
                fingers+=1
                
                
            if hand.landmark[16].x<hand.landmark[14].x:
                fingers+=1
                
                
            if hand.landmark[20].x<hand.landmark[18].x:
                fingers+=1
                
           
            
            if fingers==5:
                pyautogui.scroll(200)
                print("scroll up")
                time.sleep(0.5)
            
            if fingers==0:
                pyautogui.scroll(-200)
                print("scroll down")
                time.sleep(0.5)
            
            if fingers==2:
                pyautogui.press('space')
                print(" pause/play")
                time.sleep(0.5)
    
    cv2.imshow('Object Detection',frame)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()