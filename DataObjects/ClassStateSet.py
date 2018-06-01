from DataObjects.ClassState import State

class StateSet:
    def __init__(self, name, state):

        assert isinstance(name, str)
        self.state = name

        assert isinstance(state, State)

        self.state = name
        self.stablestate = state

        self.states = [state]
        self.startstates = []
        self.endstates = [state]


########################################################################################################################
# STABLE STATE
########################################################################################################################

    def setstatename(self, name):
        assert isinstance(name, str)
        self.state = name

    def getstablestate(self):
        return self.stablestate

    def addstartstate(self, state):
        if state not in self.states:
            self.states.append(state)
            self.startstates.append(state)
            state.addstartstateset(self)
            return self.states
        return 0

    def addendstate(self, state):
        if state not in self.states:
            self.states.append(state)
            self.endstates.append(state)
            state.addendstateset(self)
            return self.states
        return 0

    def getstates(self):
        return self.states

    def getstartstates(self):
        return self.startstates

    def getendstates(self):
        return self.endstates

    def removestates(self, states):
        for state in states:
            if state in self.states:
                self.states.remove(state)
            if state in self.startstates:
                self.startstates.remove(state)
            if state in self.endstates:
                self.endstates.remove(state)

    def teststateexist(self, state):
        if state in self.states:
            return 1
        return 0