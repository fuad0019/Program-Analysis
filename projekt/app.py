from pathlib import Path 
import json

with open('projekt/patterns.json') as f:
    patterns = json.load(f)

dc = Path("decompiled/")
classes = {}

with open("projekt/VarDeclare.json") as p:
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
    for key, value in patterns.items():
        if memory_oprs == value['pattern']:
            return key


def translateToJava(patternName):
    return patterns[patternName]['equivalentJava']

def writeToFile(JavaCode):
    # TODO: Implement writing to local Java file
    print(JavaCode)
    pass


def bytecode_interp(am):
    memory = [] 
    pattern_list = []
    bytecode_list = find_method(am)["code"]["bytecode"]

    for i in range(len(bytecode_list)): # Loop dynamically adapts to the bytecode length
        b = bytecode_list[i]
        pattern = detectPattern(memory) 
        if pattern != None:
            pattern_list.append(pattern)
            memory = []
        memory.append(b)
        #print(memory)
    
    pattern = detectPattern(memory) 
    if pattern != None:
        pattern_list.append(pattern)
    
    print(pattern_list)
    javaCode = []
    for pattern in pattern_list:
        javaCode.append(translateToJava(pattern))
    print(javaCode)
    #writeToFile(javaCode)
    return "\n".join(javaCode)

am = "Vardeclare", "DeclareInt"
#bytecode_interp(am)



def test_noop():
    print(" ")
    c = "dtu/compute/exec/Simple", "noop"
    (l, s) = [1], []
    print("---", c, "---")         
    s = bytecode_interp(c, l, s, print)
    print(s)
    print("--- DONE ---") 

def test_zero():
    print(" ")
    c = "dtu/compute/exec/Simple", "zero"
    (l, s) = [1], []
    print("---", c, "---")         
    s = bytecode_interp(c, l, s, print)
    print(s)
    print("--- DONE ---") 

def test_identity():
    print(" ")
    c = "dtu/compute/exec/Simple", "identity"
    (l, s) = [1], []
    print("---", c, "---")         
    s = bytecode_interp(c, l, s, print)
    print(s)
    print("--- DONE ---")   

def test_add():
    print(" ")
    c = "dtu/compute/exec/Simple", "add"
    (l, s) = [2,3], []
    print("---", c, "---")         
    s = bytecode_interp(c, l, s, print)
    print(s)
    print("--- DONE ---")

def test_min(): 
    print(" ")
    c = "dtu/compute/exec/Simple", "min"
    (l, s) = [4,3], []
    print("---", c, "---")         
    s = bytecode_interp(c, l, s, print)
    print(s)
    print("--- DONE ---")

def test_min(): 
    print(" ")
    c = "dtu/compute/exec/Simple", "min"
    (l, s) = [4,3], []
    print("---", c, "---")         
    s = bytecode_interp(c, l, s, print)
    print(s)
    print("--- DONE ---")

def test_factorial(): 
    print(" ")
    c = "dtu/compute/exec/Simple", "factorial"
    (l, s) = [5, 2], []
    print("---", c, "---")         
    s = bytecode_interp(c, l, s, print)
    print(s)
    print("--- DONE ---")

def test_hundredAndTwo(): 
    print(" ")
    c = "dtu/compute/exec/Simple", "hundredAndTwo"
    (l, s) = [], []
    print("---", c, "---")         
    s = bytecode_interp(c, l, s, print)
    print(s)
    print("--- DONE ---")

def test_hundredAndTwo(): 
    print(" ")
    c = "dtu/compute/exec/Simple", "hundredAndTwo"
    (l, s) = [], []
    print("---", c, "---")         
    s = bytecode_interp(c, l, s, print)
    print(s)
    print("--- DONE ---")



