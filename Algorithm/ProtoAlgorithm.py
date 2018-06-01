import copy
import time

from DataObjects.ClassState import State
from DataObjects.ClassStateSet import StateSet

from Algorithm.TraceNode import NodeObj

from Parser.ForkTree import ForkTree

from Monitor.ProtoCCTable import *


class ProtoAlgorithm:

    def __init__(self, parser, config):

        self.arch = parser.getArchitectures()
        self.msg = parser.getMessages()
        self.stableStates = parser.getStableStates()
        self.datamsgs = parser.getDataMsgTypes()

        self.cacheIds = parser.getCacheIdentifiers()
        self.dirIds = parser.getDirIdentifiers()
        self.access = parser.getAccess()
        self.evict = parser.getEvict()

        self.archProtoGen = {}
        self.renamedMessages = {}
        self.hiddenChangeStates = []

        self.cacheStateSets = []

        self.progressMessages = []

        # Options State Generation
        # Option merges states based on their names
        self.enableStateNameMerging = config.enableStateNameMerging

        # Options Cache
        self.CCconservativeInv = config.CCconservativeInv
        self.nonstalling = config.nonstalling

        self.maxNestingDepthCC = config.maxNestingDepthCC

        # Options Directory
        self.DCconservativeInv = config.DCconservativeInv
        self.maxNestingDepthDC = 0

        # Options Access Assignment
        self.stableStatesOnly = config.stableStatesOnly

        self.conservativeAccess = config.conservativeAccess
        self.ignoreDeferedStates = config.ignoreDeferedStates

        self.maxagressiveAccess = config.maxagressiveAccess

        # Options Merging
        self.maxMergingIter = config.maxMergingIter

        # Run ProtoGen
        self._ProcessArch()

    def _ProcessArch(self):

        pheader("Caches")
        pdebug(list(self.cacheIds))

        pheader("Directories")
        pdebug(list(self.dirIds))

        # First process the caches
        for arch in self.cacheIds:
            talgo = time.time()
            pheader("Architecture: " + arch)

            stablestates = self.stableStates[arch]
            statesets = self._InputProcessing(arch, stablestates)
            traces = self._AssignStateSets(arch, statesets, stablestates)

            self._FindProgressMessages(statesets)
            self._FindHiddenProgessMessages(statesets)

            self.renamedMessages.update(self._ProcessRemoteRequests(statesets, traces))

            self._ProtoGenAlgorithm(statesets, stablestates, self.maxNestingDepthCC, self._CacheDefer)

            self._AssignAccess(statesets, stablestates)

            self._MergeStates(statesets)

            pdebug("Runtime: " + arch + " = " + str(time.time() - talgo))

            statedict = self._ExtractStatesFromSets(statesets)

            self._pTransitions(arch, statedict)

            self.cacheStateSets += list(statesets.values())

            self.archProtoGen.update({arch: statedict})
            pdebug("")

        for arch in self.dirIds:
            talgo = time.time()
            pheader("Architecture: " + arch)

            stablestates = self.stableStates[arch]
            statesets = self._InputProcessing(arch, stablestates)
            self._AssignStateSets(arch, statesets, stablestates)

            self._ProcessRequestsMessages(self.renamedMessages, statesets)
            self._CompleteTransitions(self.cacheStateSets, statesets)

            self._ProtoGenAlgorithm(statesets, stablestates, self.maxNestingDepthDC, self._DirectoryDefer)

            self._MergeStates(statesets)

            pdebug("Runtime: " + arch + " = " + str(time.time() - talgo))

            statedict = self._ExtractStatesFromSets(statesets)

            self._pTransitions(arch, statedict)

            self.archProtoGen.update({arch: statedict})
            pdebug("")

    def _InputProcessing(self, arch, stablestates):
        transitions = self.arch[arch]

        statenamelist, statetransmap = self._SortStates(transitions)
        states = self._CreateStates(statenamelist, statetransmap)
        self._UpdateTransitions(states, transitions)
        self._CheckDuplicateTransitions(states)
        return self._StateSetGeneration(states, stablestates)

    def _ProtoGenAlgorithm(self, statesets, stablestates, maxdepth, deferfunc):
        newstates = 1
        nestingdepth = 0
        while newstates and nestingdepth < maxdepth:
            newstates = self._GenerateTransientStates(statesets, stablestates, deferfunc)
            nestingdepth += 1

        self._AppendDefferedMessages(statesets, stablestates)

    ########################################################################################################################
    # PUBLIC FUNCTIONS
    ########################################################################################################################
    def getArchStates(self):
        return self.archProtoGen

    def getCacheStates(self):
        cachedict = {}
        for cache in self.cacheIds:
            cachedict.update({cache: self.archProtoGen[cache]})
        return cachedict

    def getDirStates(self):
        dirdict = {}
        for directory in self.dirIds:
            dirdict.update({directory: self.archProtoGen[directory]})
        return dirdict

    def getMessages(self):
        msglist = copy.copy(self.msg)

        replacemsg = []

        for message in msglist:
            if message in self.renamedMessages:
                replacemsg.append(message)
                for assignment in self.renamedMessages[message]:
                    msglist.append(assignment[1])

        return [msg for msg in msglist if msg not in replacemsg]

    def getRenamedMessages(self):
        return self.renamedMessages

    def testNonStalling(self):
        return self.nonstalling

    def getMaxNestingDepth(self):
        return 0

    def getDCconservativeInv(self):
        return self.DCconservativeInv

    ########################################################################################################################
    # DEBUG
    ########################################################################################################################

    def _pStates(self, statesets):
        states = self._ExtractStatesFromSets(statesets)
        statelist = []

        for statekey in sorted(states.keys()):
            statelist.append(states[statekey])

        ProtoCCTablePrinter().pstates(statelist)

    def _pTransitions(self, arch, statedict):
        transitions = self._pGetTransitions(statedict)
        pheader(arch + ": Total number of transitions: " + str(len(transitions)))
        ProtoCCTablePrinter().ptransitiontable(transitions)

    def _pGetTransitions(self, statedict):
        transitions = []
        for state in sorted(statedict.keys()):
            transitions += statedict[state].gettransitions()
        return transitions

    ########################################################################################################################
    # TRACE TREE
    ########################################################################################################################

    def _CreateTraceTree(self, state, stablestates):

        tracetree = ForkTree()

        basenode = tracetree.insertnode(NodeObj(state))

        nextlist = self._GetTransFinalstates([basenode], state.gettransitions())

        while nextlist:
            endnodes = []
            for nextnode in nextlist:
                endnodes += tracetree.appenddata(nextnode[1], nextnode[0])

            nextlist = []
            for node in endnodes:
                state = node.getdata().getstate()
                if not [stateid for stateid in stablestates if state.getstatename() == stateid]:
                    nextlist += self._GetTransFinalstates([node], state.gettransitions())

        return tracetree

    @staticmethod
    def _GetTransFinalstates(nodes, transitions):
        nextlist = []

        for node in nodes:
            state = node.getdata().getstate()
            nextstates = []

            for transition in transitions:
                finalstate = transition.getfinalstate()
                if finalstate != state:
                    nextstates.append(NodeObj(finalstate, transition))

            nextlist.append([node, nextstates])

        return nextlist

    ########################################################################################################################
    # MISC
    ########################################################################################################################

    def _ExtractStatesFromSets(self, statesets):
        statedict = {}
        for stateset in statesets:
            states = statesets[stateset].getstates()
            for state in states:
                statedict.update({state.getstatename(): state})
        return statedict

    def _GetStableStates(self, statesets):
        stablestates = []
        for stateset in statesets:
            stablestates.append(statesets[stateset].getstablestate())

        return stablestates

    ########################################################################################################################
    # 1) INPUT PROCESSING -- CC/DC
    ########################################################################################################################

    @staticmethod
    def _SortStates(transitions):
        statetransmap = {}
        statenamelist = {}
        startnames = []
        finalnames = []

        for transition in transitions:
            startstate = transition.getstartstate().getstatename()
            finalstate = transition.getfinalstate().getstatename()

            if startstate != finalstate:
                startnames.append(startstate)
                finalnames.append(finalstate)

            if startstate in statenamelist:
                statenamelist.update({startstate: statenamelist[startstate] + [transition.getstartstate()]})
            else:
                statenamelist.update({startstate: [transition.getstartstate()]})

            if finalstate in statenamelist:
                statenamelist.update({finalstate: statenamelist[finalstate] + [transition.getfinalstate()]})
            else:
                statenamelist.update({finalstate: [transition.getfinalstate()]})

            if startstate in statetransmap:
                statetransmap.update({startstate: statetransmap[startstate] + [transition]})
            else:
                statetransmap.update({startstate: [transition]})

        perror("Terminal state found in input description", set(startnames) == set(finalnames))

        return statenamelist, statetransmap

    def _CreateStates(self, statenamelist, statetransmap):
        states = {}
        for statename in statenamelist:
            states.update({statename: State(statename, self.access, self.evict)})
            states[statename].addtransitions(statetransmap[statename])
        return states

    @staticmethod
    def _UpdateTransitions(states, transitions):
        for transition in transitions:
            transition.setstartstate(states[transition.getstartstate().getstatename()])
            transition.setfinalstate(states[transition.getfinalstate().getstatename()])

    @staticmethod
    def _CheckDuplicateTransitions(states):
        for state in states:
            guards = []
            for transition in states[state].gettransitions():
                guard = transition.getguard() + "".join(transition.getcond())
                perror("Duplicated transitions in node " + state +
                       ", Guard: " + guard,
                       not any(guard == refguard for refguard in guards))
                guards.append(guard)

    ########################################################################################################################
    # 2) STATE SET GENERATION -- CC/DC
    ########################################################################################################################

    @staticmethod
    def _StateSetGeneration(states, stablestates):

        stateset = {}

        for stablestate in stablestates:
            state = states.get(stablestate, 0)
            cset = StateSet(stablestate, state)
            stateset.update({stablestate: cset})
            state.addendstateset(cset)

        return stateset

    ########################################################################################################################
    # 3) STATE SET ASSIGNMENT -- CC/DC
    ########################################################################################################################
    def _AssignStateSets(self, arch, statesets, stablestates):
        traces = []
        for stateset in statesets:
            settraces = self._CreateTraceTree(statesets[stateset].getstablestate(), stablestates).gettraces()
            if arch in self.cacheIds:
                self.CacheTraceAssignment(self.access + self.evict, settraces, statesets)
            elif arch in self.dirIds:
                self.DirectoryTraceAssignment(self.access + self.evict, settraces, statesets)
            else:
                perror('Unknown architecture', 0)

            traces += settraces
        return traces

    def CacheTraceAssignment(self, accessids, traces, statesets, exhaustive=1):

        self._BackwardSearch(accessids, traces, statesets, exhaustive)
        self._ForwardSearch(traces)

        return statesets

    def DirectoryTraceAssignment(self, accessids, traces, statesets, exhaustive=1):
        self._BackwardSearch(accessids, traces, statesets, exhaustive)

        return statesets

    def _BackwardSearch(self, accessids, traces, statesets, exhaustive):
        remoterequests = self._RemoteRequests(statesets)
        # Run backwards
        for trace in traces:
            # The length of the trace is startstate, n*transientstates, endstate
            # A trace of length 2 only encompasses start and endstate and can therefore be ignored
            if len(trace) > 2:

                startset = trace[-1].getstate().getstatesets()[0]
                endset = trace[0].getstate().getstatesets()[0]

                for ind in range(0, len(trace) - 1):
                    transition = trace[ind].gettransition()

                    guard = transition.getguard()
                    finalstate = transition.getfinalstate()

                    # Dependent on agression level different assignments
                    if [access for access in accessids if guard == access]:
                        startset.addstartstate(finalstate)

                        if exhaustive == 1:
                            endset.addendstate(finalstate)

                    else:
                        endset.addendstate(finalstate)

                        if [remoterequest for remoterequest in remoterequests if guard == remoterequest]:
                            endset = self._UpdateEndSet(guard, endset, statesets)

    def _ForwardSearch(self, traces):
        for trace in traces:
            if len(trace) > 2:
                startsets = [trace[-1].getstate().getstatesets()[0]]

                for ind in range(len(trace) - 2, 0, -1):
                    transition = trace[ind].gettransition()

                    guard = transition.getguard()
                    finalstate = transition.getfinalstate()

                    newset = self._SearchSetGuard(startsets, guard, finalstate)

                    if newset:
                        startsets = [newset]
                    else:
                        startsets = finalstate.getstatesets()

    @staticmethod
    def _SearchSetGuard(startsets, guard, finalstate):
        for startset in startsets:
            for remoterequest in startset.getstablestate().getremote():
                if guard == remoterequest.getguard():
                    newset = remoterequest.getfinalstate().getstatesets()[0]
                    newset.addstartstate(finalstate)
                    return newset
        return 0

    @staticmethod
    def _RemoteRequests(statesets):
        remoterequests = []
        for stateset in statesets:
            transitions = statesets[stateset].getstablestate().getremote()

            for transition in transitions:
                remoterequests.append(transition.getguard())

        return list(set(remoterequests))

    @staticmethod
    def _UpdateEndSet(guard, endset, statesets):
        for stateset in statesets:
            transitions = statesets[stateset].getstablestate().getremote()

            for transition in transitions:
                if transition.getguard() == guard and transition.getfinalstate() == endset.getstablestate():
                    return statesets[stateset]

        return endset

    ####################################################################################################################
    # AGGRESSIVE DEFER RESPONSE MESSAGES
    ####################################################################################################################
    def _FindProgressMessages(self, statesets):
        statedict = self._ExtractStatesFromSets(statesets)

        for state in statedict:
            if statedict[state].getstartstatesets():
                for transition in statedict[state].gettransitions():
                    if not transition.getfinalstate().getstartstatesets():
                        if not transition.getguard() in self.progressMessages:
                            self.progressMessages.append(transition.getguard())

    def _FindHiddenProgessMessages(self,statesets):
        statedict = self._ExtractStatesFromSets(statesets)

        for state in statedict:
            for transition in statedict[state].gettransitions():
                outmsgtypes = transition.getoutmsgtypes()
                for outmsg in outmsgtypes:
                    if outmsg in self.progressMessages and len(outmsgtypes) > 1:
                        for outmsgadd in outmsgtypes:
                            if outmsgadd not in self.progressMessages:
                                self.progressMessages.append(outmsgadd)
                    break

