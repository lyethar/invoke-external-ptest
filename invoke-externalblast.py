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
╲╲_______╱╲__╱_____╱  ╲______╱╲________╱╲____╱___╱╲________╱    ╲________╱╲___╱____╱ ╲______╱ ╲________╱╲________╱╲___╱____╱╲________╱ ╲______╱  \n\n\n """)
print(Style.RESET_ALL)

def dnsenum():
	print(Fore.GREEN + "Hold on tight! Enumerating DNS!\n")
	print(Style.RESET_ALL)
	print(Fore.YELLOW)
	os.system("whois " + domain + " > domain-whois.txt")
	os.system("""cat domain-whois.txt | grep -e 'Domain Status:' -e 'Domain Name' > dns-locks.txt""")
	os.system("cat dns-locks.txt")
	print(Style.RESET_ALL)
	
def ikescan():
	print(Fore.GREEN + "\nEnumerating using Ikescan\n")
	print(Style.RESET_ALL)
	
	# Appending Lines to lines array
	with open(scope) as file_in:
    		lines = []
    		for line in file_in:
        		lines.append(line)
    
	for l in lines:
    		print(Fore.GREEN + "\nEnumerating " + l)
    		print(Style.RESET_ALL)
    		print(Fore.YELLOW)
    		os.system('ike-scan -A ' + l + ' > ike-scan-results.txt')
    		print(Style.RESET_ALL)
    		
def metalookup():
	print(Fore.GREEN + "\nInstalling pymeta\n")
	print(Style.RESET_ALL)
	
	print(Fore.YELLOW)
	os.system("pip3 install pymetasec")
	print(Fore.GREEN + "\nUsing pymeta!\n")
	print(Fore.YELLOW)
	os.system("pymeta -d " + domain)
	


#Arguments
domain = sys.argv[1]
scope = sys.argv[2]
	
printBanner()
dnsenum()
ikescan()
metalookup()
