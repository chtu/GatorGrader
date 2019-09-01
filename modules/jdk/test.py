import os
import subprocess

# Current working directory
cwd = os.getcwd()
path_to_jdk = os.path.join(cwd, "jdk-12.0.2")
path_to_javac = os.path.join(path_to_jdk, "bin", "javac")
path_to_java = os.path.join(path_to_jdk, "bin", "java")

# The commands for the terminal
command = "%s %s" % (path_to_javac, "Test.java")
run_cmd = "%s %s" % (path_to_java, "Test")

# Run the commands
proc1 = subprocess.Popen(command, shell=True)
proc2 = subprocess.Popen(run_cmd, shell=True)