########################################################################################################################
# 4) PREPROCESSING
########################################################################################################################
    ####################################################################################################################
    # CACHE
    ####################################################################################################################

    # In every state all remote requests should be unique
    def _ProcessRemoteRequests(self, statesets, traces):
        # Get message identifiers
        messagesets = {}
        for stateset in statesets:
            messagesets.update(
                {statesets[stateset].getstablestate().getstatename():
                     set([transition.getguard() for transition in statesets[stateset].getstablestate().getremote()])})

        # Detect conflicts
        conflicts = []
        for refset in messagesets:
            for compset in messagesets:
                refentry = messagesets[refset]
                compentry = messagesets[compset]
                if refset != compset:
                    conflict = refentry.intersection(compentry)
                    if conflict:
                        entry = [{refset, compset}, conflict]
                        if entry not in conflicts:
                            conflicts.append(entry)

        # Get connectivity to avoid unnecessary renaming
        connectivity = self._GetTraceConnectivityPairs(traces)

        renamedmsg = {}

        # Resolve guard name conflicts
        for conflict in conflicts:
            if conflict[0] in connectivity:
                for messageid in conflict[1]:
                    rename = {messageid: []}
                    for setid in conflict[0]:
                        stateset = statesets[setid]
                        newmessageid = messageid + "_" + stateset.getstablestate().getstatename()

                        rename[messageid].append([setid, newmessageid])
                        states = stateset.getstates()
                        for state in states:
                            transition = state.gettransitionbyguard(messageid)
                            assert not isinstance(transition, list), "No support yet for transition list"
                            if transition:
                                transition.replaceguard(newmessageid)

                    renamedmsg.update(rename)

        pheader("Renamed Messages:")
        pdebug(renamedmsg)

        return renamedmsg

    def _GetTraceConnectivityPairs(self, traces):
        pairs = []
        for trace in traces:
            pair = {trace[-1].getstate().getstatename(), trace[0].getstate().getstatename()}
            if trace[0].gettransition().getinmsg() or trace[0].gettransition().getoutmsg():
                if pair not in pairs:
                    pairs.append(pair)
            else:
                if pair not in self.hiddenChangeStates:
                    self.hiddenChangeStates.append(pair)
        return pairs

    ####################################################################################################################
    # DIRECTORY
    ####################################################################################################################
    def _ProcessRequestsMessages(self, renamedmessages, statesets):
        for message in renamedmessages:
            curname = message
            for repentry in renamedmessages[message]:
                newname = repentry[1]
                stateset = repentry[0]

                if stateset not in statesets:
                    perror("Messages need to be renamed, but ProtoGen cannot determine dependencies at directory")

                for state in statesets[stateset].getstates():
                    transitions = state.gettransitions()

                    for transition in transitions:
                        transition.renameoutmsg(curname, newname)

