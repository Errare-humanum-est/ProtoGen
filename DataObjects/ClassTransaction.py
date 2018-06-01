import copy
from Monitor.Debug import *
from DataObjects.ClassStateNode import StateNode
from DataObjects.ClassTransition import Transition
from Parser.ForkTree import ForkTree


class Transaction:

    def __init__(self, startstate, guard, finalstate):

        assert isinstance(startstate, StateNode)
        assert isinstance(finalstate, StateNode)
        assert isinstance(guard, str)

        self.messages = {}
        self.trans = []

        self.startState = startstate
        self.interfinalState = finalstate.getstatename()
        self.access = guard

        self.TransTree = ForkTree()
        self.ifTree = 0
        self.TransTree.insertnode(Transition(startstate, finalstate, guard))
        self.IfTree = ForkTree()

########################################################################################################################
# DATA ACCESS
########################################################################################################################

    def gettransitions(self):
        return self.trans

    def getMessageMap(self):
        return self.messages

########################################################################################################################
# TRANSITION TREE
########################################################################################################################

    def getstartstate(self):
        return self.startState

    def getinterfinalstate(self):
        return self.interfinalState

    def getnrtransitions(self):
        return len(self.trans) + 1

########################################################################################################################
# GENERAL
########################################################################################################################

    def getcurtransition(self):
        if self.ifTree:
            return self.IfTree.getcurnode().getdata()
        else:
            return self.TransTree.getcurnode().getdata()

    def getcurtransitionode(self):
        if self.ifTree:
            return self.IfTree.getcurnode()
        else:
            return self.TransTree.getcurnode()

    def addoperation(self, operation):
        if self.ifTree:
            childs = self.IfTree.getchildnodes(self.IfTree.getcurnode())
            for entry in childs:
                entry.getdata().addoperation(operation)
        else:
            return self.TransTree.getcurnode().getdata().addoperation(operation)

    def addoutmsg(self, message):
        if self.ifTree:
            childs = self.IfTree.getchildnodes(self.IfTree.getcurnode())
            for entry in childs:
                entry.getdata().addoutmsg(message)
        else:
            return self.TransTree.getcurnode().getdata().addoutmsg(message)

    def setfinalstate(self, finalstate):
        if self.ifTree:
            childs = self.IfTree.getchildnodes(self.IfTree.getcurnode())
            for entry in childs:
                entry.getdata().getfinalstate().setstatename(finalstate)
        else:
            return self.TransTree.getcurnode().getdata().getfinalstate().setstatename(finalstate)

########################################################################################################################
# IF TREE
########################################################################################################################

    def newifconstr(self):
        if not self.ifTree:
            self.IfTree.insertnode(self.getcurtransition(), self.getcurtransitionode())
        self.ifTree = 1

    def newifelse(self):
        curnode = self.IfTree.getcurnode()
        return self.IfTree.insertnode(copy.deepcopy(curnode.getdata()), curnode)

    def endif(self):
        return self.IfTree.popcurnode()

    def endifconstr(self):
        endnodes = []
        if self.ifTree:
            curnode = self.IfTree.getbasenode()
            prenode = self.TransTree.popdelcurnode(curnode)
            # Get all end nodes
            endnodes = self.IfTree.getendnodes()
            ret = self.TransTree.appendnodes(endnodes, prenode)

            if not ret:
                perror("Nodes with unknown predecessors could not be inserted into tree")

            # Clear tree
            self.IfTree = ForkTree()
        self.ifTree = 0

        return endnodes

########################################################################################################################
# TRANSITION TREE
########################################################################################################################

    def newwhen(self, startstate, finalstate, guard, prenode):
        return self.TransTree.insertnode(Transition(startstate, finalstate, guard), prenode)

    def endwhen(self):
        # Push if tree at end of transition tree
        return self.TransTree.popcurnode()

    def pushtransition(self):
        # Extract tree into simple transitions
        self.trans += self.TransTree.treetolist()

########################################################################################################################
# MESSAGE SECTION
########################################################################################################################

    def addmessage(self, mname, message):
        self.messages.update({mname: message})

    def getmessage(self, mname):
        msg = self.messages.get(mname)
        if not msg:
            perror("KeyError: Message was never instantiated")
        return msg

########################################################################################################################
# DEBUG
########################################################################################################################

    def pbase(self):
        return ("Transaction:: " +
                "Start: " + self.startState.pstate() +
                "  *Guard: " + self.access +
                "  Final: " + self.interfinalState)

