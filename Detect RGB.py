import cv2 
import numpy as np

vid = cv2.VideoCapture(0)

while True:
    _, frame = vid.read()
    
    cv2.imshow("frame", frame)
    
    #setting values for base colors
    b = frame[:,:,0]
    g = frame[:,:,1]
    r = frame[:,:,2]
    
    #computing the mean
    b_mean = np.mean(b)
    g_mean = np.mean(g)
    r_mean = np.mean(r)
    
    print("Blue" if b_mean > g_mean and b_mean > r_mean else "Green" if g_mean > r_mean and g_mean > b_mean else "Red" )
    
    #Breaking the loop if "q" is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

vid.release()
cv2.destroyAllWindows()