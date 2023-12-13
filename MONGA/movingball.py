import cv2

cap = cv2.VideoCapture(r"C:\Users\Maker-R03\DISSEMINA-IFF\MONGA\img\movingball.mp4")

# Create the MOG2 background subtractor object
mog = cv2.createBackgroundSubtractorMOG2()


while cap.isOpened():
    ret, gray = cap.read()

    # Apply background subtraction
    fgmask = mog.apply(gray)

    
    # Display the foreground mask
    if ret:
        resizedFgmask = cv2.resize(fgmask, None, fx = 0.5, fy = 0.5)
        cv2.imshow("foreground", resizedFgmask)
    else:
       print('no video')
       cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
       continue

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()