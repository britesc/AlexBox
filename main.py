"""
    2 Core Driver.
"""

"""
    System Includes.
"""
import machine
from utime import sleep
import _thread
import gc

"""
    Application Includes.
"""
from lib.version_info import *
from lib import utilities_filesystem as uf
from lib import display_functions as ilcd
# from lib import ups_b as ups
# from lib.display_pins import *
# from lib import display_lcd_2in as dlcd
# from lib import display_initialise as ilcd
# from lib import neo6m_gps as gps
# from lib import adafruit_datalogger as dl
# from lib import adafruit_rtc as rtc

"""
    Priority
    
    10 - Initialise Display
    
    20 - Check if Configured
        If NOT Configured call setup_config.py
   
    30 - Initialise GPS
    32 - Initialise RTCs
    34 - Initialise Dataloger
    36 - Read config.json
    38 - Initialise Cores 0 and 1
    
    40 - Show Main Main
"""
   
"""
    main function only called if we are the primary invocation.
"""

def main() -> None:
    try:
        print(f"Hello from {AppName}-Main! Version: {VersionString}\n")
        
        # Priority 10
        print("main.py - Setting Up Disply\n")
        myLCD = ilcd.LCD_2inch()
        myLCD.display_setup()
        myLCD.display_colour_bars()
        
        
        # Priority 38
        print("main.py - Creating Core 1 Thread\n")
        core1_thread = _thread.start_new_thread(core1_thread_actions,())
        print("main.py - Creating Core 0 Thread\n")        
        core0_thread_actions()

    except Exception as err:
        print(f"Unfortunately the Application has encountered an error and is unable to continue.\n")
        print(f"Exception {err=}, {type(err)=}\n")
        
"""
    Things that should run using core 0.
"""
def core0_thread_actions() -> None:
    print(f"This is Core 0")
    sleep(0.5)


"""
    Things that should run using core 1.
"""
def core1_thread_actions() -> None:
    print(f"This is Core 1")
    sleep(0.5)
      
    
if __name__ == "__main__":
    main()
