class Message:
    def __init__(self, name, obj="", src="", dest="", payload="", vc="", msgobj=0):

        assert isinstance(name, str)
        assert isinstance(src, str)
        assert isinstance(dest, str)
        assert isinstance(vc, str)

        self.type = name
        self.src = src
        self.dest = dest
        self.vc = vc
        self.obj = obj
        self.msgobj = msgobj

        # payload depends on message type
        if isinstance(payload, list) and all(isinstance(msg, str) for msg in payload):
            self.payload = payload
        elif isinstance(payload, str):
            self.payload = [payload]
        else:
            assert 0

    def setmsgtype(self, name):
        self.type = name

    def getmsgtype(self):
        return self.type

    def getmsgobj(self):
        return self.obj

    def setvc(self, vc):
        self.vc = vc

    def getvc(self):
        return self.vc

    def getmsgobj(self):
        return self.msgobj
