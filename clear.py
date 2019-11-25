import os
import subprocess

from modules.main import EvaluatorProgram as evaluator
from modules.settings import Path as path, Settings as settings
import modules.filename_util as fu
import shutil


def clear_folders_from_dir(dir):
	for folder_name in os.listdir(dir):
		if folder_name[0] == '.':
			continue
		path = os.path.join(dir, folder_name)
		shutil.rmtree(path)

def clear_files_from_dir(dir):
	for filename in os.listdir(dir):
		if filename[0] == '.':
			continue
		path = os.path.join(dir, filename)
		# os.system(f"rm {path}")
		os.remove(path)

def copy_to_initial_dir(dir):
	dir_files = os.listdir(dir)
	for i in range(0, len(dir_files)):
		folder_name = dir_files[i]
		if folder_name[0] == '.':
			continue
		# Path to the test file
		src_path = os.path.join(dir, (folder_name))
		# Set destination of the file
		dest_path = os.path.join(path.initial_sub_dir, folder_name)

		shutil.copytree(src_path, dest_path)

def clear_initial_dir():
	for folder in os.listdir(path.initial_sub_dir):
		if folder[0] == ".":
			continue
		if folder != settings.placeholder:
			shutil.rmtree(os.path.join(path.initial_sub_dir, folder))

def clear_directories():
	clear_initial_dir()
	for folder in os.listdir(path.invalid_dir):
		if folder[0] == '.':
			continue
		folder_path = os.path.join(path.invalid_dir, folder)
		clear_files_from_dir(folder_path)
	clear_files_from_dir(path.valid_checked_dir)
	clear_files_from_dir(path.valid_sub_dir)
	clear_files_from_dir(path.valid_checked_graded_dir)
	clear_folders_from_dir(path.unzipped_dir)

def clear_plag_dir():
	for filename in os.listdir(path.plagiarism_check_dir):
		if filename[0] == ".":
			continue

		if filename != 'moss':
			dir_path = os.path.join(path.plagiarism_check_dir, filename)
			

			os.remove(dir_path)

def clear_submission_dir():
	for filename in os.listdir(path.initial_sub_dir):
		if folder[0] == ".":
			continue

		if filename != settings.placeholder:
			shutil.rmtree(os.path.join(path.initial_sub_dir, filename))


fu.init_storage_dirs()

clear_directories()
clear_plag_dir()
print("Directories cleared.")
