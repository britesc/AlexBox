"""
    Display Functions.
"""

import utime
from lib import display_lcd_2in as dlcd

from machine import (
    Pin,
    SPI,
    PWM
) 

from lib.display_pins import *


LONG_DELAY    = 10
MEDIUM_DELAY  = (LONG_DELAY / 2)
SHORT_DELAY   = (LONG_DELAY / 100)
PWM_FREQUENCY = 1000
PWM_DUTY_MAX  = 32768
PWM_DUTY_MIN  = 0
PWM_DUTY_STEP = (PWM_DUTY_MAX / 100)


"""
    Initialise Display.
    
    Initialise Waveshare 2 inch LCD TFT Screen 320x240
"""

def InitialiseDisplay() -> None:
    print("[display_initialise.py] - Initialising Display")
    display_setup()
    display_colour_bars() # type: ignore
    print("[display_initialise.py] - Initialised Display")


"""
    Setup the Display.

    This has to be called first as it sets up the display.
    It should be called from main before the cores are configured as it is used throught the application.
"""

def display_setup() -> None:
    print("[display_initialise.py] - Setting the pins and PWM for Backlight")
    pwm = PWM(Pin(BL))
    pwm.freq(1000)
    pwm.duty_u16(PWM_DUTY_MAX) # max 65535

    LCD = dlcd.LCD_2inch()
    #color BRG
    LCD.fill(LCD.GREEN)
    LCD.show()
    utime.sleep(SHORT_DELAY)


"""
    Set the Backlight.

    Increase or Decrease the brightness of the display
    Pass a value between 0 - 100 with 0 being off and 100 maximum
    The value will be convert to a duty cycle and passed to the BL pin
    which has been set as a PWM pin.
"""

def display_set_backlight(percentage) -> None:
    print("[display_initialise.py] - Setting the backlight")    
    new_value = (PWM_DUTY_STEP * percentage)
    if new_value > PWM_DUTY_MAX:
        new_value = PWM_DUTY_MAX
    if new_value < PWM_DUTY_MIN:
        new_value = PWM_DUTY_MIN
    pwm.duty_u16(new_value)		

"""
    Get the Backlight Value.

    Returns the value of the Backlight.
    The value is 0 - 100 with 0 being off and 100 being maximum.
    The returned value is converted to percentage, not the actual duty cycle value.
"""

def display_get_backlight() -> int:
    print("[display_initialise.py] - Getting the backlight")
    pwm_val = pwm.duty_u16()
    if pwm_val > PWM_DUTY_MAX:
        pwm_val = PWM_DUTY_MAX
    if pwm_val < PWM_DUTY_MIN:
        pwm_val = PWM_DUTY_MIN	
    ret_val = (pwm_val / PWM_DUTY_MAX) * 100 	
    return ret_val


def display_colour_bars() -> None:
    LCD = dlcd.LCD_2inch()
    print("[display_initialise.py] - Displaying the Colour Bars")    
    utime.sleep(SHORT_DELAY)
    LCD.fill_rect(0,0,320,24,LCD.RED)
    LCD.rect(0,0,320,24,LCD.RED)
    LCD.text("Raspberry Pi Pico W",2,8,LCD.WHITE)
    utime.sleep(SHORT_DELAY)
    LCD.show()
    LCD.fill_rect(0,24,320,24,LCD.BLUE)
    LCD.rect(0,24,320,24,LCD.BLUE)
    LCD.text("Copyright JTB 2024",2,32,LCD.WHITE)
    utime.sleep(SHORT_DELAY)
    LCD.show()
    LCD.fill_rect(0,48,320,24,LCD.GREEN)
    LCD.rect(0,48,320,24,LCD.GREEN)
    LCD.text("All Rights Reserved",2,54,LCD.WHITE)
    utime.sleep(SHORT_DELAY)
    LCD.show()
    LCD.fill_rect(0,72,320,24,LCD.PALEBLUE)
    LCD.rect(0,72,320,24,LCD.PALEBLUE)
    utime.sleep(SHORT_DELAY)
    LCD.show()
    LCD.fill_rect(0,96,320,24,LCD.PURPLE)
    LCD.rect(0,96,320,24,LCD.PURPLE)
    utime.sleep(SHORT_DELAY)
    LCD.show()
    LCD.fill_rect(0,120,320,24,LCD.LIGHTBLUE)
    LCD.rect(0,120,320,24,LCD.LIGHTBLUE)
    utime.sleep(SHORT_DELAY)
    LCD.show()
    LCD.fill_rect(0,144,320,24,LCD.YELLOW)
    LCD.rect(0,144,320,24,LCD.YELLOW)
    utime.sleep(SHORT_DELAY)
    LCD.show()
    LCD.fill_rect(0,168,320,24,LCD.TAN)
    LCD.rect(0,168,320,24,LCD.TAN)
    utime.sleep(SHORT_DELAY)
    LCD.show()
    LCD.fill_rect(0,192,320,24,LCD.ORANGE)
    LCD.rect(0,192,320,24,LCD.ORANGE)
    utime.sleep(SHORT_DELAY)
    LCD.show()
    LCD.fill_rect(0,216,320,24,LCD.GRAY)
    LCD.rect(0,216,320,24,LCD.GRAY)
    utime.sleep(SHORT_DELAY)
    LCD.show()
    LCD.fill(LCD.BLACK)
    utime.sleep(SHORT_DELAY)
    LCD.show()
    utime.sleep(MEDIUM_DELAY)
    LCD.fill(LCD.BLACK)
    