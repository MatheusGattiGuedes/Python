from gpiozero import TrafficLights
from time import sleep

luz = TrafficLights(2, 3, 4)

luz.green.on()

while True:
    sleep(10)
    luz.green.off()
    luz.amber.on()
    sleep(1)
    luz.amber.off()
    luz.red.on()
    sleep(10)
    luz.red.off()
    luz.green.on()
