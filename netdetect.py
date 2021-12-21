#!/usr/bin/python3

"""Developed by Shyam Karthick(@TheHumanGoogle).
   Under the repo- Network-Detective in github.
   For suggestions/bug fixes,contact: lopinghealer@gmail.com"""
	
from socket import *
import optparse
from threading import *
import pyfiglet

def connScan(tgthost, tgtport):
	try:
		sock = socket(AF_INET, SOCK_STREAM)
		sock.connect((tgthost,tgtport))
		print('[+] %d/TCP Open.' % (tgtport))
	except:
		print('[-] %d/TCP Closed.' % (tgtport))
	finally:
		sock.close()

def portscan(tgthost,tgtports):
	try:
		tgtIP = gethostbyname(tgthost)
	except:
		print('Unknown Host %s .' %(tgthost))
	try:
		tgtname = gethostbyaddr(tgtIP)
		print('[+] Scan results for: ' + tgtname[0])
	except:
		print('[+] Scan results for: ' + tgtIP)
	setdefaulttimeout(1)
	for tgtport in tgtports:
		t = Thread(target=connScan, args=(tgthost,int(tgtport)))
		t.start()

def main():
	banner = pyfiglet.figlet_format('NET-DETECT')
	print(banner)
	print('[+]Title: Network Detective.')
	print('[+]Developed By: Shyam Karthick.')
	print('[+]Licensed Under: GNU GPLv3.0 .')
	print('[+]Contact: lopinghealer@gmail.com .')
	parser = optparse.OptionParser('Usage of program: ' + '-H <Target Host> -p <Target Port>')
	parser.add_option('-H',dest='tgthost',type='string',help='Specify Target Host.')
	parser.add_option('-p',dest='tgtports',type='string',help='Specify Target Ports separated by comma.')
	(options,args) = parser.parse_args()
	tgthost = options.tgthost
	tgtports = str(options.tgtports).split(',')
	if (tgthost == None) | (tgtports[0] == None):
		print(parser.usage)
		exit(0)
	portscan(tgthost,tgtports)

if __name__ == '__main__':
	main()
