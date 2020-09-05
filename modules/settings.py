import os
import subprocess
import sys

sys.path.append("..")

from config import main_class as mc


# INSTRUCTIONS: Set the main class for this assignment.
# If students submit a Java file that has a different file and/or main class name,
# they will fail the validation.
# The main class for this assignment


# Current working directory
cwd = os.getcwd()


class Settings:
	# Set this main class
	main_class = mc

	#placeholder file for git
	placeholder = "placeholder.txt"

	def get_platform(self):
		# Constants for operating systems
		linux = "linux"
		osx = 'mac'
		windows = 'windows'

		platforms = {
			'linux1' : linux,
			'linux2' : linux,
			'darwin' : osx,
			'win32' : windows
		}
		if sys.platform not in platforms:
			return sys.platform
		return platforms[sys.platform]

	def get_jdk_path(self):
		'''
		if Settings.get_platform() == "linux" or Settings.get_platform() == "windows":
			jdk_folder_path = os.path.join(cwd, "modules", "jdk", Settings.get_platform(), "jdk-12.0.2", "bin")
			jdk_11_path = os.path.join(cwd, "modules", "jdk", Settings.get_platform(), "jdk-11.0.2", "bin")
		elif Settings.get_platform() == "mac":
			jdk_12_path = os.path.join(cwd, "modules", "jdk", "mac", "jdk-12.0.2.jdk", "Contents", "Home", "bin")
			jdk_11_path = os.path.join(cwd, "modules", "jdk", "mac", "jdk-11.0.2.jdk", "Contents", "Home", "bin")
'''
		system_dir_path = os.path.join(cwd, "modules", "_PLACE_JDK_HERE")

		jdk_path = None

		for folder_name in os.listdir(system_dir_path):
			if folder_name[0:3] == "jdk":
				jdk_path = os.path.join(system_dir_path, folder_name)
				break

		if self.get_platform() == "linux" or self.get_platform() == "windows":
			jdk_path = os.path.join(jdk_path, "bin")
		elif self.get_platform() == "mac":
			jdk_path = os.path.join(jdk_path, "Contents", "Home", "bin")

		return jdk_path

class Path:
	# base directory
	base_dir = cwd

	# Storage directory
	storage_dir = os.path.join(cwd, 'storage')
	# Files working directory
	fwd = os.path.join(cwd, 'files')
	# Main java file
	main_java_file = "%s.java" % Settings.main_class
	# Emails dir
	emails = os.path.join(base_dir, "_PLACE_EMAILS_HERE")
	emails_file = os.path.join(emails, "emails.csv")
	test_emails_file = os.path.join(emails, "test_emails.csv")


	# initial submissions directory
	initial_sub_dir = os.path.join(cwd, '_PLACE_SUBMISSIONS_HERE')
	# validated filenames directory (valid)
	valid_sub_dir = os.path.join(storage_dir, 'to_be_unzipped_and_compiled')
	# validated and ungraded submissions directory
	valid_checked_dir = os.path.join(storage_dir, 'valid_ungraded')
	# validated and graded submissions directory
	valid_checked_graded_dir = os.path.join(storage_dir, 'valid_graded')
	# unzipped files directory
	unzipped_dir = os.path.join(storage_dir, 'unzipped')
	# plagiarism check folder
	plagiarism_check_dir = os.path.join(storage_dir, 'plagiarism_check')
	# Moss file
	moss_path = os.path.join(base_dir, "modules", "_PLACE_MOSS_HERE", 'moss')
	# Plag check samples
	# This is for files obtained online to compare the student submissions
	# to see if they copied directly from online.
	plag_sample_dir = os.path.join(storage_dir, '_PLACE_PLAG_CHECK_SAMPLE_HERE')

	# Directories for invalid submissions
	# invalid submissions directory
	invalid_dir = os.path.join(storage_dir, 'invalid')
	# Invalid due to improper name
	invalid_sub_dir = os.path.join(invalid_dir, '1_invalid_submission')
	# unzip failure directory
	unzip_fail_dir = os.path.join(invalid_dir, '2_unable_to_unzip')
	# invalid java file directory
	invalid_java_file_dir = os.path.join(invalid_dir, '3_invalid_java_file')
	# submissions with package statements included
	package_statement_dir = os.path.join(invalid_dir, '4_package_statements_dir')
	# non-compilable java files directory
	non_compilable_dir = os.path.join(invalid_dir, '5_unable_to_compile')

	# Test files
	test_files_dir = os.path.join(storage_dir, "test_files")


	# All storage directories
	storage_directories = [invalid_dir, valid_sub_dir, valid_checked_dir, valid_checked_graded_dir,
		unzipped_dir, plagiarism_check_dir, invalid_sub_dir, unzip_fail_dir,
		invalid_java_file_dir, non_compilable_dir, package_statement_dir]



class Commands:
	# JDK
	settings = Settings()
	jdk_bin = settings.get_jdk_path()

	# java command
	java = os.path.join(jdk_bin, "java")

	# javac command
	javac = os.path.join(jdk_bin, "javac")


class Design:
	border1 =  "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
	border2 =  "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	border3 =  "============================================================================"
	border4 =  "----------------------------------------------------------------------------"
	border5 =  "############################################################################"
	border6 =  "<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>"
	border7 =  "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&"
	border8 =  "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
	border9 =  "////////////////////////////////////////////////////////////////////////////"
	border10 = "/////////////////////////////// START OF FILE //////////////////////////////"
	border11 = "//////////////////////////////// END OF FILE ///////////////////////////////"






