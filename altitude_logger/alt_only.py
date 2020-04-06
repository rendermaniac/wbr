from microbit import display as d, Image, sleep 
import os, utime as t, bme280 as b280
from micropython import const
bme = b280.bme280(); alt = bme.altitude
s = 0; td = 0; launch = False; data = None; n = len(os.listdir())
d.show(Image.HAPPY)
sleep(1000); alt(); sleep(1000)
duration = const(120000); bme.set_qnh(bme.pressure())
lh = alt();
while True:
    h = alt()
    if not launch and h > lh:
        data = open("alt{}.csv".format(n-2), "w")
        s = t.ticks_ms()
        launch = True
    if launch:
        d.show(Image.TRIANGLE)
        td = t.ticks_diff(t.ticks_ms(), s)
        data.write("{},{}\n".format(td, h))
        if td > duration:
            d.show(Image.YES)
            data.close()
            break
    sleep(200)