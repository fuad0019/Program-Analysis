from main import * 
import subprocess
import glob
import pathlib
import os 

TestInputFile = "projekt/ressources/java_files/input_files/Eval/Evaluate1.java"
TestOutputFile = "projekt/ressources/java_files/input_files/Eval/Evaluate2.java"
#lastOutput = 

#input(Class) -> ByteCode -> Decompile -> JAVA -> ByteCode -> Decompile 
def compile_java(java_file, output_dir):
    try:
        # Create the output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Compile the Java file
        subprocess.check_call(["javac", "-d", output_dir, java_file])
        print(f"{java_file} compiled successfully to {output_dir}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to compile {java_file}. Error: {e}")

def analyse_bytecode(folder_path, target_folder_path):
    print(folder_path)
    print(target_folder_path)
    # This function analyzes Java bytecode files (.class) using the jvm2json tool. It takes 
    # a folder path as input, finds all .class files in the specified folder and its subdirectories, 
    # and then uses the subprocess module to run the jvm2json tool to convert each .class file into a 
    # corresponding JSON file (.json).
    class_files = glob.glob(folder_path + '/**/*.class', recursive=True)
    for class_file in class_files:
        json_file = pathlib.Path(class_file).name
        json_file = json_file.replace('.class', '.json')
        command = [
            "jvm2json",
            "-s", class_file,
            "-t", target_folder_path+json_file
        ]
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


# Takes a Java file as input, decompiles and saves it in output. Outpu
def EvaluateDecompiler (input, output): 
    print("Evaluating")
    compile_java(input, "projekt/ressources/evaluation_files/input_class/")
   # analyse_bytecode(input, "projekt/ressources/evaluation_files/output_json/")
    #main(input, output)
   # main(output, )




EvaluateDecompiler(TestInputFile, TestOutputFile)
