import cv2

import numpy as np

import matplotlib.pyplot as plt


####################
## FUNCTION ##
####################

def draw_circle(event,x, y, flags, param): # event is right click left click etc. , flags and param are extra parameter
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),100,(0,255,0),-1) # 100 is radius

cv2.namedWindow(winname='mouse_drawing')
cv2.setMouseCallback('mouse_drawing', draw_circle)




###############################
## SHOWING IMAGE WITH OPEN CV ##
################################




img = np.zeros((512,512,3),dtype=np.int16)
while True:
    cv2.imshow('mouse_drawing', img)
    
    if cv2.waitKey(20) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()