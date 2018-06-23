from PIL import ImageGrab
import numpy as np
import cv2
import time

last_time = time.time()
while(True):
    # 800x500 windowed mode
    printscreen =  np.array(ImageGrab.grab(bbox=(0,52,800,500)))
    #Convert view mode to RGB. COLORS STILL STORED AS BGR
    rgb = cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    #Get separate channels. Sets other channels to 0
##    r = rgb.copy()
##    r[:, :, 0] = 0
##    r[:, :, 1] = 0
##    g = rgb.copy()
##    g[:, :, 0] = 0
##    g[:, :, 2] = 0
##    b = rgb.copy()
##    b[:, :, 1] = 0
##    b[:, :, 2] = 0
    print('loop took {} seconds'.format(time.time()-last_time))
    last_time = time.time()
##    cv2.imshow('red', r)
##    cv2.imshow('green', g)
##    cv2.imshow('blue', b)
    cv2.imshow('grayscale', gray)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
