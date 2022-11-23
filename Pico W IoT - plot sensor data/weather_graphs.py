import anvil.pico
import uasyncio as a
import dht
from machine import Pin

UPLINK_KEY = "<put your Uplink key here>"

sensor = dht.DHT11(Pin(14))

@anvil.pico.callable_async
async def dht11read():
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    return(temp, hum)

# Connect the Anvil Uplink. In MicroPython, this call will block forever.
anvil.pico.connect(UPLINK_KEY)