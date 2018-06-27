import numpy as np
import cv2
import mss
import time
import pyvjoy
import grabscreen as gs
from controllerinput import ControllerInputs
import random
import recordinputs as inputs
import os

file_name = 'training_data.npy'

if os.path.isfile(file_name):
    print('File exists, loading previous data...')
    training_data = list(np.load(file_name))
else:
    print('File does not exist, starting fresh')
    training_data = []
# gives us time to get situated in the game
for i in list(range(4))[::-1]:
    print(i+1)
    time.sleep(1)
j=ControllerInputs(1)

box = {'top': 52, 'left': 8, 'width': 800, 'height': 448}
sct = mss.mss()
##last_time = time.time()
while True:
    screen = gs.grab_screen(sct, box)
    screen = cv2.resize(screen, (80, 45))
    presses = inputs.get_inputs()
    training_data.append([screen,presses])
    if len(training_data) % 100 == 0:
        print(len(training_data))
    if len(training_data) % 1000 == 0:
        print("DON'T QUIT YET")
        np.save(file_name, training_data)
        print('Safe to quit')
    

    
##    activations = [random.random(),random.random(),random.random(),random.random(),
##                   random.random(),random.random(),random.random(),random.random(),
##                   random.random(),random.random(),random.random(),random.random(),
##                   random.random(),random.random(),random.random(),random.random()]
##    j.setAllInputs(activations)
##    time.sleep(0.015)
##    print('loop took {} seconds'.format(time.time()-last_time))
##    last_time = time.time()
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
