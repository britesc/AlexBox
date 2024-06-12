# WS 320x240 display example
from machine import Pin,SPI,PWM
import framebuf
import time
import os

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
    def __init__(self):
        self.width = 320
        self.height = 240
        
        self.cs = Pin(CS,Pin.OUT)
        self.rst = Pin(RST,Pin.OUT)
        
        self.cs(1)
        self.spi = SPI(1)
        self.spi = SPI(1,1000_000)
        self.spi = SPI(1,100000_000,polarity=0, phase=0,sck=Pin(SCK),mosi=Pin(MOSI),miso=None)
        self.dc = Pin(DC,Pin.OUT)
        self.dc(1)
        self.buffer = bytearray(self.height * self.width * 2)
        super().__init__(self.buffer, self.width, self.height, framebuf.RGB565)
        self.init_display()
        
        self.RED   =   0x07E0
        self.GREEN =   0x001f
        self.BLUE  =   0xf800
        self.WHITE =   0xffff
        self.BALCK =   0x0000
        
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
        
  
if __name__=='__main__':
    pwm = PWM(Pin(BL))
    pwm.freq(1000)
    pwm.duty_u16(32768)#max 65535

    LCD = LCD_2inch()
    #color BRG
    LCD.fill(LCD.BLUE)
    LCD.show()
    
    
    while(1):
        time.sleep(0.1)
        LCD.fill_rect(0,0,320,24,LCD.RED)
        LCD.rect(0,0,320,24,LCD.RED)
        LCD.text("Raspberry Pi Pico",2,8,LCD.WHITE)
        time.sleep(0.1)
        LCD.show()
        LCD.fill_rect(0,24,320,24,LCD.BLUE)
        LCD.rect(0,24,320,24,LCD.BLUE)
        LCD.text("PicoGo",2,32,LCD.WHITE)
        time.sleep(0.1)
        LCD.show()
        LCD.fill_rect(0,48,320,24,LCD.GREEN)
        LCD.rect(0,48,320,24,LCD.GREEN)
        LCD.text("Pico-LCD-2",2,54,LCD.WHITE)
        time.sleep(0.1)
        LCD.show()
        LCD.fill_rect(0,72,320,24,0X07FF)
        LCD.rect(0,72,320,24,0X07FF)
        time.sleep(0.1)
        LCD.show()
        LCD.fill_rect(0,96,320,24,0xF81F)
        LCD.rect(0,96,320,24,0xF81F)
        time.sleep(0.1)
        LCD.show()
        LCD.fill_rect(0,120,320,24,0x7FFF)
        LCD.rect(0,120,320,24,0x7FFF)
        time.sleep(0.1)
        LCD.show()
        LCD.fill_rect(0,144,320,24,0xFFE0)
        LCD.rect(0,144,320,24,0xFFE0)
        time.sleep(0.1)
        LCD.show()
        LCD.fill_rect(0,168,320,24,0XBC40)
        LCD.rect(0,168,320,24,0XBC40)
        time.sleep(0.1)
        LCD.show()
        LCD.fill_rect(0,192,320,24,0XFC07)
        LCD.rect(0,192,320,24,0XFC07)
        time.sleep(0.1)
        LCD.show()
        LCD.fill_rect(0,216,320,24,0X8430)
        LCD.rect(0,216,320,24,0X8430)
        time.sleep(0.1)
        LCD.show()
        LCD.fill(0xFFFF)
        time.sleep(0.1)
        LCD.show()
    time.sleep(10)
    LCD.fill(0xFFFF)

'''
LCD.rect(0,0,160,128,colour(0,0,255)) # Blue Frame
LCD.text("WaveShare", 44,10,colour(255,0,0))
LCD.text('Pico Display 1.8"', 10,24,colour(255,255,0))
LCD.text("160x128 SPI", 38,37,colour(0,255,0))
LCD.text("Tony Goodhew", 30,48,colour(100,100,100))
c = colour(255,240,0)
printstring("New Font - Size 1",14,65,1,0,0,c)
c = colour(255,0,255)
printstring("Now size 2",12,78,2,0,0,c)
c = colour(0,255,255)
printstring("Size 3",30,100,3,0,0,c)

LCD.pixel(0,0,0xFFFF)     # Left Top - OK
LCD.pixel(0,239,0xFFFF)   # Left Bottom - OK
LCD.pixel(319,0,0xFFFF)   # Right Top - OK
LCD.pixel(319,239,0xFFFF) # Right Bottom - OK
LCD.show()
utime.sleep(20)
'''

