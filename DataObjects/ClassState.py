class State:

    def __init__(self, name, access=0, evict=0):

        if isinstance(access, list):
            self.access = access
        elif isinstance(access, str):
            self.access = [access]
        else:
            self.access = []

        if isinstance(evict, list):
            self.evict = evict
        elif isinstance(evict, str):
            self.evict = [evict]
        else:
            self.evict = []

        assert isinstance(name, str)
        self.state = name

        self.setTrans = []

        self.accessMiss = []
        self.accessHit = []

        self.evictMiss = []
        self.evictHit = []

        self.remoteMiss = []
        self.remoteHit = []
        self.dataAck = []

        self.startstateSets = []
        self.endstateSets = []

        self.deferredRespMsg = []

########################################################################################################################
# STATE ID
########################################################################################################################

    def setstatename(self, name):
        assert isinstance(name, str)
        self.state = name

    def getstatename(self):
        return self.state

########################################################################################################################
# STATE TRANSITION
########################################################################################################################

    def addtransitions(self, transitions):
        if isinstance(transitions, list):
            transitionlist = transitions
        else:
            transitionlist = [transitions]

        self.setTrans += transitionlist
        self.classifytransitions(transitionlist)
        return self.setTrans

    def addremotemiss(self, transition):
        self.setTrans.append(transition)
        self.remoteMiss.append(transition)

    def gettransitions(self):
        return self.setTrans

    def classifytransitions(self, transitions):
        for transition in transitions:
            startstateid = transition.getstartstate().getstatename()
            finalstateid = transition.getfinalstate().getstatename()

            if transition.getaccess():
                if [access for access in self.access if transition.getaccess() == access]:
                    if not transition.getoutmsg():              # startstateid == finalstateid or
                        self.accessHit.append(transition)
                    else:
                        self.accessMiss.append(transition)
                else:
                    if startstateid == finalstateid:
                        self.evictHit.append(transition)
                    else:
                        self.evictMiss.append(transition)
            else:
                # if startstateid == finalstateid:
                #     self.remoteHit.append(transition)
                # else:
                if transition.getoutmsg():
                    self.remoteMiss.append(transition)
                else:
                    self.dataAck.append(transition)

    ####################################################################################################################
    # TRANSITION TESTING
    ####################################################################################################################

    def getaccess(self):
        return self.accessHit + self.accessMiss

    def getaccesshit(self):
        return self.accessHit

    def getaccessmiss(self):
        return self.accessMiss

    def getevict(self):
        return self.evictHit + self.evictMiss

    def getevictmiss(self):
        return self.evictMiss

    def getremote(self):
        return self.remoteHit + self.remoteMiss

    def getdataack(self):
        return self.dataAck


    ####################################################################################################################
    # PROTOGEN FUNCTIONS
    ####################################################################################################################

    def gettransitionbyguard(self, guard):
        for transition in self.setTrans:
            if transition.getguard() == guard:
                return transition
        return 0
        # rettransitions = []
        # for transition in self.setTrans:
        #     if transition.getguard() == guard:
        #         rettransitions.append(transition)
        #
        # if rettransitions:
        #     if len(rettransitions) == 1:
        #         # Default cache case
        #         # Theory: Multiple transitions by same guard possible for directory depending on interal state
        #         return rettransitions[0]
        #     else:
        #         # multiple transitions by same guard possible for directory depending on interal state
        #         return rettransitions
        # else:
        #     return 0

    def getmulttransitionsbyguard(self, guard):
        rettransitions = []
        for transition in self.setTrans:
            if transition.getguard() == guard:
                rettransitions.append(transition)

        if rettransitions:
            return rettransitions
        else:
            return 0

    def replaceremotestate(self, oldremotestate, newremotestate):
        for transition in self.setTrans:
            startstate = transition.getstartstate()
            finalstate = transition.getfinalstate()

            if startstate == oldremotestate:
                transition.setstartstate(newremotestate)

            if finalstate == oldremotestate:
                transition.setfinalstate(newremotestate)

########################################################################################################################
# STATE SET
########################################################################################################################
    def addstartstateset(self, state):
        if isinstance(state, list):
            states = state
        else:
            states = [state]

        for entry in states:
            if entry not in self.startstateSets:
                self.startstateSets.append(entry)

        return self.startstateSets

    def addendstateset(self, state):
        if isinstance(state, list):
            states = state
        else:
            states = [state]

        for entry in states:
            if entry not in self.endstateSets:
                self.endstateSets.append(entry)

        return self.endstateSets

    def getstatesets(self):
        return self.startstateSets + self.endstateSets

    def getstartstatesets(self):
        return self.startstateSets

    def getendstatesets(self):
        return self.endstateSets

    def removestateset(self, stateset):
        if stateset in self.startstateSets:
            self.startstateSets.remove(stateset)
        if stateset in self.endstateSets:
            self.endstateSets.remove(stateset)

########################################################################################################################
# PENDING MESSAGES
########################################################################################################################

    def getdefermessages(self):
        return self.deferredRespMsg

    def adddefermessage(self, message):
        if isinstance(message, list):
            self.deferredRespMsg += message
        else:
            self.deferredRespMsg.append(message)

########################################################################################################################
# POST CLASSIFICATION FUNCTIONS
########################################################################################################################

    def testexclusive(self):
        for transition in self.accessHit:
            if transition.getaccess() == self.access[1]:
                return 1
        return 0

    def getnraccess(self):
        return len(self.accessMiss) + len(self.accessHit)

    def getnrremote(self):
        return len(self.remoteMiss) + len(self.remoteHit)

########################################################################################################################
# DEBUG
########################################################################################################################

    def pstate(self):
        return self.state

    def pbase(self):
        return "State:: Name:" + self.state + "  *Access: " + str(self.access)
