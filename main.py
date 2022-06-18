from utime import sleep

from mfrc522 import MFRC522
from machine import Pin, SPI

spi = SPI(1, baudrate=2500000, polarity=0, phase=0)
spi.init()
rdr = MFRC522(spi=spi, gpioRst=4, gpioCs=5)

green = Pin(16, Pin.OUT)
green.off()
red = Pin(2, Pin.OUT)
red.off()


def read_card():
    (stat, tag_type) = rdr.request(rdr.REQIDL)
    if stat == rdr.OK:
        (stat, raw_uid) = rdr.anticoll()
        if stat == rdr.OK:
            return "uid: 0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])


def blink_led(led):
    led.on()
    sleep(1)
    led.off()


print("Place card")

while True:
    card_id = read_card()
    if card_id:
        if "0xeb1e9622" in card_id:
            blink_led(green)
        else:
            blink_led(red)
