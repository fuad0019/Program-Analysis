import json
import random, string


with open("./patterns.json") as f:
    patterns = json.load(f)

localVariables = {}


def detectPattern(memory):
    memory_oprs = [item["opr"] for item in memory]
    print(memory_oprs)

    typeInferredString = ""
    for key, value in patterns.items():
        if memory_oprs == value["pattern"]:
            if key == "DeclareVariable":
                pushOpr = list(filter(lambda x: x["opr"] == "push", memory))[0]
                storeOpr = list(filter(lambda x: x["opr"] == "store", memory))[0]

                variableName = randomword(10)
                localVariables[storeOpr["index"]] = variableName

                typeOfVariable = pushOpr["value"]["type"]
                valueOfVariable = pushOpr["value"]["value"]
                typeInferredString = (
                    patterns[key]["equivalentJava"]
                    .replace("type", typeOfVariable)
                    .replace("value", str(valueOfVariable))
                    .replace("variable", variableName)
                )

            if key == "DeclareVariableAndAssignObject" or key == "ConstructObject":
                newOpr = list(filter(lambda x: x["opr"] == "new", memory))[0]
                storeOpr = list(filter(lambda x: x["opr"] == "store", memory))[0]

                typeOfObject = newOpr["class"]
                
                variableName = randomword(10)
                localVariables[storeOpr["index"]] = variableName

                typeInferredString = (
                    patterns[key]["equivalentJava"]
                    .replace("type", str(typeOfObject))
                    .replace("variable", variableName)
                )

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
                    typeInferredString = (
                        patterns[key]["equivalentJava"]
                        .replace("methodCall", str(methodName))
                        .replace("variable", localVariables[loadOpr["index"]])
                    )

            if key == "VarReturn":
                loadOpr = list(filter(lambda x: x["opr"] == "load", memory))[0]

                typeInferredString = patterns[key]["equivalentJava"].replace(
                    "variable", localVariables[loadOpr["index"]]
                )
            return typeInferredString
    print(key)


def bytecode_interp(method):
    memory = []
    javaCodeList = []
    bytecode_list = method["code"]["bytecode"]

    for i in range(
        len(bytecode_list)
    ):  # Loop dynamically adapts to the bytecode length
        b = bytecode_list[i]
        memory.append(b)
        javaCode = detectPattern(memory)
        if javaCode:
            print("DETECTED PATTERN")
            print(f"Javcode: {javaCode}")

            javaCodeList.append(javaCode)
            memory = []
        # print(memory)

    print("Finished Method")
    print(javaCode)

    return "\n".join(javaCodeList)


def randomword(length):
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def test_noop():
    print(" ")
    c = "dtu/compute/exec/Simple", "noop"
    (l, s) = [1], []
    print("---", c, "---")
    s = bytecode_interp(c, l, s, print)
    print(s)
    print("--- DONE ---")
