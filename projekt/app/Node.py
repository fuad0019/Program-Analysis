
class Node:
    def __init__(self):
        self.predessors = []
        self.successors = []
        self.basicBlock = []
        self.index = None
    
    

    def AddSuccessor(self, successor):
        self.successors.append(successor)
    
    def getSuccessors(self):
        return self.successors


    def AddPredessor(self, predessor):
        self.predessors.append(predessor)

    def getPredessor(self):
        return self.predessors
    
    def addToBasicBlock(self, opr):
        self.basicBlock.append(opr)
    
    def getBasicBlock(self):
        return self.basicBlock

    def addIndex(self,index):
        self.index = index
    
    def getIndex(self):
        return self.index
        



        
