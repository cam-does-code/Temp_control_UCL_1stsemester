from machine import Pin, PWM, ADC
from time import sleep

pot_pin = 32
pot = ADC(Pin(pot_pin))
pot.atten(ADC.ATTN_11DB) # Kalibrering til korrekte målinger
pot.width(ADC.WIDTH_10BIT) # Fra 0 - 4095 range til 0 - 1023 range 

frequency = 5000
led = PWM(Pin(4), frequency)

while True:
#    for i in range(pot.read()):
    led.duty(pot.read())
    print(pot.read())
    sleep(0.2) 
     
     