from machine import Pin, I2C
from time import sleep
import machine, onewire, ds18x20, time
import ssd1306

# ESP32 GPIO 32
relay = Pin(32, Pin.OUT)
# relay_pump = Pin(26, Pin.OUT)
# sensor = dht.DHT11(Pin(2))
ds_pin = machine.Pin(4)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

roms = ds_sensor.scan()
print('Found DS devices: ', roms)

temp_up = Pin(26, Pin.IN)
temp_down = Pin(25, Pin.IN)
end = Pin(27, Pin.IN)

dat = machine.Pin(22)       # the device is on GPIO0

i2c = I2C(scl=Pin(22), sda=Pin(21), freq=100000)      #Init i2c
lcd=ssd1306.SSD1306_I2C(128,64,i2c)           #create LCD object,Specify col and row

# while True:
#     temp = ds_sensor.read_temp
#     print('Temperature: ', , 'C') 
#     if ds_sensor.read_temp >= 24:
#         relay.value(0)

#     elif ds_sensor.read_temp < 24:
#         relay.value(1)
#     sleep(2)
set_temp = 20
print("set temp")
while True:
        lcd.fill(0)
        lcd.text("Choose temp:",10,16) 
        lcd.text(str(set_temp),10,40)
        lcd.show()
        if temp_up.value() == 1:
            set_temp += 1
            print(set_temp)
        elif temp_down.value() == 1:
            set_temp -= 1
            print(set_temp)
        elif end.value() == 1:
            break
        else:
            continue
x = 0
while True:
    ds_sensor.convert_temp()
    # if end.value() == 1:
    #     while(True):
    #         if temp_up.value() == 1:
    #             set_temp += 1
    #             print(set_temp)
    #         elif temp_down.value() == 1:
    #             set_temp -= 1
    #             print(set_temp)
    #         elif end.value() == 1:
    #             break
    #         else:
    #             continue
    time.sleep_ms(750)
    for rom in roms:
        print(rom)
        print(ds_sensor.read_temp(rom))
        time.sleep(1) 
        lcd.fill(0)
        lcd.text("Set temp:" + str(set_temp),10,16) 
        lcd.text("Current:" + str(ds_sensor.read_temp(rom)),10,40)
        lcd.show() 
        if ds_sensor.read_temp(rom) >= set_temp:
            if x != 0:
                relay.value(0)
                x = 0
        elif ds_sensor.read_temp(rom) < set_temp:
            if x != 1:
                relay.value(1)
                x = 1

          
    time.sleep(1)