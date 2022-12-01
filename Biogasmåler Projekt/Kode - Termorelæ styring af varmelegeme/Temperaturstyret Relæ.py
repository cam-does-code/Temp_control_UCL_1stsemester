from machine import Pin
from time import sleep
import dht

# ESP32 GPIO 32
relay = Pin(32, Pin.OUT)
relay_pump = Pin(26, Pin.OUT)
sensor = dht.DHT11(Pin(2))

while True:
    sensor.measure()
    temp = sensor.temperature()
      
    print('Temperature: ', temp, 'C') 
    if temp >= 24:
        relay.value(0)
    elif temp < 24:
        relay.value(1)
    sleep(2)

# while True:
#   # RELAY ON
#   relay.value(0)
#   print('off')
#   sleep(2)
#   # RELAY OFF
#   relay.value(1)
#   print('on')
#   sleep(2)