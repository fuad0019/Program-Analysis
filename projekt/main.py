from code_generation import generate_class

from file_writer import *

def main():
    inputFileName = "VarDeclareTest.json"
    OutputFile = "VarDeclare.java"
    
    json_data = read_file(inputFileName)

    content = generate_class(json_data)


    write_to_file(content, OutputFile)

if __name__ == "__main__":
    main()

