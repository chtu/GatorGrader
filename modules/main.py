import os
import subprocess
from modules.settings import Path, Design, Settings
from modules.validator import Validator
from modules.refresher import Refresher
from modules.submission import SubmissionFile
from modules.plagiarism_checker import perform_plagiarism_check
import modules.filename_util as fu
import shutil

def clear():
	# Windows
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')

def clear_and_print_header(main_class):
	clear()
	print_header(main_class)

def print_header(main_class):
	print(Design.border3)
	print(f"GatorGrader | CSC 210-04: {main_class}")
	print(Design.border3)

def remove_hidden(names):
	for name in names:
		if name[0] == '.':
			names.remove(name)
	return names

def replace_spaces_in_filename(filename):
	return_str = ""
	for i in range(0, len(filename)):
		ch = filename[i]
		if ch == ' ':
			return_str += '_'
		else:
			return_str += ch
	return return_str

def replace_spaces_in_dir_files(path_to_dir):
	new_list = []
	for filename in remove_hidden(os.listdir(path_to_dir)):
		filename_path = os.path.join(path_to_dir, filename)
		new_name = replace_spaces_in_filename(filename)

		new_list.append(new_name)
		new_name_path = os.path.join(path_to_dir, new_name)

		os.rename(filename_path, new_name_path)

	return new_list

def run_student_submission(sub):
	print(f"Running program. Press Control+C to stop.")
	print(Design.border5)
	sub.run_program()
	print(f"\n{Design.border5}")
	print(f"Program ended for user: {sub.first_name} {sub.last_name} ({sub.id_number}).")
	print(Design.border2)

def print_submission_header(index, all_submissions, sub):
	print(f"Student: {sub.first_name} {sub.last_name} ({sub.id_number})")
	print(f"Progress: {index+1} out of {len(all_submissions)}")
	print(Design.border4)

def print_submission_file_info(path_to_directory, main_class):
	filenames = remove_hidden(os.listdir(path_to_directory))
	for i in range(0, len(filenames)):
		sub = SubmissionFile(filenames[i], os.path.join(path_to_directory, filenames[i]), main_class)
		print (f"  {i+1}. ({sub.id_number}) {sub.first_name} {sub.last_name}")

def print_invalid_submissions(main_class):
	print("Displaying submissions that were deemed invalid.")
	print(Design.border3)

	print("INVALID FILENAME")
	print(Design.border4)
	print("The following submissions were invalid due to one or more of the following reasons:")
	print("  - The student didn't follow the naming instructions.")
	print("  - The student didn't submit a zip file.\n")

	invalid_submission_files = remove_hidden(os.listdir(Path.invalid_sub_dir))
	for i in range(0, len(invalid_submission_files)):
		print(f"  {i+1}. {invalid_submission_files[i]}")
	print(Design.border3)

	print("INVALID ZIP FILE")
	print(Design.border4)
	print("The following submissions were invalid because the file failed to unzip.")
	print("This could likely be due to the file not actual being a zip file, or there")
	print("might be something wrong with the permissions attached to the file.\n")
	print_submission_file_info(Path.unzip_fail_dir, main_class)
	print(Design.border3)

	print("INVALID JAVA FILE")
	print(Design.border4)
	print("The following submissions were invalid due to one or more of the following reasons:")
	print("  - The Java file was not given the name instructed by the assignment.")
	print("  - The student didn't submit a Java file.\n")
	print_submission_file_info(Path.invalid_java_file_dir, main_class)
	print(Design.border3)

	print("JAVA FILES WITH PACKAGE STATEMENTS")
	print(Design.border4)
	print("The following submissions were invalid due to one or more of the following reasons:")
	print("  - The Java file included a package statement when it wasn't supposed to.\n")
	print_submission_file_info(Path.package_statement_dir, main_class)
	print(Design.border3)

	print("FAILED TO COMPILE")
	print(Design.border4)
	print("The following submissions were invalid because they failed to compile.\n")
	print_submission_file_info(Path.non_compilable_dir, main_class)
	print(Design.border3)


# ============================================================
#       MAIN PROGRAM
# ============================================================

