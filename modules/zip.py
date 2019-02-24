import os
import subprocess

cwd = os.getcwd()

for folder in os.listdir(cwd):
	if folder != "zip.py":
		command = f"zip -r {folder}.zip {folder}"