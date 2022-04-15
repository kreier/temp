# /micropython/apps/temperature_tft.py

from machine import Pin, SPI, ADC
import st7789, time

import vga1_16x32 as font

pin_temp = ADC(Pin(36))
pin_temp.atten(ADC.ATTN_11DB)  # full range: 3.3V
pin_lipo = ADC(Pin(34))
pin_lipo.atten(ADC.ATTN_11DB)

white = st7789.color565(255,255,255)
blue  = st7789.color565(0,0,255)
green = st7789.color565(0,255,0)
red   = st7789.color565(255,0,0)
black = st7789.color565(0,0,0)

tft = st7789.ST7789(
    SPI(2, baudrate=30000000, polarity=1, phase=1, sck=Pin(18), mosi=Pin(19), miso=Pin(14)),
    135, 240,
    reset = Pin(23, Pin.OUT),
    cs    = Pin(5,  Pin.OUT),
    dc    = Pin(16, Pin.OUT),
    backlight = Pin(4, Pin.OUT),
    rotation=1)
tft.init()
tft.fill(0)

def main():
    temp_raw = supersample(pin_temp, 100)
    lipo_raw = supersample(pin_lipo, 100)
    text1   = "{:.1f} C   ".format(temp_raw * 0.0793 + 10.8)
#    text2   = "{:.} ".format(lipo_raw)
    text2   = "{:.3f} V   ".format((lipo_raw * 0.000793 + 0.108) * 2)
    tft.text(font, "Temperature:",    0,   0, green, black)
    tft.text(font, text1,           140,  32, white, black)
    tft.text(font, "Voltage LiPo:",   0,  74, blue,  black)
    tft.text(font, text2,           140, 102, red,   black)

def supersample(pin, iterations):
    raw = 0
    for k in range(iterations):
        raw += pin.read()
    raw = raw / iterations
    return raw

while True:
    main()
    time.sleep(0.5)
    
print("Done.")
