import cv2

vid = cv2.VideoCapture(0)

while True:
    r, frame = vid.read()
    if r:
        frame = cv2.flip(frame, 1)
        cv2.imshow("Camera", frame)
        cv2.imwrite("images/mask.jpeg", frame)
        if cv2.waitKey(5) & 0xff == ord('p'):
            break

vid.release()
cv2.destroyAllWindows()