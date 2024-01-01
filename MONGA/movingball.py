import cv2

cap = cv2.VideoCapture(0)

# Create the MOG2 background subtractor object
mog = cv2.createBackgroundSubtractorMOG2()


while cap.isOpened():
    ret, gray = cap.read()

    # Apply background subtraction
    fgmask = mog.apply(gray)

    
    # Display the foreground mask
    if ret:
        import pyautogui
        screen_width, screen_height = pyautogui.size()

        fgmask = cv2.resize(fgmask, (screen_width, screen_height))
        cv2.imshow("detect moves", fgmask)
    else:
       print('no video')
       cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
       continue

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()