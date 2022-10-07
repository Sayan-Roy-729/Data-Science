import numpy as np
import cv2


##############
## FUNCTION ##
##############

def draw_circle(event, x, y, flags, param):
    
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, center = (x, y), radius=100, color=(0, 255, 0), thickness=-1)

cv2.namedWindow(winname="my_drawing")
cv2.setMouseCallback("my_drawing", draw_circle)

###############################
## SHOWING IMAGE WITH OPENCV ##
###############################

img = np.zeros((512, 512, 3), dtype=np.uint8)

while True:
    cv2.imshow("my_drawing", img)
    
    # break the loop while pressing the Esc key on keyboard
    if cv2.waitKey(20) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()
