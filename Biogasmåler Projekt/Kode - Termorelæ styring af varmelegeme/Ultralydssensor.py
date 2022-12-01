from hcsr04 import HCSR04
from time import sleep
from machine import Pin

# ESP32
sensor = HCSR04(trigger_pin=14, echo_pin=12, echo_timeout_us=10000)
relay = Pin(32, Pin.OUT)

while True:
    distance = sensor.distance_cm()
    print('Distance:', distance, 'cm')
    if distance < 10:
        relay.value(1)
    else:
        relay.value(0)
    sleep(1)