import json
from VariableNamer import *
from correctTypeInferer import inferTypeAndValue, inferValue
from FlowGraph import *
from SubSequence import is_subsequence


with open("./patterns.json") as f:
    patterns = json.load(f)

pushMap = {} # TO know what operator we are on


#variableNamer = VariableNamer()


def detectPattern(memory, method, variableNamer, flowGraph, javaCodeList):
    memory_oprs = [item["opr"] for item in memory]
    print(memory_oprs)

    newJavaCodeList = javaCodeList.copy()

    typeInferredString = ""

    flowGraph.addOprToCurrentNode(memory[-1])

    for key, value in patterns.items():
        
        if memory_oprs == value["pattern"]:
            print(f"\n THIS IS THE KEY {key}")
            if key == "DeclareVariable":
                pushOpr = list(filter(lambda x: x["opr"] == "push", memory))[0]
                storeOpr = list(filter(lambda x: x["opr"] == "store", memory))[0]

                variableNamer.SetVariableName(storeOpr["index"])

                typeOfVariable = str(pushOpr["value"]["type"])
                valueOfVariable = pushOpr["value"]["value"]

                type, value = inferTypeAndValue(typeOfVariable, valueOfVariable)
                typeInferredString = (
                    patterns[key]["equivalentJava"]
                    .replace("type", type)
                    .replace("value", str(value))
                    .replace(
                        "variable", variableNamer.GetVariableName(storeOpr["index"])
                    )
                )
                newJavaCodeList.append(typeInferredString)

            if key == "DeclareVariableFromParam":
                loadOpr = list(filter(lambda x: x["opr"] == "load", memory))[0]
                storeOpr = list(filter(lambda x: x["opr"] == "store", memory))[0]

                variableNamer.SetVariableName(storeOpr["index"])

                typeOfVariable = str(loadOpr["type"])
                nameOfVariable = variableNamer.GetVariableName(loadOpr["index"])

                #type, value = inferTypeAndValue(typeOfVariable, valueOfVariable)
                typeInferredString = (
                    patterns[key]["equivalentJava"]
                    .replace("type", typeOfVariable)
                    .replace("value", str(nameOfVariable))
                    .replace(
                        "variable", variableNamer.GetVariableName(storeOpr["index"])
                    )
                )
                newJavaCodeList.append(typeInferredString)

            if key == "DeclareVariableAndAssignObject" :
                print(memory)

                newOpr = list(filter(lambda x: x["opr"] == "new", memory))[0]
                storeOpr = list(filter(lambda x: x["opr"] == "store", memory))[0]

                typeOfObject = newOpr["class"]

                variableNamer.SetVariableName(
                    storeOpr["index"]
                )  # Assign local variable and save it in a list

                # Insert correct type and value in java code
                typeInferredString = (
                    patterns[key]["equivalentJava"]
                    .replace("type", str(typeOfObject))
                    .replace(
                        "variable", variableNamer.GetVariableName(storeOpr["index"])
                    )
                )
                newJavaCodeList.append(typeInferredString)

            if  key == "ConstructObject":
                print(memory)
                
                newOpr = list(filter(lambda x: x["opr"] == "new", memory))[0]

                typeOfObject = newOpr["class"]

                

                # Insert correct type and value in java code
                typeInferredString = (
                    patterns[key]["equivalentJava"]
                    .replace("type", str(typeOfObject))
                   
                )
                newJavaCodeList.append(typeInferredString)

            if key == "methodCall":
                invokeOpr = list(filter(lambda x: x["opr"] == "invoke", memory))[0]
                loadOpr = list(
                    filter(lambda x: x["opr"] == "load" and x["type"] == "ref", memory)
                )[0]
                # Just making sure no excpetions occur because value in dictionary is None
                if (
                    invokeOpr["access"] == "virtual"
                    and invokeOpr["method"]
                    and invokeOpr["method"]["name"]
                ):
                    methodName = invokeOpr["method"]["name"]

                    # Insert correct variable name methodname in javacode
                    typeInferredString = (
                        patterns[key]["equivalentJava"]
                        .replace("methodCall", str(methodName))
                        .replace(
                            "variable", variableNamer.GetVariableName(loadOpr["index"])
                        )  # get local variable and insert it methodcall
                    )
                    newJavaCodeList.append(typeInferredString)

            if key == "VarReturn":
                loadOpr = list(filter(lambda x: x["opr"] == "load", memory))[0]
                # Insert correct variable name in javacode

                typeInferredString = patterns[key]["equivalentJava"].replace(
                    "variable", variableNamer.GetVariableName(loadOpr["index"])
                )
                newJavaCodeList.append(typeInferredString)

            
                
            
              #Important that this is outside of conditional indentation

          
        elif is_subsequence(patterns["conditional"]["pattern"], memory_oprs):

                print(f"\n THIS IS THE KEY {key}")
                oprsToCompare = [memory[-3], memory[-2]]

                valuesToCompare = []

                for opr in oprsToCompare:
                    print(opr)
                    if opr["opr"] == "load":
                        variableName = variableNamer.GetVariableName(opr["index"])
                        valuesToCompare.append(variableName)

                    if opr["opr"] == "push":
                        value = inferValue(opr["value"]["type"], opr["value"]["value"])
                        valuesToCompare.append(value)

                #There's errors in the jvm2json tool with the comparitor operators being wrongly mapped

                #TODO: change this to operator map
                if memory[-1]["condition"] == "ge":
                    comparer = "<"
                elif memory[-1]["condition"] == "le":
                    comparer = ">"
                elif memory[-1]["condition"] == "ne":
                    comparer = "=="
                elif memory[-1]["condition"] == "gt":
                    comparer = "<="
                elif memory[-1]["condition"] == "lt":
                    comparer = ">="
                elif memory[-1]["condition"] == "eq":
                    comparer = "!="

                endPositionOfIf =   memory[-1]["target"]




                print(comparer)

                typeInferredString = patterns["conditional"]["equivalentJava"].replace("variable1", str(valuesToCompare[0])).replace("comparer", comparer).replace("variable2", str(valuesToCompare[1]))
                print(typeInferredString)
                
                newJavaCodeList.append(typeInferredString)
                flowGraph.addIndexToCurrentNode(len(newJavaCodeList)-1)
                flowGraph.CreateNode()
                

                
                break

        elif is_subsequence(patterns["jump"]["pattern"], memory_oprs):
            print(f"\n THIS IS THE Jump {key}")
            flowGraph.CreateNode()
            flowGraph.addOprToCurrentNode(memory[-1]) 
                
            result = flowGraph.detectLoop( memory[-1])

            print(result)
            if result[0] == True:
                inLoop ,indexForHeader = result
                print(indexForHeader)
                javaCodeConditional = newJavaCodeList[indexForHeader]
                print(f"This is the old String {javaCodeConditional}")
                typeInferredString = (
                        javaCodeConditional
                        .replace("if", "while")
                    )
                print(f"This is the new String {typeInferredString}")

                newJavaCodeList[indexForHeader] = typeInferredString

                newJavaCodeList.append("}")
                break



        
      
                # get local variable and insert it when returning
    return newJavaCodeList
    


def bytecode_interp(method, variableNamer):
    memory = []
    javaCodeList = []
    bytecode_list = method["code"]["bytecode"]

    flowGraph = FlowGraph()
    flowGraph.CreateNode()

    for i in range(
        len(bytecode_list)
    ):  # Loop dynamically adapts to the bytecode length
        b = bytecode_list[i]
        memory.append(b)

        newjavaCodeList = detectPattern(memory, method, variableNamer, flowGraph, javaCodeList)
        if len(javaCodeList) != len(newjavaCodeList):
            javaCodeList = newjavaCodeList
            print("DETECTED PATTERN")
            print(f"LENGTH OF LIST {len(newjavaCodeList)}")   
            print(f"Javcode: {javaCodeList}")

            
            memory = []
        # print(memory)

    print("Finished Method")
    print(f"Full Javcode: {javaCodeList}")

    return "\n".join(javaCodeList)


def test_noop():
    print(" ")
    c = "dtu/compute/exec/Simple", "noop"
    (l, s) = [1], []
    print("---", c, "---")
    s = bytecode_interp(c, l, s, print)
    print(s)
    print("--- DONE ---")
