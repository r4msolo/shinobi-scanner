#! /usr/bin/env python3

'''
Name: Shinobi-Scanner 1.1
Description: Network Scanner
Version: Python 3.7
-
Author: Igor M. Martins (r4msolo)
'''

import argparse
import socket
import sys

class NetworkScan():

	#Portas encontradas | Port found
	portfound = []
		
	#Serviços encontrados | Services found
	flagfound = []

	def __init__(self):
		print(banner)
		try:
			self.parameters()
			try:
			    domain = args.address,socket.gethostbyaddr(args.address)
			    x = domain[1][0]
			    z = domain[1][2][0]
			    print(RED+BOLD+"\n => Target",x,"<=>",z,"\n"+ENDC)
			except:
			    print(RED+BOLD+"\n => Target",args.address,"\n"+ENDC)
			
			self.portScan()

		except TypeError:
			print(GREY+"[!] Use ./shinobi.py -h for help"+ENDC)
			quit()

	def portScan(self):
		#[DEFAULT] Varre todas portas se não for passado parâmetro | scans all ports as default
		if args.ports == None:
			self.ports = list(range(1,65536))
		
		#Faz a varredura nas portas somente passadas por parametro | Scans the ports passed by parameter
		elif args.ports != None:
			self.ports = args.ports

		try:
			for num, port in enumerate(self.ports):
				conn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
				conn.settimeout(2)
				if conn.connect_ex((args.address,int(port))) == 0:
					try:
						#busca o serviço por banner retornado | finds the service by the returned banner
						flag = conn.recv(40).decode("utf-8","ignore").strip("\n")
						assert flag
						conn.close()

					except:
						flag = "\tUnknown"
						conn.close()

					self.portfound.append(port)
					self.flagfound.append(flag)
				
				conn.close()		
				print(GREEN+"[!] Scanning ports",str(num+1)+"/"+str(len(self.ports)),"...","Open ports:",len(self.portfound), end = "\r")

			if len(self.portfound) >=1:
				self.showResults()
			else:
				print("\n[!] No port found")


		except KeyboardInterrupt:
			self.showResults()
			print("Scan finished by user...")
		
	def showResults(self):
		print("\n[+] Open ports found:\n[PORT]\t\t[SERVICE]\n")
		for l in self.portfound:
			index = self.portfound.index(l)
			flag = self.flagfound[index]
			print(str(l)+"/tcp"+"\t",flag)

	def parameters(self):
 		global args
 		parser = argparse.ArgumentParser()
 		parser.add_argument("-a", dest="address", action="store", help="To set the address (ex. -a 127.0.0.1)")
 		parser.add_argument("-p", dest="ports", nargs="+", action="store", help="For specific port scans (ex. -p 22 80)")
 		args = parser.parse_args()

'''Colors'''
BLUE = '\033[94m'
GREEN = '\033[92m'
GREY = '\033[93m'
RED = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'

banner = BLUE+BOLD+'''
  ____    _       _                   _       _  
 / ___|  | |__   (_)  _ __     ___   | |__   (_)
 \___ \  | '_ \  | | | '_ \   / _ \  | '_ \  | |
  ___) | | | | | | | | | | | | (_) | | |_) | | |
 |____/  |_| |_| |_| |_| |_|  \___/  |_.__/  |_|
 \t\t\t\t\t[Network Scanner]
           	  
    _______/\ 	
          /  \    \tVersion: 1.1
     _____|  |    \tAuthor: R4MSOLO
        __/()\__  
       /   /\   \ 
 _____/___/  \___\            
'''+ENDC

if __name__ == "__main__":
	NetworkScan()
