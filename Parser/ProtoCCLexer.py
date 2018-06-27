# $ANTLR 3.5.2 /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g 2018-06-27 16:26:45

import sys
from antlr3 import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EOF=-1
T__87=87
T__88=88
T__89=89
T__90=90
T__91=91
T__92=92
T__93=93
T__94=94
T__95=95
T__96=96
T__97=97
T__98=98
T__99=99
T__100=100
T__101=101
T__102=102
T__103=103
ACCESS=4
ARCH=5
ARCH_=6
ARRAY=7
ARRAY_=8
ASSIGN_=9
AWAIT=10
AWAIT_=11
BOOL=12
BOOLID=13
BOOL_=14
BREAK=15
BREAK_=16
CACHE=17
CACHE_=18
CBRACE=19
CCBRACE=20
CEBRACE=21
COMMA=22
COMMENT=23
COND_=24
CONSTANT=25
CONSTANT_=26
DATA=27
DATA_=28
DDOT=29
DIR=30
DIR_=31
DOT=32
ELEMENT_=33
ELSE=34
ENDIFELSE_=35
ENDIF_=36
ENDPROC_=37
ENDWHEN_=38
EQUALSIGN=39
FIFO=40
FIFO_=41
GUARD_=42
ID=43
ID_=44
IF=45
IFELSE_=46
IF_=47
INITSTATE_=48
INITVAL_=49
INT=50
INTID=51
INT_=52
LINE_COMMENT=53
MACHN_=54
MCAST_=55
MINUS=56
MSG=57
MSGCSTR_=58
MSG_=59
NCOND_=60
NEG=61
NETWORK=62
NETWORK_=63
NEXT=64
NEXT_=65
NID=66
OBJSET_=67
OBRACE=68
OCBRACE=69
OEBRACE=70
PLUS=71
PROC=72
PROC_=73
RANGE_=74
SEMICOLON=75
SEND_=76
SET=77
SETFUNC_=78
SET_=79
STABLE=80
STABLE_=81
STATE=82
TRANS_=83
WHEN=84
WHEN_=85
WS=86

# token names
tokenNamesMap = {
    0: "<invalid>", 1: "<EOR>", 2: "<DOWN>", 3: "<UP>",
    -1: "EOF", 87: "T__87", 88: "T__88", 89: "T__89", 90: "T__90", 91: "T__91", 
    92: "T__92", 93: "T__93", 94: "T__94", 95: "T__95", 96: "T__96", 97: "T__97", 
    98: "T__98", 99: "T__99", 100: "T__100", 101: "T__101", 102: "T__102", 
    103: "T__103", 4: "ACCESS", 5: "ARCH", 6: "ARCH_", 7: "ARRAY", 8: "ARRAY_", 
    9: "ASSIGN_", 10: "AWAIT", 11: "AWAIT_", 12: "BOOL", 13: "BOOLID", 14: "BOOL_", 
    15: "BREAK", 16: "BREAK_", 17: "CACHE", 18: "CACHE_", 19: "CBRACE", 
    20: "CCBRACE", 21: "CEBRACE", 22: "COMMA", 23: "COMMENT", 24: "COND_", 
    25: "CONSTANT", 26: "CONSTANT_", 27: "DATA", 28: "DATA_", 29: "DDOT", 
    30: "DIR", 31: "DIR_", 32: "DOT", 33: "ELEMENT_", 34: "ELSE", 35: "ENDIFELSE_", 
    36: "ENDIF_", 37: "ENDPROC_", 38: "ENDWHEN_", 39: "EQUALSIGN", 40: "FIFO", 
    41: "FIFO_", 42: "GUARD_", 43: "ID", 44: "ID_", 45: "IF", 46: "IFELSE_", 
    47: "IF_", 48: "INITSTATE_", 49: "INITVAL_", 50: "INT", 51: "INTID", 
    52: "INT_", 53: "LINE_COMMENT", 54: "MACHN_", 55: "MCAST_", 56: "MINUS", 
    57: "MSG", 58: "MSGCSTR_", 59: "MSG_", 60: "NCOND_", 61: "NEG", 62: "NETWORK", 
    63: "NETWORK_", 64: "NEXT", 65: "NEXT_", 66: "NID", 67: "OBJSET_", 68: "OBRACE", 
    69: "OCBRACE", 70: "OEBRACE", 71: "PLUS", 72: "PROC", 73: "PROC_", 74: "RANGE_", 
    75: "SEMICOLON", 76: "SEND_", 77: "SET", 78: "SETFUNC_", 79: "SET_", 
    80: "STABLE", 81: "STABLE_", 82: "STATE", 83: "TRANS_", 84: "WHEN", 
    85: "WHEN_", 86: "WS"
}
Token.registerTokenNamesMap(tokenNamesMap)

