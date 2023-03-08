#!/bin/python3 

import sys
from colorama import Fore, Back, Style 
import subprocess 
import os 
import argparse


# Define Banner
def printBanner():
	print (Fore.YELLOW + """
   ________  ________  ________  ________  ____ ___  ________       _______  ________  ________   _______  _______   ________  ________  ________ 
  ╱        ╲╱    ╱   ╲╱    ╱   ╲╱        ╲╱    ╱   ╲╱        ╲    ╱╱       ╲╱    ╱   ╲╱        ╲╱╱      ╱ ╱       ╲ ╱        ╲╱        ╲╱        ╲
 _╱       ╱╱         ╱         ╱         ╱         ╱         ╱   ╱╱        ╱_       _╱        _╱╱       ╲╱        ╱╱         ╱        _╱        _╱
╱         ╱         ╱╲        ╱         ╱        _╱        _╱   ╱        _╱         ╱╱       ╱╱         ╱        ╱╱         ╱-        ╱╱       ╱  
╲╲_______╱╲__╱_____╱  ╲______╱╲________╱╲____╱___╱╲________╱    ╲________╱╲___╱____╱ ╲______╱ ╲________╱╲________╱╲___╱____╱╲________╱ ╲______╱  \n\n\n """)
print(Style.RESET_ALL)

def dnsenum(domain):
	print(Fore.GREEN + "Hold on tight! Enumerating DNS!\n")
	print(Style.RESET_ALL)
	print(Fore.YELLOW)
	os.system("whois " + domain + " > domain-whois.txt")
	os.system("""cat domain-whois.txt | grep -e 'Domain Status:' -e 'Domain Name' > dns-locks.txt""")
	os.system("cat dns-locks.txt")
	print(Style.RESET_ALL)
	
def ikescan(scope):
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
    		
def metalookup(domain):
	print(Fore.GREEN + "\nInstalling pymeta\n")
	print(Style.RESET_ALL)
	
	print(Fore.YELLOW)
	os.system("pip3 install pymetasec")
	print(Fore.GREEN + "\nUsing pymeta!\n")
	print(Fore.YELLOW)
	os.system("pymeta -d " + domain)
	
def parse_args():
	parser = argparse.ArgumentParser()

	parser.add_argument("-d", "--domain", type=str,
		help="The domain you want to enumerate")
	parser.add_argument("-s", "--scope", type=str,
			help="The scope.txt file.")
	return parser.parse_args()



#Arguments
def main():
	args = parse_args()
	domain = args.domain
	scope = args.scope
	printBanner()
	dnsenum(domain)
	ikescan(scope)
	metalookup(domain)
	
if __name__ == '__main__':
	main()
