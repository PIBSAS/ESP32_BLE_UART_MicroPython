from machine import Pin
import bluetooth
from BLE import BLEUART
import utime
from neopixel import NeoPixel as neo #Porque el ESP32 S3 tiene un Addressable RGB LED Neopixel

name = "Cerveza"
print(name, " Conectado al Ble")

ble = bluetooth.BLE()
uart = BLEUART(ble,name)
#led = Pin(2, Pin.OUT) # ESP32 con led
led = Pin(48, Pin.OUT) # ESP32 con Addressable RGB LED
def on_rx():
    rx_recibe = uart.read().decode().strip()
    uart.write("ESP 32 S3 dice: " + str(rx_recibe) + "\n")
    print(rx_recibe)
    
    ##Esto agregaa en el minuto 15, sin esto el bluetooth ya anda y el celu lo ve
    if rx_recibe == "a":
        #led.value(1) #ESP32 con led
        #ESP32 con Neopixel
        np=neo(led,1)
        np[0] = (127, 0, 0) # Rojo
        np.write()
        ##
        print("on")
    if rx_recibe == "b":
        #led.value(1) #ESP32 con led
        #ESP32 con Neopixel
        np=neo(led,1)
        np[0] = (0, 0, 0) # Se podria elegir otro color en vez de un apagado
        np.write()
        ##
        print("off")
    ##
uart.irq(handler = on_rx)
