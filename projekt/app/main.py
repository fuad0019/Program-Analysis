from code_generation import generate_class

from file_writer import *

def main(inputPath, outputPath):
    inputFile = ""
    outputFile = ""
    if(inputPath == None or outputPath == None):
        inputFile = "/Users/joakimbryld/Documents/GitHub/Program-Analysis/projekt/ressources/json_bytecode_files/EvalLoopsDC.json"
        outputFile = "/Users/joakimbryld/Documents/GitHub/Program-Analysis/projekt/ressources/java_files/output_files/EvalLoopsDCDC.java"
    else: 
        inputFile = inputPath
        outputFile = outputPath

    
    json_data = read_file(inputFile)

    content = generate_class(json_data)


    write_to_file(content, outputFile)

if __name__ == "__main__":
    main(None, None)

