from machine import Pin, SPI
import st7789

import vga1_16x32 as font

def main():
    tft = st7789.ST7789(
        SPI(2, baudrate=30000000, polarity=1, phase=1, sck=Pin(18), mosi=Pin(19)),
        135,
        240,
        reset=Pin(23, Pin.OUT),
        cs=Pin(5, Pin.OUT),
        dc=Pin(16, Pin.OUT),
        backlight=Pin(4, Pin.OUT),
        rotation=3)

    tft.init()
    tft.fill(0)
    tft.text(
        font,
        "Temperature",
        30,
        10,
        st7789.color565(255,255,255),
        st7789.color565(0,0,0)
    )
    tft.text(font,"38.5 C",60,60,st7789.color565(255,255,255),st7789.color565(0,0,0))

main()
