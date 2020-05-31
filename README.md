# wbr

The acronym wbr stands for water bottle rocket software. This currently logs altitude based on a micro:bit connected to an enviro:bit sensor board.

Current features include:

* Automatic sequential file naming
* Abort option to cancel logging
* Altimeter Calibration step
* Countdown whilst logging data
* Maximum height display
* Stores data for up to 5 flights. Will abort if disk is full

Logging is determined by time delay rather than acting off a trigger.

The driver software is a slightly modifed version of the enviro:bit python library https://github.com/pimoroni/micropython-envirobit
