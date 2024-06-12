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
from lib import utilities_filesystem as uf
from lib import ups_b as ups
from lib import display_lcd_2in as lcd
from lib import neo6m_gps as gps
from lib import adafruit_datalogger as dl
from lib import adafruit_rtc as rtc

"""
    Priority
    
    10 - Initialise Display
    
    20 - Check if Configured
        If NOT Configured call setup_config.py
   
    30 - Initialise GPS
    32 - Initialise RTCs
    34 - Initialise Dataloger
    36 - Read config.json
    38 - Show Main Main
    
    
"""

"""
    Version String to be updated after each development.
"""
VersionMajor  = 1
VersionMinor  = 0
VersionBuild  = 4
VersionDev    = 10004
VersionString = f"{VersionMajor}.{VersionMinor}.{VersionBuild},{VersionDev} "

AppName       = "EARS"
AppType		  = ["Personal","Squad","Section","PLatoon"]


"""
    Initialise Display.
    
    Initialise Waveshare 2 inch LCD TFT Screen 320x240
"""
def InitialiseDisplay() -> None:
    print("Initialising Display")

    

"""
    main function only called if we are the primary invocation.
"""
def main() -> None:
    try:
        print(f"Hello from {AppName}-Main! Version: {VersionString}\n")
        
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
