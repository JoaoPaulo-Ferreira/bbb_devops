import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import time
class ultrasound:
    def __init__(self, TRIGGER, ECHO):
        self.TRIGGER = TRIGGER
        self.ECHO = ECHO
        GPIO.setup(TRIGGER, GPIO.OUT)
        GPIO.setup(ECHO, GPIO.IN)

    def distance(self):
        GPIO.output(self.TRIGGER, GPIO.LOW)
        time.sleep(0.000005)

        GPIO.output(self.TRIGGER, GPIO.HIGH)
        time.sleep(0.00002)

        GPIO.output(self.TRIGGER, GPIO.LOW)

        #variaveis para salvar os tempos
        StartTime = time.time()
        StopTime = time.time()
        #variaveis para controle de timeout,
        #caso fique preso no loop por tempo suficiente para percorrer 2m sai do loop e retorna -1
        ControlStart = time.time()
        ControlStop = time.time()

        while GPIO.input(self.ECHO) == 0:
            StartTime = time.time()
            ControlStop = time.time()
            if((((ControlStop - ControlStart) * 34300)/2) >= 200):
                return -1

        while GPIO.input(self.ECHO) == 1:
            #print("deb2")
            StopTime = time.time()

        TimeElapsed = StopTime - StartTime
        #distance = ((TimeElapsed * 34300) / 2)
        distance = ((TimeElapsed * 34584) / 2)
        return distance

class servo:
    def __init__(self, pin = "P8_13"):
        self.pin = pin
        self.duty_min = 3
        self.duty_max = 14.5
        self.duty_span = self.duty_max - self.duty_min
        PWM.start(pin, (100-self.duty_min), 60.0, 1)

        def set_angle(self, angle):
            angle_f = float(angle)
            duty = 100 - ((angle_f / 180) * self.duty_span + self.duty_min)
            PWM.set_duty_cycle(self.pin, duty)
            return 0
