from code_interpreter import *
from VariableNamer import *

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


def extract_methods_signature(method, variableNamer):
    name = method.get("name", "Unknown")
    params = method.get("params", [])
    access = method.get("access", "Unknown")
    return_type = method.get("returns", {}).get("type", "Unknown")
    if name == "<init>":
        return ""
    # Finds access of the method

    # Determines if method is static
    if len(access) > 1 and access[1] == "static":
        access = f"{access[0]} {access[1]}"
    else:
        access = f"{access[0]}"

    # Handles return type
    if return_type == None or return_type == "null":
        return_type = "void"
    else:
        return_type = return_paramfinder(return_type)

    # Handles variables
    # TODO each param should have a name, but this should correspond to the variable name in used in the code.
    param_list = []
    if len(params) == 0:
        params = ""
    else:
        index = 1
        for param in params:
            variableNamer.SetVariableName(index)
            param_list.append(f"{paramfinder(param)} {variableNamer.GetVariableName(index)}")
            index += 1

        params = ", ".join(param_list)

    return f"{access} {return_type} {name}({params})"


def extract_class_signature(json_data):
    class_signatur = []
    class_name = json_data.get("name", "Unkown")
    line = class_name.strip().split("/")
    last_line = line[-1]

    access = json_data.get("access", "Unkown")
    class_signatur.append({"name": last_line, "access": access})

    return class_signatur



def generate_method(method):
    result = ""
    # If <init> it should be handled in the class skeleton

    variableNamer = VariableNamer()

    if method["name"] == "<init>":
        return bytecode_interp(method, variableNamer)
    methodSignature = extract_methods_signature(method,variableNamer)

    method_line = f"{methodSignature} {'{'}\n{bytecode_interp(method, variableNamer)}{'}'}\n\n"

    result += method_line

    return result


def generate_class(bytecode):
    class_signatur = extract_class_signature(bytecode)

    access = class_signatur[0]["access"][0]
    name = class_signatur[0]["name"]

    # TODO Use the code from init to declare global variables
    #init = method_info[0]

    bytecode_methods = bytecode.get("methods", [])

    method = ""
    for bytecode_method in bytecode_methods[0:8]:
        method = method + f"{generate_method(bytecode_method)}\n"

    result = f"{access} class {name} {'{'}\n\
{method}\
{'}'}"
    return result






