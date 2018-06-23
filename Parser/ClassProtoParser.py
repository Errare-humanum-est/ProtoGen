import antlr3
import re

from Monitor.Debug import *
from Monitor.ProtoCCTable import ProtoCCTablePrinter

from Parser.ProtoCCLexer import ProtoCCLexer
from Parser.ProtoCCParser import ProtoCCParser
from Parser.ProtoCCcomTreeFct import *

from DataObjects.ClassProtoCCObject import PCCObject
from DataObjects.ClassStateNode import StateNode
from DataObjects.ClassTransaction import Transaction
from DataObjects.ClassMessage import Message

from Graphv.ProtoCCGraph import ProtoCCGraph

class ProtoParser:

    # PARSER TOKENS ####################################################################################################
    Objects = {
        'CONSTANT_': '_CreateConstant',
        'NETWORK_': '_CreateNetwork',
        'CACHE_': '_CreateCache',
        'DIR_': '_CreateDir',
        'MSG_': '_CreateMsgObj',
        'ARCH_': '_CreateArch',
    }

    ArchEntity = {
        'MACHN_': '_CheckMachine',
        'PROC_': '_CreateProc',
        'STABLE_': '_CreateStableSet',
    }

    TransEntity = {
        'TRANS_': '_CreateTrans',
        'ASSIGN_': '_CreateAssign',
        'SEND_': '_SendMsg',
        'MCAST_': '_SendMsg',
        'AWAIT_': '_TransactionFork',
        'WHEN_': '_NewTransition',
        'ENDWHEN_': '_EndTransition',
        'GUARD_': '_SetTransGuard',
        'ENDPROC_': '_EndProcess',
        'BREAK_': '_EndTransaction',
        'IFELSE_': '_CreateIfElse',
        'IF_': '_NewIfElseFork',
        'ENDIF_': '_HandleEndif',
        'COND_': '_HandleCond',
        'NCOND_': '_HandleCond',
        'SETFUNC_': '_SetFunctions',
    }

    AssignObj = {
        'MSGCSTR_': '_CreateMsg',
        'SETFUNC_': '_SetFunctions',
    }

    Access = ['load', 'store']
    Evict = ['evict']
    Accesses = Access + Evict

    Data = 'DATA_'
    State = 'State'

    # PROTO DATA OBJECTS ###############################################################################################
    constNode = {}
    networkNode = []
    cacheSeq = []
    cacheNode = {}
    dirSeq = []
    dirNode = {}
    msgNode = []
    msgTypes = []
    archNode = {}
    stableStates = {}

    dataMsgTypes = []

    def __init__(self, file=""):
        if file:
            self.file = file
            lexer = ProtoCCLexer(antlr3.StringStream(open(file).read()))
            parser = ProtoCCParser(antlr3.CommonTokenStream(lexer))
            tree = parser.document().getTree()
            pdebug(tree.toStringTree())
            self._ParseNodes(tree)
            #self._dArch()


