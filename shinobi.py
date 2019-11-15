#! /usr/bin/env python3

'''
Name: Shinobi-Scanner 1.0
Description: Network Scanner
Version: Python 3.7
-
Author: R4MSOLO
'''

import argparse
import socket
import sys

class NetworkScan():

	def __init__(self):
		print(banner)
		try:
			self.parameters()
			domain = args.address,socket.gethostbyaddr(args.address)
			x = domain[1][0]
			z = domain[1][2]
			print(RED+BOLD+"\n => Target",x,"<=>",z,"\n"+ENDC)
			self.portScan()

		except TypeError:
			print(GREY+"[!] Use ./shinobi.py -h for help"+ENDC)
			quit()

	def portScan(self):

		#Portas encontradas | Port found
		portfound = []
		
		#Serviços encontrados | Services found
		flagfound = []

		#[DEFAULT] Varre todas portas se não for passado parâmetro | scans all ports as default
		if args.ports == None:
			self.ports = list(range(1,65536))
		
		#Faz a varredura nas portas somente passadas por parametro | Scans the ports passed by parameter
		elif args.ports != None:
			self.ports = args.ports

		
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

				portfound.append(port)
				flagfound.append(flag)
				conn.close()

			print(GREEN+"[!] Scanning ports",str(num+1)+"/"+str(len(self.ports)),"...","Open ports:",len(portfound), end = "\r")
		
		
		print("\n\n[+] Open ports found:\n[PORT]\t\t[SERVICE]\n")
		for l in portfound:
			index = portfound.index(l)
			flag = flagfound[index]
			print(str(l)+"/tcp"+"\t",flag)

	def parameters(self):
 		global args
 		parser = argparse.ArgumentParser()
 		parser.add_argument("-a", dest="address", action="store", help="To set the address (ex. -a 127.0.0.1)")
 		parser.add_argument("-p", dest="ports", nargs="+", action="store", help="For specific port scans (ex. -p 22 80)")
 		args = parser.parse_args()

'''Colors'''
PURPLE = '\033[95m'
GREEN = '\033[92m'
GREY = '\033[93m'
RED = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'

banner = PURPLE+BOLD+'''
  ____    _       _                   _       _  
 / ___|  | |__   (_)  _ __     ___   | |__   (_)
 \___ \  | '_ \  | | | '_ \   / _ \  | '_ \  | |
  ___) | | | | | | | | | | | | (_) | | |_) | | |
 |____/  |_| |_| |_| |_| |_|  \___/  |_.__/  |_|
 \t\t\t\t\t[Scanner]
           	  
    _______/\ 	
          /  \    \tVersion: 1.0
     _____|  |    \tAuthor: R4MSOLO
        __/()\__  
       /   /\   \ 
 _____/___/  \___\            
'''+ENDC

if __name__ == "__main__":
	try:
            NetworkScan()
	except KeyboardInterrupt:
            print("\nScan finished by user...")

