import os
import subprocess
from modules.settings import Path, Settings as settings, Commands
from modules.submission import SubmissionFile
import modules.filename_util as fu
from zipfile import ZipFile


def remove_file_if_exists(submission_file):
	found = False
	for folder in os.listdir(Path.invalid_dir):
		if folder[0] == '.': #Skip hidden folders
			continue
		folder_path = os.path.join(Path.invalid_dir, folder)
		for filename in os.listdir(folder_path):
			if submission_file == filename:
				file_path = os.path.join(folder_path, submission_file)
				# os.system(f"rm {file_path}")
				os.remove(file_path)
				found = True
				break
		if found:
			break

class Validator:
	def validate(submission_file, path_to_dir, main_class):
		remove_file_if_exists(submission_file)
		sub = SubmissionFile(submission_file, path_to_dir, main_class)

		# Check if the filename is valid.
		if sub.filename_is_valid():
			sub.move(Path.valid_sub_dir)
		else:
			parts = path_to_dir.split('/')
			ilearn_sub_dir_parts = parts[len(parts)-1].split('_')
			student_name = ilearn_sub_dir_parts[0]

			# Check each part of the automatically generated iLearn submission folder
			# to get the name of the student
			for i in range(1, len(ilearn_sub_dir_parts)):
				try:
					int(ilearn_sub_dir_parts[i])
					break
				except:
					student_name += f"_{ilearn_sub_dir_parts[i]}"
					new_filename = f"{student_name}__INCORRECT__{sub.filename}"
					sub.rename(new_filename)
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
		message = "Starting."
		try:
			subprocess.check_call([Commands.javac, java_file_path, '-d', user_dir])
			message += "\nCompilation success."

			with open(compile_info_path, "a+") as f:
				f.write("Compilatin successful.")
			# Check to make sure there wasn't a package statement in the java
			# file. If not, then move to invalid and return
			class_file = f"{main_class}.class"
			class_file_found = False
			for file in os.listdir(user_dir):
				if file == class_file:
					class_file_found = True
					break
			if not class_file_found:
				sub.move(Path.package_statement_dir)
				return

		except Exception as e:
			# Error occurred during compilation. Send to invalid
			sub.move(Path.non_compilable_dir)
			#os.system(f'echo "Compilation failed." > {compile_info_path}'
			with open(compile_info_path, "a+") as f:
				f.write(f"Compilation failed.\n{message}\n{str(e)}")
			return

		# If the program reaches this point, then that means the submission
		# was validated with positive results and no errors occurred
		sub.move(Path.valid_checked_dir)




