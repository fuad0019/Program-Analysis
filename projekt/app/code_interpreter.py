import json
from VariableNamer import *
from correctTypeInferer import inferTypeAndValue, inferValue
from FlowGraph import *
from SubSequence import is_subsequence


with open("projekt/app/patterns.json") as f:
    patterns = json.load(f)


pushList = [] # TO PUSH JAVACODE AT LATER POINT, SUCH AS CLOSING BRACKET


#variableNamer = VariableNamer()


def ValidateIf (memory): 
    counter = 0
    for m in memory: 
        counter = counter + 1
        if m["opr"]  == "if" or m["opr"]  == "ifz":
            if counter == 3: 
               return True
    return False
            

def MatchOperant (operant):
    if operant == "add": 
        return "+"
    if operant == "sub": 
        return "-"
    if operant == "mul": 
        return "*"
    if operant == "div": 
        return "/"


        


def detectPattern(memory, method, variableNamer, flowGraph, javaCodeList):

    newJavaCodeList = javaCodeList.copy()

    global pushList


    if len(pushList)>0:
        currentOpr = memory[-1]
        print(method)
        indexCurrentOpr = method["code"]["bytecode"].index(currentOpr)
        print(f"INDEX of Current OPR: {indexCurrentOpr}")


        for pushElement in pushList:
            print(pushElement)
            if indexCurrentOpr == pushElement[0]:
                newJavaCodeList.append(pushElement[1])



    memory_oprs = [item["opr"] for item in memory]
    print(memory_oprs)

    

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

            if key == "IncrementVariable":
                loadOpr = list(filter(lambda x: x["opr"] == "load", memory))[0]
                pushOpr = list(filter(lambda x: x["opr"] == "push", memory))[0]
                binaryOpr = list(filter(lambda x: x["opr"] == "binary", memory))[0]
                storeOpr = list(filter(lambda x: x["opr"] == "store", memory))[0]


                variableName = variableNamer.GetVariableName(loadOpr["index"])
                variableNamer.SetVariableName(storeOpr["index"])
                typeOfValue = pushOpr["value"]["type"]
                valueOfValue = pushOpr["value"]["value"]

                value = inferValue(typeOfValue, valueOfValue)
                typeInferredString = (
                    patterns[key]["equivalentJava"]
                    .replace("value", str(value))
                    .replace("outsideVariable", variableNamer.GetVariableName(storeOpr["index"]))
                    .replace(
                        "insideVariable", variableName
                    ) 
                    .replace(
                        "opr",str(MatchOperant(binaryOpr["operant"]))
                    ) 
                )
                newJavaCodeList.append(typeInferredString)

            if key == "TwoVariableArithmetic":
                loadOprs = list(filter(lambda x: x["opr"] == "load", memory))
                binaryOpr = list(filter(lambda x: x["opr"] == "binary", memory))[0]
                storeOpr = list(filter(lambda x: x["opr"] == "store", memory))[0]


                variableName1 = variableNamer.GetVariableName(loadOprs[0]["index"])
                variableName2 = variableNamer.GetVariableName(loadOprs[1]["index"])

                variableNamer.SetVariableName(storeOpr["index"])
                typeOfValue = storeOpr["type"]

                typeInferredString = (
                    patterns[key]["equivalentJava"]
                    .replace("type", typeOfValue)
                    .replace("varc", variableNamer.GetVariableName(storeOpr["index"]))
                    .replace("vara", variableName1)
                    .replace(
                        "varb", variableName2
                    ) 
                    .replace(
                        "opr", MatchOperant(binaryOpr["operant"])
                    ) 
                )
                newJavaCodeList.append(typeInferredString)

            if key == "ThreeVariableArithmetic":
                    loadOprs = list(filter(lambda x: x["opr"] == "load", memory))
                    binaryOpr = list(filter(lambda x: x["opr"] == "binary", memory))[0]
                    storeOpr = list(filter(lambda x: x["opr"] == "store", memory))[0]
 
                    #type vard = vara opr varb opr varc;
                    variableName1 = variableNamer.GetVariableName(loadOprs[0]["index"])
                    variableName2 = variableNamer.GetVariableName(loadOprs[1]["index"])
                    variableName3 = variableNamer.GetVariableName(loadOprs[2]["index"])

                    variableNamer.SetVariableName(storeOpr["index"])
                    typeOfValue = storeOpr["type"]

                    typeInferredString = (
                        patterns[key]["equivalentJava"]
                        .replace("type", typeOfValue)
                        .replace("vard", variableNamer.GetVariableName(storeOpr["index"]))
                        .replace("vara", variableName1)
                        .replace("varb", variableName2)
                        .replace("varc", variableName3)
 
                        .replace(
                            "opr", MatchOperant(binaryOpr["operant"])
                        ) 
                    )
                    newJavaCodeList.append(typeInferredString)


            if key == "DeclareVariableFromParam":
                loadOpr = list(filter(lambda x: x["opr"] == "load", memory))[0]
                storeOpr = list(filter(lambda x: x["opr"] == "store", memory))[0]

                variableNamer.SetVariableName(storeOpr["index"])

                typeOfVariable = str(loadOpr["type"])
                nameOfVariable = variableNamer.GetVariableName(storeOpr["index"])
                nameOfValue = variableNamer.GetVariableName(loadOpr["index"])

                #type, value = inferTypeAndValue(typeOfVariable, valueOfVariable)
                typeInferredString = (
                    patterns[key]["equivalentJava"]
                    .replace("type", typeOfVariable)
                    .replace("value", str(nameOfValue))
                    .replace(
                        "variable", nameOfVariable
                    )
                )
                newJavaCodeList.append(typeInferredString)


            if key == "DeclareVariableFromGlobal":
                loadOpr = list(filter(lambda x: x["opr"] == "load", memory))[0]
                getOpr = list(filter(lambda x: x["opr"] == "get", memory))[0]
                storeOpr = list(filter(lambda x: x["opr"] == "store", memory))[0]
                variableNamer.SetVariableName(storeOpr["index"])
                typeOfVariable = str(storeOpr["type"])
                nameOfVariable = variableNamer.GetVariableName(storeOpr["index"])
                nameOfValue = getOpr["field"]["name"]
                #type, value = inferTypeAndValue(typeOfVariable, valueOfVariable)
                typeInferredString = (
                    patterns[key]["equivalentJava"]
                    .replace("type", typeOfVariable)
                    .replace("value", str(nameOfValue))
                    .replace(
                        "variable", nameOfVariable
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

            if key == "VarReturnValue":
                pushOpr = list(filter(lambda x: x["opr"] == "push", memory))[0]
                # Insert correct variable name in javacode
                print(pushOpr)

                if pushOpr["value"]["type"] == "string": 
                    word_with_quotes = f'"{pushOpr["value"]["value"]}"'
                    typeInferredString = patterns[key]["equivalentJava"].replace("type", word_with_quotes)
                elif pushOpr["value"]["type"] == "float": 
                    word_with_quotes = f'{pushOpr["value"]["value"]}f'
                    typeInferredString = patterns[key]["equivalentJava"].replace("type", word_with_quotes)
                else: 
                    typeInferredString = patterns[key]["equivalentJava"].replace(
                        "type", str(pushOpr["value"]["value"]))
                
                newJavaCodeList.append(typeInferredString)
            
            if key == "Return":
                newJavaCodeList.append("return;")       
            
              #Important that this is outside of conditional indentation

          
        elif is_subsequence(patterns["conditional1"]["pattern"], memory_oprs) or is_subsequence(patterns["conditional2"]["pattern"], memory_oprs):

                print(f"\n THIS IS THE KEY {key}")
                
                if not ValidateIf(memory):
                    break



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

                pushList.append((endPositionOfIf, "\n}", "if"))




                print(comparer)

                typeInferredString = patterns["conditional1"]["equivalentJava"].replace("variable1", str(valuesToCompare[0])).replace("comparer", comparer).replace("variable2", str(valuesToCompare[1]))
                print(typeInferredString)
                
                newJavaCodeList.append(typeInferredString)
                index = len(newJavaCodeList)-1
                print(f"WE HAVE SET THE INDEX: {index}")
                flowGraph.addIndexToCurrentNode(index)
                flowGraph.CreateNode()
                

                
                break

        elif is_subsequence(patterns["jump"]["pattern"], memory_oprs):
            pushList = [value for key, value in enumerate(pushList) if value[-1] != "if"]
            print(f"This is {pushList}")
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
    print(f"Full Javcode: {javaCodeList}\n")

    return "\n".join(javaCodeList)


def test_noop():
    print(" ")
    c = "dtu/compute/exec/Simple", "noop"
    (l, s) = [1], []
    print("---", c, "---")
    s = bytecode_interp(c, l, s, print)
    print(s)
    print("--- DONE ---")
