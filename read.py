from time import sleep

from mfrc522 import MFRC522
from machine import Pin
from machine import SPI

spi = SPI(1, baudrate=2500000, polarity=0, phase=0)
# Using Hardware SPI pins:
#     sck=18   # yellow
#     mosi=23  # orange
#     miso=19  # blue
#     rst=4    # white
#     cs=5     # green, DS
# *************************
# To use SoftSPI,
# from machine import SOftSPI
# spi = SoftSPI(baudrate=100000, polarity=0, phase=0, sck=sck, mosi=mosi, miso=miso)
green = Pin(16, Pin.OUT)
green.value(0)

red = Pin(2, Pin.OUT)
red.value(0)

spi.init()
rdr = MFRC522(spi=spi, gpioRst=4, gpioCs=5)
print("Place card")

while True:

    (stat, tag_type) = rdr.request(rdr.REQIDL)
    if stat == rdr.OK:
        (stat, raw_uid) = rdr.anticoll()
        if stat == rdr.OK:
            card_id = "uid: 0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])
            print(card_id)
            if "0xeb1e9622" in card_id:
                green.on()
                sleep(1)
                green.off()
            else:
                red.on()
                sleep(1)
                red.off()

# "uid: 0xeb1e9622"
# "uid: 0x048cdc2b"


