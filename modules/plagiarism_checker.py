import os
import subprocess
from modules.settings import Path as path
import modules.filename_util as fu
import shutil

base_prefix = "__BASE__"

# Uses the MOSS tool offered by Stanford to check similarity among the submissions
# that at least had a proper zip file and name.
def perform_plagiarism_check(main_class):
	# Loop through the folders in the unzipped directory
	# If the filename is a java file, add it to the plagiarism check directory
	# so that we can add it.
	for folder in os.listdir(path.unzipped_dir):
		if folder[0] != '.':
			folder_path = os.path.join(path.unzipped_dir, folder)
			for filename in os.listdir(folder_path):
				filename_parts = filename.split('.')
				if len(filename_parts) != 2:
					continue
				# Copy Java files over to the plag check directory
				if filename_parts[1] == "java":
					src_path = os.path.join(path.unzipped_dir, folder, filename)
					new_name = f"{folder}_{filename}"
					new_name = fu.remove_spaces(new_name)
					dest_path = os.path.join(path.plagiarism_check_dir, new_name)
					


					# os.system(f"cp {src_path} {dest_path}")
					shutil.copyfile(src_path, dest_path)

	# Copy all the files from the sample program directory
	for filename in os.listdir(path.plag_sample_dir):
		filename_parts = filename.split('.')
		if len(filename_parts) != 2:
			continue
		if filename_parts[1] == "java":
			src_path = os.path.join(path.plag_sample_dir, filename)
			new_name = f"{base_prefix}{filename}"
			new_name = fu.remove_spaces(new_name)
			print(new_name)
			dest_path = os.path.join(path.plagiarism_check_dir, new_name)
			


			# os.system(f"cp {src_path} {dest_path}")
			shutil.copyfile(src_path, dest_path)

	# Get the list of files. Escape the space chars if necessary
	file_args = ""
	sample_file_args = ""
	for filename in os.listdir(path.plagiarism_check_dir):
		if filename[0] != '.':
			if base_prefix == filename[0:len(base_prefix)]:
				sample_file_args += f" -b {filename}"
			else:
				file_args += f" {filename}"

	if file_args != "":
		# Change directory to the plagiarism check directory.
		# This is because if we include a long path, the path will be printed in the results.
		# This keeps the plag check results much simpler.
		os.chdir(path.plagiarism_check_dir)
		

		# os.system(f"../../modules/_PLACE_MOSS_HERE/moss -l java{sample_file_args}{file_args}")
		if os.path.exists(path.moss_path):
			cmd = f"{path.moss_path} -l java{sample_file_args}{file_args}"
			os.system(cmd)
		else:
			print("You do not have a proper MOSS file.")
			print("Follow the instructions under \"Registering for Moss\"")
			print("on the following web page: https://theory.stanford.edu/~aiken/moss/")
		

		# Change back to original directory.
		os.chdir(path.base_dir)

		# clear the plag check directory
		for filename in os.listdir(path.plagiarism_check_dir):
			if filename[0] != '.':
				file_path = os.path.join(path.plagiarism_check_dir, filename)
				

				# os.system(f"rm {file_path}")
				os.remove(file_path)
	else:
		print("There are no files to check.")