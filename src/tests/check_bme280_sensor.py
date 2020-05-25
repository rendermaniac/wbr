from microbit import display, Image, running_time
import bme280

bme = bme280.bme280()
p0 = bme.pressure()
bme.set_qnh(p0)
display.show(Image.YES)

while True:
    if not running_time() % 100:
        print ((bme.altitude(),))
        print('\n')