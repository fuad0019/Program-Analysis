import json

def read_file(filePath):
    with open(filePath, "r") as json_file:
        json_data = json.load(json_file)

    return json_data


    


def write_to_file(content, fileName):
    output_file = open(fileName, "w")
    output_file.write(content)
