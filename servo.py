import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
pwm=GPIO.PWM(11, 1)
pwm.start(0)
pwm.ChangeDutyCycle(5) # left -90 deg position
sleep(1)
pwm.stop()
GPIO.cleanup()