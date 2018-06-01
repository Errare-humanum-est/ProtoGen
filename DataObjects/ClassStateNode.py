class StateNode:

    def __init__(self, name, protocacc):
        assert isinstance(protocacc, list)
        self.accesses = protocacc

        assert isinstance(name, str)

        self.state = name

    def testaccess(self, access):
        if access in self.accesses:
            return 1
        return 0

########################################################################################################################
# STATE ID
########################################################################################################################

    def setstatename(self, name):
        assert isinstance(name, str)
        self.state = name

    def getstatename(self):
        return self.state

########################################################################################################################
# DEBUG
########################################################################################################################

    def pstate(self):
        return self.state

    def pbase(self):
        return "State:: Name:" + self.state
