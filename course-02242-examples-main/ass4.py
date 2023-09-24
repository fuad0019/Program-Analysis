from pathlib import Path 
import json

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
    memory = {}
    mstack = [(l,s,(am,0))] # list of local variables, a operator stack, absolute method with index of what we want to execute

    #mstack[0] = lv
  #  print(local_vars, "local vars")
    for i in range(0,30):
        log("→", mstack, end ="")
        (lv, os, (am_,i)) = mstack[-1] #Local variables, operator stack, 
       # print("-----mstack----", mstack[-1], "IUEHIUH")
        #print(lv, "local variable")
        b = find_method(am)["code"]["bytecode"][i] #The actual bytecode 
        if b["opr"] == "return":
            if b["type"] == None: 
                log(" (return)")
                return None
            elif b["type"] == "int": 
                log(" (return)")
                return os[-1]
                
            else:
                log("Unsupported operation", b)
                return None
        elif b["opr"] == "push":
            log(" (push)")
            v = b["value"]
            _ = mstack.pop()
            mstack.append((lv, os + [v["value"]], (am_,i + 1))) 
            log() 
        elif b["opr"] == "load":
            log(" (load)")
            index = b["index"]
            if b["type"] == "ref":
                value = lv[index]
            else:
                value = lv[index]
            _ = mstack.pop()
            mstack.append((lv, os + [value], (am_, i + 1)))

        #BINARY
        elif b["opr"] == "binary":
            log(" (binary)")
            if b["operant"] == "add":
                value = os[-2] + os[-1]
            elif b["operant"] == "mul":
                value = os[-2] * os[-1]
            os = os[:-2] + [value]  # Update the operator stack with the result
            mstack.append((lv, os, (am_, i + 1)))   

            

        #IF
        elif b["opr"] == "if":
            log(" (if)")
            if b["condition"] == "gt":
                if(os[-2] > os[-1]):
                    return True
                else:
                    return False

        elif b["opr"] == "store":
            log(" (store)")
            lv, os, pc = mstack.pop(-1)
            value = os[-1]
            if b["index"] >= len(lv):
                lv = lv + [value]
            else:
                lv[b["index"]] = value
            pc = (am_, i + 1)  # Update the program counter without modifying the state
            mstack.append((lv, os[:-1], pc))

        elif b["opr"] == "incr":
            lv, os, pc = mstack.pop(-1)
            log(" (incr)")
            index = b["index"]
            amount = b["amount"]
            lv[index] = lv[index] + amount
            mstack.append((lv, os[:-1], (am_, i + 1)))


        elif b["opr"] == "ifz":
            log(" (ifz)")
            condition = b["condition"]
            target = b["target"]
            if os[-1] == 0:
                mstack.pop() 
                mstack.append((lv, os, (am_, target)))  
            else:
                mstack[-1] = (lv, os, (am_, i + 1))
        elif b["opr"] == "goto":
            log(" (goto)")
            target = b["target"]
            mstack.pop()  
            mstack.append((lv, os, (am_, target)))


        
        else:
            log("Unsupported operation", b)
            return None

print()
cases = [
    #("dtu/compute/exec/Simple", "noop"),
    #("dtu/compute/exec/Simple", "zero"),
    #("dtu/compute/exec/Simple", "hundredAndTwo"),
    ("dtu/compute/exec/Simple", "identity"),
    #("dtu/compute/exec/Simple", "add"),
    #("dtu/compute/exec/Calls", "helloWorld"),

] 


#for class_name, method_name in methods.keys():
#    print(f"Class: {class_name}, Method: {method_name}")


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



for class_name, method_name in methods.keys():
    method_to_execute = "test_" + method_name

    # Check if the method exists in the global or local namespace
    if method_to_execute in globals() or method_to_execute in locals():
        # Execute the method
        exec(method_to_execute + "()")
