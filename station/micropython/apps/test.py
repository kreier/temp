from machine import Pin, SPI
import st7789
spi = SPI(2, baudrate=30000000, polarity=1, phase=1, sck=Pin(18), mosi=Pin(19), miso=Pin(14))
display = st7789.ST7789(
    spi, 135, 240,
    reset     = Pin(23, Pin.OUT),
    cs        = Pin(5,  Pin.OUT),
    dc        = Pin(16, Pin.OUT),
    backlight = Pin(4,  Pin.OUT),
    rotation  = 1)
        
display.init()
display.fill(65535)
