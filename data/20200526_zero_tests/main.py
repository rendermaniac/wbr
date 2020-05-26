import bme280
import os
from microbit import display, Image, button_a, sleep, running_time

calibrate = 300
duration = 120000 # logging time in ms
countdown = 120

if not button_a.is_pressed():

    n = len(os.listdir()) - 1 # 1 indexed

    hc = 0.0
    offset = 0.0
    max_height = 0.0

    bme = bme280.bme280()
    bme.set_qnh(bme.pressure())

    if n > 5:
        display.scroll("Disk Full!", loop=True) # blocks

    display.scroll("calibrating ")
    for x in range(calibrate):
        hc = bme.altitude()
        offset += hc
        sleep(10)

    data = open("flt{}.csv".format(n), "w")
    data.write("time,altitude\n")
    offset = hc / calibrate
    delay = running_time()

    while True:
        td = running_time() - delay # will be zero

        if not td % 2000:
            if countdown == 0:
                display.show(Image.YES)
            else:
                display.scroll("{:d}".format(countdown))
            countdown -= 2

        if not td % 400:
            h = bme.altitude() + offset # compensate for ground error
            max_height = h if h > max_height else max_height
            data.write("{},{}\n".format(td, h))

        if td > duration:
            break

    data.close()
    sleep(2000)
    display.scroll("max height: {:.2f}m flights left: {:d}".format(max_height, 5-n), loop=True)

else:
    display.show(Image.NO)