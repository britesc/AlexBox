from machine import Pin, SPI
import gc

from drivers.st7789.st7789_4bit import *
SSD = ST7789

# WIRING
# Pico      Display
# GPIO Pin

VIN=36
VCC=36
GND=23
MOSI=11
CLK=10
CS=9
DC=8
RST=12
BL=13

gc.collect()  # Precaution before instantiating framebuf
# Conservative low baudrate. Can go to 62.5MHz.
spi = SPI(1, 30_000_000, sck=Pin(CLK), mosi=Pin(MOSI), miso=None)
pcs = Pin(CS, Pin.OUT, value=1)
prst = Pin(RST, Pin.OUT, value=1)
pbl = Pin(BL, Pin.OUT, value=1)
pdc = Pin(DC, Pin.OUT, value=0)

ssd = SSD(spi, height=240, width=320, dc=pdc, cs=pcs, rst=prst, disp_mode=LANDSCAPE, display=PI_PICO_LCD_2)
