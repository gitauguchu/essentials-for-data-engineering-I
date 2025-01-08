#The sys module helps us interact with the python system itself
import sys

#Getting the python version
python_version = sys.version
print("Python version", python_version, sep=":")

#Getting the platform information
platform = sys.platform
print("Platform information", platform, sep=":")

#Getting the python path
python_path = sys.path
print("Python path", python_path, sep=":")

#Accessing command-line arguments
arguments = sys.argv
print("Command-line arguments", arguments, sep=":")

#Get the first argument passed in
first_argument = sys.argv[1] if len(sys.argv) > 1 else None
print("First argument passed in", first_argument, sep=":")

#Terminating the program with a specific exit code
exit_code = 0
sys.exit(exit_code)