
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
from ultrasound import ultrasound
import time
SERVO = "P8_13"
TRIGGER_I = "P9_12"
TRIGGER_II = "P9_16"
ECHO_I = "P9_23"
ECHO_II = "P9_14"


# duty_min = 3
# duty_max = 14.5
# duty_span = duty_max - duty_min

# PWM.start(SERVO, (100-duty_min), 60.0, 1)

us1 = ultrasound(TRIGGER_I, ECHO_I)
us2 = ultrasound(TRIGGER_II, ECHO_II)



while True:
    dist = us1.distance()
    time.sleep(0.1)
    distII = us2.distance()
    time.sleep(0.1)
    print(dist ," | ", distII)


    # print ("    Measured Distance = %.1f cm" % dist)
    # print ("medida ultrasounII = %.2f" % distance)
# GPIO.setup(TRIGGER_I, GPIO.OUT)
# GPIO.setup(TRIGGER_II, GPIO.OUT)
# GPIO.setup(ECHO_I, GPIO.IN)
# GPIO.setup(ECHO_II, GPIO.IN)
#
# while True:
#     angle = input("Angle (0 to 180 x to exit):")
#     if angle == 'x':
#         PWM.stop(SERVO)
#         PWM.cleanup()
#         break
#     angle_f = float(angle)
#     duty = 100 - ((angle_f / 180) * duty_span + duty_min)
#     PWM.set_duty_cycle(SERVO, duty)
