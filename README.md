# GatorGrader
GatorGrader was created to help CSC 210 instructors at SFSU grade Java assignments more quickly.  
The GatorGrader tool can do the following:
* Compile and run single Java file submissions downloaded from SFSU's iLearn portal.
* Cross check all submissions for plagiarism using Stanford's MOSS software (only available on Mac and Linux).

## Requirements
* Python 3

## How to use GatorGrader
*NOTE: The program isn't set up optimally, mostly because I made it quickly. I plan on creating a new version that is easier to work with.*
When you are using the GatorGrader with a unique assignment, you should perform the following steps.
1. Clone the repo, then make a copy of the folder. You should rename this copy something relevant, such as *Assignment01_Grader*. Delete the *.git* directory so that the copy is no longer linked to the repo.
1. **(If you are cloning this for the first time)** Obtain the MOSS script from Stanford so that you can access their online plagiarism tool. You can follow the directions on [Stanford's official MOSS page](https://theory.stanford.edu/~aiken/moss/) under *Registering for Moss*. The process is automated and free, so you should receive the script within a couple hours if you follow the directions correctly.  
1. **(Additionally, for first time users)** You should download the jdk from the [OpenJDK download page](https://jdk.java.net/12/). Download the JDK for your operating system, unpack it, and then place the resulting JDK folder in the *modules/jdk/\<your platform\>* directory.
1. In *modules/settings.py*, you should set the **main_class** field. The main class should be whatever you required the students to use when you assigned your project.
1. Download all of the submissions from the relevant iLearn assignment. You will be placing every individual student's submission folder in the directory called *_PLACE_SUBMISSIONS_HERE*. Depending on how you download it, you may have to unzip a folder containing all of the submissions.
1. **If you have other files from the web that you'd like to compare against the student submissions**, you can place them in the *storage/_PLACE_PLAG_CHECK_SAMPLE_HERE* directory. You can name these files to whatever you'd like. The program doesn't actually compile them, they are only used to check if students copied off of them.
1. Make sure you are in the same directory as run.py, then run the following command:  
```python3 run.py```  
  
1. The program should let you know how many submissions it detects, and should start by prompting you to process the submissions. If you do, it will check to make sure the submission guidelines were followed, including naming the folder, proper Java filename and main class, and being able to compile. If any submissions are invalid for any reason, you can check which ones were flagged in the prompt that follows.

If you have any issues with running your assignment, feel free to let me know and I can update these instructions.  
GatorGrader is a simple program that stores the data in filesystem, not a database. Future versions of this tool will employ a web server and database to offer more flexibility.  
## Contributing to GatorGrader
If you would like to help improve this tool, let me know and I'd be happy to add you as a contributor as long as you work at SFSU. I created a bunch of test files that you can use to make sure it's working properly. Test the program by calling:  
```python3 test.py```

## Updates

* (2019-09-10) The operating system didn't for use of JDKs that weren't downloaded by that computer, so I removed them and included instructions for people cloning for the first time. Now, you will have to download the JDK for your operating system and place it in the correct directory before running your program.
* (2019-09-01) The program was updated to include the JDK in the project, so you no longer need to download the JDK for the program to run the student submissions. This will work on Mac, Windows, and Linux operating systems. Code was also modified to work on Windows, so Windows users will now be able to run the program. However, MOSS (the plagiarism detection software) is only available on Mac and Linux.