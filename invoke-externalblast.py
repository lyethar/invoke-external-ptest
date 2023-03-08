#!/bin/python3 

import sys
from colorama import Fore, Back, Style 
import subprocess 
import os 


# Define Banner
def printBanner():
	print (Fore.YELLOW + """
   ________  ________  ________  ________  ____ ___  ________       _______  ________  ________   _______  _______   ________  ________  ________ 
  ╱        ╲╱    ╱   ╲╱    ╱   ╲╱        ╲╱    ╱   ╲╱        ╲    ╱╱       ╲╱    ╱   ╲╱        ╲╱╱      ╱ ╱       ╲ ╱        ╲╱        ╲╱        ╲
 _╱       ╱╱         ╱         ╱         ╱         ╱         ╱   ╱╱        ╱_       _╱        _╱╱       ╲╱        ╱╱         ╱        _╱        _╱
╱         ╱         ╱╲        ╱         ╱        _╱        _╱   ╱        _╱         ╱╱       ╱╱         ╱        ╱╱         ╱-        ╱╱       ╱  
╲╲_______╱╲__╱_____╱  ╲______╱╲________╱╲____╱___╱╲________╱    ╲________╱╲___╱____╱ ╲______╱ ╲________╱╲________╱╲___╱____╱╲________╱ ╲______╱   """)
print(Style.RESET_ALL)

def dnsenum():
	print(Fore.GREEN + "Hold on tight! Enumerating DNS!\n")
	print(Style.RESET_ALL)
	
