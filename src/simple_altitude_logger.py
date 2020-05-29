import bme280
import os
from microbit import display, Image, button_a, sleep, running_time

calibrate = 300
duration = 125000 # logging time in ms
countdown = 120
max_files = 5

if not button_a.is_pressed():

    n = len(os.listdir()) - 1 # 1 indexed

    hc = 0.0
    offset = 0.0
    max_height = 0.0

    bme = bme280.bme280()

    if n > max_files:
        display.scroll("Disk Full!", loop=True) # blocks

    display.scroll("calibrating ")
    bme.set_qnh(bme.pressure())
    for x in range(calibrate):
        hc = bme.altitude()
        offset += hc
        sleep(10)

    data = open("flt{}.csv".format(n), "w")
    data.write("time,altitude\n")
    offset = hc / calibrate
    x = 0
    y = 0
    delay = running_time()

    while True:
        td = running_time() - delay # will be zero

        if not td % 500:
            h = bme.altitude() + offset # compensate for ground error
            max_height = h if h > max_height else max_height
            data.write("{},{}\n".format(td, h))

        if not td % 5000:
            display.set_pixel(x, y, 9)
            x = (x + 1) % 5
            if x == 0:
                y = (y + 1) % 5

        if td > duration:
            display.show(Image.YES)
            break

    data.close()
    sleep(2000)
    display.scroll("max height: {:.2f}m flights left: {:d}".format(max_height, max_files-n), loop=True)

else:
    display.show(Image.NO)