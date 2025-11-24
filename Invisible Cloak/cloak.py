import cv2
import numpy as np

# opens webcam
vid = cv2.VideoCapture(0)

#taking bg image 
bg = cv2.imread("images/mask.jpeg")

while True:
    r, frame = vid.read()
    if r:
        frame = cv2.flip(frame, 1)
    
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        #color codes for the cloak
        lb = np.array([85, 30, 120])
        ub = np.array([105, 255, 255])

        mask = cv2.inRange(hsv, lb, ub)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))
        mask = cv2.dilate(mask, np.ones((3,3), np.uint8), iterations=1)

        inv_mask = cv2.bitwise_not(mask)

        res1 = cv2.bitwise_and(frame, frame, mask=inv_mask)
        res2 = cv2.bitwise_and(bg, bg, mask=mask)
        
        cl = cv2.addWeighted(res1, 1, res2, 1, 0)

        cv2.imshow("Camera", cl)

        if cv2.waitKey(1) & 0xff == ord('m'):
            break

vid.release()
cv2.destroyAllWindows()