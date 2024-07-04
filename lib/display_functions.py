"""
    Waveshare LCD 2 Inch Display.
    
    Class to control the display.
    Currently easiest is all in one.

"""


from machine import (
    Pin,
    SPI,
    PWM
)    
import framebuf

import utime
import gc

LONG_DELAY    = 10
MEDIUM_DELAY  = (LONG_DELAY / 2)
SHORT_DELAY   = (LONG_DELAY / 100)
PWM_FREQUENCY = 1000
PWM_DUTY_MAX  = 32768
PWM_DUTY_MIN  = 0
PWM_DUTY_STEP = (PWM_DUTY_MAX / 100)

"""
    Pins Table.
    
    The connections from the Display to the Pico W.
"""

# LCD Connection to Raspberry Pi Pico W
# LCD   Pico
#________________________________
# VCC = VSYS
# GND = GND
# DIN = GP11
MOSI  = 11
# CLK = GP10
SCK   = 10
# CS  = GP9
CS    = 9
# DC  = GP8
DC    = 8
# RST = GP12
RST   = 12
# BL  = GP13
BL    = 13


class LCD_2inch(framebuf.FrameBuffer): # For 320x240 display
    def __init__(self, MOSI=11, SCK=10, CS=9, DC=8, RST=12, BL=13):
        print("[display_functions.py] - Version 0002\n")
        print("[display_functions.py] - Initialising Class - Start")
        
        """
            Setup Display Pins.
        """
        self.MOSI=MOSI
        self.SCK=SCK
        self.CS=CS
        self.DC=DC
        self.RST=RST
        self.BL=BL
        
        """
            Set Display Size.
        """
        self.width = 320
        self.height = 240
        
        """
            Set RGB565 Palette.           
        """
        self.RED       =   0x07E0
        self.GREEN     =   0x001f
        self.BLUE      =   0xf800
        self.WHITE     =   0xffff
        self.BLACK     =   0x0000
        self.GRAY      =   0X8430
        self.ORANGE    =   0XFC07
        self.TAN       =   0XBC40
        self.YELLOW    =   0xFFE0
        self.LIGHTBLUE =   0x7FFF
        self.PURPLE    =   0xF81F
        self.PALEBLUE  =   0x07FF


        self.cs = Pin(self.CS,Pin.OUT)
        self.rst = Pin(self.RST,Pin.OUT)
        
        self.cs(1)
        self.spi = SPI(1)
        self.spi = SPI(1,1000_000)
        self.spi = SPI(1,100000_000, polarity=0, phase=0, sck=Pin(self.SCK), mosi=Pin(self.MOSI), miso=None)
        self.dc = Pin(self.DC,Pin.OUT)
        self.dc(1)
        self.buffer = bytearray(self.height * self.width * 2)
        super().__init__(self.buffer, self.width, self.height, framebuf.RGB565)
        self.init_display()
        
    def write_cmd(self, cmd):
        self.cs(1)
        self.dc(0)
        self.cs(0)
        self.spi.write(bytearray([cmd]))
        self.cs(1)

    def write_data(self, buf):
        self.cs(1)
        self.dc(1)
        self.cs(0)
        self.spi.write(bytearray([buf]))
        self.cs(1)

    def init_display(self):
        """Initialize display"""  
        self.rst(1)
        self.rst(0)
        self.rst(1)
        
        self.write_cmd(0x36)
        self.write_data(0x70)

        self.write_cmd(0x3A) 
        self.write_data(0x05)

        self.write_cmd(0xB2)
        self.write_data(0x0C)
        self.write_data(0x0C)
        self.write_data(0x00)
        self.write_data(0x33)
        self.write_data(0x33)

        self.write_cmd(0xB7)
        self.write_data(0x35) 

        self.write_cmd(0xBB)
        self.write_data(0x19)

        self.write_cmd(0xC0)
        self.write_data(0x2C)

        self.write_cmd(0xC2)
        self.write_data(0x01)

        self.write_cmd(0xC3)
        self.write_data(0x12)   

        self.write_cmd(0xC4)
        self.write_data(0x20)

        self.write_cmd(0xC6)
        self.write_data(0x0F) 

        self.write_cmd(0xD0)
        self.write_data(0xA4)
        self.write_data(0xA1)

        self.write_cmd(0xE0)
        self.write_data(0xD0)
        self.write_data(0x04)
        self.write_data(0x0D)
        self.write_data(0x11)
        self.write_data(0x13)
        self.write_data(0x2B)
        self.write_data(0x3F)
        self.write_data(0x54)
        self.write_data(0x4C)
        self.write_data(0x18)
        self.write_data(0x0D)
        self.write_data(0x0B)
        self.write_data(0x1F)
        self.write_data(0x23)

        self.write_cmd(0xE1)
        self.write_data(0xD0)
        self.write_data(0x04)
        self.write_data(0x0C)
        self.write_data(0x11)
        self.write_data(0x13)
        self.write_data(0x2C)
        self.write_data(0x3F)
        self.write_data(0x44)
        self.write_data(0x51)
        self.write_data(0x2F)
        self.write_data(0x1F)
        self.write_data(0x1F)
        self.write_data(0x20)
        self.write_data(0x23)
        
        self.write_cmd(0x21)

        self.write_cmd(0x11)

        self.write_cmd(0x29)

    def show(self):
        self.write_cmd(0x2A)
        self.write_data(0x00)
        self.write_data(0x00)
        self.write_data(0x01)
        self.write_data(0x3f)
        
        self.write_cmd(0x2B)
        self.write_data(0x00)
        self.write_data(0x00)
        self.write_data(0x00)
        self.write_data(0xEF)
        
        self.write_cmd(0x2C)
        
        self.cs(1)
        self.dc(1)
        self.cs(0)
        self.spi.write(self.buffer)
        self.cs(1)
        
    """
        Setup the Display.

        This has to be called first as it sets up the display.
        It should be called from main before the cores are configured as it is used throught the application.
    """

    def display_setup(self) -> None:
        print("[display_functions.py] - Setting the pins and PWM for Backlight")
        self.pwm = PWM(Pin(BL))
        self.pwm.freq(1000)
        self.pwm.duty_u16(PWM_DUTY_MAX) # max 65535

        print("[display_functions.py] - PWM Set")
        
        self.LCD = framebuf
        
        print("[display_functions.py] - LCD Set")
        
        #color BRG
        self.fill(self.BLUE)
        self.show()
        utime.sleep(SHORT_DELAY)
        print("[display_functions.py] - LCD Set Done")

    """
        Display Colour Bars.

        Display a series of color bars and 3 lines of copyright text.
    """
    def display_colour_bars(self) -> None:
        print("[display_functions.py] - Displaying the Colour Bars - Start")
        utime.sleep(SHORT_DELAY)
        self.fill_rect(0,0,320,24,self.RED)
        print("[display_functions.py] - Displaying the Colour Bars - 1")
        self.rect(0,0,320,24,self.RED)
        self.text("Raspberry Pi Pico W",9,8,self.WHITE)
        utime.sleep(SHORT_DELAY)
        self.show()
        self.fill_rect(0,24,320,24,self.BLUE)
        self.rect(0,24,320,24,self.BLUE)
        self.text("Copyright JTB 2024",9,32,self.WHITE)
        utime.sleep(SHORT_DELAY)
        self.show()
        self.fill_rect(0,48,320,24,self.GREEN)
        self.rect(0,48,320,24,self.GREEN)
        self.text("All Rights Reserved",9,54,self.WHITE)
        utime.sleep(SHORT_DELAY)
        self.show()
        self.fill_rect(0,72,320,24,self.PALEBLUE)
        self.rect(0,72,320,24,self.PALEBLUE)
        # self.text("123456789a123456789b123456789c123456789d",2,54,self.BLACK)        
        utime.sleep(SHORT_DELAY)
        self.show()
        self.fill_rect(0,96,320,24,self.PURPLE)
        self.rect(0,96,320,24,self.PURPLE)
        utime.sleep(SHORT_DELAY)
        self.show()
        self.fill_rect(0,120,320,24,self.LIGHTBLUE)
        self.rect(0,120,320,24,self.LIGHTBLUE)
        utime.sleep(SHORT_DELAY)
        self.show()
        self.fill_rect(0,144,320,24,self.YELLOW)
        self.rect(0,144,320,24,self.YELLOW)
        utime.sleep(SHORT_DELAY)
        self.show()
        self.fill_rect(0,168,320,24,self.TAN)
        self.rect(0,168,320,24,self.TAN)
        utime.sleep(SHORT_DELAY)
        self.show()
        self.fill_rect(0,192,320,24,self.ORANGE)
        self.rect(0,192,320,24,self.ORANGE)
        utime.sleep(SHORT_DELAY)
        self.show()
        self.fill_rect(0,216,320,24,self.GRAY)
        self.rect(0,216,320,24,self.GRAY)
        utime.sleep(SHORT_DELAY)
        self.show()
        self.fill(self.BLACK)
        utime.sleep(SHORT_DELAY)
        self.show()
        utime.sleep(MEDIUM_DELAY)
        self.fill(self.BLACK)
        print("[display_functions.py] - Displaying the Colour Bars - End")

