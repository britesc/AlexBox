"""
    2 Core Driver.
"""

"""
    System Includes.
"""
import machine
# import traceback
from utime import sleep
import _thread

"""
    Application Includes.
"""
from lib.version_info import *
from lib import utilities_filesystem as uf
# from lib import ups_b as ups
from lib.display_pins import *
from lib import display_lcd_2in as dlcd
from lib.display_initialise import *
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
        InitialiseDisplay()
        
        
        # Priority 38
        core1_thread = _thread.start_new_thread(core1_thread_actions,())
        core0_thread_actions()

    except Exception as err:
        print("Unfortunately the Application has encountered an error \
and is unable to continue.\n")
        print(f"Exception {err=}, {type(err)=}\n")
        # traceback.print_exc()
        # traceback.print_exception() # type: ignore
        
"""
    Things that should run using core 0.
"""
def core0_thread_actions() -> None:
    print("This is Core0\n")
    sleep(0.5)


"""
    Things that should run using core 1.
"""
def core1_thread_actions() -> None:
    print("This is Core1\n")
    sleep(0.5)
      
    
if __name__ == "__main__":
    main()
