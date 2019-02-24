import os
import subprocess
from modules.settings import Settings as settings, Path as path



def insert_escape_char(filename):
	return_str = ""
	for i in range(0, len(filename)):
		ch = filename[i]
		if ch == ' ':
			return_str += "\\"
		return_str += ch
	return return_str


def init_storage_dirs():
	for storage_dir in path.storage_directories:
		if not os.path.exists(storage_dir):
			os.system(f"mkdir {storage_dir}")