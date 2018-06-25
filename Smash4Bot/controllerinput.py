import pyvjoy

class ControllerInputs(object):
    MAX_VJOY = 32767
    THRESHOLD = 0.75

    def __init__(self, VJoyDeviceNumber):
        self.device = pyvjoy.VJoyDevice(VJoyDeviceNumber)

    def setAllInputs(self, activations):
        self.A(activations[0])
        self.B(activations[1])
        self.X(activations[2])
        self.Y(activations[3])
        self.L(activations[4])
        self.R(activations[5])
        self.ZL(activations[6])
        self.ZR(activations[7])
        self.DUp(activations[8])
        self.DDown(activations[9])
        self.DLeft(activations[10])
        self.DRight(activations[11])
        self.LeftY(activations[12])
        self.LeftX(activations[13])
        self.RightY(activations[14])
        self.RightX(activations[15])

    def reset(self):
        self.device.reset()
        self.LeftY(0.5)
        self.LeftX(0.5)
        self.RightY(0.5)
        self.RightX(0.5)
    
    def A(self, activation):
        if activation > self.THRESHOLD:
            self.device.set_button(1,1)
        else:
            self.device.set_button(1,0)
    def B(self, activation):
        if activation > self.THRESHOLD:
            self.device.set_button(2,1)
        else:
            self.device.set_button(2,0)
    def X(self, activation):
        if activation > self.THRESHOLD:
            self.device.set_button(3,1)
        else:
            self.device.set_button(3,0)
    def Y(self, activation):
        if activation > self.THRESHOLD:
            self.device.set_button(4,1)
        else:
            self.device.set_button(4,0)
    def L(self, activation):
        if activation > self.THRESHOLD:
            self.device.set_button(5,1)
        else:
            self.device.set_button(5,0)
    def R(self, activation):
        if activation > self.THRESHOLD:
            self.device.set_button(6,1)
        else:
            self.device.set_button(6,0)
    def ZL(self, activation):
        if activation > self.THRESHOLD:
            self.device.set_button(7,1)
        else:
            self.device.set_button(7,0)
    def ZR(self, activation):
        if activation > self.THRESHOLD:
            self.device.set_button(8,1)
        else:
            self.device.set_button(8,0)
    def DUp(self, activation):
        if activation > self.THRESHOLD:
            self.device.set_button(9,1)
        else:
            self.device.set_button(9,0)
    def DDown(self, activation):
        if activation > self.THRESHOLD:
            self.device.set_button(10,1)
        else:
            self.device.set_button(10,0)
    def DLeft(self, activation):
        if activation > self.THRESHOLD:
            self.device.set_button(11,1)
        else:
            self.device.set_button(11,0)
    def DRight(self, activation):
        if activation > self.THRESHOLD:
            self.device.set_button(12,1)
        else:
            self.device.set_button(12,0)
    def LeftY(self, activation):
        self.device.set_axis(pyvjoy.HID_USAGE_Y, int(activation*self.MAX_VJOY))
    def LeftX(self, activation):
        self.device.set_axis(pyvjoy.HID_USAGE_X, int(activation*self.MAX_VJOY))
    def RightY(self, activation):
        self.device.set_axis(pyvjoy.HID_USAGE_RY, int(activation*self.MAX_VJOY))
    def RightX(self, activation):
        self.device.set_axis(pyvjoy.HID_USAGE_RX, int(activation*self.MAX_VJOY))
