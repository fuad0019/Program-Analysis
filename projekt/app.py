from pathlib import Path 
import json
import requests

import json
patterns = requests.get('./patterns.json').json()


dc = Path("decompiled/")

classes = {}


for f in dc.glob("**/*.json"):
    with open(f) as p:

        doc = json.load(p)
        #print(doc["name"])
        classes[doc["name"]] = doc 
#print(classes["dtu/compute/exec/Simple"])
methods = {}
for cls in classes.values():
    for m in cls["methods"]:
        methods[(cls["name"], m["name"])] = m #Creates a tuple as a key, containing class name and method name

def find_method(am):
    return methods[(am)]


def print_bytecode(am):
    m = find_method(am)
    assert m is not None
    print(m["code"]["bytecode"])


def bytecode_interp(am, l, s, log):
    memory = [] #To hold our operations in 

    for i in range(0,30):
        
        #GET PARAMETERS,NAME, RETURN TYPE FIRST
        
        #BODY
        b = find_method(am)["code"]["bytecode"][i] #The actual bytecode 
    

        memory.append(b)

        

        pattern = detectPattern(memory)
        javaCode = translateToJava(pattern)
        writeToFile(javaCode)


def detectPattern(memory):

# This checks if the sequence of instructions in memory is the same as in one of the patterns
# then return name of pattern to 
    for key,value in patterns:
        if all(x in value.pattern for x in memory):
            return key
         

def translateToJava(patternName):
    return patterns[patternName].equivalentJava



def writeToFile(JavaCode):
    #TODO: iMPLEMENT WRITING TO LOCAL JAVA FILE
    return

  


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



