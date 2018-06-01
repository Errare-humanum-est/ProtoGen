from antlr3.tree import CommonTree

from DataObjects.ClassMessage import Message
from DataObjects.ClassStateNode import StateNode
from DataObjects.ClassState import State


class Transition:
    def __init__(self, startstate, finalstate, access='', inmsg='', outmsg='', cond='', operation=''):

        assert isinstance(startstate, StateNode)
        assert isinstance(finalstate, StateNode)

        if access:
            assert isinstance(access, str) or isinstance(access, Message)

        if not startstate.testaccess(access) and inmsg == '':
            self.inMsg = access
            self.access = ''
        else:
            self.access = access
            self.inMsg = inmsg

        if inmsg:
            assert isinstance(inmsg, Message)

        if isinstance(outmsg, list) and all(isinstance(msg, Message) for msg in outmsg):
            self.outMsg = outmsg
        elif isinstance(outmsg, Message):
            self.outMsg = [outmsg]
        elif outmsg == '':
            self.outMsg = []
        else:
            assert 0, "Unknown output message format"

        if operation:
            if isinstance(operation, list):
                assert all(isinstance(entry, CommonTree) for entry in operation)
                self.operation = operation
            else:
                assert isinstance(operation, CommonTree)
                self.operation = [operation]
        else:
            self.operation = []

        # The cond field is only for debugging options
        # The operation field is vital for the correctness of the parser
        if cond:
            if isinstance(cond, list):
                assert all(isinstance(entry, str) for entry in cond)
                self.cond = cond
            else:
                assert isinstance(cond, CommonTree)
                self.cond = [cond]
        else:
            self.cond = []

        self.startState = startstate
        self.finalState = finalstate

        self.defermsg = []
        self.refguard = ''
        self.outmsgrename = {}

########################################################################################################################
# SETUP FUNCTIONS
########################################################################################################################
    def addoperation(self, treenode):
        assert isinstance(treenode, CommonTree)
        self.operation.append(treenode)

    def getoperation(self):
        return self.operation

    def setstartstate(self, startstate):
        assert isinstance(startstate, (StateNode, State))
        self.startState = startstate

    def getstartstate(self):
        return self.startState

    def setfinalstate(self, finalstate):
        assert isinstance(finalstate, (StateNode, State))
        self.finalState = finalstate

    def getfinalstate(self):
        return self.finalState

    def getaccess(self):
        return self.access

    def getinmsg(self):
        return self.inMsg

    def setinmsg(self, inmsg):
        assert isinstance(inmsg, Message)
        self.inMsg = inmsg

    def addoutmsg(self, message):
        assert isinstance(message, Message)
        self.outMsg.append(message)

    def getoutmsg(self):
        return self.outMsg

    def setoutmsg(self, outmsg):
        if outmsg:
            assert isinstance(outmsg, Message)
        self.outMsg = outmsg

    def deferoutmsg(self, defermsgs=0):
        if not defermsgs:
            msg = self.outMsg
            self.outMsg = []
            self.defermsg += [entry for entry in msg if entry not in self.defermsg]
            return msg

        else:
            newoutmsg = []
            defermsg = []
            for msg in self.outMsg:
                if isinstance(msg, Message):
                    msgid = msg.getmsgtype()
                else:
                    msgid = msg
                if msgid in defermsgs:
                    defermsg.append(msg)
                else:
                    newoutmsg.append(msg)

            self.defermsg += [entry for entry in defermsg if entry not in self.defermsg]
            self.outMsg = newoutmsg

            return defermsg

    def deferspecoutmsg(self, nondefermsg):
        defermsg = []
        for msg in self.outMsg:
            if isinstance(msg, Message):
                msgid = msg.getmsgtype()
            else:
                msgid = msg
            if msgid not in nondefermsg:
                defermsg.append(msg)

        for msg in defermsg:
            self.outMsg.remove(msg)

        self.defermsg += defermsg

        return self.defermsg

    def getdefermsg(self):
        return self.defermsg

    def getguard(self):
        if self.access:
            guard = self.access
        else:
            if isinstance(self.inMsg, Message):
                guard = self.inMsg.getmsgtype()
            else:
                guard = self.inMsg
        return guard

    def getrefguard(self):
        return self.refguard

    def addcond(self, cond):
        self.cond.append(cond)

    def getcond(self):
        return self.cond

    def getoutmsgrenamed(self):
        return self.outmsgrename

    def getoutmsgtypes(self):
        msgouttypes = []
        for message in self.outMsg:
            if isinstance(message, str):
                msgouttypes.append(message)
            else:
                msgouttypes.append(message.getmsgtype())
        return msgouttypes


########################################################################################################################
# PROTOGEN FUNCTIONS
########################################################################################################################

    def replaceguard(self, guard):
        assert isinstance(guard, str)

        if self.access:
            self.access = guard
        else:
            self.refguard = self.inMsg
            if isinstance(self.inMsg, Message):
                self.inMsg.setmsgtype(guard)
            else:
                self.inMsg = guard

    def renameoutmsg(self, curname, newname):
        for outmsg in self.outMsg:
            if outmsg.getmsgtype() == curname:
                outmsg.setmsgtype(newname)
            self.outmsgrename.update({curname: newname})


########################################################################################################################
# DEBUG FUNCTIONS
########################################################################################################################

    def pbase(self):
        return ("Transition:: SS: " + self.startState.pstate() +
                "  FS: " + self.finalState.pstate() +
                " Guard: " + str(self.getguard()))

