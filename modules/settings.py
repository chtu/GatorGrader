import os
import subprocess


# INSTRUCTIONS: Set the main class for this assignment.
# If students submit a Java file that has a different file and/or main class name,
# they will fail the validation.
# The main class for this assignment


class Settings:
	# Set this main class
	main_class = 'MainClass'




	#placeholder file for git
	placeholder = "placeholder.txt"

class Path:
	# Current working directory
	cwd = os.getcwd()
	# Storage directory
	storage_dir = os.path.join(cwd, 'storage')
	# Files working directory
	fwd = os.path.join(cwd, 'files')
	# Main java file
	main_java_file = "%s.java" % Settings.main_class

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
	moss_path = os.path.join(plagiarism_check_dir, 'moss')
	# Plag check samples
	# This is for files obtained online to compare the student submissions
	# to see if they copied directly from online.
	plag_sample_dir = os.path.join(storage_dir, '_PLACE_PLAG_CHECK_SAMLE_HERE')

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






