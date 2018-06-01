from DataObjects.ClassState import State
from DataObjects.ClassTransition import Transition


class NodeObj:

    def __init__(self, state, transition=0):
        assert isinstance(state, State)
        assert isinstance(transition, (Transition, int))
        self.state = state
        self.transition = transition

    def getstate(self):
        return self.state

    def gettransition(self):
        return self.transition
