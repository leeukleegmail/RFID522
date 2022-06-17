from time import sleep

from mfrc522 import MFRC522
from machine import Pin, SPI

spi = SPI(1, baudrate=2500000, polarity=0, phase=0)
spi.init()
rdr = MFRC522(spi=spi, gpioRst=4, gpioCs=5)


green = Pin(16, Pin.OUT)
green.off()
red = Pin(2, Pin.OUT)
red.off()

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

            print(rdr.request(rdr.REQALL))

# "uid: 0xeb1e9622"
# "uid: 0x048cdc2b"


