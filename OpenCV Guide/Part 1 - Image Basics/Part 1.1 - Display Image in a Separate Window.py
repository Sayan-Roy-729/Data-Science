import cv2

img = cv2.imread("../DATA/00-puppy.jpg")

while True:
    cv2.imshow("Puppy", img)
    
    # press the Esc key to close the window & 1 means 1 ms
    if cv2.waitKey(1) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()