########################################################################################################################
# PUBLIC FUNCTIONS
########################################################################################################################

    def checkAccessBehaviourDefined(self):
        # Ensure SSP specifies behaviour for every access in every stable state
        for stable_state in self.getStableStates().get('cache'):
            access_found_dict = { access: False for access in self.Accesses }
            if 'I' in stable_state: # Don't expect evictions in Invalid state
                # TODO this puts some pretty strict assumptions on the state
                # naming convention - is there a way around this?
                access_found_dict['evict'] = True
            for trans in self.getArchitectures().get('cache'):
                if (trans.getstartstate().getstatename() == stable_state
                        and trans.getaccess() != ''):
                    access_found_dict[trans.getaccess()] = True
            for access, found in access_found_dict.items():
                if not found:
                    pwarning("No behaviour for an access of type \"" + access
                             + "\" modelled for (cache) stable state \""
                             + stable_state + "\" in the input SSP.")
                    return False
        # Have checked every stable state without finding any faults
        return True

    def checkAllStatesReachable(self):
        for arch in self.getArchitectures():
            arch_start_state_name = ''
            
            if arch == 'cache':
                for key, val in self.cacheNode[arch].getvariables().items():
                    if val == 'INITSTATE_':
                        arch_start_state_name = key
            else: # otherwise arch is directory
                for key, val in self.dirNode[arch].getvariables().items():
                    if val == 'INITSTATE_':
                        arch_start_state_name = key

            if arch_start_state_name == '':
                pwarning("Unable to locate the name of the initial state of "
                         "architecture \"" + arch + "\".")
                return False

            # Build up a graph of the transitions for the architecture
            # (X : {A, B, ..} -> there are transitions
            # from X to A, B, ...)
            transition_graph = {}
            for trans in self.getArchitectures().get(arch):
                trans_state_name = trans.getstartstate().getstatename()
                if trans_state_name in transition_graph:
                    transition_graph[trans_state_name].add(
                        trans.getfinalstate().getstatename())
                else:
                    transition_graph[trans_state_name] = {
                        trans.getfinalstate().getstatename()}

            # Keep track of which states have been visited
            visited_map = set()

            # Explore transition graph via DFS, adding to the visited map
            # as we go
            self._dfsExploreFromVertex(
                    arch_start_state_name, transition_graph, visited_map)

            # Make sure all stable states are reachable from the initial state
            for state_name in self.getStableStates().get(arch):
                if state_name not in visited_map:
                    pwarning('State \"' + state_name + '\" of architecture \"'
                             + arch + '\" is not reachable from the initial '
                             'state as it has been defined in the input .pcc'
                             ' file.')
                    return False
        
        # Have now checked all specified architectures without finding any
        # "lost" states
        return True

    def getArchitectures(self):
        archtrans = {}
        for arch in self.archNode:
            archtrans.update({arch: self._extractTransitions(self.archNode[arch])})
        return archtrans

    def _extractTransitions(self, transactions):
        transitions = []
        for transaction in transactions:
            transitions += transaction.gettransitions()

        transitions = self._filterTransitions(transitions)

        return transitions

    def getConstants(self):
        return self.constNode

    def getNetwork(self):
        return self.networkNode

    def getMessages(self):
        return self.msgTypes

    def getMessageNodes(self):
        return self.msgNode

    def getCaches(self):
        return self.cacheNode

    def getCacheSeq(self):
        return self.cacheSeq

    def getCacheIdentifiers(self):
        return self.cacheNode.keys()

    def getDir(self):
        return self.dirNode

    def getDirSeq(self):
        return self.dirSeq

    def getDirIdentifiers(self):
        return self.dirNode.keys()

    def getAccess(self):
        return self.Access

    def getEvict(self):
        return self.Evict

    def getStableStates(self):
        return self.stableStates

    def getDataMsgTypes(self):
        return self.dataMsgTypes

    def getFilename(self):
        return self.file

########################################################################################################################
# PARSER ENTRY POINT
########################################################################################################################

    def _ParseNodes(self, tree):
        objects = tree.getChildren()
        for obj in objects:
            method_fct = self.Objects[obj.getText()]
            method = getattr(self, method_fct, lambda: '__UnknownNode__')
            method(obj)

        self._pArchTable()

    @staticmethod
    def _UnknownNode(obj):
        perror("Unknown Node Identifier")
        perror(obj.getText())

