from machine import Pin, ADC
from time import sleep

oversampling = 100

volt_lm35 = ADC(Pin(12))
volt_lm35.atten(ADC.ATTN_11DB)  # full range: 3.3V

for i in range(20):
    volt_raw = 0
    for cycle in range(oversampling):
        volt_raw += volt_lm35.read()
    volt_raw = volt_raw / oversampling
    print("The raw voltage is {:.}".format(volt_raw))
    temperature = volt_raw * 0.826 + 150
    print("The Temperature is {:1.2} °C".format(temperature / 10))
    sleep(1)
   