class ProtoCCLexer(Lexer):

    grammarFileName = "/home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g"
    api_version = 1

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super().__init__(input, state)

        self.delegates = []

        self.dfa8 = self.DFA8(
            self, 8,
            eot = self.DFA8_eot,
            eof = self.DFA8_eof,
            min = self.DFA8_min,
            max = self.DFA8_max,
            accept = self.DFA8_accept,
            special = self.DFA8_special,
            transition = self.DFA8_transition
            )






    # $ANTLR start "ARCH"
    def mARCH(self, ):
        try:
            _type = ARCH
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:7:6: ( 'Architecture' )
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:7:8: 'Architecture'
            pass 
            self.match("Architecture")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ARCH"



    # $ANTLR start "ARRAY"
    def mARRAY(self, ):
        try:
            _type = ARRAY
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:8:7: ( 'array' )
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:8:9: 'array'
            pass 
            self.match("array")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ARRAY"



    # $ANTLR start "AWAIT"
    def mAWAIT(self, ):
        try:
            _type = AWAIT
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:9:7: ( 'await' )
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:9:9: 'await'
            pass 
            self.match("await")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "AWAIT"



    # $ANTLR start "BOOLID"
    def mBOOLID(self, ):
        try:
            _type = BOOLID
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:10:8: ( 'bool' )
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:10:10: 'bool'
            pass 
            self.match("bool")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "BOOLID"



    # $ANTLR start "BREAK"
    def mBREAK(self, ):
        try:
            _type = BREAK
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:11:7: ( 'break' )
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:11:9: 'break'
            pass 
            self.match("break")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "BREAK"



    # $ANTLR start "CACHE"
    def mCACHE(self, ):
        try:
            _type = CACHE
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:12:7: ( 'Cache' )
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:12:9: 'Cache'
            pass 
            self.match("Cache")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "CACHE"



    # $ANTLR start "CBRACE"
    def mCBRACE(self, ):
        try:
            _type = CBRACE
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:13:8: ( ')' )
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:13:10: ')'
            pass 
            self.match(41)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "CBRACE"



    # $ANTLR start "CCBRACE"
    def mCCBRACE(self, ):
        try:
            _type = CCBRACE
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:14:9: ( '}' )
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:14:11: '}'
            pass 
            self.match(125)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "CCBRACE"



    # $ANTLR start "CEBRACE"
    def mCEBRACE(self, ):
        try:
            _type = CEBRACE
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:15:9: ( ']' )
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:15:11: ']'
            pass 
            self.match(93)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "CEBRACE"



    # $ANTLR start "COMMA"
    def mCOMMA(self, ):
        try:
            _type = COMMA
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:16:7: ( ',' )
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:16:9: ','
            pass 
            self.match(44)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "COMMA"



    # $ANTLR start "CONSTANT"
    def mCONSTANT(self, ):
        try:
            _type = CONSTANT
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:17:10: ( '#' )
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:17:12: '#'
            pass 
            self.match(35)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "CONSTANT"



    # $ANTLR start "DATA"
    def mDATA(self, ):
        try:
            _type = DATA
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:18:6: ( 'Data' )
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:18:8: 'Data'
            pass 
            self.match("Data")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "DATA"



    # $ANTLR start "DDOT"
    def mDDOT(self, ):
        try:
            _type = DDOT
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:19:6: ( ':' )
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:19:8: ':'
            pass 
            self.match(58)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "DDOT"



    # $ANTLR start "DIR"
    def mDIR(self, ):
        try:
            _type = DIR
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:20:5: ( 'Directory' )
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:20:7: 'Directory'
            pass 
            self.match("Directory")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "DIR"



    # $ANTLR start "DOT"
    def mDOT(self, ):
        try:
            _type = DOT
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:21:5: ( '.' )
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:21:7: '.'
            pass 
            self.match(46)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "DOT"



    # $ANTLR start "ELSE"
    def mELSE(self, ):
        try:
            _type = ELSE
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:22:6: ( 'else' )
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:22:8: 'else'
            pass 
            self.match("else")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ELSE"



    # $ANTLR start "EQUALSIGN"
    def mEQUALSIGN(self, ):
        try:
            _type = EQUALSIGN
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:23:11: ( '=' )
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:23:13: '='
            pass 
            self.match(61)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "EQUALSIGN"



    # $ANTLR start "FIFO"
    def mFIFO(self, ):
        try:
            _type = FIFO
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:24:6: ( 'FIFO' )
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:24:8: 'FIFO'
            pass 
            self.match("FIFO")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "FIFO"



    # $ANTLR start "IF"
    def mIF(self, ):
        try:
            _type = IF
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:25:4: ( 'if' )
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:25:6: 'if'
            pass 
            self.match("if")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "IF"



    # $ANTLR start "INTID"
    def mINTID(self, ):
        try:
            _type = INTID
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:26:7: ( 'int' )
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:26:9: 'int'
            pass 
            self.match("int")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "INTID"



    # $ANTLR start "MINUS"
    def mMINUS(self, ):
        try:
            _type = MINUS
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:27:7: ( '-' )
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:27:9: '-'
            pass 
            self.match(45)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "MINUS"



    # $ANTLR start "MSG"
    def mMSG(self, ):
        try:
            _type = MSG
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:28:5: ( 'Message' )
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:28:7: 'Message'
            pass 
            self.match("Message")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "MSG"



    # $ANTLR start "NEG"
    def mNEG(self, ):
        try:
            _type = NEG
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:29:5: ( '!' )
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:29:7: '!'
            pass 
            self.match(33)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "NEG"



    # $ANTLR start "NETWORK"
    def mNETWORK(self, ):
        try:
            _type = NETWORK
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:30:9: ( 'Network' )
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:30:11: 'Network'
            pass 
            self.match("Network")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "NETWORK"



    # $ANTLR start "NEXT"
    def mNEXT(self, ):
        try:
            _type = NEXT
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:31:6: ( 'next' )
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:31:8: 'next'
            pass 
            self.match("next")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "NEXT"



    # $ANTLR start "NID"
    def mNID(self, ):
        try:
            _type = NID
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:32:5: ( 'ID' )
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:32:7: 'ID'
            pass 
            self.match("ID")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "NID"



    # $ANTLR start "OBRACE"
    def mOBRACE(self, ):
        try:
            _type = OBRACE
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:33:8: ( '(' )
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:33:10: '('
            pass 
            self.match(40)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "OBRACE"



    # $ANTLR start "OCBRACE"
    def mOCBRACE(self, ):
        try:
            _type = OCBRACE
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:34:9: ( '{' )
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:34:11: '{'
            pass 
            self.match(123)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "OCBRACE"



    # $ANTLR start "OEBRACE"
    def mOEBRACE(self, ):
        try:
            _type = OEBRACE
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:35:9: ( '[' )
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:35:11: '['
            pass 
            self.match(91)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "OEBRACE"



    # $ANTLR start "PLUS"
    def mPLUS(self, ):
        try:
            _type = PLUS
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:36:6: ( '+' )
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:36:8: '+'
            pass 
            self.match(43)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "PLUS"



    # $ANTLR start "PROC"
    def mPROC(self, ):
        try:
            _type = PROC
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:37:6: ( 'Process' )
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:37:8: 'Process'
            pass 
            self.match("Process")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "PROC"



    # $ANTLR start "SEMICOLON"
    def mSEMICOLON(self, ):
        try:
            _type = SEMICOLON
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:38:11: ( ';' )
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:38:13: ';'
            pass 
            self.match(59)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "SEMICOLON"



    # $ANTLR start "SET"
    def mSET(self, ):
        try:
            _type = SET
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:39:5: ( 'set' )
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:39:7: 'set'
            pass 
            self.match("set")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "SET"



    # $ANTLR start "STABLE"
    def mSTABLE(self, ):
        try:
            _type = STABLE
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:40:8: ( 'Stable' )
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:40:10: 'Stable'
            pass 
            self.match("Stable")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "STABLE"



    # $ANTLR start "STATE"
    def mSTATE(self, ):
        try:
            _type = STATE
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:41:7: ( 'State' )
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:41:9: 'State'
            pass 
            self.match("State")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "STATE"



    # $ANTLR start "WHEN"
    def mWHEN(self, ):
        try:
            _type = WHEN
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:42:6: ( 'when' )
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:42:8: 'when'
            pass 
            self.match("when")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "WHEN"



    # $ANTLR start "T__87"
    def mT__87(self, ):
        try:
            _type = T__87
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:43:7: ( '!=' )
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:43:9: '!='
            pass 
            self.match("!=")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__87"



    # $ANTLR start "T__88"
    def mT__88(self, ):
        try:
            _type = T__88
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:44:7: ( '&' )
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:44:9: '&'
            pass 
            self.match(38)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__88"



    # $ANTLR start "T__89"
    def mT__89(self, ):
        try:
            _type = T__89
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:45:7: ( '<' )
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:45:9: '<'
            pass 
            self.match(60)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__89"



    # $ANTLR start "T__90"
    def mT__90(self, ):
        try:
            _type = T__90
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:46:7: ( '<=' )
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:46:9: '<='
            pass 
            self.match("<=")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__90"



    # $ANTLR start "T__91"
    def mT__91(self, ):
        try:
            _type = T__91
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:47:7: ( '==' )
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:47:9: '=='
            pass 
            self.match("==")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__91"



    # $ANTLR start "T__92"
    def mT__92(self, ):
        try:
            _type = T__92
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:48:7: ( '>' )
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:48:9: '>'
            pass 
            self.match(62)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__92"



    # $ANTLR start "T__93"
    def mT__93(self, ):
        try:
            _type = T__93
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:49:7: ( '>=' )
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:49:9: '>='
            pass 
            self.match(">=")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__93"



    # $ANTLR start "T__94"
    def mT__94(self, ):
        try:
            _type = T__94
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:50:7: ( 'Ordered' )
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:50:9: 'Ordered'
            pass 
            self.match("Ordered")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__94"



    # $ANTLR start "T__95"
    def mT__95(self, ):
        try:
            _type = T__95
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:51:7: ( 'Unordered' )
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:51:9: 'Unordered'
            pass 
            self.match("Unordered")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__95"



    # $ANTLR start "T__96"
    def mT__96(self, ):
        try:
            _type = T__96
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:52:7: ( 'add' )
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:52:9: 'add'
            pass 
            self.match("add")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__96"



    # $ANTLR start "T__97"
    def mT__97(self, ):
        try:
            _type = T__97
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:53:7: ( 'clear' )
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:53:9: 'clear'
            pass 
            self.match("clear")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__97"



    # $ANTLR start "T__98"
    def mT__98(self, ):
        try:
            _type = T__98
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:54:7: ( 'contains' )
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:54:9: 'contains'
            pass 
            self.match("contains")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__98"



    # $ANTLR start "T__99"
    def mT__99(self, ):
        try:
            _type = T__99
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:55:7: ( 'count' )
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:55:9: 'count'
            pass 
            self.match("count")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__99"



    # $ANTLR start "T__100"
    def mT__100(self, ):
        try:
            _type = T__100
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:56:8: ( 'del' )
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:56:10: 'del'
            pass 
            self.match("del")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__100"



    # $ANTLR start "T__101"
    def mT__101(self, ):
        try:
            _type = T__101
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:57:8: ( 'mcast' )
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:57:10: 'mcast'
            pass 
            self.match("mcast")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__101"



    # $ANTLR start "T__102"
    def mT__102(self, ):
        try:
            _type = T__102
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:58:8: ( 'send' )
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:58:10: 'send'
            pass 
            self.match("send")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__102"



    # $ANTLR start "T__103"
    def mT__103(self, ):
        try:
            _type = T__103
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:59:8: ( '|' )
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:59:10: '|'
            pass 
            self.match(124)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__103"



    # $ANTLR start "WS"
    def mWS(self, ):
        try:
            _type = WS
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:141:5: ( ( ' ' | '\\t' | '\\r' | '\\n' ) )
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:141:9: ( ' ' | '\\t' | '\\r' | '\\n' )
            pass 
            if self.input.LA(1) in {9, 10, 13, 32}:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            #action start
            _channel=HIDDEN;
            #action end




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "WS"



    # $ANTLR start "COMMENT"
    def mCOMMENT(self, ):
        try:
            _type = COMMENT
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:149:5: ( '/*' ( options {greedy=false; } : . )* '*/' )
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:149:9: '/*' ( options {greedy=false; } : . )* '*/'
            pass 
            self.match("/*")


            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:149:14: ( options {greedy=false; } : . )*
            while True: #loop1
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if (LA1_0 == 42) :
                    LA1_1 = self.input.LA(2)

                    if (LA1_1 == 47) :
                        alt1 = 2
                    elif ((0 <= LA1_1 <= 46) or (48 <= LA1_1 <= 65535) or LA1_1 in {}) :
                        alt1 = 1


                elif ((0 <= LA1_0 <= 41) or (43 <= LA1_0 <= 65535) or LA1_0 in {}) :
                    alt1 = 1


                if alt1 == 1:
                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:149:42: .
                    pass 
                    self.matchAny()


                else:
                    break #loop1


            self.match("*/")


            #action start
            _channel=HIDDEN;
            #action end




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "COMMENT"



    # $ANTLR start "LINE_COMMENT"
    def mLINE_COMMENT(self, ):
        try:
            _type = LINE_COMMENT
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:153:5: ( '//' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n' )
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:153:7: '//' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n'
            pass 
            self.match("//")


            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:153:12: (~ ( '\\n' | '\\r' ) )*
            while True: #loop2
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if ((0 <= LA2_0 <= 9) or (14 <= LA2_0 <= 65535) or LA2_0 in {11, 12}) :
                    alt2 = 1


                if alt2 == 1:
                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:
                    pass 
                    if (0 <= self.input.LA(1) <= 9) or (14 <= self.input.LA(1) <= 65535) or self.input.LA(1) in {11, 12}:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop2


            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:153:26: ( '\\r' )?
            alt3 = 2
            LA3_0 = self.input.LA(1)

            if (LA3_0 == 13) :
                alt3 = 1
            if alt3 == 1:
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:153:26: '\\r'
                pass 
                self.match(13)




            self.match(10)

            #action start
            _channel=HIDDEN;
            #action end




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LINE_COMMENT"



    # $ANTLR start "BOOL"
    def mBOOL(self, ):
        try:
            _type = BOOL
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:158:5: ( 'true' | 'false' )
            alt4 = 2
            LA4_0 = self.input.LA(1)

            if (LA4_0 == 116) :
                alt4 = 1
            elif (LA4_0 == 102) :
                alt4 = 2
            else:
                nvae = NoViableAltException("", 4, 0, self.input)

                raise nvae


            if alt4 == 1:
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:158:9: 'true'
                pass 
                self.match("true")



            elif alt4 == 2:
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:158:18: 'false'
                pass 
                self.match("false")



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "BOOL"



    # $ANTLR start "INT"
    def mINT(self, ):
        try:
            _type = INT
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:159:5: ( ( '0' .. '9' )+ )
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:159:7: ( '0' .. '9' )+
            pass 
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:159:7: ( '0' .. '9' )+
            cnt5 = 0
            while True: #loop5
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if ((48 <= LA5_0 <= 57) or LA5_0 in {}) :
                    alt5 = 1


                if alt5 == 1:
                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57) or self.input.LA(1) in {}:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    if cnt5 >= 1:
                        break #loop5

                    eee = EarlyExitException(5, self.input)
                    raise eee

                cnt5 += 1




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "INT"



    # $ANTLR start "ACCESS"
    def mACCESS(self, ):
        try:
            _type = ACCESS
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:161:7: ( 'load' | 'store' | 'evict' )
            alt6 = 3
            LA6 = self.input.LA(1)
            if LA6 in {108}:
                alt6 = 1
            elif LA6 in {115}:
                alt6 = 2
            elif LA6 in {101}:
                alt6 = 3
            else:
                nvae = NoViableAltException("", 6, 0, self.input)

                raise nvae


            if alt6 == 1:
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:161:9: 'load'
                pass 
                self.match("load")



            elif alt6 == 2:
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:161:18: 'store'
                pass 
                self.match("store")



            elif alt6 == 3:
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:161:28: 'evict'
                pass 
                self.match("evict")



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ACCESS"



    # $ANTLR start "ID"
    def mID(self, ):
        try:
            _type = ID
            _channel = DEFAULT_CHANNEL

            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:163:5: ( ( 'a' .. 'z' | 'A' .. 'Z' | '_' ) ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' )* )
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:163:7: ( 'a' .. 'z' | 'A' .. 'Z' | '_' ) ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' )*
            pass 
            if (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122) or self.input.LA(1) in {95}:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:163:31: ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' )*
            while True: #loop7
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if ((48 <= LA7_0 <= 57) or (65 <= LA7_0 <= 90) or (97 <= LA7_0 <= 122) or LA7_0 in {95}) :
                    alt7 = 1


                if alt7 == 1:
                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122) or self.input.LA(1) in {95}:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop7




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ID"



    def mTokens(self):
        # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:8: ( ARCH | ARRAY | AWAIT | BOOLID | BREAK | CACHE | CBRACE | CCBRACE | CEBRACE | COMMA | CONSTANT | DATA | DDOT | DIR | DOT | ELSE | EQUALSIGN | FIFO | IF | INTID | MINUS | MSG | NEG | NETWORK | NEXT | NID | OBRACE | OCBRACE | OEBRACE | PLUS | PROC | SEMICOLON | SET | STABLE | STATE | WHEN | T__87 | T__88 | T__89 | T__90 | T__91 | T__92 | T__93 | T__94 | T__95 | T__96 | T__97 | T__98 | T__99 | T__100 | T__101 | T__102 | T__103 | WS | COMMENT | LINE_COMMENT | BOOL | INT | ACCESS | ID )
        alt8 = 60
        alt8 = self.dfa8.predict(self.input)
        if alt8 == 1:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:10: ARCH
            pass 
            self.mARCH()



        elif alt8 == 2:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:15: ARRAY
            pass 
            self.mARRAY()



        elif alt8 == 3:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:21: AWAIT
            pass 
            self.mAWAIT()



        elif alt8 == 4:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:27: BOOLID
            pass 
            self.mBOOLID()



        elif alt8 == 5:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:34: BREAK
            pass 
            self.mBREAK()



        elif alt8 == 6:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:40: CACHE
            pass 
            self.mCACHE()



        elif alt8 == 7:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:46: CBRACE
            pass 
            self.mCBRACE()



        elif alt8 == 8:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:53: CCBRACE
            pass 
            self.mCCBRACE()



        elif alt8 == 9:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:61: CEBRACE
            pass 
            self.mCEBRACE()



        elif alt8 == 10:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:69: COMMA
            pass 
            self.mCOMMA()



        elif alt8 == 11:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:75: CONSTANT
            pass 
            self.mCONSTANT()



        elif alt8 == 12:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:84: DATA
            pass 
            self.mDATA()



        elif alt8 == 13:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:89: DDOT
            pass 
            self.mDDOT()



        elif alt8 == 14:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:94: DIR
            pass 
            self.mDIR()



        elif alt8 == 15:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:98: DOT
            pass 
            self.mDOT()



        elif alt8 == 16:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:102: ELSE
            pass 
            self.mELSE()



        elif alt8 == 17:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:107: EQUALSIGN
            pass 
            self.mEQUALSIGN()



        elif alt8 == 18:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:117: FIFO
            pass 
            self.mFIFO()



        elif alt8 == 19:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:122: IF
            pass 
            self.mIF()



        elif alt8 == 20:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:125: INTID
            pass 
            self.mINTID()



        elif alt8 == 21:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:131: MINUS
            pass 
            self.mMINUS()



        elif alt8 == 22:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:137: MSG
            pass 
            self.mMSG()



        elif alt8 == 23:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:141: NEG
            pass 
            self.mNEG()



        elif alt8 == 24:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:145: NETWORK
            pass 
            self.mNETWORK()



        elif alt8 == 25:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:153: NEXT
            pass 
            self.mNEXT()



        elif alt8 == 26:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:158: NID
            pass 
            self.mNID()



        elif alt8 == 27:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:162: OBRACE
            pass 
            self.mOBRACE()



        elif alt8 == 28:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:169: OCBRACE
            pass 
            self.mOCBRACE()



        elif alt8 == 29:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:177: OEBRACE
            pass 
            self.mOEBRACE()



        elif alt8 == 30:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:185: PLUS
            pass 
            self.mPLUS()



        elif alt8 == 31:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:190: PROC
            pass 
            self.mPROC()



        elif alt8 == 32:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:195: SEMICOLON
            pass 
            self.mSEMICOLON()



        elif alt8 == 33:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:205: SET
            pass 
            self.mSET()



        elif alt8 == 34:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:209: STABLE
            pass 
            self.mSTABLE()



        elif alt8 == 35:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:216: STATE
            pass 
            self.mSTATE()



        elif alt8 == 36:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:222: WHEN
            pass 
            self.mWHEN()



        elif alt8 == 37:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:227: T__87
            pass 
            self.mT__87()



        elif alt8 == 38:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:233: T__88
            pass 
            self.mT__88()



        elif alt8 == 39:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:239: T__89
            pass 
            self.mT__89()



        elif alt8 == 40:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:245: T__90
            pass 
            self.mT__90()



        elif alt8 == 41:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:251: T__91
            pass 
            self.mT__91()



        elif alt8 == 42:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:257: T__92
            pass 
            self.mT__92()



        elif alt8 == 43:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:263: T__93
            pass 
            self.mT__93()



        elif alt8 == 44:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:269: T__94
            pass 
            self.mT__94()



        elif alt8 == 45:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:275: T__95
            pass 
            self.mT__95()



        elif alt8 == 46:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:281: T__96
            pass 
            self.mT__96()



        elif alt8 == 47:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:287: T__97
            pass 
            self.mT__97()



        elif alt8 == 48:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:293: T__98
            pass 
            self.mT__98()



        elif alt8 == 49:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:299: T__99
            pass 
            self.mT__99()



        elif alt8 == 50:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:305: T__100
            pass 
            self.mT__100()



        elif alt8 == 51:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:312: T__101
            pass 
            self.mT__101()



        elif alt8 == 52:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:319: T__102
            pass 
            self.mT__102()



        elif alt8 == 53:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:326: T__103
            pass 
            self.mT__103()



        elif alt8 == 54:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:333: WS
            pass 
            self.mWS()



        elif alt8 == 55:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:336: COMMENT
            pass 
            self.mCOMMENT()



        elif alt8 == 56:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:344: LINE_COMMENT
            pass 
            self.mLINE_COMMENT()



        elif alt8 == 57:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:357: BOOL
            pass 
            self.mBOOL()



        elif alt8 == 58:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:362: INT
            pass 
            self.mINT()



        elif alt8 == 59:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:366: ACCESS
            pass 
            self.mACCESS()



        elif alt8 == 60:
            # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:1:373: ID
            pass 
            self.mID()








    # lookup tables for DFA #8

    DFA8_eot = DFA.unpack(
        "\1\uffff\4\57\5\uffff\1\57\2\uffff\1\57\1\74\2\57\1\uffff\1\57\1"
        "\102\3\57\4\uffff\1\57\1\uffff\3\57\1\uffff\1\114\1\116\5\57\3\uffff"
        "\2\57\1\uffff\1\57\1\uffff\13\57\2\uffff\1\57\1\146\2\57\2\uffff"
        "\2\57\1\153\5\57\4\uffff\6\57\2\uffff\6\57\1\177\10\57\1\uffff\1"
        "\u0088\3\57\1\uffff\1\57\1\u008d\11\57\1\u0098\7\57\1\uffff\1\u00a0"
        "\2\57\1\u00a3\1\57\1\u00a5\1\57\1\u00a7\1\uffff\2\57\1\u00aa\1\57"
        "\1\uffff\1\u00ac\3\57\1\u00b0\5\57\1\uffff\1\57\1\u00b7\1\57\1\u00b9"
        "\1\57\1\u00bb\1\u00bc\1\uffff\1\u00bd\1\u00be\1\uffff\1\57\1\uffff"
        "\1\u00b9\1\uffff\2\57\1\uffff\1\57\1\uffff\1\u00b9\1\57\1\u00c4"
        "\1\uffff\2\57\1\u00c7\1\57\1\u00c9\1\u00ca\1\uffff\1\u00b7\1\uffff"
        "\1\57\4\uffff\4\57\1\u00d0\1\uffff\2\57\1\uffff\1\57\2\uffff\2\57"
        "\1\u00d6\1\u00d7\1\u00d8\1\uffff\1\u00d9\4\57\4\uffff\1\57\1\u00df"
        "\1\57\1\u00e1\1\u00e2\1\uffff\1\57\2\uffff\1\57\1\u00e5\1\uffff"
        )

    DFA8_eof = DFA.unpack(
        "\u00e6\uffff"
        )

    DFA8_min = DFA.unpack(
        "\1\11\1\162\1\144\1\157\1\141\5\uffff\1\141\2\uffff\1\154\1\75\1"
        "\111\1\146\1\uffff\1\145\1\75\2\145\1\104\4\uffff\1\162\1\uffff"
        "\1\145\1\164\1\150\1\uffff\2\75\1\162\1\156\1\154\1\145\1\143\2"
        "\uffff\1\52\1\162\1\141\1\uffff\1\157\1\uffff\1\143\1\162\1\141"
        "\1\144\1\157\1\145\1\143\1\164\1\162\1\163\1\151\2\uffff\1\106\1"
        "\60\1\164\1\163\2\uffff\1\164\1\170\1\60\1\157\1\156\1\157\1\141"
        "\1\145\4\uffff\1\144\1\157\1\145\1\156\1\154\1\141\2\uffff\1\165"
        "\1\154\1\141\1\150\1\141\1\151\1\60\1\154\1\141\1\150\1\141\2\145"
        "\1\143\1\117\1\uffff\1\60\1\163\1\167\1\164\1\uffff\1\143\1\60\1"
        "\144\1\162\1\142\1\156\1\145\1\162\1\141\1\164\1\156\1\60\1\163"
        "\1\145\1\163\1\144\1\151\1\171\1\164\1\uffff\1\60\1\153\1\145\1"
        "\60\1\143\1\60\1\164\1\60\1\uffff\1\141\1\157\1\60\1\145\1\uffff"
        "\1\60\1\145\1\154\1\145\1\60\1\162\1\144\1\162\1\141\1\164\1\uffff"
        "\1\164\1\60\1\145\1\60\1\164\2\60\1\uffff\2\60\1\uffff\1\164\1\uffff"
        "\1\60\1\uffff\1\147\1\162\1\uffff\1\163\1\uffff\1\60\1\145\1\60"
        "\1\uffff\2\145\1\60\1\151\2\60\1\uffff\1\60\1\uffff\1\145\4\uffff"
        "\1\157\1\145\1\153\1\163\1\60\1\uffff\1\144\1\162\1\uffff\1\156"
        "\2\uffff\1\143\1\162\3\60\1\uffff\1\60\1\145\1\163\1\164\1\171\4"
        "\uffff\1\144\1\60\1\165\2\60\1\uffff\1\162\2\uffff\1\145\1\60\1"
        "\uffff"
        )

    DFA8_max = DFA.unpack(
        "\1\175\1\162\1\167\1\162\1\141\5\uffff\1\151\2\uffff\1\166\1\75"
        "\1\111\1\156\1\uffff\1\145\1\75\2\145\1\104\4\uffff\1\162\1\uffff"
        "\2\164\1\150\1\uffff\2\75\1\162\1\156\1\157\1\145\1\143\2\uffff"
        "\1\57\1\162\1\141\1\uffff\1\157\1\uffff\1\143\1\162\1\141\1\144"
        "\1\157\1\145\1\143\1\164\1\162\1\163\1\151\2\uffff\1\106\1\172\1"
        "\164\1\163\2\uffff\1\164\1\170\1\172\1\157\1\164\1\157\1\141\1\145"
        "\4\uffff\1\144\1\157\1\145\1\165\1\154\1\141\2\uffff\1\165\1\154"
        "\1\141\1\150\1\141\1\151\1\172\1\154\1\141\1\150\1\141\2\145\1\143"
        "\1\117\1\uffff\1\172\1\163\1\167\1\164\1\uffff\1\143\1\172\1\144"
        "\1\162\1\164\1\156\1\145\1\162\1\141\1\164\1\156\1\172\1\163\1\145"
        "\1\163\1\144\1\151\1\171\1\164\1\uffff\1\172\1\153\1\145\1\172\1"
        "\143\1\172\1\164\1\172\1\uffff\1\141\1\157\1\172\1\145\1\uffff\1"
        "\172\1\145\1\154\1\145\1\172\1\162\1\144\1\162\1\141\1\164\1\uffff"
        "\1\164\1\172\1\145\1\172\1\164\2\172\1\uffff\2\172\1\uffff\1\164"
        "\1\uffff\1\172\1\uffff\1\147\1\162\1\uffff\1\163\1\uffff\1\172\1"
        "\145\1\172\1\uffff\2\145\1\172\1\151\2\172\1\uffff\1\172\1\uffff"
        "\1\145\4\uffff\1\157\1\145\1\153\1\163\1\172\1\uffff\1\144\1\162"
        "\1\uffff\1\156\2\uffff\1\143\1\162\3\172\1\uffff\1\172\1\145\1\163"
        "\1\164\1\171\4\uffff\1\144\1\172\1\165\2\172\1\uffff\1\162\2\uffff"
        "\1\145\1\172\1\uffff"
        )

    DFA8_accept = DFA.unpack(
        "\5\uffff\1\7\1\10\1\11\1\12\1\13\1\uffff\1\15\1\17\4\uffff\1\25"
        "\5\uffff\1\33\1\34\1\35\1\36\1\uffff\1\40\3\uffff\1\46\7\uffff\1"
        "\65\1\66\3\uffff\1\72\1\uffff\1\74\13\uffff\1\51\1\21\4\uffff\1"
        "\45\1\27\10\uffff\1\50\1\47\1\53\1\52\6\uffff\1\67\1\70\17\uffff"
        "\1\23\4\uffff\1\32\23\uffff\1\56\10\uffff\1\24\4\uffff\1\41\12\uffff"
        "\1\62\7\uffff\1\4\2\uffff\1\14\1\uffff\1\20\1\uffff\1\22\2\uffff"
        "\1\31\1\uffff\1\64\3\uffff\1\44\6\uffff\1\71\1\uffff\1\73\1\uffff"
        "\1\2\1\3\1\5\1\6\5\uffff\1\43\2\uffff\1\57\1\uffff\1\61\1\63\5\uffff"
        "\1\42\5\uffff\1\26\1\30\1\37\1\54\5\uffff\1\60\1\uffff\1\16\1\55"
        "\2\uffff\1\1"
        )

    DFA8_special = DFA.unpack(
        "\u00e6\uffff"
        )


    DFA8_transition = [
        DFA.unpack("\2\51\2\uffff\1\51\22\uffff\1\51\1\23\1\uffff\1\11\2"
        "\uffff\1\40\1\uffff\1\27\1\5\1\uffff\1\32\1\10\1\21\1\14\1\52\12"
        "\55\1\13\1\34\1\41\1\16\1\42\2\uffff\1\1\1\57\1\4\1\12\1\57\1\17"
        "\2\57\1\26\3\57\1\22\1\24\1\43\1\33\2\57\1\36\1\57\1\44\5\57\1\31"
        "\1\uffff\1\7\1\uffff\1\57\1\uffff\1\2\1\3\1\45\1\46\1\15\1\54\2"
        "\57\1\20\2\57\1\56\1\47\1\25\4\57\1\35\1\53\2\57\1\37\3\57\1\30"
        "\1\50\1\6"),
        DFA.unpack("\1\60"),
        DFA.unpack("\1\63\15\uffff\1\61\4\uffff\1\62"),
        DFA.unpack("\1\64\2\uffff\1\65"),
        DFA.unpack("\1\66"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\67\7\uffff\1\70"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\71\11\uffff\1\72"),
        DFA.unpack("\1\73"),
        DFA.unpack("\1\75"),
        DFA.unpack("\1\76\7\uffff\1\77"),
        DFA.unpack(""),
        DFA.unpack("\1\100"),
        DFA.unpack("\1\101"),
        DFA.unpack("\1\103"),
        DFA.unpack("\1\104"),
        DFA.unpack("\1\105"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\106"),
        DFA.unpack(""),
        DFA.unpack("\1\107\16\uffff\1\110"),
        DFA.unpack("\1\111"),
        DFA.unpack("\1\112"),
        DFA.unpack(""),
        DFA.unpack("\1\113"),
        DFA.unpack("\1\115"),
        DFA.unpack("\1\117"),
        DFA.unpack("\1\120"),
        DFA.unpack("\1\121\2\uffff\1\122"),
        DFA.unpack("\1\123"),
        DFA.unpack("\1\124"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\125\4\uffff\1\126"),
        DFA.unpack("\1\127"),
        DFA.unpack("\1\130"),
        DFA.unpack(""),
        DFA.unpack("\1\131"),
        DFA.unpack(""),
        DFA.unpack("\1\132"),
        DFA.unpack("\1\133"),
        DFA.unpack("\1\134"),
        DFA.unpack("\1\135"),
        DFA.unpack("\1\136"),
        DFA.unpack("\1\137"),
        DFA.unpack("\1\140"),
        DFA.unpack("\1\141"),
        DFA.unpack("\1\142"),
        DFA.unpack("\1\143"),
        DFA.unpack("\1\144"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\145"),
        DFA.unpack("\12\57\7\uffff\32\57\4\uffff\1\57\1\uffff\32\57"),
        DFA.unpack("\1\147"),
        DFA.unpack("\1\150"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\151"),
        DFA.unpack("\1\152"),
        DFA.unpack("\12\57\7\uffff\32\57\4\uffff\1\57\1\uffff\32\57"),
        DFA.unpack("\1\154"),
        DFA.unpack("\1\156\5\uffff\1\155"),
        DFA.unpack("\1\157"),
        DFA.unpack("\1\160"),
        DFA.unpack("\1\161"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\162"),
        DFA.unpack("\1\163"),
        DFA.unpack("\1\164"),
        DFA.unpack("\1\165\6\uffff\1\166"),
        DFA.unpack("\1\167"),
        DFA.unpack("\1\170"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\171"),
        DFA.unpack("\1\172"),
        DFA.unpack("\1\173"),
        DFA.unpack("\1\174"),
        DFA.unpack("\1\175"),
        DFA.unpack("\1\176"),
        DFA.unpack("\12\57\7\uffff\32\57\4\uffff\1\57\1\uffff\32\57"),
        DFA.unpack("\1\u0080"),
        DFA.unpack("\1\u0081"),
        DFA.unpack("\1\u0082"),
        DFA.unpack("\1\u0083"),
        DFA.unpack("\1\u0084"),
        DFA.unpack("\1\u0085"),
        DFA.unpack("\1\u0086"),
        DFA.unpack("\1\u0087"),
        DFA.unpack(""),
        DFA.unpack("\12\57\7\uffff\32\57\4\uffff\1\57\1\uffff\32\57"),
        DFA.unpack("\1\u0089"),
        DFA.unpack("\1\u008a"),
        DFA.unpack("\1\u008b"),
        DFA.unpack(""),
        DFA.unpack("\1\u008c"),
        DFA.unpack("\12\57\7\uffff\32\57\4\uffff\1\57\1\uffff\32\57"),
        DFA.unpack("\1\u008e"),
        DFA.unpack("\1\u008f"),
        DFA.unpack("\1\u0090\21\uffff\1\u0091"),
        DFA.unpack("\1\u0092"),
        DFA.unpack("\1\u0093"),
        DFA.unpack("\1\u0094"),
        DFA.unpack("\1\u0095"),
        DFA.unpack("\1\u0096"),
        DFA.unpack("\1\u0097"),
        DFA.unpack("\12\57\7\uffff\32\57\4\uffff\1\57\1\uffff\32\57"),
        DFA.unpack("\1\u0099"),
        DFA.unpack("\1\u009a"),
        DFA.unpack("\1\u009b"),
        DFA.unpack("\1\u009c"),
        DFA.unpack("\1\u009d"),
        DFA.unpack("\1\u009e"),
        DFA.unpack("\1\u009f"),
        DFA.unpack(""),
        DFA.unpack("\12\57\7\uffff\32\57\4\uffff\1\57\1\uffff\32\57"),
        DFA.unpack("\1\u00a1"),
        DFA.unpack("\1\u00a2"),
        DFA.unpack("\12\57\7\uffff\32\57\4\uffff\1\57\1\uffff\32\57"),
        DFA.unpack("\1\u00a4"),
        DFA.unpack("\12\57\7\uffff\32\57\4\uffff\1\57\1\uffff\32\57"),
        DFA.unpack("\1\u00a6"),
        DFA.unpack("\12\57\7\uffff\32\57\4\uffff\1\57\1\uffff\32\57"),
        DFA.unpack(""),
        DFA.unpack("\1\u00a8"),
        DFA.unpack("\1\u00a9"),
        DFA.unpack("\12\57\7\uffff\32\57\4\uffff\1\57\1\uffff\32\57"),
        DFA.unpack("\1\u00ab"),
        DFA.unpack(""),
        DFA.unpack("\12\57\7\uffff\32\57\4\uffff\1\57\1\uffff\32\57"),
        DFA.unpack("\1\u00ad"),
        DFA.unpack("\1\u00ae"),
        DFA.unpack("\1\u00af"),
        DFA.unpack("\12\57\7\uffff\32\57\4\uffff\1\57\1\uffff\32\57"),
        DFA.unpack("\1\u00b1"),
        DFA.unpack("\1\u00b2"),
        DFA.unpack("\1\u00b3"),
        DFA.unpack("\1\u00b4"),
        DFA.unpack("\1\u00b5"),
        DFA.unpack(""),
        DFA.unpack("\1\u00b6"),
        DFA.unpack("\12\57\7\uffff\32\57\4\uffff\1\57\1\uffff\32\57"),
        DFA.unpack("\1\u00b8"),
        DFA.unpack("\12\57\7\uffff\32\57\4\uffff\1\57\1\uffff\32\57"),
        DFA.unpack("\1\u00ba"),
        DFA.unpack("\12\57\7\uffff\32\57\4\uffff\1\57\1\uffff\32\57"),
        DFA.unpack("\12\57\7\uffff\32\57\4\uffff\1\57\1\uffff\32\57"),
        DFA.unpack(""),
        DFA.unpack("\12\57\7\uffff\32\57\4\uffff\1\57\1\uffff\32\57"),
        DFA.unpack("\12\57\7\uffff\32\57\4\uffff\1\57\1\uffff\32\57"),
        DFA.unpack(""),
        DFA.unpack("\1\u00bf"),
        DFA.unpack(""),
        DFA.unpack("\12\57\7\uffff\32\57\4\uffff\1\57\1\uffff\32\57"),
        DFA.unpack(""),
        DFA.unpack("\1\u00c0"),
        DFA.unpack("\1\u00c1"),
        DFA.unpack(""),
        DFA.unpack("\1\u00c2"),
        DFA.unpack(""),
        DFA.unpack("\12\57\7\uffff\32\57\4\uffff\1\57\1\uffff\32\57"),
        DFA.unpack("\1\u00c3"),
        DFA.unpack("\12\57\7\uffff\32\57\4\uffff\1\57\1\uffff\32\57"),
        DFA.unpack(""),
        DFA.unpack("\1\u00c5"),
        DFA.unpack("\1\u00c6"),
        DFA.unpack("\12\57\7\uffff\32\57\4\uffff\1\57\1\uffff\32\57"),
        DFA.unpack("\1\u00c8"),
        DFA.unpack("\12\57\7\uffff\32\57\4\uffff\1\57\1\uffff\32\57"),
        DFA.unpack("\12\57\7\uffff\32\57\4\uffff\1\57\1\uffff\32\57"),
        DFA.unpack(""),
        DFA.unpack("\12\57\7\uffff\32\57\4\uffff\1\57\1\uffff\32\57"),
        DFA.unpack(""),
        DFA.unpack("\1\u00cb"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u00cc"),
        DFA.unpack("\1\u00cd"),
        DFA.unpack("\1\u00ce"),
        DFA.unpack("\1\u00cf"),
        DFA.unpack("\12\57\7\uffff\32\57\4\uffff\1\57\1\uffff\32\57"),
        DFA.unpack(""),
        DFA.unpack("\1\u00d1"),
        DFA.unpack("\1\u00d2"),
        DFA.unpack(""),
        DFA.unpack("\1\u00d3"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u00d4"),
        DFA.unpack("\1\u00d5"),
        DFA.unpack("\12\57\7\uffff\32\57\4\uffff\1\57\1\uffff\32\57"),
        DFA.unpack("\12\57\7\uffff\32\57\4\uffff\1\57\1\uffff\32\57"),
        DFA.unpack("\12\57\7\uffff\32\57\4\uffff\1\57\1\uffff\32\57"),
        DFA.unpack(""),
        DFA.unpack("\12\57\7\uffff\32\57\4\uffff\1\57\1\uffff\32\57"),
        DFA.unpack("\1\u00da"),
        DFA.unpack("\1\u00db"),
        DFA.unpack("\1\u00dc"),
        DFA.unpack("\1\u00dd"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u00de"),
        DFA.unpack("\12\57\7\uffff\32\57\4\uffff\1\57\1\uffff\32\57"),
        DFA.unpack("\1\u00e0"),
        DFA.unpack("\12\57\7\uffff\32\57\4\uffff\1\57\1\uffff\32\57"),
        DFA.unpack("\12\57\7\uffff\32\57\4\uffff\1\57\1\uffff\32\57"),
        DFA.unpack(""),
        DFA.unpack("\1\u00e3"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u00e4"),
        DFA.unpack("\12\57\7\uffff\32\57\4\uffff\1\57\1\uffff\32\57"),
        DFA.unpack("")
    ]

    # class definition for DFA #8

    class DFA8(DFA):
        pass


 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(ProtoCCLexer)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
