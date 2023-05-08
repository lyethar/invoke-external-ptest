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


def invokescan(scope):
	print(Fore.GREEN + "\nUsing nmap to scan scope!")	
	print(Style.RESET_ALL)
	print(Fore.YELLOW)
	os.system('nmap -sS -Pn -T3 -iL ' + scope + ' -oA outpuFile')


def invoketrevorsprayrecon(domain):
	print(Fore.GREEN + "\nUsing trevorspray to enumerate endpoint!")
	os.system('trevorspray --recon ' + domain + ' > trevorspray-recon.txt')
	os.system("""cat trevorspray-recon.txt | grep 'token_endpoint' > token_endpoint""")
	os.system("""sed -i '1d' token_endpoint""")
	os.system("""sed -i '$d' token_endpoint""")
	os.system("""cat token_endpoint | tr -d "[:space:]" > token_endpoint2""")
	os.system("""cat token_endpoint2 | cut -d ":" -f3 > token_endpoint3""")
	os.system("""sed -i 's/,//g' token_endpoint3""")
	os.system("""sed -i 's/"//g' token_endpoint3""")
	os.system("""sed -i -e 's/^/https:/' token_endpoint3""")
	print('Using the following endpoint to gather users!')
	print(Fore.YELLOW)
	os.system('cat token_endpoint3')
	userlists = ["https://raw.githubusercontent.com/insidetrust/statistically-likely-usernames/master/john.smith.txt","https://raw.githubusercontent.com/insidetrust/statistically-likely-usernames/master/jjsmith.txt","https://raw.githubusercontent.com/insidetrust/statistically-likely-usernames/master/johnsmith.txt","https://raw.githubusercontent.com/insidetrust/statistically-likely-usernames/master/jsmith.txt"]
	for x in userlists:
    		os.system('wget ' + x + ' 2>/dev/null')
	os.system('for file in $(ls | grep smith); do echo $file >> file_list.txt; done')
	with open("file_list.txt") as file_in:
    		lines = []
    		for line in file_in:
        		lines.append(line)   
	for l in lines:
    		print("\nEnumerating: " + domain + " using " + l)
    		os.system('trevorspray --recon ' + domain + ' -u ' + l + ' --threads 10' )

def parse_args():
	parser = argparse.ArgumentParser()

	parser.add_argument("-d", "--domain", type=str,
		help="The domain you want to enumerate")
	parser.add_argument("-s", "--scope", type=str,
			help="The scope.txt file.")	
	parser.add_argument("-x", "--nmap", type=str,
			help="Defines wether to launch an nmap scan or not.")
			
	return parser.parse_args()



#Arguments
def main():
	args = parse_args()
	domain = args.domain
	scope = args.scope
	nmap = args.nmap
	if not nmap:
		printBanner()
		dnsenum(domain)
		invoketrevorsprayrecon(domain)
		metalookup(domain)
		ikescan(scope)
	else:
		printBanner()
		dnsenum(domain)
		invoketrevorsprayrecon(domain)
		metalookup(domain)
		ikescan(scope)
		invokescan(scope)
		
	
if __name__ == '__main__':
	main()
