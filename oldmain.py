# WS 320x240 display example
from machine import Pin,SPI,PWM
import framebuf
import utime
import os

from lib import version_info
from lib import display_lcd_2in
from lib import display_initialise


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
  
if __name__=='__main__':
    pwm = PWM(Pin(BL))
    pwm.freq(1000)
    pwm.duty_u16(32768)#max 65535

    LCD = display_lcd_2in.LCD_2inch()
    #color BRG
    LCD.fill(LCD.BLUE)
    LCD.show()
    utime.sleep(10)
    display_colour_bars() # type: ignore
    utime.sleep(10)
    display_author()     # type: ignore
    
def display_colour_bars() -> None:
    #while(1):
    utime.sleep(0.1)
    LCD.fill_rect(0,0,320,24,LCD.RED)
    LCD.rect(0,0,320,24,LCD.RED)
    LCD.text("Raspberry Pi Pico",2,8,LCD.WHITE)
    utime.sleep(0.1)
    LCD.show()
    LCD.fill_rect(0,24,320,24,LCD.BLUE)
    LCD.rect(0,24,320,24,LCD.BLUE)
    LCD.text("PicoGo",2,32,LCD.WHITE)
    utime.sleep(0.1)
    LCD.show()
    LCD.fill_rect(0,48,320,24,LCD.GREEN)
    LCD.rect(0,48,320,24,LCD.GREEN)
    LCD.text("Pico-LCD-2",2,54,LCD.WHITE)
    utime.sleep(0.1)
    LCD.show()
    LCD.fill_rect(0,72,320,24,LCD.PALEBLUE)
    LCD.rect(0,72,320,24,LCD.PALEBLUE)
    utime.sleep(0.1)
    LCD.show()
    LCD.fill_rect(0,96,320,24,LCD.PURPLE)
    LCD.rect(0,96,320,24,LCD.PURPLE)
    utime.sleep(0.1)
    LCD.show()
    LCD.fill_rect(0,120,320,24,LCD.LIGHTBLUE)
    LCD.rect(0,120,320,24,LCD.LIGHTBLUE)
    utime.sleep(0.1)
    LCD.show()
    LCD.fill_rect(0,144,320,24,LCD.YELLOW)
    LCD.rect(0,144,320,24,LCD.YELLOW)
    utime.sleep(0.1)
    LCD.show()
    LCD.fill_rect(0,168,320,24,LCD.TAN)
    LCD.rect(0,168,320,24,LCD.TAN)
    utime.sleep(0.1)
    LCD.show()
    LCD.fill_rect(0,192,320,24,LCD.ORANGE)
    LCD.rect(0,192,320,24,LCD.ORANGE)
    utime.sleep(0.1)
    LCD.show()
    LCD.fill_rect(0,216,320,24,LCD.GRAY)
    LCD.rect(0,216,320,24,LCD.GRAY)
    utime.sleep(0.1)
    LCD.show()
    LCD.fill(LCD.BLACK)
    utime.sleep(0.1)
    LCD.show()
    utime.sleep(10)
    LCD.fill(LCD.BLACK)

def display_author() -> None:
    LCD.rect(0,0,160,128,colour(0,0,255)) # type: ignore # Blue Frame
    LCD.text("WaveShare", 44,10,colour(255,0,0)) # type: ignore
    LCD.text('Pico Display 1.8"', 10,24,colour(255,255,0)) # type: ignore
    LCD.text("320x240 SPI", 38,37,colour(0,255,0)) # type: ignore
    LCD.text("Tony Goodhew", 30,48,colour(100,100,100)) # type: ignore
    c = colour(255,240,0) # type: ignore
    printstring("New Font - Size 1",14,65,1,0,0,c) # type: ignore
    c = colour(255,0,255) # type: ignore
    printstring("Now size 2",12,78,2,0,0,c) # type: ignore
    c = colour(0,255,255) # type: ignore
    printstring("Size 3",30,100,3,0,0,c) # type: ignore

    LCD.pixel(0,0,0xFFFF)     # Left Top - OK
    LCD.pixel(0,239,0xFFFF)   # Left Bottom - OK
    LCD.pixel(319,0,0xFFFF)   # Right Top - OK
    LCD.pixel(319,239,0xFFFF) # Right Bottom - OK
    LCD.show()
    utime.sleep(20)
