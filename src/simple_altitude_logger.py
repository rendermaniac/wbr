import bme280
import os
from microbit import display, Image, button_a, sleep, running_time

calibrate = 300
duration = 125000 # logging time in ms
countdown = 120

if not button_a.is_pressed():

    n = len(os.listdir()) - 1 # 1 indexed

    hc = 0.0
    offset = 0.0
    max_height = 0.0

    bme = bme280.bme280()

    display.show(Image.CONFUSED)
    bme.set_qnh(bme.pressure())
    for x in range(calibrate):
        hc = bme.altitude()
        offset += hc
        sleep(10)

    fn = "flt{}.csv".format(n)
    data = open(fn, "w")
    data.write("time,altitude\n")
    offset = hc / calibrate
    x = 0
    y = 0
    delay = running_time()
    display.clear()

    while True:
        td = running_time() - delay # will be zero

        if not td % 500:
            h = bme.altitude() + offset # compensate for ground error
            max_height = h if h > max_height else max_height
            df = "{},{}\n".format(td, h)
            data.write(df)

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
    msg = "#{:d}: {:.2f}m".format(n, max_height)
    display.scroll(msg, loop=True)

else:
    display.show(Image.NO)