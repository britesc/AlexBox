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
import utilities_filesystem


"""
    Version String to be updated after each development.
"""
VersionString = "1.0.3"

"""
    main function only called if we are the primary invocation.
"""
def main() -> None:
    try:
        print(f"Hello from Main! Version: {VersionString}\n")
        
        core1_thread = _thread.start_new_thread(core1_thread_actions,())
        core0_thread_actions()

    except Exception as err:
        print("Unfortunately the Application has encountered an error \
and is unable to continue.\n")
        print(f"Exception {err=}, {type(err)=}\n")
        # traceback.print_exc()
        # traceback.print_exception() # type: ignore
        
def setup_app() -> None:
    pass

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
