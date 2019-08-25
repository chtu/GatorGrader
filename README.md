# GatorGrader
GatorGrader was created to help CSC 210 instructors at SFSU grade Java assignments more quickly.  
The GatorGrader tool can do the following:
* Compile and run single Java file submissions downloaded from SFSU's iLearn portal.
* Cross check all submissions for plagiarism using Stanford's MOSS software.

## Requirements
* Python 3
* (Minimum) Java 8. It should be able to compile and run in the command line.
* For now, Linux or Mac OS, but I believe it can be easily modified for Windows.

## How to use GatorGrader
*NOTE: The program isn't set up optimally, mostly because I made it quickly. I plan on creating a new version that is easier to work with.*
When you are using the GatorGrader with a unique assignment, you should perform the following steps.
1. Clone the repo, then make a copy of the folder. You should rename this copy something relevant, such as *Assignment01_Grader*. Delete the *.git* directory so that the copy is no longer linked to the repo.
1. **(If you are cloning this for the first time)** Obtain the MOSS script from Stanford so that you can access their online plagiarism tool. You can follow the directions on [Stanford's official MOSS page](https://theory.stanford.edu/~aiken/moss/) under *Registering for Moss*. The process is automated and free, so you should receive the script within a couple hours if you follow the directions correctly.
1. In *modules/settings.py*, you should set the **main_class** field. The main class should be whatever you required the students to use when you assigned your project.
1. Download all of the submissions from the relevant iLearn assignment. You will be placing every individual student's submission folder in the directory called *_PLACE_SUBMISSIONS_HERE*. Depending on how you download it, you may have to unzip a folder containing all of the submissions.
1. **If you have other files from the web that you'd like to compare against the student submissions**, you can place them in the *storage/_PLACE_PLAG_CHECK_SAMPLE_HERE* directory. You can name these files to whatever you'd like. The program doesn't actually compile them, they are only used to check if students copied off of them.
2. 1. Make sure you are in the same directory as run.py, then run the following command:  
```python3 run.py```  
  
1. The program should let you know how many submissions it detects, and should start by prompting you to process the submissions. If you do, it will check to make sure the submission guidelines were followed, including naming the folder, proper Java filename and main class, and being able to compile. If any submissions are invalid for any reason, you can check which ones were flagged in the prompt that follows.

If you have any issues with running your assignment, feel free to let me know and I can update these instructions.  
GatorGrader is a simple program that stores the data in filesystem, not a database. Future versions of this tool will employ a web server and database to offer more flexibility.  
## Contributing to GatorGrader
If you would like to help improve this tool, let me know and I'd be happy to add you as a contributor as long as you work at SFSU. I created a bunch of test files that you can use to make sure it's working properly. Test the program by calling:  
```python3 test.py```