import os
import subprocess



def insert_escape_char(filename):
	return_str = ""
	for i in range(0, len(filename)):
		ch = filename[i]
		if ch == ' ':
			return_str += "\\"
		return_str += ch
	return return_str
