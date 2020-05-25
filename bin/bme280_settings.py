# See https://github.com/adafruit/Adafruit_CircuitPython_BMP280/blob/master/adafruit_bmp280.py#L289

STANDBY_TC_0_5 = 0x00   # 0.5ms
STANDBY_TC_10 = 0x06    # 10ms
STANDBY_TC_20 = 0x07    # 20ms
STANDBY_TC_62_5 = 0x01  # 62.5ms
STANDBY_TC_125 = 0x02   # 125ms
STANDBY_TC_250 = 0x03   # 250ms
STANDBY_TC_500 = 0x04   # 500ms
STANDBY_TC_1000 = 0x05  # 1000ms

IIR_FILTER_DISABLE = 0
IIR_FILTER_X2 = 0x01
IIR_FILTER_X4 = 0x02
IIR_FILTER_X8 = 0x03
IIR_FILTER_X16 = 0x04

OVERSCAN_DISABLE = 0x00
OVERSCAN_X1 = 0x01
OVERSCAN_X2 = 0x02
OVERSCAN_X4 = 0x03
OVERSCAN_X8 = 0x04
OVERSCAN_X16 = 0x05

MODE_SLEEP = 0x00
MODE_FORCE = 0x01
MODE_NORMAL = 0x03

def get_ctrl_meas(overscan_temperature, overscan_pressure, mode):
    ctrl_meas = overscan_temperature << 5
    ctrl_meas += overscan_pressure << 2
    ctrl_meas += mode
    return ctrl_meas

def get_config(t_standby, iir_filter, mode):
    config = 0
    if mode == MODE_NORMAL:
        config += t_standby << 5
    if iir_filter:
        config += iir_filter << 2
    return config

mode = MODE_NORMAL
ctrl_meas = get_ctrl_meas(OVERSCAN_X1, OVERSCAN_X8, mode)
config = get_config(STANDBY_TC_0_5, IIR_FILTER_DISABLE, mode)
print("CTRL_MEAS {0:b} CONFIG {1:b}".format(ctrl_meas, config))