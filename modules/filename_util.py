import os
import subprocess
from modules.settings import Settings as settings, Path as path




def init_storage_dirs():
	for storage_dir in path.storage_directories:
		if not os.path.exists(storage_dir):
			# os.system(f"mkdir {storage_dir}")
			os.mkdir(storage_dir)