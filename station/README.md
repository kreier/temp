# Temp project - measurement station

## Code in MicroPython with a T-Display

This setup allows for easier debugging, direct response in REPL and on the display.

The firmware was taken from Russ Hughes [st7789 Micropython](https://github.com/russhughes/st7789_mpy/) project. Latest here: 1.18. Flashing with
``` sh
esptool.exe flash_id
esptool.exe read_mac

esptool.exe --port COM23 erase_flash
esptool.exe --port COM23 write_flash -z 0x1000 firmware.bin
```

Programming was done with Thonny.

``` py
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
```

## Initial idea from November 24, 2021

For simplicity we program the measurement station in Arduino C.  The software has main 3 tasks to perform

- Measure the temperature
- Connect to the WiFi
- Connect to the server/API and submit the data

Further extensions can include

- Analyse the response from the server for successful submission
- Have the station powered by a LiIon backup battery
- Check battery voltage and adjust power consumption (deep_sleep) accordingly
- Store measurements locally if submission to the database is not possible
