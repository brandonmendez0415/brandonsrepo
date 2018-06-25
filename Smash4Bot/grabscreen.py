import numpy as np
import cv2
import mss

def grab_screen(sct, box):
    rgb = np.array(sct.grab(box))
    r = rgb.copy()
    r[:, :, 0] = r[:, :, 2]
    r[:, :, 1] = r[:, :, 2]
    gray = cv2.cvtColor(r, cv2.COLOR_RGB2GRAY)
    return gray
