import os
import subprocess
from modules.settings import Path
from modules.submission import SubmissionFile


def remove_file_if_exists(submission_file):
	found = False
	for folder in os.listdir(Path.invalid_dir):
		if folder[0] == '.': #Skip hidden folders
			continue
		folder_path = os.path.join(Path.invalid_dir, folder)
		for filename in os.listdir(folder_path):
			if submission_file == filename:
				file_path = os.path.join(folder_path, submission_file)
				os.system(f"rm {file_path}")
				found = True
				break
		if found:
			break

class Validator:
	def validate(submission_file, full_path, main_class):
		remove_file_if_exists(submission_file)
		sub = SubmissionFile(submission_file, full_path, main_class)

		# Check if the filename is valid.
		if sub.filename_is_valid():
			sub.move(Path.valid_sub_dir)
		else:
			sub.move(Path.invalid_sub_dir)
			return

		# Check if it properly unzips
		try:
			sub.unzip()
		except:
			sub.move(Path.unzip_fail_dir)
			return

		# Check if the Java filename is correct
		if not sub.java_file_is_valid():
			sub.move(Path.invalid_java_file_dir)
			return

		# Check if the Java file compiles properly.
		user_dir = os.path.join(Path.unzipped_dir, sub.user_dir_name)
		java_file_path = os.path.join(user_dir, f"{main_class}.java")
		compile_info_filename = "compile_info.txt"
		compile_info_path = os.path.join(user_dir, compile_info_filename)
		try:
			subprocess.check_call(['javac', java_file_path, '-d', user_dir])
			os.system(f'echo "Compilation successful." > {compile_info_path}')
		except Exception as e:
			sub.move(Path.non_compilable_dir)
			os.system(f'echo "Compilation failed." > {compile_info_path}')

			return

		# If the program reaches this point, then that means the submission
		# was validated with positive results and no errors occurred
		sub.move(Path.valid_checked_dir)




