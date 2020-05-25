# See https://physics.stackexchange.com/questions/333475/how-to-calculate-altitude-from-current-temperature-and-pressure
from microbit import display, Image, running_time
import math
import bme280

bme = bme280.bme280()
p0 = bme.pressure()
bme.set_qnh(p0)
display.show(Image.YES)

while True:
    if not running_time() % 100:
        barometric = bme.altitude()
        p = bme.pressure()
        t = bme.temperature()
        hyposometric = ((math.pow((p0/p), 1.0/5.257) - 1.0) * (t + 273.15)) / 0.0065
        print ((barometric,hyposometric))
        print('\n')