# /micropython/apps/mqtt_test.py  2022-04-09

import network
import secrets
import machine
import time
from mqtt import MQTTClient 

try:
    from secrets import secrets
except ImportError:
    print("WiFi secrets are kept in secrets.py, please add them there!")
    raise

start = 0

aio_topic = secrets["aio_username"] + "/feeds/current"

def sub_cb(topic, msg): 
   print("Returned:", float(msg.decode('UTF-8')), end='')
   print(" pure bytecode:", msg, "as string", msg.decode('UTF-8'))

wlan = network.WLAN(network.STA_IF)
print("Connecting to %s " % secrets["ssid"], end='')
wlan.active(True)
while not wlan.isconnected():
    try:
        print('.', end='')
        wlan.connect(secrets["ssid"], secrets["password"])
        time.sleep(1)
    except:
        print("connection error, retrying")

print("\nConnection to Wifi successful.") 
 
client = MQTTClient("device_id", "io.adafruit.com",user=secrets["aio_username"], password=secrets["aio_password"], port=1883) 
client.set_callback(sub_cb)
print("Connecting to AIO ...")
client.connect()
client.subscribe(topic=aio_topic)
print("Success!")

def aio_send(message):
    try:
        client.publish(topic=aio_topic, msg=message)
    except:
        print("This did not work")

while True: 
    print("Sending:  3.141527")
    start = time.ticks_ms()
    aio_send("3.141527")
    time.sleep(1)
    try:
        client.check_msg()
    except:
        print("Some error.")        
    print("The roundtrip for this message took {:.0f} milliseconds".format(time.ticks_ms() - start - 1000))
    time.sleep(20) 
    print("Sending:  2.71827182845")
    start = time.ticks_ms()
    aio_send("2.71827182845")
    time.sleep(1)
    try:
        client.check_msg()
    except:
        print("Some error.")        
    print("The roundtrip for this message took {:.0f} milliseconds".format(time.ticks_ms() - start - 1000))
    time.sleep(20)
