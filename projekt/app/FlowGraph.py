#Build first node
#Take bytecode as input
#if not conditional
    #Append as a basic block to tail node
#If conditional
    #create new node and add
#take conditional as input
#Add


import random, string
from Node import *

class FlowGraph:
    def __init__(self):
        self.Nodes = []
        self.currentNode = None
        self.visitedProgramCounters = []
        

    def addOprToCurrentNode(self, opr):
        self.visitedProgramCounters.append(opr["offset"])
        self.currentNode.addToBasicBlock(opr)

    def addIndexToCurrentNode(self, index):
        self.addIndexToCurrentNode(index)
        

    
    def CreateNode(self, indexJavaCode):
        node = Node()
        if self.currentNode: 
            node.AddPredessor(self.currentNode)
            self.currentNode.AddSuccessor(node)

        if indexJavaCode:
            node.addIndex(indexJavaCode)

        self.currentNode = node
        self.Nodes.append(node)

        
        


    def detectLoop(self,gotoOpr ):

        inLoop = False
     
        
        
            
            
            
        if gotoOpr["target"]  in self.visitedProgramCounters:

            node = filter(lambda node: [opr for opr in node.getbasicBlock() if opr["index"] == gotoOpr["target"]] )
             
            while len(node.getSuccessors())>0:
                headerIndex = node.getIndex()
                if headerIndex:
                    break
                node = node.getSuccessors()[0]

        return inLoop, headerIndex
                

                











    