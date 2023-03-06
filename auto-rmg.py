#!/usr/bin/env python3
#Coded by: Wyatt Becker
import os
import argparse
parser = argparse.ArgumentParser(description='''Parse nmap scans to enum Java-RMI vulns''')
parser.add_argument('-d', action='store', dest='document',
                    help="nmap document to parse")
parser.add_argument('-p', action='store', dest='RMGpath', default='/usr/local/bin/rmg.jar',
                    help="path to rmg.jar (default: /usr/local/bin/rmg.jar)")
parser.add_argument('-o', action='store', dest='output',default='rmi-hosts.txt', help='File to store RMI hosts (default: rmi-hosts.txt)')
parser.add_argument('-t', action='store', dest='timeout',default='2s', help='timeout for rmg scan (default: 2s)')
args = parser.parse_args()

if not args.document:
	parser.print_help()
	print()
	print("Specify the nmap document to parse with -d ")
	print()
	exit()

os.system('cat '+str(args.document)+'|grep "java-rmi\\| for " |grep java-rmi -B1 |awk \'{print $1,$5}\'|sed \'s/Nmap //g\' |cut -d \' \' -f1 |sed \'s/\\/tcp//g\' |sed \'s/--//g\' |grep "\\S" > tmp')
f=open(args.output,"w")
with open("tmp") as a:
	for line in a:
		if "." in line:
			host=line
		else:
			f.write(str(host.rstrip())+" "+str(line))
os.system("rm tmp 2>/dev/null")
f.close()
with open(args.output) as f:
	for line in f:
		print("************************")
		print(line.rstrip())
		print("************************")
		os.system("timeout --foreground "+args.timeout+" java -jar "+str(args.RMGpath)+" enum " + str(line))
