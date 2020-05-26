from bme280 import bme280
from microbit import display, Image, running_time

bme = bme280()
p0 = bme.pressure()
bme.set_qnh(p0)
display.show(Image.YES)

while True:
    if not running_time() % 100:
        print ((bme.altitude(),))
        print('\n')