from antlr3.tree import CommonTree
from Parser.ProtoCCParser import ProtoCCParser
from Parser.ProtoCCcomTreeFct import *
from Monitor.Debug import pdebug

class PCCObject:
    def __init__(self, node):

        assert isinstance(node, CommonTree)

        self.structure = node

        definitions = node.getChildren()
        self.name = definitions[0].getText()
        self.variables = {}
        self._getvarnames(definitions, self.variables)
        pdebug("Object: " + node.getText() + " " + self.name + " -> varNames: " + str(self.variables))

    @staticmethod
    def _getvarnames(nodes, variables):
        assign = 'INITVAL_'
        for node in nodes:
            # Check if data type
            if node.getText() in ProtoCCParser.tokenNames:
                entry = toStringList(node)
                if assign in entry:
                    variables.update({entry[entry.index(assign)-1]: node.getText()})
                else:
                    variables.update({entry[-1]: node.getText()})

    def getname(self):
        return self.name

    def getvariables(self):
        return self.variables

    def testname(self, name):
        if name == self.name:
            return 1
        return 0

    def testvariable(self, name):
        if name in self.variables:
            return 1
        return 0

    def getnode(self):
        return self.structure
