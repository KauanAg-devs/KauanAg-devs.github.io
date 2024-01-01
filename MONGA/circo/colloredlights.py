import cv2 as cv
import pyautogui

cap = cv.VideoCapture(r'/home/kauanag/aaa-dissemina/MONGA/img/colloredlights.gif')
print(cap.isOpened())
screen_width, screen_height = pyautogui.size()

while True:
    bool, frame = cap.read()
    
    if not bool:
        cap.set(cv.CAP_PROP_POS_FRAMES, 0)
        continue

    frame = cv.resize(frame, (screen_width, screen_height))
    cv.imshow('Lights', frame)
    
    key = cv.waitKey(100)

    if key == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
