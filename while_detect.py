#!/usr/bin/python3
################################################################################
# Authors:
#       Haru Zheng              <towwy321@gmail.com>
#
################################################################################

import re
import sys

# Simple code
txt = '''
#include <stdio.h>
#include <stdlib.h>

void func1(void) {
	while (1) {
		if (1 == 0) {
			printf("GG\n");
		}
		while (0) {
			;
		}
	}
}


int main(void) {
	int a = 0;
	while (a++ < 10) {
		;
	}
	return 0;
}
'''

# Show help
def help():
	print('''
		./<Python_file>.py -h/--help/help
		./<Python_file>.py <FILE_NAME>
		python3 ./<Python_file>.py <FILE_NAME>
	''')

# Print with line number
def print_linenum(context, line = 0):
	for data in context.split('\n'):
		print(str(line) + ":", data)
		line += 1

# Index to line number of file
def index2linenumber(file_name, index):
	fd = open(str(file_name), "r")
	txt = fd.read()
	txt = txt[0:index]
	return (len(re.findall('\n', txt)) + 1)

# Search while in file (now support c code and linux coding style)
def search_while(file_name):
	fd = open(str(file_name), "r")
	txt = fd.read()
	index_count = 0

	while (1):
		# If this file not have while, it will be exit.
		if (re.search("\n[\t]+while", txt) == None):
			if (index_count == 0):
				print("\n-------------------------------\n")
				print(file_name, "not have while.")
			break

		print("\n-------------------------------\n")

		x = re.search("\n[\t]+while", txt).start() + 1
		index_count += x
		linenumber = index2linenumber(file_name, index_count)

		print("In file '" + str(file_name) + "'")
		print("Start index is", index_count, "(" + str(hex(index_count))+ ")")
		print("Start line is", linenumber)
		print(file_name, ":", linenumber)

		txt_tmp = txt[x:]
		scope = txt_tmp

		n = 0
		count = 0
		b = scope.find("{")
		e = scope.find("}")
		s = scope

		if (s[0:scope.find("\n")].find("{") == -1):
			n = -1
			count += scope.find("\n") + s[scope.find("\n")+1:].find("\n")

		while (1):
			if (n == -1):
				break
			if (b < e and b > -1):
				count += b
				count += 1
				n += 1
				s = s[b+1:]
			elif (b > e or b == -1):
				count += e
				count += 1
				n -= 1
				s = s[e+1:]

			b = s.find("{")
			e = s.find("}")

			if (n == 0):
				break

		print_linenum(txt_tmp[0:count], linenumber)
		txt = txt[x+5:]
		index_count += 5
		if (txt.find("while") == -1):
			break

	print("\n-------------------------------\n")
	print(file_name , "is done.")
	print("\n-------------------------------\n")

# Main Function
def _main_():
	print("Argv has", sys.argv)

	if (len(sys.argv) > 1):
		if (str(sys.argv[1]) == "help" or str(sys.argv[1]) == "-h" or str(sys.argv[1]) == "--help"):
			help()
			return

		argv = sys.argv[1:]
		for file_list in argv:
			print("Curret file is", file_list)
			search_while(str(file_list))
	else:
		help()

_main_()

