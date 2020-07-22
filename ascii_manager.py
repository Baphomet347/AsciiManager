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
	script_dir = os.path.dirname(__file__)
	if command == "-l" or command == "-list":
		#currentDirectory = pathlib.Path('./txt')
		#for currentFiles in currentDirectory.iterdir():
		#removetable = str.maketrans('.txt', 'txt/')
		#print currentFiles
		rel_path = "txt/"
		abs_file_path = os.path.join(script_dir, rel_path)
		lst = sorted(os.listdir(abs_file_path))
		print(lst)
	elif command == "-help" or command == "-h":
		rel_path = "readme.txt"
		abs_file_path = os.path.join(script_dir, rel_path)
		file = open(abs_file_path ,mode='r')
		datatext= file.read()
		file.close()
		print(datatext)
	else:
		textfile = str(command)
		rel_path = "txt/"+textfile
		abs_file_path = os.path.join(script_dir, rel_path)
		file = open(abs_file_path ,mode='r', encoding="utf8")
		datatext= file.read()
		data = datatext
		file.close()
		pyperclip.copy(data)
		print(data)
		print("")
		print("* "+command+" saved to clipboard. *")
except Exception as e:
	print("command or text not found. try ascii -h/-help or ascii -l/-list.")

