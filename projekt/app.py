from pathlib import Path 
import json

with open('./patterns.json') as f:
    patterns = json.load(f)

dc = Path("decompiled/")
classes = {}

with open("./VarDeclare.json") as p:
    doc = json.load(p)
    classes[doc["name"]] = doc 

methods = {}
for cls in classes.values():
    for m in cls["methods"]:
        methods[(cls["name"], m["name"])] = m 

def find_method(am):
    return methods[(am)]

def print_bytecode(am):
    m = find_method(am)
    assert m is not None

def detectPattern(memory):
    memory_oprs = [item['opr'] for item in memory]  
    print(memory_oprs)
    for key, value in patterns.items():
        if memory_oprs == value['pattern']:
            if key == "DeclareVariable":
                pushOpr = list(filter(lambda x : x['opr'] == "push",memory))[0]
                typeOfVariable = pushOpr["value"]["type"]
                valueOfVariable = pushOpr["value"]["value"]
                return "declare", key, typeOfVariable, valueOfVariable
        
            return "other",key
    print(key)


def translateToJava(pattern):

    print(pattern)
    if pattern[0] == "declare":
            category,name,typeVariable,valueVariable = pattern
            typeInferredString = patterns[name]['equivalentJava'].replace("type", typeVariable).replace("value", str(valueVariable))

    elif pattern[0] == "other":
            category,name = pattern
            typeInferredString = patterns[name]['equivalentJava']

    print(typeInferredString)

    return typeInferredString

def writeToFile(JavaCode):
    # TODO: Implement writing to local Java file
    print(JavaCode)
    pass


def bytecode_interp(am):
    memory = [] 
    bytecode_list = find_method(am)["code"]["bytecode"]
    print(bytecode_list)
    for i in range(len(bytecode_list)): # Loop dynamically adapts to the bytecode length
        b = bytecode_list[i]
        memory.append(b)
        pattern = detectPattern(memory) 
        if pattern:
            javaCode = translateToJava(pattern)
            writeToFile(javaCode)


        
        

am = "Vardeclare", "DeclareString"
bytecode_interp(am)



def test_noop():
    print(" ")
    c = "dtu/compute/exec/Simple", "noop"
    (l, s) = [1], []
    print("---", c, "---")         
    s = bytecode_interp(c, l, s, print)
    print(s)
    print("--- DONE ---") 





