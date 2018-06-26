import xboxinputs as xi


c = xi.XInputJoystick(0)

x = c.get_state().gamepad

inputs = [x.buttons, x.left_trigger, x.right_trigger,
          x.l_thumb_y, x.l_thumb_x, x.r_thumb_y, x.r_thumb_x]

activations = [(inputs[0] & 4096)/4096, (inputs[0] & 8192)/8192,
               (inputs[0] & 16384)/16384, (inputs[0] & 32768)/32768,
               (inputs[0] & 256)/256, (inputs[0] & 512)/512,
               inputs[1]/255, inputs[2]/255,
               (inputs[0] & 1)/1, (inputs[0] & 2)/2,
               (inputs[0] & 4)/4, (inputs[0] & 8)/8,
               (inputs[3]+32768)/65535, (inputs[4]+32768)/65535,
               (inputs[5]+32768)/65535, (inputs[6]+32768)/65535]

print(activations)
##while 1:
##    c = inputs.devices.gamepads[0]
##    print(c.__read_device())