########################################################################################################################
# SECTIONS
########################################################################################################################

    def _CreateConstant(self, obj):
        self.constNode.update(self._getObjName(obj.getParent()))

    def _CreateNetwork(self, obj):
        self.networkNode.append(obj)

    def _CreateCache(self, obj):
        self.cacheNode.update(self._createObj(obj))
        self.cacheSeq.append(self._getName(obj.getChild(0)))

    def _CreateDir(self, obj):
        self.dirNode.update(self._createObj(obj))
        self.dirSeq.append(self._getName(obj.getChild(0)))

    def _CreateMsgObj(self, obj):
        self.msgNode.append(PCCObject(obj))

        msgformat = obj.getChildren()

        msgtype = ""
        for ind in range(0, len(msgformat)):
            if ind == 0:
                msgtype = msgformat[ind].getText()
            else:
                if msgformat[ind].getText() == self.Data:
                    self.dataMsgTypes.append(msgtype)

    def _CreateArch(self, arch):
        machname = ''
        transactions = []
        stablestates = []

        for comp in arch.getChildren():
            method_fct = self.ArchEntity[comp.getText()]
            method = getattr(self, method_fct, lambda: '__UnknownNode__')
            result = method(comp)

            if isinstance(result, str):
                machname = result
            elif isinstance(result, Transaction):
                transactions.append(result)
            elif isinstance(result, list):
                stablestates += result
            else:
                perror("Unexpected data type")

        self.archNode.update({machname: transactions})
        self.stableStates.update({machname: stablestates})


        pdebug("Architecture " + machname +
               ", #Transactions: " + str(len(transactions)))

########################################################################################################################
# OBJECT METHODS
########################################################################################################################

    @staticmethod
    def _getName(obj):
        return obj.getText()

    def _getObjName(self, child):
        return {self._getName(child.getChild(0)): child.getChild(0)}

    def _createObj(self, obj):
        return {self._getName(obj.getChild(0)): PCCObject(obj)}

########################################################################################################################
# ARCHITECTURE
########################################################################################################################

    def _CheckMachine(self, comp):
        # Make sanity check if Object for architecture exists
        machname = comp.getChildren()

        if len(machname) > 1:
            perror("Machine name error" + str(machname))

        refcache = list(filter(lambda x: machname[0].getText() == x.getname(),
                               (list(self.cacheNode.values()) + list(self.dirNode.values()))))

        if len(refcache) == 0:
            perror("The machine was not defined: " + str(machname[0].getText()), refcache)

        elif len(refcache) > 1:
            perror("Machine names are ambigous " + refcache[0].getname())

        else:
            refcache = refcache[0]

        if not refcache:
            perror("Architecture " + refcache.GetName() + " does not exist as Machine")

        return machname[0].getText()

    @staticmethod
    def _CreateStableSet(stable):
        stablenodes = stable.getChildren()

        stablestates = []
        for node in stablenodes:
            stablestates.append(node.getText())

        return stablestates

    def _CreateProc(self, architecture, transaction=0):

        for comp in architecture.getChildren():
            method_fct = self.TransEntity[comp.getText()]
            method = getattr(self, method_fct, lambda: '__UnknownNode__')
            transaction = method(comp, transaction)

        return transaction

    def _EndProcess(self, comp=0, transaction=0):
        nrinit = transaction.getnrtransitions()
        endnodes = transaction.endifconstr()
        if endnodes:
            for node in endnodes:
                curtrans = node.getdata()
                if curtrans.getfinalstate().getstatename() == transaction.getinterfinalstate():
                    curtrans.getfinalstate().setstatename(curtrans.getstartstate().getstatename())
        else:
            curtrans = transaction.getcurtransition()
            if curtrans.getfinalstate().getstatename() == transaction.getinterfinalstate() \
                    and curtrans.getfinalstate().getstatename() == self.State:
                    curtrans.getfinalstate().setstatename(curtrans.getstartstate().getstatename())

        transaction.pushtransition()
        pdebug("New transitions due to fork: " + str(transaction.getnrtransitions() - nrinit))

        return transaction

    def _CreateTrans(self, trans, transaction):
        if not isinstance(transaction, int):
            perror("Nested transactions are not permited")

        transsetup = toStringList(trans)

        # Static format
        startstate = StateNode(transsetup[1], self.Accesses)

        if len(transsetup) > 3:
            finalstate = StateNode(transsetup[3], self.Accesses)
        else:
            finalstate = StateNode(self.State, self.Accesses)

        transaction = Transaction(startstate, transsetup[2], finalstate)

        return transaction

