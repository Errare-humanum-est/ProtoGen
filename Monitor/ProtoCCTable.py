from Monitor.Debug import *
from DataObjects.ClassMessage import Message
from Parser.ProtoCCcomTreeFct import *


class ProtoCCTablePrinter:
    Spacing = 20
    TransFormat = ["StartState", "FinalState", "Access", "InMsg", "OutMsg", "Cond"]

    def ptransactions(self, transactions):
        if testdebug():
            transitions = []
            for transaction in transactions:
                transitions += transaction.gettransitions()

            self.ptransitiontable(transitions)

    def ptransition(self, transition):
        ptable(self.TransFormat, [self.outtransition(transition)])

    def ptransitiontable(self, transitions):
        output = []
        for transition in transitions:
            output.append(self.outtransition(transition))
        ptable(self.TransFormat, output)

    @staticmethod
    def outtransition(transition):
        StartState = transition.getstartstate().getstatename()
        FinalState = transition.getfinalstate().getstatename()

        Access = transition.getaccess()
        InMsg = transition.getinmsg()
        if isinstance(InMsg, Message):
            pInMsg = InMsg.getmsgtype()
        else:
            pInMsg = InMsg

        pOutMsg = ""

        for OutMsg in transition.getoutmsg():
            if pOutMsg != "":
                pOutMsg += "; "
            pOutMsg += OutMsg.getmsgtype() + "@" + OutMsg.getvc() + ""

        pCond = ""
        for cond in transition.getcond():
            pCond += cond + "; "

        return [StartState, FinalState, Access, pInMsg, pOutMsg, pCond]

    @staticmethod
    def ptransaction(transactions):
        for transaction in transactions:
            ProtoCCTablePrinter().ptransitions(transaction.gettransitions())

    @staticmethod
    def ptransitions(transitions):
        for transition in transitions:
            ProtoCCTablePrinter().ptransition(transition)
            pdebug('$')
            ops = objListToStringList(transition.getoperation())
            for entry in ops:
                pdebug(entry)
            pdebug()

    def pstates(self, states):
        for state in states:
            pheader('$$$$' + state.getstatename())
            self.ptransitions(state.gettransitions())
