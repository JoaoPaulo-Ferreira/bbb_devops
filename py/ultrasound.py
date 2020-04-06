import Adafruit_BBIO.GPIO as GPIO
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
        sleep(0.1)
        return distance
