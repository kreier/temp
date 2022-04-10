# /micropython/apps/temperature_mqtt.py  2022-04-09
import network
import secrets
import time
from machine import Pin, SPI, ADC
from mqtt import MQTTClient 

try:
    from secrets import secrets
except ImportError:
    print("WiFi secrets are kept in secrets.py, please add them there!")
    raise

start    = 0
last_msg = 0

aio_topic = secrets["aio_username"] + "/feeds/temperature"
wlan = network.WLAN(network.STA_IF)

pin_temp = ADC(Pin(12))
pin_temp.atten(ADC.ATTN_11DB)  # full range: 3.3V
pin_lipo = ADC(Pin(34))
pin_lipo.atten(ADC.ATTN_11DB)

def sub_cb(topic, msg):
    last_msg = float(msg.decode('UTF-8'))
    print("Returned:", last_msg, "pure bytecode:", msg, "as string", msg.decode('UTF-8'))

def wifi_start():
    wlan.active(True)
    while not wlan.isconnected():
        try:
            wlan.connect(secrets["ssid"], secrets["password"])
        except:
            print("connection error, retrying")
        print('.', end='')
        time.sleep(1)

def wifi_stop():
    wlan.active(False)

def supersample(pin, iterations):
    raw = 0
    for k in range(iterations):
        raw += pin.read()
    raw = raw / iterations
    return raw

def aio_send(message):
    #wifi_start()
    #client.ping()
    failure = True
    while failure:
        try:
            client.publish(topic=aio_topic, msg=message)
            failure = False
        except:
            client.connect()
            client.subscribe(topic=aio_topic)
            print("This did not work")
        time.sleep(1)
        if failure == False:
            try:
                failure = True
                client.check_msg()
                failure = False
            except:
                print("Some error.")
        print('.', end='')



    temp_raw = supersample(pin_temp, 100)
    lipo_raw = supersample(pin_lipo, 100)

print("Connecting to %s " % secrets["ssid"], end='')
wifi_start()
print("\nConnection to Wifi successful.") 
 
client = MQTTClient("device_id", "io.adafruit.com", user=secrets["aio_username"], password=secrets["aio_password"], port=1883) 
client.set_callback(sub_cb)
print("Connecting to AIO ...")
client.connect()
client.subscribe(topic=aio_topic)
print("Success!")

while True:
    temp_raw = supersample(pin_temp, 100)
    lipo_raw = supersample(pin_lipo, 100)
    text_temp = "{:.1f} C   ".format(temp_raw * 0.0793 + 10.8)
    text_lipo = "{:.3f} V   ".format((lipo_raw * 0.000793 + 0.108) * 2)
    print("Sending:", text_temp)
    start = time.ticks_ms()
    aio_send(text_temp)
    print("The roundtrip for this message took {:.0f} milliseconds".format(time.ticks_ms() - start - 1000))
    time.sleep(60) 

