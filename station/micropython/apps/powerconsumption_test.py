# /micropython/apps/powerconsumption_test.py 2022-04-10
# Power cycle check ESP32 TTGO T-Display

import machine
import network
import time
from machine import Pin, SPI
import st7789
import vga1_bold_16x32 as font

white = st7789.color565(255,255,255)
black = st7789.color565(0,0,0)

def main():
    tft = st7789.ST7789(
        SPI(1, baudrate=30000000, sck=Pin(18), mosi=Pin(19)),
        135,
        240,
        reset=Pin(23, Pin.OUT),
        cs=Pin(5, Pin.OUT),
        dc=Pin(16, Pin.OUT),
        backlight=Pin(4, Pin.OUT),
        rotation=1)

    tft.init()
    tft.text(font, "10s just TFT",    0,   0, white, black)
    time.sleep(10)
    tft.text(font, "10s WIFI    ",    0,  32, white, black)
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    while not wlan.isconnected():
        try:
            wlan.connect("Hofkoh", "kreier2013")
        except:
            print("connection error, retrying")
        print('.', end='')
        time.sleep(1)
    time.sleep(10)
    tft.text(font, "10s Lightsleep",    0,  64, white, black)
    time.sleep(1)
    machine.lightsleep(10000)
    tft.text(font, "10s Deepsleep ",    0,  96, white, black)
    time.sleep(1)
    machine.deepsleep(10000)

main()

