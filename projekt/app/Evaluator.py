from main import * 
import subprocess
import glob
import pathlib
import os 

TestInputFile = "projekt/ressources/evaluation_files/test1.java"
TestOutputFile = "projekt/ressources/evaluation_files/test2.java"
#HOWTO: First compile the original java file, you want decompile. Convert the .class file
#to json, with JVM2Json. Decompile the json, this is your file1.
# Now compile file1, convert to json, and decompile, this your file2. 
#This method will then compare the two, and see if they are identical, which means the decompiler works. 
def EvaluateDecompiler(file1, file2):
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:

            content1 = f1.read()
            content2 = f2.read()

            if content1 == content2:
                print("The two files are indentical")
            else:
                print("The two files are not identical")
    except IOError as e:
        print(f"An error occurred while reading the files: {e}")
        return False


EvaluateDecompiler(TestInputFile, TestOutputFile)
