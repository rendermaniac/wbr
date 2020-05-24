from microbit import display, Image, button_a, sleep, running_time
import os
import math
import bme280

delay = 5000
duration = 30000
max_height = 0

display.show(Image.HAPPY)
bme = bme280.bme280()
p0 = bme.pressure()
sleep(delay)
display.show(Image.YES)

if not button_a.is_pressed():

    p0 = bme.pressure()
    bme.set_qnh(p0)

    n = len(os.listdir())
    data = open("alt{}.csv".format(n-2), "w")
    data.write("time,altitude,pressure,hyposometric,h2\n")

    while True:
        td = running_time() - delay

        if not td % 500:
            h = bme.altitude()
            p = bme.pressure()
            t = bme.temperature()
            h1 = ((math.pow((p0/p), 1.0/5.257) - 1.0) * (t + 273.15)) / 0.0065
            h2 = math.log(p0/p) * ((287.058 * (t + 273.15)) / 9.80665)

            max_height = h2 if h2 > max_height else max_height
            data.write("{},{},{},{},{}\n".format(td, h, p, h1, h2))

        if td > duration:
            break

    data.close()
    display.scroll("{:.2f}".format(max_height), loop=True)

else:
    display.show(Image.NO)