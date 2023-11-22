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
        self.currentNode.addIndex(index) 
        

    
    def CreateNode(self):
        node = Node()
        if self.currentNode: 
            node.AddPredessor(self.currentNode)
            self.currentNode.AddSuccessor(node)

        

        self.currentNode = node
        self.Nodes.append(node)




    def detectLoop(self,gotoOpr ):

        inLoop = False

            
        print(self.Nodes)
            
        print(gotoOpr["target"]) #2
        print(self.visitedProgramCounters) #[0,1,2,3,4]


        if gotoOpr["target"]  in self.visitedProgramCounters:
            inLoop = True

            node = list(filter(lambda node: [opr for opr in node.getBasicBlock() if opr["offset"] == gotoOpr["target"]], self.Nodes ))[0]
            print(len(self.Nodes))
            while len(node.getSuccessors())>0:
                
                headerIndex = node.getIndex()
                print(f"iterator: {headerIndex}")
                if headerIndex is not None:
                    break
                node = node.getSuccessors()[0]

        return inLoop, headerIndex
                

                











    