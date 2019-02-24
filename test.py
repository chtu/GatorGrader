import os
import subprocess

from modules.main import EvaluatorProgram as evaluator
from modules.settings import Path as path, Settings as settings
import modules.filename_util as fu

def clear_folders_from_dir(dir):
	for folder_name in os.listdir(dir):
		if folder_name[0] == '.':
			continue
		path = os.path.join(dir, folder_name)
		os.system(f"rm -rf {path}")

def clear_files_from_dir(dir):
	for filename in os.listdir(dir):
		if filename[0] == '.':
			continue
		path = os.path.join(dir, filename)
		os.system(f"rm {path}")

def copy_to_initial_dir(dir):
	dir_files = os.listdir(dir)
	for i in range(0, len(dir_files)):
		folder_name = fu.insert_escape_char(dir_files[i])
		if folder_name[0] == '.':
			continue
		# Path to the test file
		src_path = os.path.join(dir, (folder_name))
		# Set destination of the file
		dest_path = os.path.join(path.initial_sub_dir, folder_name)
		command = f"cp -r {src_path} {dest_path}"
		#print(command)
		os.system(command)

def clear_initial_dir():
	for folder in os.listdir(path.initial_sub_dir):
		if folder != settings.placeholder:
			os.system(f"rm -rf {os.path.join(path.initial_sub_dir, folder)}")

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
		if filename != 'moss':
			dir_path = os.path.join(path.plagiarism_check_dir, fu.insert_escape_char(filename))
			os.system(f"rm {dir_path}")

# Run the test

print("Restoring test data...")
fu.init_storage_dirs()
clear_directories()
copy_to_initial_dir(path.test_files_dir)

print("Default test data restored. Running program.")
evaluator.run('Test')
clear_directories()
clear_plag_dir()
print("Test run complete.")