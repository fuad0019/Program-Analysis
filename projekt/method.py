import json

def extract_methods_info(json_data):
    methods_info = []
    methods = json_data.get("methods", [])
    for method in methods:
        name = method.get("name", "Unknown")
        params = method.get("params", [])
        access = method.get("access", "Unknown")
        return_type = method.get("returns", {}).get("type", "Unknown")
        methods_info.append({"name": name, "access": access, "params": params, "return_type": return_type})
    return methods_info

def extract_class_info(json_data):
    class_info = []
    class_ = json_data.get("name", "Unkown")
    line = class_.strip().split('/')
    last_line = line[-1]

    access = json_data.get("access", "Unkown")
    class_info.append({"name": last_line, "access": access })

    return class_info


file_path = "/Users/joakimbryld/Documents/GitHub/Program-Analysis/course-02242-examples-main/decompiled/dtu/compute/exec/Simple.json"  # Replace with the actual path to your JSON file
with open(file_path, "r") as json_file:
    json_data = json.load(json_file)

print(extract_class_info(json_data))



# methods_info = extract_methods_info(json_data)

# for method_info in methods_info:
#     print("Method Name:", method_info["name"])
#     print("Access:", method_info["access"])
#     print("Parameters:", method_info["params"])
#     print("Return Type:", method_info["return_type"])
#     print("-" * 30)

