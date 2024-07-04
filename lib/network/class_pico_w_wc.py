#!/usr/bin/env python3
# coding: utf-8
# class_pico_w_wc.py :- Used to create Pico W WiFi Connection
"""
    EARS WiFi Connectiom.
    
    This class creates and destroys the EARS WiFi Connection.
    Version: 1.0.22
    Dated: 20240704
    Author: jB
"""
# Declare Imports
import network
import utime

# Define Class
class Ears_WC:
    
# Start Class Intrinsic Functions    
    def __init__(self, ssid, password) -> None:
        """
            Class __init__ function.
        """
        self.ClassVersion = "1.0.22"
        self.ssid         = ssid
        self.password     = password
        self.delay        = 3
        self.wc           = network.WLAN(network.STA_IF)
        self.ip           = "0.0.0.0"
        self.subnet       = "0.0.0.0"
        self.gateway      = "0.0.0.0"
        self.dns          = "0.0.0.0"
        self.mac          = "00:00:00:00:00:00"
        self.channel     = 0
        self.hostname    = ""
        
    def __str__(self) -> str:
        """ The __str__ Function """
        return "Ears_IF"

    def __repr__(self) -> str:
        """ The __repr__ Function """
        return "Ears_IF"

    def getClassVersion(self) -> str:
        """ The Version String of this Class """
        return self.ClassVersion

# Start Class Extrinsic Functions

    def start(self) -> bool:
        """
            Class Start Wireless Connection Function.
            
            Return: Boolean True for Started, False for Not Started.
            Has a 3 second delay to ensure started
        """

        self.wc.active(True)
        
        if not self.wc.isconnected():
            self.wc.active(True)
            self.wc.connect(self.ssid, self.password)
            while not self.wc.isconnected():
                pass        
        
            
        if self.wc.active() == True:
            tmp = self.wc.ifconfig()
            self.ip       = tmp[0]
            self.subnet   = tmp[1]
            self.gateway  = tmp[2]
            self.dns      = tmp[3]
            self.mac      = self._mac2Str(self.wc.config('mac'))
            self.channel  = self.wc.config('channel')
            self.hostname = network.hostname()
            return True
        else:
            self._clear_details()        
            return False
        
    def stop(self) -> bool:
        """
            Class Stop Wireless Connection Function.
            
            Return: Boolean True for Stopped, False for Not Stopped.
            Has a 3 second delay to ensure stopped
        """    
      
        self.wc.active(False)

        if self.wc.isconnected():
            self.wc.disconnect()
            self.wc.active(False )
            while self.wc.isconnected():
                pass           
          
        if self.wc.active() == False:
            self._clear_details() 
            return True
        else:
            return False         

    def get_wc_ssid(self) -> str:
        """
            Get EARS Wireless Connection SSID.
        """
        return self.ssid

    def get_wc_password(self) -> str:
        """
            Get EARS Wireless Connection Password.
        """
        return self.password
 
    def get_wc_ip(self) -> str:
        """
            Get EARS Wireless Connection IP Address.
        """
        return self.ip
    
    def get_wc_subnet(self) -> str:
        """
            Get EARS Wireless Connection Subnet Address.
        """
        return self.subnet    

    def get_wc_gateway(self) -> str:
        """
            Get EARS Wireless Connection Gateway Address.
        """
        return self.gateway
    
    def get_wc_dns(self) -> str:
        """
            Get EARS Wireless Connection DNS Address.
        """
        return self.dns
    
    def get_wc_mac(self) -> str:
        """
            Get EARS Wireless Connection MAC Address.
        """
        return self.mac
    
    def get_wc_channel(self) -> int:
        """
            Get EARS Wireless Connection Channel Number.
        """
        return self.channel    
    
    def get_wc_hostname(self) -> str:
        """
            Get EARS Wireless Connection Hostname.
        """
        return self.hostname
    
    def _clear_details(self) -> None:
        """
            Internal function to clear IF Info.
        """
        self.ip       = "0.0.0.0"
        self.subnet   = "0.0.0.0"
        self.gateway  = "0.0.0.0"
        self.dns      = "0.0.0.0"
        self.mac      = "00:00:00:00:00:00"
        self.channel  = 0
        self.hostname = ""
        
    def _mac2Str(self, mac): 
        return ':'.join([f"{b:02X}" for b in mac])        

if __name__ == "__main__":
    wc = Ears_WC("GL-AX1800-216","B1gR3dD0g")
    print("Class Testing by running directly\n")
    WC_UP = wc.start()
    print(f"Class Version = {wc.getClassVersion()}\n")
    if WC_UP:
        print("EARS Wireless Connection Started\n")
        print(f"SSID          = {wc.get_wc_ssid()}\n")
        print(f"PASSWORD      = {wc.get_wc_password()}\n")
        print(f"IP            = {wc.get_wc_ip()}\n")
        print(f"SubNet        = {wc.get_wc_subnet()}\n")
        print(f"GateWay       = {wc.get_wc_gateway()}\n")
        print(f"DNS           = {wc.get_wc_dns()}\n")
        print(f"MAC           = {wc.get_wc_mac()}\n")
        print(f"Channel       = {wc.get_wc_channel()}\n")
        print(f"Hostname      = {wc.get_wc_hostname()}\n")
        WC_UP = wc.stop()
        if WC_UP:
            print("EARS Wireless Connection Stopped\n")
        else:
            print("EARS Wireless Connection Stop Failed\n")
    else:
        print("EARS Wireless Connection Failed\n")
    