from method import *
from app import *


def paramfinder(param):
    if "base" in param["type"]:
        return param["type"]["base"]
    elif "kind" in param["type"] and param["type"]["kind"] == "class":
        name = param["type"]["name"].split("/")[-1]
        return name
    elif "kind" in param["type"] and param["type"]["kind"] == "array":
        print(paramfinder(param["type"]))
        return paramfinder(param["type"]) + "[]"
    
def return_paramfinder(param):
    if "base" in param:
        return param["base"]
    elif "kind" in param and param["kind"] == "class":
        name = param["name"].split("/")[-1]
        return name
    elif "kind" in param and param["kind"] == "array":
        print(paramfinder(param))
        return paramfinder(param) + "[]"
        

def generate_method_skeleton(method_info, am):
    result = ""
    for method in method_info[0:3]:
        print(method)
        #If <init> it should be handled in the class skeleton
        if method["name"] == "<init>":
            continue

        if method["name"] == "main":
            result += f"public static void main(String [] args) {'{}'}\n\n"
            continue

        #Finds access of the method
        access = method["access"]

        #Determines if method is static
        if len(access) > 1 and access[1] == "static":
            access = f"{access[0]} {access[1]}"
        else:
            access = f"{access[0]}"

        #Handles return type
        return_type = method["return_type"]
        if return_type == None or return_type == "null":    
            return_type = "void"
        else:
            return_type = return_paramfinder(return_type)

        #Handles variables
        #TODO each param should have a name, but this should correspond to the variable name in used in the code.
        params = method["params"]
        param_list = []
        if len(params) == 0:
            params = ""
        else:
            for param in params:
                param_list.append(paramfinder(param))
                
            params = ", ".join(param_list)        

        name = method["name"]

        print(method["name"])
        x = am, method["name"]
        method_line = f"{access} {return_type} {name}({params}) {'{'}\n{bytecode_interp(x)}{'}'}\n\n"

        result += method_line

    return result

def generate_class_skeleton(class_info, method_info, am):
    access = class_info[0]['access'][0]
    name = class_info[0]['name']

    #TODO Use the code from init to declare global variables
    init = method_info[0]



    result = f"{access} class {name} {'{'}\n\
{generate_method_skeleton(method_info, am)}\
{'}'}"  


    return result


def write_to_file(class_info, method_info, am):
    output_file = open(f"{class_info[0]['name']}.java", "w")
    output_file.write(generate_class_skeleton(class_info, method_info, am))

file_path = "projekt/VarDeclare.json"  # Replace with the actual path to your JSON file
with open(file_path, "r") as json_file:
    json_data = json.load(json_file)

class_info = extract_class_info(json_data)
method_info = extract_methods_info(json_data)

am = "Vardeclare"

write_to_file(class_info,method_info, am)
