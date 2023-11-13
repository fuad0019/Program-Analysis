import random, string


class VariableNamer:
    def __init__(self):
        self.localVariables = {}  
        self.counter = 0     

    def GetVariableName(self, index):
        if index in self.localVariables:
            return self.localVariables[index]

    
    def SetVariableName(self, index):
            variableName = self.randomword(10)
            self.localVariables[index] = variableName #Assign local variable and save it in a list
    
    def randomword(self,length):
        letters = string.ascii_lowercase
        return "".join(random.choice(letters) for i in range(length))

