from code_generation import generate_class

from file_writer import *

def main(inputPath, outputPath):
    inputFileName = ""
    outputFile = ""
    if(inputPath == None or outputPath == None):
        inputFileName = "projekt/ressources/json_bytecode_files/VarDeclareTest.json"
        OutputFile = "projekt/ressources/java_files/output_files/VarDeclare.java"
    else: 
        inputFileName = inputPath
        outputFile = outputPath

    
    json_data = read_file(inputFileName)

    content = generate_class(json_data)


    write_to_file(content, OutputFile)

if __name__ == "__main__":
    main(None, None)

