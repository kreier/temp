from machine import Pin, ADC
from time import sleep

volt_lm35 = ADC(Pin(12))
volt_lm35.atten(ADC.ATTN_11DB)  # full range: 3.3V

while True:
    volt_raw = volt_lm35.read()
    print("The raw voltage is {:.}".format(volt_raw))
    temperature = volt_raw * 0.826 + 150
    print("The Temperature is {:.2} °C".format(temperature / 1000))
    sleep(1)
    