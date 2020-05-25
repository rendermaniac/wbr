from microbit import display, Image, button_a, sleep, running_time
import os
import bme280

calibrate = 300
duration = 60000

progress = duration / 10
countdown = 10

offset = 0.0
max_height = 0.0

display.scroll("calibrating ")
bme = bme280.bme280()
bme.set_qnh(bme.pressure())


for x in range(calibrate):
    hc = bme.altitude()
    offset += hc
    sleep(10)

offset = hc / calibrate

if not button_a.is_pressed():

    n = len(os.listdir()) - 1
    data = open("flt{}.csv".format(n), "w")
    data.write("time,altitude\n")
    delay = running_time()

    while True:
        td = running_time() - delay

        if not td % progress:
            if countdown == 0:
                display.show(Image.YES)
            else:
                display.scroll("{:d}".format(countdown))
            countdown -= 1

        if not td % 200:
            h = bme.altitude() + offset
            max_height = h if h > max_height else max_height
            data.write("{},{}\n".format(td, h))

        if td > duration:
            break

    data.close()
    sleep(1000)
    display.scroll("flight {:d}: {:.2f}".format(n, max_height), loop=True)

else:
    display.show(Image.NO)