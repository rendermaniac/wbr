from microbit import display, Image, button_a, sleep, running_time
import os
import bme280

calibrate = 500
duration = 60000
max_height = 0

display.show(Image.HAPPY)
bme = bme280.bme280()
bme.set_qnh(bme.pressure())

offset = 0.0
for x in range(calibrate):
    hc = bme.altitude()
    offset += hc
    sleep(10)

offset = hc / calibrate 
display.show(Image.YES)

if not button_a.is_pressed():
    
    n = len(os.listdir())
    data = open("alt{}.csv".format(n-2), "w")
    data.write("time,altitude\n")
    delay = running_time()

    while True:
        td = running_time() - delay

        if not td % 200:
            h = bme.altitude() + offset
            max_height = h if h > max_height else max_height
            data.write("{},{}\n".format(td, h))

        if td > duration:
            break

    data.close()
    display.scroll("{:.2f}".format(max_height), loop=True)

else:
    display.show(Image.NO)