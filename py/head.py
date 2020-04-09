
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
from comps import *
import time
SERVO = "P8_13"
TRIGGER_I = "P9_12"
TRIGGER_II = "P9_16"
ECHO_I = "P9_23"
ECHO_II = "P9_14"

#############################################################
#                    TEMP                                   #
#############################################################
f = open("measurements.txt", "a")



#############################################################


us1 = ultrasound(TRIGGER_I, ECHO_I)
us2 = ultrasound(TRIGGER_II, ECHO_II)
motor = servo(SERVO)

angle = 0
INCREASE_MODE = True
while True:
    while(INCREASE_MODE == True):
        dist = us1.distance()
        # time.sleep(0.1)
        distII = us2.distance()
        time.sleep(0.1)
        print("distances = ", dist, " | ", distII, "     angle = ", angle)

        #############################################################
        WriteToFile(f, dist, distII, angle):
        #############################################################
        
        if(angle == 180):
            INCREASE_MODE = False
            time.sleep(0.1)
            break
        angle = angle + 1
        motor.set_angle(angle)

    while(INCREASE_MODE == False):
        dist = us1.distance()
        # time.sleep(0.1)
        distII = us2.distance()
        time.sleep(0.1)
        print("distances = ", dist, " | ", distII, "     angle = ", angle)

        #############################################################
        WriteToFile(f, dist, distII, angle):
        #############################################################

        if(angle == -1):
            INCREASE_MODE = True
            time.sleep(0.1)
            break
        angle = angle - 1
        motor.set_angle(angle)
