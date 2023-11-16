from main import * 
import subprocess
import glob
import pathlib
import os 
import difflib

TestInputFile = "projekt/ressources/evaluation_files/test1.java"
TestOutputFile = "projekt/ressources/evaluation_files/test2.java"
#HOWTO: First compile the original java file, you want to decompile. Convert the .class file
#to json, with JVM2Json. Decompile the json, this is your file1.
# Now compile file1, convert to json, and decompile, this your file2. 
#This method will then compare the two, and give a percentage on how similar they are.  
def EvaluateDecompiler(file1, file2):
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            content1 = f1.readlines()
            content2 = f2.readlines()

            similarity = difflib.SequenceMatcher(None, content1, content2).ratio()
            similarity_percentage = similarity * 100

            diff = difflib.unified_diff(content1, content2, fromfile=file1, tofile=file2)

            print(f"Similarity: {similarity_percentage:.2f}%")
            print("Differences (if any):")
            diff_text = ''.join(diff)
            print(diff_text if diff_text else "No differences found.")
            
            return similarity_percentage
    except IOError as e:
        print(f"An error occurred while reading the files: {e}")
        return 0

EvaluateDecompiler(TestInputFile, TestOutputFile)
