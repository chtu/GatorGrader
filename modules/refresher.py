import os
import subprocess
from modules.settings import Path, Design
import shutil

def move_back_to_initial_dir(dir):
	for filename in os.listdir(dir):
		if filename[0] == '.':
			continue
		src_path = os.path.join(dir, filename)
		dest_path = os.path.join(Path.initial_sub_dir, filename)
		os.move(src_path, dest_path)

def clear_initial_dir():
	for folder in os.listdir(Path.initial_sub_dir):
		shutil.rmtree(os.path.join(Path.initial_sub_dir, folder))

class Refresher:
	def run():
		print("Restoring test data...")
		clear_initial_dir()

		for folder in os.listdir(Path.invalid_dir):
			if folder[0] == '.':
				continue
			folder_path = os.path.join(Path.invalid_dir, folder)
			for file in os.listdir(folder_path):
				src_path = os.path.join(folder_path, file)
				dest_path = os.path.join(Path.initial_sub_dir, file)
				os.move(src_path, dest_path)

		move_back_to_initial_dir(Path.valid_checked_dir)
		move_back_to_initial_dir(Path.valid_sub_dir)
		move_back_to_initial_dir(Path.valid_checked_graded_dir)

		test_zips = os.listdir(Path.initial_sub_dir)
		for i in range(0, len(test_zips)):
			test_zip_folder = os.path.join(Path.initial_sub_dir, f"test_zip_{i+1}")
			os.mkdir(test_zip_folder)
			os.move(os.path.join(Path.initial_sub_dir, test_zips[i]), os.path.join(test_zip_folder, test_zips[i]))


		for folder in os.listdir(Path.unzipped_dir):
			if folder[0] == '.':
				continue
			folder_path = os.path.join(Path.unzipped_dir, folder)
			shutil.rmtree(folder_path)

		print("Default test data restored.")