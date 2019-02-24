import os
import subprocess
from modules.settings import Path as path
import modules.filename_util as fu


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
				# Copy Java files over to the plag check directory
				if filename_parts[1] == "java":
					src_path = os.path.join(path.unzipped_dir, folder, fu.insert_escape_char(filename))
					new_name = f"{folder}_{fu.insert_escape_char(filename)}"
					dest_path = os.path.join(path.plagiarism_check_dir, new_name)
					os.system(f"cp {src_path} {dest_path}")

	# Get the list of files. Escape the space chars if necessary
	file_args = ""
	for filename in os.listdir(path.plagiarism_check_dir):
		if filename[0] != '.':
			file_args += f" {fu.insert_escape_char(filename)}"

	if file_args != "":
		# Change directory to the plagiarism check directory.
		# This is because if we include a long path, the path will be printed in the results.
		# This keeps the plag check results much simpler.
		os.chdir(path.plagiarism_check_dir)
		os.system(f"../../modules/_PLACE_MOSS_HERE/moss -l java{file_args}")
		# Change back to original directory.
		os.chdir(path.cwd)

		# clear the plag check directory
		for filename in os.listdir(path.plagiarism_check_dir):
			if filename[0] != '.':
				file_path = os.path.join(path.plagiarism_check_dir, fu.insert_escape_char(filename))
				os.system(f"rm {file_path}")
	else:
		print("There are no files to check.")