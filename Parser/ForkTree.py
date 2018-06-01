class Node:
    def __init__(self, predecessor, data):
        self.predecessor = predecessor
        self.data = data
        self.sucessor = []

    def getpredecessor(self):
        return self.predecessor

    def setpredecessor(self, predecessor):
        self.predecessor = predecessor
        return predecessor

    def addsuccessor(self, sucessor):
        if isinstance(sucessor, Node):
            self.sucessor.append(sucessor)
            return 1
        return 0

    def getsuccessors(self):
        return self.sucessor

    def testsuccessor(self):
        if self.sucessor:
            return 1
        return 0

    def removesucessor(self, successor):
        if self.sucessor:
            return self.sucessor.remove(successor)
        else:
            return 0

    def getdata(self):
        return self.data


class ForkTree:

    def __init__(self):
        self.Tree = []
        self.curNode = 0

    def gettreenodecontent(self):
        ret = []
        for node in self.Tree:
            ret.append(node.getdata())
        return ret

    def getcurnode(self):
        return self.curNode

    def getcurnodepre(self):
        return self.curNode.getpredecessor()

    def getbasenode(self):
        for indsel in range(0, len(self.Tree)):
            found = 0
            predecessor = self.Tree[indsel].getpredecessor()
            for indent in range(0, len(self.Tree)):
                if indsel != indent and predecessor == self.Tree[indent]:
                    found = 1
                    break

            if not found:
                return predecessor
        return 0

    def popcurnode(self):
        self.curNode = self.getcurnodepre()
        return self.curNode

    def popdelcurnode(self, curnode):
        prenode = self.popcurnode()
        self.Tree.remove(curnode)
        if prenode:
            prenode.removesucessor(curnode)
        return prenode

    def insertnode(self, data, prenode=0):
        if not prenode:
            node = self.curNode
        else:
            node = prenode

        newnode = Node(node, data)
        self.Tree.append(newnode)

        if node and self.curNode:
            self.curNode.addsuccessor(newnode)

        self.curNode = newnode

        return newnode

    def appendnodes(self, nodes, predecessor):
        if predecessor and predecessor not in self.Tree:
            return 0
        for entry in nodes:
            entry.setpredecessor(predecessor)
            self.Tree.append(entry)
            if predecessor:
                predecessor.addsuccessor(entry)
            self.curNode = entry
        return self.curNode

    def appenddata(self, data, predecessor):
        nodes = []
        if predecessor and predecessor not in self.Tree:
            return 0
        for entry in data:
            node = Node(predecessor, entry)
            nodes.append(node)
            self.Tree.append(node)
            if predecessor:
                predecessor.addsuccessor(node)

        return nodes

    def getpredecessor(self):
        self.curNode = self.curNode.getpredecessor()
        return self.curNode

    def getnodeandchilds(self):
        childs = self.curNode.getsuccessors()
        nodes = [self.curNode]
        while childs:
            newchilds = []
            for entry in childs:
                nodes.append(entry)
                newchilds += entry.getsuccessors()

            childs = newchilds

        return nodes

    def getchildnodes(self, curnode):
        children = [curnode]
        successors = curnode.getsuccessors()

        while successors:
            nextsuc = []
            for entry in successors:
                children.append(entry)
                nextsuc += entry.getsuccessors()

            if not nextsuc:
                return children

            successors = nextsuc
        return children

    def getendnodes(self):
        endnodes = []
        for entry in self.Tree:
            if not entry.testsuccessor():
                endnodes.append(entry)

        return endnodes

    def gettraces(self):
        traces = []
        endnodes = self.getendnodes()

        for endnode in endnodes:
            node = endnode
            trace = [node.getdata()]

            while node.getpredecessor():
                node = node.getpredecessor()
                trace.append(node.getdata())

            traces.append(trace)

        return traces

    def treetoarray(self):
        # Get end nodes
        endnodes = []
        for entry in self.Tree:
            if entry.testsuccessor():
                endnodes.append(entry)

        ret = []
        for entry in endnodes:
            curcond = []
            curcond += entry.getdata()
            predecessor = entry.getpredecessor()

            # Search backwards for predecessor
            while predecessor:
                curcond += predecessor.getdata()
                predecessor = predecessor.getpredecessor()

            ret.append(curcond)

    # Print all generated transactions
    def treetolist(self):
        ret = []
        for entry in self.Tree:
            ret.append(entry.getdata())

        return ret







