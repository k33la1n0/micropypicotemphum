from machine import Pin, I2C
import time
import dht
from ssd1306 import SSD1306_I2C
#
# OLED pixel definition (WxH)
WIDTH  = 128 
HEIGHT = 32
# I2C0 pin assignments
SCL = 5
SDA = 4
# DHT22 sensor
sensor = dht.DHT22(Pin(2))
# Initialize I2C0, Scan and Debug print of SSD1306 I2C device address
i2c = I2C(0, scl=Pin(SCL), sda=Pin(SDA), freq=200000)
# Initialize OLED
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)
# give the display time to response for showing temp. and humi.
time.sleep_ms(250)

while True:
    # fetch the measure from the dht22 sensor
    sensor.measure()
    # clear the display from old information
    oled.fill(0)
    # declaration the temp. and humi. data from the dht22
    temp = sensor.temperature()
    hum = sensor.humidity()
    # say the display 'show temp. data'
    oled.text("Temp. {} C".format(temp),5,5)
    # say the display 'show humi. data' (e.g. [de] luftfeuchtigkeit)
    oled.text("Feucht. {:.0f} % ".format(hum),5,15)
    #Show display with the fetch data from temp and hum
    oled.show()
    # Wait for Five seconds. Then proceed to collect next sensor reading.
    time.sleep_ms(5000)
