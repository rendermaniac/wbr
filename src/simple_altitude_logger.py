from microbit import display, Image,sleep, running_time
import os
import bme280

delay = 1000
duration = 12000
max_height = 0

display.show(Image.HAPPY)
sleep(1000)
bme = bme280.bme280()
bme.set_qnh(bme.pressure())

n = len(os.listdir())
data = open("alt{}.csv".format(n-2), "w")
data.write("time,altitude\n")

while True:
    td = running_time() - delay

    if not td % 200:
        h = bme.altitude()
        max_height = h if h > max_height else max_height
        data.write("{},{}\n".format(td, h))

    if td > duration:
        break

data.close()
display.scroll("{:.2f}".format(max_height), loop=True)