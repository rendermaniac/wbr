from microbit import pin2, running_time, display, Image, sleep
import os
from utime import ticks_ms

n = len(os.listdir())
f = open("sound{}.csv".format(n + 1), "w")
display.show(Image.NO)

while True:
    s = pin2.read_analog()
    t = ticks_ms()
    f.write("{},{}\n".format(t, s))
    sleep(200)

    if t > 60000:
        break


display.show(Image.YES)
f.close()