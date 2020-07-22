#!/usr/bin/python

#pip install pyperclip, 
#pip install Pillow
#python3 -m pip install requests

import pyperclip
import sys
import getopt
import os

command = sys.argv[1].lower()
try: 
#print 'Argument List:', str(sys.argv)
#print ("First argument: %s" % str(sys.argv[1]))
	if command == "-l" or command == "-list":
		#currentDirectory = pathlib.Path('./txt')
		#for currentFiles in currentDirectory.iterdir():
		#removetable = str.maketrans('.txt', 'txt/')
		#print currentFiles
		lst = sorted(os.listdir("./txt"))
		print lst
	elif command == "-help" or command == "-h":
		file = open("readme.txt" ,mode='r')
		datatext= file.read()
		file.close()
		print datatext
	else:
		textfile = str(command)
		file = open("txt/"+textfile ,mode='r')
		datatext= file.read()
		data = datatext.decode('utf-8')
		file.close()
		pyperclip.copy(data)
		print ""
		print data
		print ""
		print "* "+command+" saved to clipboard. *"
		
except Exception as e:
	print "command or text not found. try ascii -h/-help or ascii -l/-list."