class EvaluatorProgram:
	def run(main_class):
		main_java_file = main_class + ".java"
		clear_and_print_header(main_class)
		print(f"Beginning program on a {Settings.get_platform()} platform.")
		fu.init_storage_dirs()
		print(Design.border4)

		# Validate all of the submissions first
		all_submissions = []
		all_submission_folders = replace_spaces_in_dir_files(Path.initial_sub_dir)

		for i in range(0, len(all_submission_folders)):
			submission_folder = all_submission_folders[i]
			if submission_folder == Settings.placeholder:
				continue
			submission_files = remove_hidden(os.listdir(os.path.join(Path.initial_sub_dir, submission_folder)))
			for file in submission_files:
				parts = file.split('.')
				if parts[len(parts)-1] == "zip":
					path_to_sub_folder = os.path.join(Path.initial_sub_dir, submission_folder)
					all_submissions.append([file, path_to_sub_folder])
					break


		if len(all_submissions) > 0:
			if len(all_submissions) == 1:
				validation_greeting = "\nYou have 1 submission that has yet to be validated."
			else:
				validation_greeting = "\nYou have %d submissions that have yet to be validated." % len(all_submissions)
			while True:
				print(validation_greeting)
				print("\nWould you like to validate them now?")
				print("  Y: yes")
				print("  N: no")
				response = input("Response: ")

				if response == "Y" or response == "y":
					for i in range(0, len(all_submissions)):
						submission = all_submissions[i][0]
						path = all_submissions[i][1]
						clear_and_print_header(main_class)
						print(f"Validating {i+1} out of {len(all_submissions)} submissions.")
						print(Design.border4)
						Validator.validate(submission, path, main_class)
						shutil.rmtree(all_submissions[i][1])
					break
				elif response == "N" or response == "n":
					break
				else:
					clear_and_print_header(main_class)
					print("Please enter a valid response.")

		clear_and_print_header(main_class)
		while True:
			all_valid_submissions = remove_hidden(os.listdir(Path.valid_checked_dir))
			if len(all_valid_submissions) > 0:
				if len(all_valid_submissions) == 1:
					print(f"\nYou have 1 ungraded submission.\n")
				else:
					print(f"\nYou have {len(all_valid_submissions)} ungraded submissions.\n")
			else:
				print("You are all up to date.\n")
			print("What would you like to do?")
			print("  1: Evaluate ungraded projects.")
			print("  2: View invalid submissions.")
			print(". 3: Perform plagiarism check.")
			#print("  3: Pick a program by ID number.")
			print("  0: Quit the program.")
			command = input("Your choice: ")

			if command == "1":
				for i in range(0, len(all_valid_submissions)):
					submission = all_valid_submissions[i]
					continue_to_next = True
					sub = SubmissionFile(submission, Path.valid_checked_dir, main_class)
					clear_and_print_header(main_class)
					print_submission_header(i, all_valid_submissions, sub)
					run_student_submission(sub)
					while True:
						print("Please choose an option:\n")
						print("  (nothing): Set current student to graded and continue")
						print("  1: Continue to next student without setting current to graded.")
						print("  2: View the Java file.")
						print("  3: Run program again.")
						print("  4: Exit back to menu, but do not set this student to graded.")
						print("  0: Set to graded and exit back to menu.")
						command = input("Your command: ")
						if command == "":
							continue_to_next = True
							sub.set_to_graded()
							break
						elif command == "1":
							continue_to_next = True
							break
						elif command == "2":
							clear_and_print_header(main_class)
							print_submission_header(i, all_valid_submissions, sub)
							print(f"File contents for user: {sub.first_name} {sub.last_name} ({sub.id_number})")
							print(Design.border10)
							sub.display()
							print(Design.border11)
						elif command == "3":
							clear_and_print_header(main_class)
							print_submission_header(i, all_valid_submissions, sub)
							run_student_submission(sub)
						elif command == "4":
							continue_to_next = False
							clear_and_print_header(main_class)
							break
						elif command == "0":
							continue_to_next = False
							sub.set_to_graded()
							clear_and_print_header(main_class)
							break
						else:
							print("Please enter a valid value.\n")
					if not continue_to_next:
						clear_and_print_header(main_class)
						break
				clear_and_print_header(main_class)
			elif command == "2":
				clear_and_print_header(main_class)
				print_invalid_submissions(main_class)
				print("\nPress ENTER to return to the menu.")
				input()
				clear_and_print_header(main_class)
			elif command == "3":
				clear_and_print_header(main_class)
				print("Performing a plagiarism check with Stanford's MOSS tool.")
				print(Design.border4)
				perform_plagiarism_check(main_class)
				print(Design.border2)
				print("\nPress ENTER to return to the menu.")
				input()
				clear_and_print_header(main_class)
				'''
			elif command == "3":
				clear_and_print_header(main_class)
				while True:
					print("Enter the ID number of the user whose project you want to examine.")
					str_input = input("Student's ID: ")

					if len(str_input) != 9:
						print("Please enter a valid ID number.")
						continue

					try:
						id_number = (int)str_input
						if id_number < 100000000 or id_number > 999999999:
							print("Please enter a valid ID number.")
							continue
						# The ID input is valid
						clear_and_print_header(main_class)
						print(f"Displaying project for use with ID: {id_number}")
						print(Design.border)
					except:
						print("Please enter a valid ID number.")
						continue
			'''
			elif command == "0":
				clear()
				break
			else:
				clear_and_print_header(main_class)
				print("Please enter a valid choice.")




# Start running through all of the valid submissions
