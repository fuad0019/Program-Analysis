import random, string


class VariableNamer:
    def __init__(self):
        self.localVariables = {}  
        self.counter = 0     

    def GetVariableName(self, index):
        if index in self.localVariables:
            return self.localVariables[index]

    
    def SetVariableName(self, index):
            variableName = f"var{self.counter}"
            self.localVariables[index] = variableName #Assign local variable and save it in a list
            self.counter += 1
    
    def randomword(self,length): #bruges ikke 
        letters = string.ascii_lowercase
        return "".join(random.choice(letters) for i in range(length))

