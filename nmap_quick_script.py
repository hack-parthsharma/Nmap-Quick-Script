#################################################################
## Title: Nmap Quick Script                                    ##         
## Author: Robel Campbell                                      ## 
## Position: Penetration Tester                                ## 
## Company: ePlus Technology                                   ## 
## Date Created: 7/3/2019                                      ## 
## Website: https://github.com/robel1889/nmap_quick_script.git ##
#################################################################

import os 
import sys

print("Nmap Quick Script Tool! \nA python script to automate frequent nmap scans at work. \nWritten By: Robel Campbell \nhttps://github.com/robel1889/nmap_quick_script.git")


def usage():
    print("\nPlease enter a list of valid IP addresses.\n")
    print ("Usage: python3 ", sys.argv[0], " <ip list file>\n")
 

if (len(sys.argv) < 2 or len(sys.argv) > 2):
    usage()
    sys.exit()
else:
    # Create nmap directory if it doesn't exist.
    if not os.path.exists('nmap/'):
        print("\n[+] Creating nmap directory...\n")
        os.makedirs('nmap')
    else: 
        print("\n[+] Nmap directory already exists...\n")
            
    # Run all three nmap scans and store results in all file formats.
    print("\n[+] Enumerating hosts-up!...\n")
    os.system('nmap -sP -Pn -oA nmap/hosts_up -iL %s > /dev/null' % (sys.argv[1]))

    print("\n[+] Running quick port scan!...\n")
    os.system('nmap -T4 --max-retries=1 -Pn -oA nmap/port_scan -iL %s > /dev/null' % (sys.argv[1]))

    print("\n[+] Running script scan!...This may take a minute...\n")
    os.system('nmap -sV -sC -T4 --max-retries=1 -Pn -oA nmap/script_scan -iL %s > /dev/null' % (sys.argv[1]))

    print("\n[+] Scanning complete!...please check nmap directory for results.")