########################################################################################################################
# AWAIT (WHEN GUARD)+
########################################################################################################################

    def _TransactionFork(self, node, transaction):
        transaction.endifconstr()
        curtrans = transaction.getcurtransition()
        if curtrans.getfinalstate().getstatename() == transaction.getinterfinalstate():
            # Generate new intermediate state name
            finalstate = curtrans.getstartstate().getstatename() + "_" + curtrans.getguard()
            curtrans.getfinalstate().setstatename(finalstate)
            pdebug(transaction.getcurtransition().pbase())

        self._CreateProc(node, transaction)
        return transaction

    def _NewTransition(self, node, transaction):
        transaction = self._CreateProc(node, transaction)
        return transaction

    def _SetTransGuard(self, node, transaction):
        guardtype = node.getChild(0).toString()
        guardmsg = Message(guardtype)

        if not list(filter(lambda x: guardtype == x, self.msgTypes)):
            self.msgTypes.append(guardtype)

        # Append new transition to tree (When is always succeded by a guard
        prenode = transaction.getcurtransitionode()
        startstate = transaction.getcurtransition().getfinalstate()
        finalstate = StateNode(transaction.getinterfinalstate(), self.Accesses)
        transaction.newwhen(startstate, finalstate, guardmsg, prenode)

        return transaction

    def _EndTransition(self, node=0, transaction=0):
        endnodes = transaction.endifconstr()

        # Check if the final state has changed from default
        # If not loop in intermediate state
        if not endnodes:
            transition = [transaction.getcurtransition()]
        else:
            transition = []
            for entry in endnodes:
                transition.append(entry.getdata())

        for curtrans in transition:
            if curtrans.getfinalstate().getstatename() == transaction.getinterfinalstate():
                curtrans.getfinalstate().setstatename(curtrans.getstartstate().getstatename())

        # return to preceeding tree node
        assert not transaction.getcurtransitionode() == transaction.endwhen(), "Unexpected behaviour"

        return transaction

    def _EndTransaction(self, node=0, transaction=0):
        # Check if the final state has changed from default
        # If not return to start state
        curtrans = transaction.getcurtransition()
        if curtrans.getfinalstate().getstatename() == transaction.getinterfinalstate():
            curtrans.setfinalstate(transaction.getstartstate())
        return transaction

########################################################################################################################
# ASSIGNMENT
########################################################################################################################

    @staticmethod
    def _AssignVarName(assign):
        return ''.join(toStringList((assign.getChildren())[0]))

    def _CreateAssign(self, assign, transaction):

        transaction.addoperation(assign)

        # Assign new variable name
        # [left op assign]
        assigndef = assign.getChildren()

        # Check for object initialization
        for comp in assigndef:
            if comp.getChildren():
                if not list(filter(lambda x: comp.getText() == x, self.msgTypes)):
                    try:
                        method_fct = self.AssignObj[comp.getText()]
                    except KeyError:
                        method_fct = 0

                    if method_fct:
                        method = getattr(self, method_fct, lambda: '__UnknownNode__')
                        transaction = method(comp, transaction)

        # Set state name
        if assigndef[0].toString() == transaction.getinterfinalstate():
            transaction.setfinalstate(assigndef[2].toString())
            pdebug(transaction.getcurtransition().pbase())

        return transaction

    ####################################################################################################################
    # Message assignment
    ####################################################################################################################

    def _CreateMsg(self, message, transaction):
        # msg: format
        # [object, type, src, dest, payload..]

        varname = self._AssignVarName(message.getParent())

        msg = message.getChildren()
        msgobj = msg[0].getText()

        if not list(filter(lambda x: msgobj in x.getname(), self.msgNode)):
            perror("Object related to constructor undefined")

        if msg[1].getChildren():
            perror("Expected message identifier")

        msgtype = msg[1].getText()
        msgsrc = ''.join(toStringList(msg[2]))
        msgdest = ''.join(toStringList(msg[3]))

        payload = []
        for ind in range(4, len(msg)):
            payload.append(''.join(toStringList(msg[ind])))

        msgconstr = Message(msgtype, msgobj, msgsrc, msgdest, payload, msgobj)
        transaction.addmessage(varname, msgconstr)

        if not list(filter(lambda x: msgtype == x, self.msgTypes)):
            self.msgTypes.append(msgtype)

        return transaction

