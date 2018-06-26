import numpy as np
import cv2
import mss
import time
import pyvjoy
import grabscreen as gs
from controllerinput import ControllerInputs
import random

# gives us time to get situated in the game
for i in list(range(4))[::-1]:
    print(i+1)
    time.sleep(1)
j=ControllerInputs(1)

box = {'top': 52, 'left': 8, 'width': 800, 'height': 448}
sct = mss.mss()
last_time = time.time()
while True:
    screen = gs.grab_screen(sct, box)
    screen = cv2.resize(screen, (80, 45))
    cv2.imshow('test', screen)
    activations = [random.random(),random.random(),random.random(),random.random(),
                   random.random(),random.random(),random.random(),random.random(),
                   random.random(),random.random(),random.random(),random.random(),
                   random.random(),random.random(),random.random(),random.random()]
    j.setAllInputs(activations)
##    time.sleep(0.015)
    print('loop took {} seconds'.format(time.time()-last_time))
    last_time = time.time()
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
