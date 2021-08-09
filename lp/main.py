from machine import Pin
import machine
import utime
from . import wifi
from . import wifi_info


def blink_led():
    led = Pin(25, Pin.OUT)
    for _ in range(3):
        led.on()
        utime.sleep(1)
        led.off()
        utime.sleep(1)


def to_low_power(sec: int):
    machine.deepsleep(sec*1000)

def connect_wifi():
    wf = wifi.WIFI(wifi_info.SSID, wifi_info.PASSWORD)
    wf.up()


def main():
    print("start")
    print("wifi connectiong...")
    connect_wifi()
    print("done")

    print("working ...")
    blink_led()
    print("work done")

    print("good night!")
    to_low_power(10)
