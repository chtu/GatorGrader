import os
import subprocess
from modules.settings import Path, Settings
import modules.filename_util as fu


class SubmissionFile:
	def __init__(self, filename, path_to_dir, main_class):
		self.filename = fu.insert_escape_char(filename) # Name of the file, including extension
		self.main_class = main_class
		# Set the following as None, and then validate.
		# If validation is successfull, these values will be pulled from the
		# filename itself.
		self.first_name = None
		self.last_name = None
		self.id_number = None
		self.user_dir_name = None
		self.validate_filename()

		self.column_width = 50
		self.current_dir = path_to_dir
		self.current_path = os.path.join(path_to_dir, self.filename)

		self.unzipped = False

	# Set the current location of the file
	def set_current_path(self, current_directory):
		self.current_path = os.path.join(current_directory, self.filename)
		self.current_dir = current_directory

	# Move the file to a new directory.
	# new_directory_path is the new directory where the file will reside.
	# You don't need to specify the filename itself.
	def move(self, new_directory_path):
		updated_path = os.path.join(new_directory_path, self.filename)
		os.system('mv ' + self.current_path + ' ' + updated_path)
		self.current_dir = new_directory_path
		self.current_path = updated_path

	def rename(self, new_name):
		dest_path = os.path.join(self.current_dir, new_name)
		os.system(f"mv {self.current_path} {dest_path}")
		self.filename = new_name

	def set_user_dir_name(self):
		if self.first_name != None and self.last_name != None and self.id_number != None:
			self.user_dir_name = f"{self.first_name}_{self.last_name}_{self.id_number}"

	# Move the file to a directory where it will be deemed as graded.
	def set_to_graded(self):
		self.move(Path.valid_checked_graded_dir)

	# Run the program in the console.
	def run_program(self):
		try:
			path_to_dir = os.path.join(Path.unzipped_dir, self.user_dir_name)
			path_to_file = os.path.join(path_to_dir, f"{self.main_class}.class")
			if os.path.exists(path_to_file):
				os.system('java -cp ' + path_to_dir + ' ' + self.main_class)
			else:
				print("Compilation failed.\nNo main class found.")
		except:
			print("Something caused the program to stop.")

	# Display the file contents to the user.
	def display(self):
		path_to_dir = os.path.join(Path.unzipped_dir, self.user_dir_name)
		os.system("cat " + os.path.join(path_to_dir, f"{self.main_class}.java"))

	# Validate the filename.
	def validate_filename(self):
		submission_file_parts = self.filename.split('.')
		if len(submission_file_parts) != 2: # If more than 2 periods.
			return False

		if submission_file_parts[1] != 'zip': # If ext is not zip
			return False

		filename_parts = submission_file_parts[0].split('_')
		if len(filename_parts) != 3: # If more than 2 underscores in name
			return False

		firstname = filename_parts[0]
		lastname = filename_parts[1]
		str_id_number = filename_parts[2]

		if len(str_id_number) != 9: # If id_num is not 9 characters
			return False

		# Check if the first name isn't a number.
		try:
			val = int(firstname)
			return False
		except:
			success = True
		# Check if the last name isn't a number.
		try:
			val = int(lastname)
			return False
		except:
			success = True
		# Check if the ID number is actually a number.
		try:
			id_number = int(str_id_number)
		except:
			return False
		# Check if ID number is actually 9 digits when converted to an integer.
		if id_number < 100000000 or id_number > 999999999:
			return False

		# If this point is reached, then that means that there is
		# nothing wrong with the name. Set the values of first_name,
		# last_name, and id_number.
		self.first_name = firstname
		self.last_name = lastname
		self.id_number = str_id_number
		self.set_user_dir_name()
		return True

	# Checks the validity of the zip filename.
	# We run the validation method when the object is constructed, so if any
	# of the values are None, then we can assume that the filename was not valid.
	def filename_is_valid(self):
		if self.first_name == None or self.last_name == None or self.id_number == None:
			return False
		else:
			return True

	# Unzip the file.
	# Names the unzipped directory after the ID number.
	# Overwrites any existing directory.
	def unzip(self):
		if self.filename_is_valid():
			subprocess.check_call(['unzip', '-j', '-o', self.current_path, '-d', os.path.join(Path.unzipped_dir, self.user_dir_name)])
			self.unzipped = True

	# Checks the validity of the Java file.
	# It will fail if the filename does not match the name required by the assignment,
	# or if the file extension is not "java"
	def java_file_is_valid(self):
		if self.unzipped:
			if os.path.exists(os.path.join(Path.unzipped_dir, self.user_dir_name, f"{self.main_class}.java")):
				return True
			else:
				return False
		else:
			print("Not unzipped yet.")