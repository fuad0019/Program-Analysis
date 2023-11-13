import json
from VariableNamer import *
from correctTypeInferer import inferTypeAndValue, inferValue
from FlowGraph import *


with open("projekt/app/patterns.json") as f:
    patterns = json.load(f)

variableNamer = VariableNamer()


def detectPattern(memory, method, flowGraph, javaCodeList):
    memory_oprs = [item["opr"] for item in memory]
    newJavaCodeList = javaCodeList.copy()

    typeInferredString = ""

    flowGraph.addOprToCurrentNode(memory[-1])

    for key, value in patterns.items():
        
        if memory_oprs == value["pattern"]:
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

            if key == "conditional":
                oprsToCompare = [memory[-3], memory[-2]]

                valuesToCompare = []

                for opr in oprsToCompare:
                    if opr["opr"] == "load":
                        variableName = variableNamer.GetVariableName[opr["index"]]
                        valuesToCompare.append(variableName)

                    if opr["opr"] == "push":
                        value = inferValue(opr["value"]["type"], opr["value"]["value"])
                        valuesToCompare.append(value)

                #There's errors in the jvm2json tool with the comparitor operators being wrongly mapped

                #TODO: change this to operator map
                if memory[-1]["condition"] == "ge":
                    comparer = "<"
                if memory[-1]["condition"] == "le":
                    comparer = ">"
                if memory[-1]["condition"] == "ne":
                    comparer = "=="
                if memory[-1]["condition"] == "gt":
                    comparer = "<="
                if memory[-1]["condition"] == "lt":
                    comparer = ">="
                if memory[-1]["condition"] == "eq":
                    comparer = "!="


                typeInferredString = typeInferredString = (
                        patterns[key]["equivalentJava"]
                        .replace("a", valuesToCompare[0])
                        .replace("comparer", comparer)
                        .replace("b", valuesToCompare[1])
                    )
                
                flowGraph.addIndexToCurrentNode(len(newJavaCodeList)-1)
                flowGraph.CreateNode()
                

                newJavaCodeList.append(typeInferredString)
            
              #Important that this is outside of conditional indentation

            if key == "Jump":
                print("hello")
                flowGraph.CreateNode()
                flowGraph.addOprToCurrentNode(memory[-1])
                
                result = flowGraph.detectLoop(method, method[-1])
                if result[0] == True:
                    inLoop ,indexForHeader = result

                    javaCodeConditional = newJavaCodeList[indexForHeader]
                    typeInferredString = (
                        javaCodeConditional
                        .replace("if", "while")
                    )
                    newJavaCodeList[indexForHeader] = typeInferredString
                
                # get local variable and insert it when returning
    print(key)
    return newJavaCodeList
    


def bytecode_interp(method):
    memory = []
    javaCodeList = []
    bytecode_list = method["code"]["bytecode"]

    flowGraph = FlowGraph()
    flowGraph.CreateNode(len(javaCodeList)-1)

    for i in range(
        len(bytecode_list)
    ):  # Loop dynamically adapts to the bytecode length
        b = bytecode_list[i]
        memory.append(b)

        newjavaCodeList = detectPattern(memory, method, flowGraph, javaCodeList)
        if len(javaCodeList) != len(newjavaCodeList):
            javaCodeList = newjavaCodeList
            print("DETECTED PATTERN")
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
