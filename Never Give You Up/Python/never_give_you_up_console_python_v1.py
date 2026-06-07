import cv2
import os
import pygame
import time

video_path = "NeverGiveYouUp.mp4"
audio_path = "never-give-you-up-audio.mp3"
chars = ["█", "#", "@", "S", "%", "?", "*", "+", ";", ":", ",", "."]

pygame.mixer.init()
pygame.mixer.music.load(audio_path)
cap = cv2.VideoCapture(video_path)

fps = cap.get(cv2.CAP_PROP_FPS)

pygame.mixer.music.play()
start_time = time.time()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret: break
    
    elapsed_time = time.time() - start_time
    
    target_frame = int(elapsed_time * fps)
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    small = cv2.resize(gray, (120, 30))
    
    output = ""
    for row in small:
        for pixel in row:
            if pixel < 30:
                output += " "
            else:
                index = min((255 - pixel) // 22, len(chars) - 1)
                output += chars[index]
        output += "\n"
    
   # os.system('cls' if os.name == 'nt' else 'clear')
    print(output, end="")
    
    time.sleep(max(0, (1/fps) - (time.time() - start_time - (target_frame/fps))))

cap.release()
pygame.mixer.music.stop()