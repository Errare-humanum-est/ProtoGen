class ProtoConfig:

    def __init__(self):
        # Options State Generation
        # Option merges states based on their names
        self.enableStateNameMerging = 0

        # Options Cache
        self.CCconservativeInv = 0
        self.nonstalling = 1

        self.maxNestingDepthCC = 3

        # Options Directory
        self.DCconservativeInv = 0

        # Options Access Assignment
        self.stableStatesOnly = 0

        self.conservativeAccess = 1
        self.ignoreDeferedStates = 0

        self.maxagressiveAccess = 0

        # Options Merging
        self.maxMergingIter = 10


