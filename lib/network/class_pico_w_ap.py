#!/usr/bin/env python3
# coding: utf-8
# class_pico_w_ap.py :- Used to create Pico W Access Point
"""
    EARS Access Point.
    
    This class creates and destroys the EARS Access Point.
    Version: 1.0.12
    Dated: 20240703
    Author: jB
"""

# Declare Imports
import socket
import network
import utime

# Define Class
class Ears_AP:
    
# Start Class Intrinsic Functions    
    def __init__(self) -> None:
        """
            Class __init__ function.
        """
        self.ClassVersion = "1.0.12"
        self.ssid         = "EARS::AP"
        self.password     = "EarsPassword"
        self.delay        = 3
        self.ap           = network.WLAN(network.AP_IF)
        self.ip           = "0.0.0.0"
        self.subnet       = "0.0.0.0"
        self.gateway      = "0.0.0.0"
        self.dns          = "0.0.0.0"
        self.mac          = "00:00:00:00:00:00"
        self.channel     = 0
        self.hostname    = ""        

    def __str__(self) -> str:
        """ The __str__ Function """
        return "Ears_AP"

    def __repr__(self) -> str:
        """ The __repr__ Function """
        return "Ears_AP"

    def getClassVersion(self) -> str:
        """ The Version String of this Class """
        return self.ClassVersion

# Start Class Extrinsic Functions

    def start(self) -> bool:
        """
            Class Start Access Point Function.
            
            Return: Boolean True for Started, False for Not Started.
            Has a 3 second delay to ensure started
        """    
        self.ap.config(essid=self.ssid, password=self.password)
        self.ap.active(True)
        
        if self.ap.active == False:
            utime.sleep(self.delay)
            
        if self.ap.active() == True:
            tmp = self.ap.ifconfig()
            self.ip       = tmp[0]
            self.subnet   = tmp[1]
            self.gateway  = tmp[2]
            self.dns      = tmp[3]
            self.mac      = self.ap.config('mac')
            self.channel  = self.ap.config('channel')
            self.hostname = network.hostname()
            return True
        else:
            self._clear_details()        
            return False
        
    def stop(self) -> bool:
        """
            Class Stop Access Point Function.
            
            Return: Boolean True for Stopped, False for Not Stopped.
            Has a 3 second delay to ensure stopped
        """    
        
        self.ap.active(False)
        
        if self.ap.active() == True:
            utime.sleep(self.delay)
            
        if self.ap.active() == False:
            self._clear_details() 
            return True
        else:
            return False         

    def get_ap_ssid(self) -> str:
        """
            Get EARS Access Point SSID.
        """
        return self.ssid

    def get_ap_password(self) -> str:
        """
            Get EARS Access Point Password.
        """
        return self.password
 
    def get_ap_ip(self) -> str:
        """
            Get EARS Access Point IP Address.
        """
        return self.ip
    
    def get_ap_subnet(self) -> str:
        """
            Get EARS Access Point Subnet Address.
        """
        return self.subnet    

    def get_ap_gateway(self) -> str:
        """
            Get EARS Access Point Gateway Address.
        """
        return self.gateway
    
    def get_ap_dns(self) -> str:
        """
            Get EARS Access Point DNS Address.
        """
        return self.dns
    
    def get_ap_mac(self) -> str:
        """
            Get EARS Access Point MAC Address.
        """
        return self.mac
    
    def get_ap_channel(self) -> int:
        """
            Get EARS Access Point Channel Number.
        """
        return self.channel    
    
    def get_ap_hostname(self) -> str:
        """
            Get EARS Access Point Hostname.
        """
        return self.hostname
    
    def _clear_details(self) -> None:
        """
            Internal function to clear AP Info.
        """
        self.ip       = "0.0.0.0"
        self.subnet   = "0.0.0.0"
        self.gateway  = "0.0.0.0"
        self.dns      = "0.0.0.0"
        self.mac      = "00:00:00:00:00:00"
        self.channel  = 0
        self.hostname = ""         

if __name__ == "__main__":
    ap = Ears_AP()
    print("Class Testing by running directly\n")
    AP_UP = ap.start()
    print(f"Class Version = {ap.getClassVersion()}\n")
    if AP_UP:
        print("EARS Access Point Started\n")
        print(f"SSID          = {ap.get_ap_ssid()}\n")
        print(f"PASSWORD      = {ap.get_ap_password()}\n")
        print(f"IP            = {ap.get_ap_ip()}\n")
        print(f"SubNet        = {ap.get_ap_subnet()}\n")
        print(f"GateWay       = {ap.get_ap_gateway()}\n")
        print(f"DNS           = {ap.get_ap_dns()}\n")
        print(f"MAC           = {ap.get_ap_mac()}\n")
        print(f"Channel       = {ap.get_ap_channel()}\n")
        print(f"Hostname      = {ap.get_ap_hostname()}\n")
        AP_UP = ap.stop()
        if AP_UP:
            print("EARS Access Point Stopped\n")
        else:
            print("EARS Access Point Stop Failed\n")
    else:
        print("EARS Access Point Failed\n")
    