from method import *

def generate_method_skeleton(method_info):
    result = ""
    for method in method_info:
        if method["name"] == "<init>":
            continue
        access = method["access"]
        if len(access) > 1 and access[1] == "static":
            access = f"{access[0]} {access[1]}"
        else:
            access = f"{access[0]}"

        return_type = method["return_type"]
        if return_type == None:    
            return_type = "void"
        else:
            return_type = method["return_type"]["base"]


        #TODO each param should have a name, but this should correspond to the variable name in used in the code.
        params = method["params"]
        param_list = []
        if len(params) == 0:
            params = ""
        else:
            for param in params:
                if "base" in param["type"]:
                    param_list.append(param["type"]["base"])
            params = ", ".join(param_list)        

        name = method["name"]

        method_line = f"{access} {return_type} {name}({params}) {'{}'}\n\n"

        result += method_line

    return result

def generate_class_skeleton(class_info, method_info):
    access = class_info[0]['access'][0]
    name = class_info[0]['name']

    #TODO Use the code from init to declare global variables
    init = method_info[0]



    result = f"{access} class {name} {'{'}\n\
{generate_method_skeleton(method_info)}\
{'}'}"  


    return result


def write_to_file(class_info, method_info):
    output_file = open(f"{class_info[0]['name']}.java", "w")
    output_file.write(generate_class_skeleton(class_info, method_info))



class_info = extract_class_info(json_data)
method_info = extract_methods_info(json_data)

write_to_file(class_info,method_info)
