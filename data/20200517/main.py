from microbit import display as d, Image, sleep, pin2
from os import listdir
from utime import ticks_ms, ticks_diff
import bme280

st = 0
f = None
b = bme280.bme280()
state = 0

def setup():
    d.show(Image.HAPPY)
    b.set_qnh(b.pressure())
    return 1

def ready():
    return 2

def launch():
    global f, st
    n = len(listdir())
    f = open("alt{}.csv".format(n - 2), "w")
    st = ticks_ms()
    d.show(Image.TRIANGLE)
    return 3

def fly():
    eft = ticks_diff(ticks_ms(), st)
    if eft > 60000:
        return 4
    f.write("{},{},{}\n".format(eft, b.altitude(), pin2.read_analog()))
    sleep(200)
    return 3

def land():
    d.show(Image.YES)
    f.close()
    return 4

while True:
    state = [setup, ready, launch, fly, land][state]()