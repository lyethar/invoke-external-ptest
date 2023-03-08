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
	os.system("whois " + domain + " > domain-whois.txt")
	os.system("""cat domain-whois.txt | grep -e 'Domain Status:' -e 'Domain Name' > dns-locks.txt""")
	os.system("cat dns-locks.txt")

def ikescan():
	print(Fore.GREEN + "Enumerating using Ikescan\n")
	print(Style.RESET_ALL)
	
	# Appending Lines to lines array
	with open(scope) as file_in:
    		lines = []
    		for line in file_in:
        		lines.append(line)
    
	for l in lines:
    		print(Fore.GREEN + "\nEnumerating " + l)
    		os.system('ikescan -A ' + l + ' | tee ike-scan-results.txt')


#Arguments
domain = sys.argv[1]
scope = sys.argv[2]
	
printBanner()
dnsenum()
ikescan()