########################################################################################################################
# 5) TRANSIENT STATE GENERATION
########################################################################################################################

    def _GenerateTransientStates(self, statesets, stablestates, deferfunc):

        newstates = []

        statedict = {}

        for stateset in statesets:
            statedict.update({stateset: copy.copy(statesets[stateset].getstates())})

        for stateset in statesets:
            stablestate = statesets[stateset].getstablestate()
            remotetrans = stablestate.getremote()

            for state in statedict[stateset]:

                for transition in remotetrans:

                    guard = transition.getguard()

                    existtrans = state.getmulttransitionsbyguard(guard)

                    if existtrans:
                        match = 0
                        for reftrans in existtrans:
                            if transition.getcond() == reftrans.getcond():
                                match = 1
                                break

                        if not match:
                            self._TransientStateInheritance(transition,
                                                            state,
                                                            statesets[stateset],
                                                            stablestates,
                                                            newstates,
                                                            deferfunc)

                    else:
                        self._TransientStateInheritance(transition,
                                                        state,
                                                        statesets[stateset],
                                                        stablestates,
                                                        newstates,
                                                        deferfunc)

        return newstates

    def _TransientStateInheritance(self, transition, state, stateset, stablestates, newstates, deferfunc):
        finalsets = transition.getfinalstate().getstatesets()

        # Test if stable state is startstate of current state
        if state in stateset.getstartstates():
            # Find path startstate to state
            guards = self._FindAccessTrace(state, stateset, stablestates)

            # if transition.getstartstate() == transition.getfinalstate():
            #     state.addtransitions(self._CopyModifyTransition(transition, state, state))
            # else:
            finalstate = self._SetGuardSearch(guards, finalsets)
            if finalstate:
                state.addtransitions(self._CopyModifyTransition(transition, state, finalstate))
            else:
                newstates.append(self._CopyModifyState(state, transition))
        else:
            if self.nonstalling:
                # Cache and directory dependent. Only if they have data
                if transition.getstartstate() == transition.getfinalstate() and state in stateset.getendstates():
                    newtrans = self._CopyModifyTransition(transition, state, state)
                    defermsg = deferfunc(transition, newtrans)
                    if defermsg:
                        newstates.append(self._GenerateState(state, transition, stablestates, deferfunc))
                    else:
                        state.addtransitions(newtrans)
                else:
                    newstates.append(self._GenerateState(state, transition, stablestates, deferfunc))

    ####################################################################################################################
    # COMMON
    ####################################################################################################################

    @staticmethod
    def _CopyModifyTransition(transition, startstate, finalstate):
        newtrans = copy.copy(transition)
        newtrans.setstartstate(startstate)
        newtrans.setfinalstate(finalstate)
        return newtrans

    ####################################################################################################################
    # STARTSTATE INHERITANCE
    ####################################################################################################################

    def _FindAccessTrace(self, state, stateset, stablestates):
        traces = self._CreateTraceTree(stateset.getstablestate(), stablestates).gettraces()
        for trace in traces:
            guards = []
            for ind in range(len(trace) - 2, 0, -1):
                guards.append(trace[ind].gettransition().getguard())
                if trace[ind].getstate() == state:
                    return guards
        return 0

    def _SetGuardSearch(self, guards, finalsets):
        for finalset in finalsets:
            state = finalset.getstablestate()
            found = 0
            ind = 0
            while ind < len(guards):
                transition = state.gettransitionbyguard(guards[ind])

                if isinstance(transition, list):
                    ProtoCCTablePrinter.ptransitions(transition)
                    assert 0, "No support yet for transition list"

                if transition:
                    state = transition.getfinalstate()
                    if ind == len(guards) - 1:
                        found = 1
                    ind += 1
                else:
                    ind = len(guards)

            if found:
                if set(state.getstatesets()).issuperset(set(finalsets)):
                    return state
            else:
                return 0
        return 0

    def _CopyModifyState(self, startstate, transition):
        newstate = State(startstate.getstatename() + "_" + transition.getguard(), self.access, self.evict)
        for datatrans in startstate.getdataack():
            newtrans = copy.copy(datatrans)
            newtrans.setstartstate(newstate)
            newstate.addtransitions(newtrans)

        for startset in transition.getfinalstate().getstatesets():
            startset.addstartstate(newstate)

        for endset in startstate.getendstatesets():
            endset.addendstate(newstate)

        # Create vertice
        startstate.addtransitions(self._CopyModifyTransition(transition, startstate, newstate))

        return newstate

    ####################################################################################################################
    # FINALSTATE INHERITANCE
    ####################################################################################################################

    def _GenerateState(self, startstate, transition, stablestates, deferfunc):
        newstates = []
        finalsets = transition.getfinalstate().getstatesets()
        perror("Size of finalstate set exceeds 1", len(finalsets) == 1)

        newtrans = self._CopyModifyTransition(transition, startstate, startstate)

        defermsg = deferfunc(transition, newtrans)

        newstate = self._CopyState(startstate,
                                   transition.getguard(),
                                   finalsets[0],
                                   stablestates,
                                   newstates,
                                   defermsg)

        newtrans.setfinalstate(newstate)
        startstate.addremotemiss(newtrans)

        return newstate

    def _CopyState(self, startstate, guard, stateset, stablestates, newstates, defermsg=0):
        newstate = State(self._CheckStateName(startstate.getstatename() + "__"
                                              + guard + "_"
                                              + stateset.getstablestate().getstatename(),
                                              stateset),
                         self.access, self.evict)

        newstates.append(newstate)
        stateset.addendstate(newstate)

        newstate.adddefermessage(startstate.getdefermessages())

        if defermsg:
            newstate.adddefermessage(defermsg)

        for transition in startstate.getdataack():
            newtrans = copy.copy(transition)
            newtrans.setoutmsg(copy.copy(transition.getoutmsg()))
            newtrans.setstartstate(newstate)

            if transition.getstartstate() == transition.getfinalstate():
                newtrans.setfinalstate(newstate)
            else:
                finalstate = [finalstate for finalstate in stablestates
                              if finalstate == newtrans.getfinalstate().getstatename()]
                if finalstate:
                    newtrans.setfinalstate(stateset.getstablestate())

                else:
                    finalstate = self._CopyState(newtrans.getfinalstate(),
                                                 guard,
                                                 stateset,
                                                 stablestates,
                                                 newstates,
                                                 defermsg)
                    newtrans.setfinalstate(finalstate)
            newstate.addtransitions(newtrans)
        return newstate

    def _CheckStateName(self, name, stateset):
        for state in stateset.getstates():
            if state.getstatename() == name:
                return name + "_"
        return name

    ####################################################################################################################
    # CACHE SPECIFIC FUNCTION
    ####################################################################################################################
    def _CacheDefer(self, transition, newtrans):
        if self.CCconservativeInv:
            return newtrans.deferoutmsg()
        else:
            return newtrans.deferoutmsg(self.progressMessages)

    def _DirectoryDefer(self, transition, newtrans):
        if self.DCconservativeInv:
            return newtrans.deferoutmsg()
        else:
            res = self._AccessDetection(self.cacheStateSets)

            evictmsgs = []
            for refval in res[1].values():
                evictmsgs += refval

            if not [msgtype for msgtype in evictmsgs if msgtype == transition.getguard()]:
                return newtrans.deferoutmsg(self.progressMessages)
        return 0

    ########################################################################################################################
    # 6) APPEND DEFERRED MESSAGES
    ########################################################################################################################

    def _AppendDefferedMessages(self, statesets, stablestates):
        statedict = self._ExtractStatesFromSets(statesets)

        for state in statedict:
            state = statedict[state]

            deferedmsgs = state.getdefermessages()

            if deferedmsgs:
                for transition in state.getdataack():
                    stablestate = [stablestate for stablestate in stablestates
                                   if stablestate == transition.getfinalstate().getstatename()]

                    if stablestate:
                        for deferredmsg in deferedmsgs:
                            transition.addoutmsg(deferredmsg)

    ########################################################################################################################
    # 7) TRANSIENT STATE MEMORY ACCESS
    ########################################################################################################################

    def _AssignAccess(self, statesets, stablestates):
        if not self.stableStatesOnly:

            accessdict = {}

            for stateset in statesets.values():

                traces = self._CreateTraceTree(stateset.getstablestate(), stablestates).gettraces()

                for trace in traces:
                    hasdata = 0
                    lostdata = 0
                    startaccess = trace[len(trace) - 1].getstate().getaccesshit()
                    if len(startaccess):
                        hasdata = 1
                    finalaccess = trace[0].getstate().getaccesshit()

                    for ind in range(len(trace) - 2, 0, -1):
                        state = trace[ind].getstate()

                        startstatesets = state.getstartstatesets()
                        endstatesets = state.getendstatesets()

                        prevdata = hasdata
                        hasdata = self._DetermineHasData(hasdata,
                                                         trace[ind].gettransition(),
                                                         startstatesets,
                                                         endstatesets)

                        # Determine if there was a downgrad once
                        if prevdata and not hasdata:
                            lostdata = 1

                        # Options
                        if self.conservativeAccess and hasdata and not lostdata:
                            if not self.ignoreDeferedStates or not state.getdefermessages():
                                self._ConservativeAccess(accessdict, state, startaccess, finalaccess)
                        # else:

            for state in accessdict:
                access = accessdict[state]
                for entry in access[0]:
                    # If state has not data, there cannot be any acccess, even if possible by
                    if access[1]:
                        if not state.gettransitionbyguard(entry.getguard()):
                            state.addtransitions(self._CopyModifyTransition(entry, state, state))

    def _ConservativeAccess(self, accessdict, state, startaccess, finalaccess):
        if len(startaccess) < len(finalaccess):
            newaccess = startaccess
        else:
            newaccess = finalaccess

        if state in accessdict:
            curaccess = accessdict[state][0]
            curhasdata = accessdict[state][1]

            if curhasdata:
                if len(curaccess) < len(newaccess):
                    accessdict.update({state: [newaccess, 1]})
        else:
            accessdict.update({state: [newaccess, 1]})

    def _DetermineHasData(self, hasdata, transition, startstatesets, endstatesets):
        if startstatesets:
            minaccess = self._DetermineEndMinAccess(startstatesets)

            if not minaccess:
                hasdata = 0
        else:
            endminaccess = self._DetermineEndMinAccess(endstatesets)
            if endminaccess and not hasdata:
                inobj = transition.getinmsg()
                if isinstance(inobj, str):
                    return hasdata
                if inobj.getmsgobj() in self.datamsgs:
                    hasdata = 1

        return hasdata

    @staticmethod
    def _DetermineEndMinAccess(statesets):
        minaccessset = []
        for stateset in statesets:
            stablestate = stateset.getstablestate()
            access = stablestate.getaccesshit()

            if access:
                if not minaccessset:
                    minaccessset = access

                if len(access) < len(minaccessset):
                    minaccessset = access

        return minaccessset

    # def _InheritIntersectAccess(self, statesets):

    def _InheritAccessFromSet(self, statesets):
        states = self._ExtractStatesFromSets(statesets)
        states = list(states.values())
        stablestates = self._GetStableStates(statesets)

        for state in stablestates:
            states.remove(state)

        for state in states:
            startstablestates = state.getstartstatesets()
            endstablestates = state.getendstatesets()

            minaccessset = []
            for stateset in endstablestates:
                stablestate = stateset.getstablestate()
                access = stablestate.getaccesshit()

                if access:
                    if not minaccessset:
                        minaccessset = access

                    if len(access) < len(minaccessset):
                        minaccessset = access

            for stateset in startstablestates:
                stablestate = stateset.getstablestate()
                access = stablestate.getaccesshit()

                if len(access) < len(minaccessset):
                    minaccessset = access

            if minaccessset:
                for access in minaccessset:
                    state.addtransitions(self._CopyModifyTransition(access, state, state))

                # While deferred response access is not changed..., keep memory accesses

    ########################################################################################################################
    # 8) STATE MERGING
    ########################################################################################################################

    def _MergeStates(self, statesets):
        found = 1
        itercnt = 0

        while found and itercnt < self.maxMergingIter:
            itercnt += 1
            found = 0
            setkeys = self._GetSetSeq(statesets)

            for stateset in setkeys:
                defercluster = self._ClusterStatesDeferred(statesets[stateset].getstates())

                for deferkey in sorted(defercluster.keys()):
                    contextcluster = self._ClusterTransitionContext(defercluster[deferkey])

                    for contextkey in sorted(contextcluster.keys()):
                        accesscluster = self._ClusterAccessMerge(contextcluster[contextkey])

                        for accesskey in sorted(accesscluster.keys()):
                            dependencemap = self._ClusterIndependent(accesscluster[accesskey])

                            if len(dependencemap) > 1:
                                transitionmap = self._ClusterTransitions(dependencemap)
                                if (len(transition) > 1 for transition in transitionmap.values()) \
                                        and len(transitionmap):
                                    # To test if states that shall be merged still exist is important
                                    # Greedy algorithm, a state might be mergeable with multiple different states
                                    # After it was merged one, it dissappears and is dead afterwards, therefore any
                                    # possible remaining merging must be deleted
                                    if self._TestStateExistInSet(dependencemap, statesets[stateset]):
                                        self._MergeGivenStates(dependencemap, transitionmap, statesets)
                                        found = 1

    def _GetSetSeq(self, statesets):
        statesetlist = []
        for stateset in statesets.values():
            statesetlist.append(stateset.getstablestate())

        statesetlist.sort(key=lambda x: (len(x.getaccesshit()), x.getstatename()))

        return [state.getstatename() for state in statesetlist]

    def _MergeGivenStates(self, mergestates, transitionmap, statesets):
        mergestates.sort(key=lambda x: x.getstatename())
        # mergestates.sort(key=lambda x: len(x.getstatename()))

        # Make new state
        newstate = State(mergestates[0].getstatename(), self.access, self.evict)

        for transition in transitionmap.values():
            newstate.addtransitions(transition[0])

        # Explore context
        startstatesets = []
        endstatesets = []

        for state in mergestates:
            startstatesets += state.getstartstatesets()
            endstatesets += state.getendstatesets()

        startstatesets = list(set(startstatesets))
        endstatesets = list(set(endstatesets))

        # Remove old states from all state sets
        for stateset in statesets.values():
            stateset.removestates(mergestates)

        # Now add new state to sets
        for stateset in startstatesets:
            stateset.addstartstate(newstate)

        for stateset in endstatesets:
            stateset.addendstate(newstate)

        # Update links
        for stateset in statesets.values():
            for state in stateset.getstates():
                for replacestate in mergestates:
                    state.replaceremotestate(replacestate, newstate)

    @staticmethod
    def _TestStateExistInSet(states, stateset):
        for state in states:
            if not stateset.teststateexist(state):
                return 0
        return 1

    ####################################################################################################################
    # CLUSTER STATES
    ####################################################################################################################

    def _ClusterStatesDeferred(self, states):
        ordereddeferred = 1

        msgmap = {}

        for state in states:
            defermsgs = state.getdefermessages()

            detectset = []
            for defermsg in defermsgs:
                detectset.append(defermsg.getmsgtype())

            detectkey = '$' + ''.join(detectset if ordereddeferred else detectset.sort())

            entry = msgmap.get(detectkey, 0)
            if entry:
                if state not in entry:
                    entry.append(state)
            else:
                msgmap.update({detectkey: [state]})

        return self._RemoveSingleEntries(msgmap)

    def _ClusterTransitionContext(self, defercluster):
        msgcontextmap = {}

        for state in defercluster:
            for transition in state.getdataack():
                cond = transition.getcond()[0] if transition.getcond() else "_"
                inmsg = transition.getinmsg() if isinstance(transition.getinmsg(), str) else \
                    transition.getinmsg().getmsgtype()

                identkey = inmsg + cond + transition.getfinalstate().getstatename()

                entry = msgcontextmap.get(identkey, 0)
                if entry:
                    entry.append(state)
                else:
                    msgcontextmap.update({identkey: [state]})

        return self._RemoveSingleEntries(msgcontextmap)

    def _ClusterAccessMerge(self, contextcluster):
        accessmap = {}
        for state in contextcluster:
            accesskey = "$"
            for access in state.getaccesshit():
                accesskey += access.getguard()

            entry = accessmap.get(accesskey, 0)
            if entry:
                entry.append(state)
            else:
                accessmap.update({accesskey: [state]})

        return self._RemoveSingleEntries(accessmap)

    def _ClusterIndependent(self, accesscluster):
        dependencemap = {}

        for state in accesscluster:
            for transition in state.gettransitions():
                dependencemap.update({state: []})
                finalstate = transition.getfinalstate()
                if finalstate in accesscluster and finalstate != transition.getstartstate():
                    dependencemap[state].append(finalstate)

        independentlist = []
        keys = list(dependencemap.keys())
        keys.sort(key=lambda x: x.getstatename())

        for entry in keys:
            if not len(dependencemap[entry]):
                independentlist.append(entry)

        return independentlist

    def _ClusterTransitions(self, accesscluster):
        transitionmap = {}

        for state in accesscluster:
            for transition in state.getremote() + state.getdataack():
                cond = transition.getcond()[0] if transition.getcond() else "_"
                inmsg = transition.getinmsg() if isinstance(transition.getinmsg(), str) else \
                    transition.getinmsg().getmsgtype()

                self._AppendTransitionMap(transitionmap, transition, inmsg + cond)

        for transition in state.getaccess() + state.getevict():
            identkey = transition.getaccess()

            if transition.getstartstate() == transition.getfinalstate():
                identkey += "_l"

            self._AppendTransitionMap(transitionmap, transition, identkey)

        transitionmap = self._ClusterNonAmbigousTrans(transitionmap)

        return transitionmap

    @staticmethod
    def _AppendTransitionMap(transitionmap, transition, identkey):
        entry = transitionmap.get(identkey, 0)
        if entry:
            entry.append(transition)
        else:
            transitionmap.update({identkey: [transition]})

    @staticmethod
    def _ClusterNonAmbigousTrans(transitionmap):
        match = 1

        for transitionkey in sorted(transitionmap.keys()):
            finalstates = []
            for transition in transitionmap[transitionkey]:
                finalstate = transition.getfinalstate()
                if transition.getstartstate() != finalstate:
                    finalstates.append(finalstate)

            if len(list(set(finalstates))) > 1:
                match = 0
                break

        if match == 0:
            return {}

        return transitionmap

    @staticmethod
    def _RemoveSingleEntries(statedict):
        removeguards = []
        for guard in statedict:
            if len(statedict[guard]) == 1:
                removeguards.append(guard)

        for guard in removeguards:
            del statedict[guard]

        return statedict

    ########################################################################################################################
    # 9) DIR MEMORY ACCESS
    ########################################################################################################################
    def _CompleteTransitions(self, cachestatesets, dirstatesets):
        res = self._AccessDetection(cachestatesets)
        self._AccessCompletion(dirstatesets, res[0])
        self._EvictCompletion(dirstatesets, res[1])

    def _AccessDetection(self, cachestatesets):
        accessmap = {}

        [accessmap.update({access: []}) for access in self.access + self.evict]

        states = []

        for stateset in cachestatesets:
            states += stateset.getstates()

        for state in states:

            for transition in state.getaccessmiss() + state.getevictmiss():
                accesslist = accessmap.get(transition.getguard(), 0)

                if isinstance(accesslist, list):
                    outmsgs = transition.getoutmsg()
                    for outmsg in outmsgs:
                        accesslist.append(outmsg.getmsgtype())

        # seperate evict accesses
        evictaccess = {}

        for evict in self.evict:
            evictaccess.update({evict: accessmap[evict]})
            del accessmap[evict]

        return [accessmap, evictaccess]

    def _AccessCompletion(self, dirstatesets, accessmap):
        dirstates = self._ExtractStatesFromSets(dirstatesets)
        # Only multiple messages related to same access must be considered
        for access in accessmap:
            if len(accessmap[access]) > 1:
                msgtypes = accessmap[access]

                for state in dirstates.values():
                    foundmap = {}
                    misskeys = []
                    for msgtype in msgtypes:
                        transition = state.getmulttransitionsbyguard(msgtype)
                        if transition:
                            foundmap.update({msgtype: transition})
                        else:
                            misskeys.append(msgtype)

                    if len(foundmap):
                        for misskey in misskeys:
                            transitions = foundmap[next(iter(foundmap))]

                            for transition in transitions:
                                newtrans = copy.copy(transition)
                                newtrans.setinmsg(Message(misskey))
                                state.addtransitions(newtrans)

    def _EvictCompletion(self, dirstatesets, evictaccess):
        dirstates = self._ExtractStatesFromSets(dirstatesets)
        # The possible evictions need to be present in every state due to race conditions
        evictmap = {}
        evictmsgstatemap = {}

        for evict in evictaccess:
            for state in dirstates.values():
                for evictmsg in evictaccess[evict]:
                    transitions = state.getmulttransitionsbyguard(evictmsg)
                    if transitions:
                        for transition in transitions:
                            transarray = evictmap.get(evictmsg, 0)
                            if transarray:
                                if transition not in transarray:
                                    transarray.append(transition)
                            else:
                                evictmap.update({evictmsg: [transition]})
                                evictmsgstatemap.update({state.getstatename(): evictmsg})

        # Handle cache states that are indistinguishable by directory such as E and M
        stateevictmap = {}

        for stateset in dirstatesets:
            state = dirstatesets[stateset].getstablestate().getstatename()
            for pair in self.hiddenChangeStates:
                if state in pair:
                    for entry in pair:
                        if entry != state:
                            if entry in stateevictmap:
                                stateevictmap[entry].append(evictmap[state])
                            else:
                                stateevictmap.update({entry: [evictmsgstatemap[state]]})

        # Evictions only need to be possible in stable states
        # Transient states automatically inherit from stable states
        for stateset in dirstatesets:
            state = dirstatesets[stateset].getstablestate()
            for evictaccess in evictmap:
                existtrans = state.getmulttransitionsbyguard(evictaccess)
                evicttrans = evictmap[evictaccess]

                if not existtrans:
                    hiddenstatetrans = 0
                    if state.getstatename() in stateevictmap:
                        if evictaccess in stateevictmap[state.getstatename()]:
                            hiddenstatetrans = 1

                    if hiddenstatetrans:
                        for newevicttrans in evicttrans:
                            if newevicttrans.getstartstate() == newevicttrans.getfinalstate():
                                state.addtransitions(self._CopyModifyTransition(newevicttrans, state, state))
                            else:
                                state.addtransitions(self._CopyModifyTransition(newevicttrans,
                                                                                state,
                                                                                newevicttrans.getfinalstate()))
                    else:
                        for newevicttrans in evicttrans:
                            state.addtransitions(self._CopyModifyTransition(newevicttrans, state, state))