########################################################################################################################
# NETWORK FUNCTIONs
########################################################################################################################

    def _SendMsg(self, message, transaction):
        transaction.addoperation(message)

        send = toStringList(message)
        msg = transaction.getmessage(send[2])
        msg.setvc(send[1])
        transaction.addoutmsg(msg)

        return transaction

########################################################################################################################
# IF ELSE
########################################################################################################################

    def _CreateIfElse(self, node, transaction):
        transaction.newifconstr()
        self._CreateProc(node, transaction)
        return transaction

    def _NewIfElseFork(self, node, transaction):
        transaction.newifelse()
        self._CreateProc(node, transaction)
        return transaction

    @staticmethod
    def _HandleCond(node, transaction):
        transaction.getcurtransition().addoperation(node)
        transaction.getcurtransition().addcond(''.join(toStringList(node)))
        return transaction

    @staticmethod
    def _HandleEndif(node=0, transaction=0):
        transaction.endif()
        return transaction

########################################################################################################################
# SET FUNCTION
########################################################################################################################
    @staticmethod
    def _SetFunctions(node, transaction):
        transaction.addoperation(node)
        return transaction

########################################################################################################################
# POST-PROCESSING
########################################################################################################################
    def _filterTransitions(self, transitions):
        guardtransmap = {}
        for transition in transitions:
            guard = transition.getstartstate().getstatename() + transition.getguard() + "".join(transition.getcond())

            if guard in guardtransmap:
                entryset = set([self._stripstr(op.toStringTree()) for op in guardtransmap[guard].getoperation()])
                transset = set([self._stripstr(op.toStringTree()) for op in transition.getoperation()])

                if transset.issuperset(entryset):
                    guardtransmap.update({guard: transition})
                else:
                    if not entryset.issuperset(transset):
                        perror("In State: " + transition.getstartstate().getstatename() +
                               "; At guard " + transition.getguard() +
                               "; multiple inconsistent behavioural descriptions exist for condition:" +
                               " ".join(transition.getcond()))

            else:
                guardtransmap.update({guard: transition})

        return list(guardtransmap.values())

    def _stripstr(self, string):
        return re.sub(r'\W', '', string)

########################################################################################################################
# DEBUG
########################################################################################################################

    def _dArch(self):
        for arch in self.archNode:
            transactions = self.archNode[arch]
            transitions = []
            for transaction in transactions:
                transitions += transaction.gettransitions()

            ProtoCCGraph("Spec: " + arch, transitions)

    def _pArchTable(self):
        for arch in self.archNode:
            transitions = []
            for transaction in self.archNode[arch]:
                transitions += transaction.gettransitions()

            transitions = self._filterTransitions(transitions)

            pheader(arch + ": Total number of transitions: " + str(len(transitions)))
            ProtoCCTablePrinter().ptransitiontable(transitions)

    def _pArch(self):
        for arch in self.archNode:
            self._pArchTransactions(arch, self.archNode[arch])
            self._pArchTransitions(arch, self.archNode[arch])

    def _pArchTransactions(self, name, transactions):
        pheader(name + " :Transactions Summary")
        ProtoCCTablePrinter().ptransactions(transactions)

    def _pArchTransitions(self, name, transactions):
        pheader(name + " :Transitions Summary")
        ProtoCCTablePrinter().ptransaction(transactions)

    def _pMessages(self):
        pheader("\nMessages")
        for entry in self.msgTypes:
            pdebug(entry)
        pdebug('\n')

################################################################################
# MISC
################################################################################
    def _dfsExploreFromVertex(self, start_state_name, transition_graph, visited_map):
        # do nothing if we've already explored this node
        if start_state_name not in visited_map: 
            visited_map.add(start_state_name)

            for state_name in transition_graph.get(start_state_name) or []:
                # (the 'or []' here ensures Python doesn't throw an error if
                # transition_graph.get(start_state_name) is None, but instead
                # just does nothing)
                self._dfsExploreFromVertex(state_name, transition_graph, visited_map)

