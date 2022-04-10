# /micropython/apps/temperature_mqtt_json.py  2022-04-10

import network
import secrets
import time
import gc
import machine
from mqtt import MQTTClient 

try:
    from secrets import secrets
except ImportError:
    print("WiFi secrets are kept in secrets.py, please add them there!")
    raise

start     = 0
last_msg  = 0
client_id = b'10521c66507c'

aio_topic1 = secrets["aio_username"] + "/feeds/temperature"
aio_topic2 = secrets["aio_username"] + "/feeds/lipo"
aio_topic3 = secrets["aio_username"] + "/feeds/freemem"
aio_connected = False
wlan = network.WLAN(network.STA_IF)

pin_temp = machine.ADC(machine.Pin(36))
pin_temp.atten(machine.ADC.ATTN_11DB)  # full range: 3.3V
pin_lipo = machine.ADC(machine.Pin(34))
pin_lipo.atten(machine.ADC.ATTN_11DB)

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

def aio_connect():
    try:
        client.connect()
        client.subscribe(topic=aio_topic1)
        client.subscribe(topic=aio_topic2)
        client.subscribe(topic=aio_topic3)
        print("Sucessfully connected to Adafruit IO")
        return True
    except:
        print(".", end='')
        time.sleep(5)
        return False

def aio_send(message1, message2, message3):
    #wifi_start()
    #client.ping()
    failure = True
    while failure:
        try:
            client.publish(topic=aio_topic1, msg=message1)
            print(" msg1 ", end='')
            time.sleep(1)
            client.publish(topic=aio_topic2, msg=message2)
            print(" msg2 ", end='')
            time.sleep(1)
            client.publish(topic=aio_topic3, msg=message3)
            print(" msg3 ", end='')
            failure = False
        except:
            print("Lost connection. Reconnecting ...", end='')
            aio_connected = False
            while not aio_connect():
                pass
            
        time.sleep(1) # take a second between each attempt
#        if failure == False:
#            try:
#                failure = True
#                client.check_msg()
#               failure = False
#            except:
#                print("Some error.")
#            time.sleep(1)
#        print('.', end='')

##### Here is where the real program starts

print("Connecting to %s " % secrets["ssid"], end='')
wifi_start()
print("\nConnection to Wifi successful.") 
 
client = MQTTClient(client_id, "io.adafruit.com", user=secrets["aio_username"], password=secrets["aio_password"], port=1883) 
client.set_callback(sub_cb)
print("Connecting to AIO ...")
while not aio_connect():
    pass
    
while True:
    temp_raw = supersample(pin_temp, 100)
    lipo_raw = supersample(pin_lipo, 100)
    freemem = gc.mem_free()
    text_temp = "{:.1f}".format(temp_raw * 0.0793 + 10.8)
    text_lipo = "{:.3f}".format((lipo_raw * 0.000793 + 0.108) * 2)
    #json = '{ "value": {"temp": ' + text_temp + ', "liion": ' + text_lipo + ', "mem-free": ' + str(freemem) + '}, '
    #json += '"lat": 38.1123, "lon": -91.2325, "ele": 112 }'
    #print(json)
    print("Sending:", text_temp, "and", text_lipo, end=' ')
    start = time.ticks_ms()
    aio_send(text_temp, text_lipo, str(freemem))
    print("The roundtrip for this message took {:.0f} milliseconds. Bytes free:".format(time.ticks_ms() - start - 1000), freemem)
    if freemem < 50000:
        gc.collect()
    machine.lightsleep(60000)
