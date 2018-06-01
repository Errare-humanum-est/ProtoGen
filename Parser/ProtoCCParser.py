import sys
from antlr3 import *

from antlr3.tree import *




# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EOF=-1
T__86=86
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
NETWORK=61
NETWORK_=62
NEXT=63
NEXT_=64
NID=65
OBJSET_=66
OBRACE=67
OCBRACE=68
OEBRACE=69
PLUS=70
PROC=71
PROC_=72
RANGE_=73
SEMICOLON=74
SEND_=75
SET=76
SETFUNC_=77
SET_=78
STABLE=79
STABLE_=80
STATE=81
TRANS_=82
WHEN=83
WHEN_=84
WS=85

# token names
tokenNamesMap = {
    0: "<invalid>", 1: "<EOR>", 2: "<DOWN>", 3: "<UP>",
    -1: "EOF", 86: "T__86", 87: "T__87", 88: "T__88", 89: "T__89", 90: "T__90", 
    91: "T__91", 92: "T__92", 93: "T__93", 94: "T__94", 95: "T__95", 96: "T__96", 
    97: "T__97", 98: "T__98", 99: "T__99", 100: "T__100", 101: "T__101", 
    102: "T__102", 4: "ACCESS", 5: "ARCH", 6: "ARCH_", 7: "ARRAY", 8: "ARRAY_", 
    9: "ASSIGN_", 10: "AWAIT", 11: "AWAIT_", 12: "BOOL", 13: "BOOLID", 14: "BOOL_", 
    15: "BREAK", 16: "BREAK_", 17: "CACHE", 18: "CACHE_", 19: "CBRACE", 
    20: "CCBRACE", 21: "CEBRACE", 22: "COMMA", 23: "COMMENT", 24: "COND_", 
    25: "CONSTANT", 26: "CONSTANT_", 27: "DATA", 28: "DATA_", 29: "DDOT", 
    30: "DIR", 31: "DIR_", 32: "DOT", 33: "ELEMENT_", 34: "ELSE", 35: "ENDIFELSE_", 
    36: "ENDIF_", 37: "ENDPROC_", 38: "ENDWHEN_", 39: "EQUALSIGN", 40: "FIFO", 
    41: "FIFO_", 42: "GUARD_", 43: "ID", 44: "ID_", 45: "IF", 46: "IFELSE_", 
    47: "IF_", 48: "INITSTATE_", 49: "INITVAL_", 50: "INT", 51: "INTID", 
    52: "INT_", 53: "LINE_COMMENT", 54: "MACHN_", 55: "MCAST_", 56: "MINUS", 
    57: "MSG", 58: "MSGCSTR_", 59: "MSG_", 60: "NCOND_", 61: "NETWORK", 
    62: "NETWORK_", 63: "NEXT", 64: "NEXT_", 65: "NID", 66: "OBJSET_", 67: "OBRACE", 
    68: "OCBRACE", 69: "OEBRACE", 70: "PLUS", 71: "PROC", 72: "PROC_", 73: "RANGE_", 
    74: "SEMICOLON", 75: "SEND_", 76: "SET", 77: "SETFUNC_", 78: "SET_", 
    79: "STABLE", 80: "STABLE_", 81: "STATE", 82: "TRANS_", 83: "WHEN", 
    84: "WHEN_", 85: "WS"
}
Token.registerTokenNamesMap(tokenNamesMap)

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ACCESS", "ARCH", "ARCH_", "ARRAY", "ARRAY_", "ASSIGN_", "AWAIT", "AWAIT_", 
    "BOOL", "BOOLID", "BOOL_", "BREAK", "BREAK_", "CACHE", "CACHE_", "CBRACE", 
    "CCBRACE", "CEBRACE", "COMMA", "COMMENT", "COND_", "CONSTANT", "CONSTANT_", 
    "DATA", "DATA_", "DDOT", "DIR", "DIR_", "DOT", "ELEMENT_", "ELSE", "ENDIFELSE_", 
    "ENDIF_", "ENDPROC_", "ENDWHEN_", "EQUALSIGN", "FIFO", "FIFO_", "GUARD_", 
    "ID", "ID_", "IF", "IFELSE_", "IF_", "INITSTATE_", "INITVAL_", "INT", 
    "INTID", "INT_", "LINE_COMMENT", "MACHN_", "MCAST_", "MINUS", "MSG", 
    "MSGCSTR_", "MSG_", "NCOND_", "NETWORK", "NETWORK_", "NEXT", "NEXT_", 
    "NID", "OBJSET_", "OBRACE", "OCBRACE", "OEBRACE", "PLUS", "PROC", "PROC_", 
    "RANGE_", "SEMICOLON", "SEND_", "SET", "SETFUNC_", "SET_", "STABLE", 
    "STABLE_", "STATE", "TRANS_", "WHEN", "WHEN_", "WS", "'!='", "'&'", 
    "'<'", "'<='", "'=='", "'>'", "'>='", "'Ordered'", "'Unordered'", "'add'", 
    "'clear'", "'contains'", "'count'", "'del'", "'mcast'", "'send'", "'|'"
]



class ProtoCCParser(Parser):
    grammarFileName = "/home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g"
    api_version = 1
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super().__init__(input, state, *args, **kwargs)




        self.delegates = []

        self._adaptor = None
        self.adaptor = CommonTreeAdaptor()



    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)


    class send_function_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "send_function"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:109:1: send_function : 'send' ;
    def send_function(self, ):
        retval = self.send_function_return()
        retval.start = self.input.LT(1)


        root_0 = None

        string_literal1 = None

        string_literal1_tree = None

        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:110:2: ( 'send' )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:110:4: 'send'
                pass 
                root_0 = self._adaptor.nil()


                string_literal1 = self.match(self.input, 101, self.FOLLOW_101_in_send_function571)
                string_literal1_tree = self._adaptor.createWithPayload(string_literal1)
                self._adaptor.addChild(root_0, string_literal1_tree)





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "send_function"


    class mcast_function_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "mcast_function"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:113:1: mcast_function : 'mcast' ;
    def mcast_function(self, ):
        retval = self.mcast_function_return()
        retval.start = self.input.LT(1)


        root_0 = None

        string_literal2 = None

        string_literal2_tree = None

        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:114:2: ( 'mcast' )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:114:4: 'mcast'
                pass 
                root_0 = self._adaptor.nil()


                string_literal2 = self.match(self.input, 100, self.FOLLOW_100_in_mcast_function582)
                string_literal2_tree = self._adaptor.createWithPayload(string_literal2)
                self._adaptor.addChild(root_0, string_literal2_tree)





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "mcast_function"


    class set_function_types_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "set_function_types"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:117:1: set_function_types : ( 'add' | 'count' | 'contains' | 'del' | 'clear' );
    def set_function_types(self, ):
        retval = self.set_function_types_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set3 = None

        set3_tree = None

        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:118:2: ( 'add' | 'count' | 'contains' | 'del' | 'clear' )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:
                pass 
                root_0 = self._adaptor.nil()


                set3 = self.input.LT(1)

                if (95 <= self.input.LA(1) <= 99) or self.input.LA(1) in {}:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set3))

                    self._state.errorRecovery = False


                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "set_function_types"


    class relational_operator_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "relational_operator"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:125:1: relational_operator : ( '==' | '!=' | '<=' | '>=' | '<' | '>' );
    def relational_operator(self, ):
        retval = self.relational_operator_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set4 = None

        set4_tree = None

        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:126:2: ( '==' | '!=' | '<=' | '>=' | '<' | '>' )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:
                pass 
                root_0 = self._adaptor.nil()


                set4 = self.input.LT(1)

                if (88 <= self.input.LA(1) <= 92) or self.input.LA(1) in {86}:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set4))

                    self._state.errorRecovery = False


                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "relational_operator"


    class combinatorial_operator_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "combinatorial_operator"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:134:1: combinatorial_operator : ( '&' | '|' );
    def combinatorial_operator(self, ):
        retval = self.combinatorial_operator_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set5 = None

        set5_tree = None

        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:135:5: ( '&' | '|' )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:
                pass 
                root_0 = self._adaptor.nil()


                set5 = self.input.LT(1)

                if self.input.LA(1) in {87, 102}:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set5))

                    self._state.errorRecovery = False


                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "combinatorial_operator"


    class document_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "document"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:164:1: document : ( const_decl | init_hw | arch_block | expressions )* ;
    def document(self, ):
        retval = self.document_return()
        retval.start = self.input.LT(1)


        root_0 = None

        const_decl6 = None
        init_hw7 = None
        arch_block8 = None
        expressions9 = None


        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:165:2: ( ( const_decl | init_hw | arch_block | expressions )* )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:165:4: ( const_decl | init_hw | arch_block | expressions )*
                pass 
                root_0 = self._adaptor.nil()


                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:165:4: ( const_decl | init_hw | arch_block | expressions )*
                while True: #loop1
                    alt1 = 5
                    LA1 = self.input.LA(1)
                    if LA1 in {CONSTANT}:
                        alt1 = 1
                    elif LA1 in {CACHE, DIR, MSG, NETWORK}:
                        alt1 = 2
                    elif LA1 in {ARCH}:
                        alt1 = 3
                    elif LA1 in {ID, IF, STATE}:
                        alt1 = 4

                    if alt1 == 1:
                        # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:165:5: const_decl
                        pass 
                        self._state.following.append(self.FOLLOW_const_decl_in_document903)
                        const_decl6 = self.const_decl()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, const_decl6.tree)



                    elif alt1 == 2:
                        # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:165:18: init_hw
                        pass 
                        self._state.following.append(self.FOLLOW_init_hw_in_document907)
                        init_hw7 = self.init_hw()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, init_hw7.tree)



                    elif alt1 == 3:
                        # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:165:28: arch_block
                        pass 
                        self._state.following.append(self.FOLLOW_arch_block_in_document911)
                        arch_block8 = self.arch_block()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, arch_block8.tree)



                    elif alt1 == 4:
                        # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:165:41: expressions
                        pass 
                        self._state.following.append(self.FOLLOW_expressions_in_document915)
                        expressions9 = self.expressions()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, expressions9.tree)



                    else:
                        break #loop1




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "document"


    class declarations_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "declarations"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:169:1: declarations : ( int_decl | bool_decl | state_decl | data_decl | id_decl );
    def declarations(self, ):
        retval = self.declarations_return()
        retval.start = self.input.LT(1)


        root_0 = None

        int_decl10 = None
        bool_decl11 = None
        state_decl12 = None
        data_decl13 = None
        id_decl14 = None


        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:169:14: ( int_decl | bool_decl | state_decl | data_decl | id_decl )
                alt2 = 5
                LA2 = self.input.LA(1)
                if LA2 in {INTID}:
                    alt2 = 1
                elif LA2 in {BOOLID}:
                    alt2 = 2
                elif LA2 in {STATE}:
                    alt2 = 3
                elif LA2 in {DATA}:
                    alt2 = 4
                elif LA2 in {NID, SET}:
                    alt2 = 5
                else:
                    nvae = NoViableAltException("", 2, 0, self.input)

                    raise nvae


                if alt2 == 1:
                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:169:16: int_decl
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_int_decl_in_declarations928)
                    int_decl10 = self.int_decl()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, int_decl10.tree)



                elif alt2 == 2:
                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:169:27: bool_decl
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_bool_decl_in_declarations932)
                    bool_decl11 = self.bool_decl()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, bool_decl11.tree)



                elif alt2 == 3:
                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:169:39: state_decl
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_state_decl_in_declarations936)
                    state_decl12 = self.state_decl()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, state_decl12.tree)



                elif alt2 == 4:
                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:169:52: data_decl
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_data_decl_in_declarations940)
                    data_decl13 = self.data_decl()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, data_decl13.tree)



                elif alt2 == 5:
                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:169:64: id_decl
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_id_decl_in_declarations944)
                    id_decl14 = self.id_decl()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, id_decl14.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "declarations"


    class const_decl_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "const_decl"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:171:5: const_decl : CONSTANT ID INT -> ^( CONSTANT_ ID INT ) ;
    def const_decl(self, ):
        retval = self.const_decl_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CONSTANT15 = None
        ID16 = None
        INT17 = None

        CONSTANT15_tree = None
        ID16_tree = None
        INT17_tree = None
        stream_CONSTANT = RewriteRuleTokenStream(self._adaptor, "token CONSTANT")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INT = RewriteRuleTokenStream(self._adaptor, "token INT")

        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:171:16: ( CONSTANT ID INT -> ^( CONSTANT_ ID INT ) )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:171:18: CONSTANT ID INT
                pass 
                CONSTANT15 = self.match(self.input, CONSTANT, self.FOLLOW_CONSTANT_in_const_decl956) 
                stream_CONSTANT.add(CONSTANT15)


                ID16 = self.match(self.input, ID, self.FOLLOW_ID_in_const_decl958) 
                stream_ID.add(ID16)


                INT17 = self.match(self.input, INT, self.FOLLOW_INT_in_const_decl960) 
                stream_INT.add(INT17)


                # AST Rewrite
                # elements: ID, INT
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 171:34: -> ^( CONSTANT_ ID INT )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:171:37: ^( CONSTANT_ ID INT )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(CONSTANT_, "CONSTANT_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_1, 
                stream_INT.nextNode()
                )

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "const_decl"


    class int_decl_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "int_decl"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:173:5: int_decl : INTID range ID ( EQUALSIGN INT )* SEMICOLON -> ^( INT_ range ID ( INITVAL_ INT )* ) ;
    def int_decl(self, ):
        retval = self.int_decl_return()
        retval.start = self.input.LT(1)


        root_0 = None

        INTID18 = None
        ID20 = None
        EQUALSIGN21 = None
        INT22 = None
        SEMICOLON23 = None
        range19 = None

        INTID18_tree = None
        ID20_tree = None
        EQUALSIGN21_tree = None
        INT22_tree = None
        SEMICOLON23_tree = None
        stream_EQUALSIGN = RewriteRuleTokenStream(self._adaptor, "token EQUALSIGN")
        stream_INTID = RewriteRuleTokenStream(self._adaptor, "token INTID")
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INT = RewriteRuleTokenStream(self._adaptor, "token INT")
        stream_range = RewriteRuleSubtreeStream(self._adaptor, "rule range")
        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:173:14: ( INTID range ID ( EQUALSIGN INT )* SEMICOLON -> ^( INT_ range ID ( INITVAL_ INT )* ) )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:173:16: INTID range ID ( EQUALSIGN INT )* SEMICOLON
                pass 
                INTID18 = self.match(self.input, INTID, self.FOLLOW_INTID_in_int_decl982) 
                stream_INTID.add(INTID18)


                self._state.following.append(self.FOLLOW_range_in_int_decl984)
                range19 = self.range()

                self._state.following.pop()
                stream_range.add(range19.tree)


                ID20 = self.match(self.input, ID, self.FOLLOW_ID_in_int_decl986) 
                stream_ID.add(ID20)


                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:173:31: ( EQUALSIGN INT )*
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == EQUALSIGN) :
                        alt3 = 1


                    if alt3 == 1:
                        # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:173:32: EQUALSIGN INT
                        pass 
                        EQUALSIGN21 = self.match(self.input, EQUALSIGN, self.FOLLOW_EQUALSIGN_in_int_decl989) 
                        stream_EQUALSIGN.add(EQUALSIGN21)


                        INT22 = self.match(self.input, INT, self.FOLLOW_INT_in_int_decl991) 
                        stream_INT.add(INT22)



                    else:
                        break #loop3


                SEMICOLON23 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_int_decl995) 
                stream_SEMICOLON.add(SEMICOLON23)


                # AST Rewrite
                # elements: range, ID, INT
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 173:58: -> ^( INT_ range ID ( INITVAL_ INT )* )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:173:61: ^( INT_ range ID ( INITVAL_ INT )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(INT_, "INT_")
                , root_1)

                self._adaptor.addChild(root_1, stream_range.nextTree())

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:173:77: ( INITVAL_ INT )*
                while stream_INT.hasNext():
                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(INITVAL_, "INITVAL_")
                    )

                    self._adaptor.addChild(root_1, 
                    stream_INT.nextNode()
                    )


                stream_INT.reset();

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "int_decl"


    class bool_decl_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "bool_decl"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:174:5: bool_decl : BOOLID ID ( EQUALSIGN BOOL )* SEMICOLON -> ^( BOOL_ ID ( INITVAL_ BOOL )* ) ;
    def bool_decl(self, ):
        retval = self.bool_decl_return()
        retval.start = self.input.LT(1)


        root_0 = None

        BOOLID24 = None
        ID25 = None
        EQUALSIGN26 = None
        BOOL27 = None
        SEMICOLON28 = None

        BOOLID24_tree = None
        ID25_tree = None
        EQUALSIGN26_tree = None
        BOOL27_tree = None
        SEMICOLON28_tree = None
        stream_EQUALSIGN = RewriteRuleTokenStream(self._adaptor, "token EQUALSIGN")
        stream_BOOL = RewriteRuleTokenStream(self._adaptor, "token BOOL")
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_BOOLID = RewriteRuleTokenStream(self._adaptor, "token BOOLID")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:174:15: ( BOOLID ID ( EQUALSIGN BOOL )* SEMICOLON -> ^( BOOL_ ID ( INITVAL_ BOOL )* ) )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:174:17: BOOLID ID ( EQUALSIGN BOOL )* SEMICOLON
                pass 
                BOOLID24 = self.match(self.input, BOOLID, self.FOLLOW_BOOLID_in_bool_decl1023) 
                stream_BOOLID.add(BOOLID24)


                ID25 = self.match(self.input, ID, self.FOLLOW_ID_in_bool_decl1025) 
                stream_ID.add(ID25)


                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:174:27: ( EQUALSIGN BOOL )*
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == EQUALSIGN) :
                        alt4 = 1


                    if alt4 == 1:
                        # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:174:28: EQUALSIGN BOOL
                        pass 
                        EQUALSIGN26 = self.match(self.input, EQUALSIGN, self.FOLLOW_EQUALSIGN_in_bool_decl1028) 
                        stream_EQUALSIGN.add(EQUALSIGN26)


                        BOOL27 = self.match(self.input, BOOL, self.FOLLOW_BOOL_in_bool_decl1030) 
                        stream_BOOL.add(BOOL27)



                    else:
                        break #loop4


                SEMICOLON28 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_bool_decl1034) 
                stream_SEMICOLON.add(SEMICOLON28)


                # AST Rewrite
                # elements: ID, BOOL
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 174:55: -> ^( BOOL_ ID ( INITVAL_ BOOL )* )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:174:58: ^( BOOL_ ID ( INITVAL_ BOOL )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(BOOL_, "BOOL_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:174:69: ( INITVAL_ BOOL )*
                while stream_BOOL.hasNext():
                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(INITVAL_, "INITVAL_")
                    )

                    self._adaptor.addChild(root_1, 
                    stream_BOOL.nextNode()
                    )


                stream_BOOL.reset();

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "bool_decl"


    class state_decl_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "state_decl"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:176:5: state_decl : STATE ID SEMICOLON -> ^( INITSTATE_ ID ) ;
    def state_decl(self, ):
        retval = self.state_decl_return()
        retval.start = self.input.LT(1)


        root_0 = None

        STATE29 = None
        ID30 = None
        SEMICOLON31 = None

        STATE29_tree = None
        ID30_tree = None
        SEMICOLON31_tree = None
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_STATE = RewriteRuleTokenStream(self._adaptor, "token STATE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:176:16: ( STATE ID SEMICOLON -> ^( INITSTATE_ ID ) )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:176:18: STATE ID SEMICOLON
                pass 
                STATE29 = self.match(self.input, STATE, self.FOLLOW_STATE_in_state_decl1061) 
                stream_STATE.add(STATE29)


                ID30 = self.match(self.input, ID, self.FOLLOW_ID_in_state_decl1063) 
                stream_ID.add(ID30)


                SEMICOLON31 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_state_decl1065) 
                stream_SEMICOLON.add(SEMICOLON31)


                # AST Rewrite
                # elements: ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 176:37: -> ^( INITSTATE_ ID )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:176:40: ^( INITSTATE_ ID )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(INITSTATE_, "INITSTATE_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "state_decl"


    class data_decl_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "data_decl"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:177:5: data_decl : DATA ID SEMICOLON -> ^( DATA_ ID ) ;
    def data_decl(self, ):
        retval = self.data_decl_return()
        retval.start = self.input.LT(1)


        root_0 = None

        DATA32 = None
        ID33 = None
        SEMICOLON34 = None

        DATA32_tree = None
        ID33_tree = None
        SEMICOLON34_tree = None
        stream_DATA = RewriteRuleTokenStream(self._adaptor, "token DATA")
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:177:15: ( DATA ID SEMICOLON -> ^( DATA_ ID ) )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:177:17: DATA ID SEMICOLON
                pass 
                DATA32 = self.match(self.input, DATA, self.FOLLOW_DATA_in_data_decl1084) 
                stream_DATA.add(DATA32)


                ID33 = self.match(self.input, ID, self.FOLLOW_ID_in_data_decl1086) 
                stream_ID.add(ID33)


                SEMICOLON34 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_data_decl1088) 
                stream_SEMICOLON.add(SEMICOLON34)


                # AST Rewrite
                # elements: ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 177:35: -> ^( DATA_ ID )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:177:38: ^( DATA_ ID )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(DATA_, "DATA_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "data_decl"


    class id_decl_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "id_decl"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:178:5: id_decl : ( set_decl )* NID ID SEMICOLON -> ^( ID_ ( set_decl )* ID ) ;
    def id_decl(self, ):
        retval = self.id_decl_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NID36 = None
        ID37 = None
        SEMICOLON38 = None
        set_decl35 = None

        NID36_tree = None
        ID37_tree = None
        SEMICOLON38_tree = None
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_NID = RewriteRuleTokenStream(self._adaptor, "token NID")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_set_decl = RewriteRuleSubtreeStream(self._adaptor, "rule set_decl")
        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:178:13: ( ( set_decl )* NID ID SEMICOLON -> ^( ID_ ( set_decl )* ID ) )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:178:15: ( set_decl )* NID ID SEMICOLON
                pass 
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:178:15: ( set_decl )*
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == SET) :
                        alt5 = 1


                    if alt5 == 1:
                        # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:178:15: set_decl
                        pass 
                        self._state.following.append(self.FOLLOW_set_decl_in_id_decl1107)
                        set_decl35 = self.set_decl()

                        self._state.following.pop()
                        stream_set_decl.add(set_decl35.tree)



                    else:
                        break #loop5


                NID36 = self.match(self.input, NID, self.FOLLOW_NID_in_id_decl1110) 
                stream_NID.add(NID36)


                ID37 = self.match(self.input, ID, self.FOLLOW_ID_in_id_decl1112) 
                stream_ID.add(ID37)


                SEMICOLON38 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_id_decl1114) 
                stream_SEMICOLON.add(SEMICOLON38)


                # AST Rewrite
                # elements: set_decl, ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 178:42: -> ^( ID_ ( set_decl )* ID )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:178:45: ^( ID_ ( set_decl )* ID )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(ID_, "ID_")
                , root_1)

                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:178:51: ( set_decl )*
                while stream_set_decl.hasNext():
                    self._adaptor.addChild(root_1, stream_set_decl.nextTree())


                stream_set_decl.reset();

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "id_decl"


    class set_decl_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "set_decl"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:179:5: set_decl : SET OEBRACE val_range CEBRACE -> ^( SET_ val_range ) ;
    def set_decl(self, ):
        retval = self.set_decl_return()
        retval.start = self.input.LT(1)


        root_0 = None

        SET39 = None
        OEBRACE40 = None
        CEBRACE42 = None
        val_range41 = None

        SET39_tree = None
        OEBRACE40_tree = None
        CEBRACE42_tree = None
        stream_SET = RewriteRuleTokenStream(self._adaptor, "token SET")
        stream_CEBRACE = RewriteRuleTokenStream(self._adaptor, "token CEBRACE")
        stream_OEBRACE = RewriteRuleTokenStream(self._adaptor, "token OEBRACE")
        stream_val_range = RewriteRuleSubtreeStream(self._adaptor, "rule val_range")
        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:179:14: ( SET OEBRACE val_range CEBRACE -> ^( SET_ val_range ) )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:179:16: SET OEBRACE val_range CEBRACE
                pass 
                SET39 = self.match(self.input, SET, self.FOLLOW_SET_in_set_decl1136) 
                stream_SET.add(SET39)


                OEBRACE40 = self.match(self.input, OEBRACE, self.FOLLOW_OEBRACE_in_set_decl1138) 
                stream_OEBRACE.add(OEBRACE40)


                self._state.following.append(self.FOLLOW_val_range_in_set_decl1140)
                val_range41 = self.val_range()

                self._state.following.pop()
                stream_val_range.add(val_range41.tree)


                CEBRACE42 = self.match(self.input, CEBRACE, self.FOLLOW_CEBRACE_in_set_decl1142) 
                stream_CEBRACE.add(CEBRACE42)


                # AST Rewrite
                # elements: val_range
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 179:46: -> ^( SET_ val_range )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:179:49: ^( SET_ val_range )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(SET_, "SET_")
                , root_1)

                self._adaptor.addChild(root_1, stream_val_range.nextTree())

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "set_decl"


    class objset_decl_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "objset_decl"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:180:5: objset_decl : SET OEBRACE val_range CEBRACE -> ^( OBJSET_ val_range ) ;
    def objset_decl(self, ):
        retval = self.objset_decl_return()
        retval.start = self.input.LT(1)


        root_0 = None

        SET43 = None
        OEBRACE44 = None
        CEBRACE46 = None
        val_range45 = None

        SET43_tree = None
        OEBRACE44_tree = None
        CEBRACE46_tree = None
        stream_SET = RewriteRuleTokenStream(self._adaptor, "token SET")
        stream_CEBRACE = RewriteRuleTokenStream(self._adaptor, "token CEBRACE")
        stream_OEBRACE = RewriteRuleTokenStream(self._adaptor, "token OEBRACE")
        stream_val_range = RewriteRuleSubtreeStream(self._adaptor, "rule val_range")
        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:180:17: ( SET OEBRACE val_range CEBRACE -> ^( OBJSET_ val_range ) )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:180:19: SET OEBRACE val_range CEBRACE
                pass 
                SET43 = self.match(self.input, SET, self.FOLLOW_SET_in_objset_decl1161) 
                stream_SET.add(SET43)


                OEBRACE44 = self.match(self.input, OEBRACE, self.FOLLOW_OEBRACE_in_objset_decl1163) 
                stream_OEBRACE.add(OEBRACE44)


                self._state.following.append(self.FOLLOW_val_range_in_objset_decl1165)
                val_range45 = self.val_range()

                self._state.following.pop()
                stream_val_range.add(val_range45.tree)


                CEBRACE46 = self.match(self.input, CEBRACE, self.FOLLOW_CEBRACE_in_objset_decl1167) 
                stream_CEBRACE.add(CEBRACE46)


                # AST Rewrite
                # elements: val_range
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 180:49: -> ^( OBJSET_ val_range )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:180:52: ^( OBJSET_ val_range )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(OBJSET_, "OBJSET_")
                , root_1)

                self._adaptor.addChild(root_1, stream_val_range.nextTree())

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "objset_decl"


    class range_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "range"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:182:9: range : OEBRACE val_range DOT DOT val_range CEBRACE -> ^( RANGE_ OEBRACE val_range DOT DOT val_range CEBRACE ) ;
    def range(self, ):
        retval = self.range_return()
        retval.start = self.input.LT(1)


        root_0 = None

        OEBRACE47 = None
        DOT49 = None
        DOT50 = None
        CEBRACE52 = None
        val_range48 = None
        val_range51 = None

        OEBRACE47_tree = None
        DOT49_tree = None
        DOT50_tree = None
        CEBRACE52_tree = None
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")
        stream_CEBRACE = RewriteRuleTokenStream(self._adaptor, "token CEBRACE")
        stream_OEBRACE = RewriteRuleTokenStream(self._adaptor, "token OEBRACE")
        stream_val_range = RewriteRuleSubtreeStream(self._adaptor, "rule val_range")
        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:182:15: ( OEBRACE val_range DOT DOT val_range CEBRACE -> ^( RANGE_ OEBRACE val_range DOT DOT val_range CEBRACE ) )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:182:17: OEBRACE val_range DOT DOT val_range CEBRACE
                pass 
                OEBRACE47 = self.match(self.input, OEBRACE, self.FOLLOW_OEBRACE_in_range1191) 
                stream_OEBRACE.add(OEBRACE47)


                self._state.following.append(self.FOLLOW_val_range_in_range1193)
                val_range48 = self.val_range()

                self._state.following.pop()
                stream_val_range.add(val_range48.tree)


                DOT49 = self.match(self.input, DOT, self.FOLLOW_DOT_in_range1195) 
                stream_DOT.add(DOT49)


                DOT50 = self.match(self.input, DOT, self.FOLLOW_DOT_in_range1197) 
                stream_DOT.add(DOT50)


                self._state.following.append(self.FOLLOW_val_range_in_range1199)
                val_range51 = self.val_range()

                self._state.following.pop()
                stream_val_range.add(val_range51.tree)


                CEBRACE52 = self.match(self.input, CEBRACE, self.FOLLOW_CEBRACE_in_range1201) 
                stream_CEBRACE.add(CEBRACE52)


                # AST Rewrite
                # elements: OEBRACE, val_range, DOT, DOT, val_range, CEBRACE
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 182:61: -> ^( RANGE_ OEBRACE val_range DOT DOT val_range CEBRACE )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:182:64: ^( RANGE_ OEBRACE val_range DOT DOT val_range CEBRACE )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(RANGE_, "RANGE_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_OEBRACE.nextNode()
                )

                self._adaptor.addChild(root_1, stream_val_range.nextTree())

                self._adaptor.addChild(root_1, 
                stream_DOT.nextNode()
                )

                self._adaptor.addChild(root_1, 
                stream_DOT.nextNode()
                )

                self._adaptor.addChild(root_1, stream_val_range.nextTree())

                self._adaptor.addChild(root_1, 
                stream_CEBRACE.nextNode()
                )

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "range"


    class val_range_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "val_range"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:183:9: val_range : ( INT | ID );
    def val_range(self, ):
        retval = self.val_range_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set53 = None

        set53_tree = None

        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:183:19: ( INT | ID )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:
                pass 
                root_0 = self._adaptor.nil()


                set53 = self.input.LT(1)

                if self.input.LA(1) in {ID, INT}:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set53))

                    self._state.errorRecovery = False


                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "val_range"


    class array_decl_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "array_decl"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:185:5: array_decl : ARRAY range ;
    def array_decl(self, ):
        retval = self.array_decl_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ARRAY54 = None
        range55 = None

        ARRAY54_tree = None

        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:185:16: ( ARRAY range )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:185:18: ARRAY range
                pass 
                root_0 = self._adaptor.nil()


                ARRAY54 = self.match(self.input, ARRAY, self.FOLLOW_ARRAY_in_array_decl1250)
                ARRAY54_tree = self._adaptor.createWithPayload(ARRAY54)
                self._adaptor.addChild(root_0, ARRAY54_tree)



                self._state.following.append(self.FOLLOW_range_in_array_decl1252)
                range55 = self.range()

                self._state.following.pop()
                self._adaptor.addChild(root_0, range55.tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "array_decl"


    class fifo_decl_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "fifo_decl"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:186:5: fifo_decl : FIFO range ;
    def fifo_decl(self, ):
        retval = self.fifo_decl_return()
        retval.start = self.input.LT(1)


        root_0 = None

        FIFO56 = None
        range57 = None

        FIFO56_tree = None

        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:186:14: ( FIFO range )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:186:16: FIFO range
                pass 
                root_0 = self._adaptor.nil()


                FIFO56 = self.match(self.input, FIFO, self.FOLLOW_FIFO_in_fifo_decl1262)
                FIFO56_tree = self._adaptor.createWithPayload(FIFO56)
                self._adaptor.addChild(root_0, FIFO56_tree)



                self._state.following.append(self.FOLLOW_range_in_fifo_decl1264)
                range57 = self.range()

                self._state.following.pop()
                self._adaptor.addChild(root_0, range57.tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "fifo_decl"


    class init_hw_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "init_hw"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:189:1: init_hw : ( network_block | machines | message_block );
    def init_hw(self, ):
        retval = self.init_hw_return()
        retval.start = self.input.LT(1)


        root_0 = None

        network_block58 = None
        machines59 = None
        message_block60 = None


        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:189:9: ( network_block | machines | message_block )
                alt6 = 3
                LA6 = self.input.LA(1)
                if LA6 in {NETWORK}:
                    alt6 = 1
                elif LA6 in {CACHE, DIR}:
                    alt6 = 2
                elif LA6 in {MSG}:
                    alt6 = 3
                else:
                    nvae = NoViableAltException("", 6, 0, self.input)

                    raise nvae


                if alt6 == 1:
                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:189:11: network_block
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_network_block_in_init_hw1274)
                    network_block58 = self.network_block()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, network_block58.tree)



                elif alt6 == 2:
                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:189:27: machines
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_machines_in_init_hw1278)
                    machines59 = self.machines()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, machines59.tree)



                elif alt6 == 3:
                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:189:38: message_block
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_message_block_in_init_hw1282)
                    message_block60 = self.message_block()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, message_block60.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "init_hw"


    class object_block_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "object_block"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:190:5: object_block : object_expr SEMICOLON -> object_expr ;
    def object_block(self, ):
        retval = self.object_block_return()
        retval.start = self.input.LT(1)


        root_0 = None

        SEMICOLON62 = None
        object_expr61 = None

        SEMICOLON62_tree = None
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_object_expr = RewriteRuleSubtreeStream(self._adaptor, "rule object_expr")
        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:190:18: ( object_expr SEMICOLON -> object_expr )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:190:20: object_expr SEMICOLON
                pass 
                self._state.following.append(self.FOLLOW_object_expr_in_object_block1293)
                object_expr61 = self.object_expr()

                self._state.following.pop()
                stream_object_expr.add(object_expr61.tree)


                SEMICOLON62 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_object_block1295) 
                stream_SEMICOLON.add(SEMICOLON62)


                # AST Rewrite
                # elements: object_expr
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 190:42: -> object_expr
                self._adaptor.addChild(root_0, stream_object_expr.nextTree())




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "object_block"


    class object_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "object_expr"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:191:5: object_expr : ( ID | object_func );
    def object_expr(self, ):
        retval = self.object_expr_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID63 = None
        object_func64 = None

        ID63_tree = None

        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:191:17: ( ID | object_func )
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == ID) :
                    LA7_1 = self.input.LA(2)

                    if (LA7_1 == DOT) :
                        alt7 = 2
                    elif ((86 <= LA7_1 <= 92) or LA7_1 in {BOOL, CBRACE, COMMA, ID, INT, NID, OCBRACE, SEMICOLON, 102}) :
                        alt7 = 1
                    else:
                        nvae = NoViableAltException("", 7, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 7, 0, self.input)

                    raise nvae


                if alt7 == 1:
                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:191:19: ID
                    pass 
                    root_0 = self._adaptor.nil()


                    ID63 = self.match(self.input, ID, self.FOLLOW_ID_in_object_expr1310)
                    ID63_tree = self._adaptor.createWithPayload(ID63)
                    self._adaptor.addChild(root_0, ID63_tree)




                elif alt7 == 2:
                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:191:24: object_func
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_object_func_in_object_expr1314)
                    object_func64 = self.object_func()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, object_func64.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "object_expr"


    class object_func_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "object_func"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:192:5: object_func : ID DOT object_idres ( OBRACE ( object_expr )* ( COMMA object_expr )* CBRACE )* -> ^( ID DOT object_idres ( OBRACE ( object_expr )* ( COMMA object_expr )* CBRACE )* ) ;
    def object_func(self, ):
        retval = self.object_func_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID65 = None
        DOT66 = None
        OBRACE68 = None
        COMMA70 = None
        CBRACE72 = None
        object_idres67 = None
        object_expr69 = None
        object_expr71 = None

        ID65_tree = None
        DOT66_tree = None
        OBRACE68_tree = None
        COMMA70_tree = None
        CBRACE72_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_OBRACE = RewriteRuleTokenStream(self._adaptor, "token OBRACE")
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CBRACE = RewriteRuleTokenStream(self._adaptor, "token CBRACE")
        stream_object_idres = RewriteRuleSubtreeStream(self._adaptor, "rule object_idres")
        stream_object_expr = RewriteRuleSubtreeStream(self._adaptor, "rule object_expr")
        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:192:17: ( ID DOT object_idres ( OBRACE ( object_expr )* ( COMMA object_expr )* CBRACE )* -> ^( ID DOT object_idres ( OBRACE ( object_expr )* ( COMMA object_expr )* CBRACE )* ) )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:192:19: ID DOT object_idres ( OBRACE ( object_expr )* ( COMMA object_expr )* CBRACE )*
                pass 
                ID65 = self.match(self.input, ID, self.FOLLOW_ID_in_object_func1325) 
                stream_ID.add(ID65)


                DOT66 = self.match(self.input, DOT, self.FOLLOW_DOT_in_object_func1327) 
                stream_DOT.add(DOT66)


                self._state.following.append(self.FOLLOW_object_idres_in_object_func1329)
                object_idres67 = self.object_idres()

                self._state.following.pop()
                stream_object_idres.add(object_idres67.tree)


                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:192:39: ( OBRACE ( object_expr )* ( COMMA object_expr )* CBRACE )*
                while True: #loop10
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == OBRACE) :
                        alt10 = 1


                    if alt10 == 1:
                        # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:192:40: OBRACE ( object_expr )* ( COMMA object_expr )* CBRACE
                        pass 
                        OBRACE68 = self.match(self.input, OBRACE, self.FOLLOW_OBRACE_in_object_func1332) 
                        stream_OBRACE.add(OBRACE68)


                        # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:192:47: ( object_expr )*
                        while True: #loop8
                            alt8 = 2
                            LA8_0 = self.input.LA(1)

                            if (LA8_0 == ID) :
                                alt8 = 1


                            if alt8 == 1:
                                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:192:47: object_expr
                                pass 
                                self._state.following.append(self.FOLLOW_object_expr_in_object_func1334)
                                object_expr69 = self.object_expr()

                                self._state.following.pop()
                                stream_object_expr.add(object_expr69.tree)



                            else:
                                break #loop8


                        # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:192:60: ( COMMA object_expr )*
                        while True: #loop9
                            alt9 = 2
                            LA9_0 = self.input.LA(1)

                            if (LA9_0 == COMMA) :
                                alt9 = 1


                            if alt9 == 1:
                                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:192:61: COMMA object_expr
                                pass 
                                COMMA70 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_object_func1338) 
                                stream_COMMA.add(COMMA70)


                                self._state.following.append(self.FOLLOW_object_expr_in_object_func1340)
                                object_expr71 = self.object_expr()

                                self._state.following.pop()
                                stream_object_expr.add(object_expr71.tree)



                            else:
                                break #loop9


                        CBRACE72 = self.match(self.input, CBRACE, self.FOLLOW_CBRACE_in_object_func1344) 
                        stream_CBRACE.add(CBRACE72)



                    else:
                        break #loop10


                # AST Rewrite
                # elements: ID, DOT, object_idres, OBRACE, object_expr, COMMA, object_expr, CBRACE
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 192:90: -> ^( ID DOT object_idres ( OBRACE ( object_expr )* ( COMMA object_expr )* CBRACE )* )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:193:9: ^( ID DOT object_idres ( OBRACE ( object_expr )* ( COMMA object_expr )* CBRACE )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                stream_ID.nextNode()
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_DOT.nextNode()
                )

                self._adaptor.addChild(root_1, stream_object_idres.nextTree())

                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:193:31: ( OBRACE ( object_expr )* ( COMMA object_expr )* CBRACE )*
                while stream_OBRACE.hasNext() or stream_CBRACE.hasNext():
                    self._adaptor.addChild(root_1, 
                    stream_OBRACE.nextNode()
                    )

                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:193:39: ( object_expr )*
                    while stream_object_expr.hasNext():
                        self._adaptor.addChild(root_1, stream_object_expr.nextTree())


                    stream_object_expr.reset();

                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:193:52: ( COMMA object_expr )*
                    while stream_COMMA.hasNext() or stream_object_expr.hasNext():
                        self._adaptor.addChild(root_1, 
                        stream_COMMA.nextNode()
                        )

                        self._adaptor.addChild(root_1, stream_object_expr.nextTree())


                    stream_COMMA.reset();
                    stream_object_expr.reset();

                    self._adaptor.addChild(root_1, 
                    stream_CBRACE.nextNode()
                    )


                stream_OBRACE.reset();
                stream_CBRACE.reset();

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "object_func"


    class object_idres_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "object_idres"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:194:5: object_idres : ( ID | NID );
    def object_idres(self, ):
        retval = self.object_idres_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set73 = None

        set73_tree = None

        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:194:17: ( ID | NID )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:
                pass 
                root_0 = self._adaptor.nil()


                set73 = self.input.LT(1)

                if self.input.LA(1) in {ID, NID}:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set73))

                    self._state.errorRecovery = False


                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "object_idres"


    class machines_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "machines"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:197:5: machines : ( cache_block | dir_block );
    def machines(self, ):
        retval = self.machines_return()
        retval.start = self.input.LT(1)


        root_0 = None

        cache_block74 = None
        dir_block75 = None


        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:197:14: ( cache_block | dir_block )
                alt11 = 2
                LA11_0 = self.input.LA(1)

                if (LA11_0 == CACHE) :
                    alt11 = 1
                elif (LA11_0 == DIR) :
                    alt11 = 2
                else:
                    nvae = NoViableAltException("", 11, 0, self.input)

                    raise nvae


                if alt11 == 1:
                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:197:16: cache_block
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_cache_block_in_machines1413)
                    cache_block74 = self.cache_block()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, cache_block74.tree)



                elif alt11 == 2:
                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:197:30: dir_block
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_dir_block_in_machines1417)
                    dir_block75 = self.dir_block()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, dir_block75.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "machines"


    class cache_block_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "cache_block"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:198:9: cache_block : CACHE OCBRACE ( declarations )* CCBRACE ( objset_decl )* ID SEMICOLON -> ^( CACHE_ ID ( objset_decl )* ( declarations )* ) ;
    def cache_block(self, ):
        retval = self.cache_block_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CACHE76 = None
        OCBRACE77 = None
        CCBRACE79 = None
        ID81 = None
        SEMICOLON82 = None
        declarations78 = None
        objset_decl80 = None

        CACHE76_tree = None
        OCBRACE77_tree = None
        CCBRACE79_tree = None
        ID81_tree = None
        SEMICOLON82_tree = None
        stream_OCBRACE = RewriteRuleTokenStream(self._adaptor, "token OCBRACE")
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CACHE = RewriteRuleTokenStream(self._adaptor, "token CACHE")
        stream_CCBRACE = RewriteRuleTokenStream(self._adaptor, "token CCBRACE")
        stream_objset_decl = RewriteRuleSubtreeStream(self._adaptor, "rule objset_decl")
        stream_declarations = RewriteRuleSubtreeStream(self._adaptor, "rule declarations")
        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:198:21: ( CACHE OCBRACE ( declarations )* CCBRACE ( objset_decl )* ID SEMICOLON -> ^( CACHE_ ID ( objset_decl )* ( declarations )* ) )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:198:23: CACHE OCBRACE ( declarations )* CCBRACE ( objset_decl )* ID SEMICOLON
                pass 
                CACHE76 = self.match(self.input, CACHE, self.FOLLOW_CACHE_in_cache_block1432) 
                stream_CACHE.add(CACHE76)


                OCBRACE77 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_cache_block1434) 
                stream_OCBRACE.add(OCBRACE77)


                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:198:37: ( declarations )*
                while True: #loop12
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if (LA12_0 in {BOOLID, DATA, INTID, NID, SET, STATE}) :
                        alt12 = 1


                    if alt12 == 1:
                        # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:198:37: declarations
                        pass 
                        self._state.following.append(self.FOLLOW_declarations_in_cache_block1436)
                        declarations78 = self.declarations()

                        self._state.following.pop()
                        stream_declarations.add(declarations78.tree)



                    else:
                        break #loop12


                CCBRACE79 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_cache_block1439) 
                stream_CCBRACE.add(CCBRACE79)


                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:198:59: ( objset_decl )*
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if (LA13_0 == SET) :
                        alt13 = 1


                    if alt13 == 1:
                        # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:198:59: objset_decl
                        pass 
                        self._state.following.append(self.FOLLOW_objset_decl_in_cache_block1441)
                        objset_decl80 = self.objset_decl()

                        self._state.following.pop()
                        stream_objset_decl.add(objset_decl80.tree)



                    else:
                        break #loop13


                ID81 = self.match(self.input, ID, self.FOLLOW_ID_in_cache_block1444) 
                stream_ID.add(ID81)


                SEMICOLON82 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_cache_block1446) 
                stream_SEMICOLON.add(SEMICOLON82)


                # AST Rewrite
                # elements: ID, objset_decl, declarations
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 198:85: -> ^( CACHE_ ID ( objset_decl )* ( declarations )* )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:199:13: ^( CACHE_ ID ( objset_decl )* ( declarations )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(CACHE_, "CACHE_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:199:25: ( objset_decl )*
                while stream_objset_decl.hasNext():
                    self._adaptor.addChild(root_1, stream_objset_decl.nextTree())


                stream_objset_decl.reset();

                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:199:38: ( declarations )*
                while stream_declarations.hasNext():
                    self._adaptor.addChild(root_1, stream_declarations.nextTree())


                stream_declarations.reset();

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "cache_block"


    class dir_block_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "dir_block"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:200:9: dir_block : DIR OCBRACE ( declarations )* CCBRACE ( objset_decl )* ID SEMICOLON -> ^( DIR_ ID ( objset_decl )* ( declarations )* ) ;
    def dir_block(self, ):
        retval = self.dir_block_return()
        retval.start = self.input.LT(1)


        root_0 = None

        DIR83 = None
        OCBRACE84 = None
        CCBRACE86 = None
        ID88 = None
        SEMICOLON89 = None
        declarations85 = None
        objset_decl87 = None

        DIR83_tree = None
        OCBRACE84_tree = None
        CCBRACE86_tree = None
        ID88_tree = None
        SEMICOLON89_tree = None
        stream_OCBRACE = RewriteRuleTokenStream(self._adaptor, "token OCBRACE")
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_DIR = RewriteRuleTokenStream(self._adaptor, "token DIR")
        stream_CCBRACE = RewriteRuleTokenStream(self._adaptor, "token CCBRACE")
        stream_objset_decl = RewriteRuleSubtreeStream(self._adaptor, "rule objset_decl")
        stream_declarations = RewriteRuleSubtreeStream(self._adaptor, "rule declarations")
        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:200:19: ( DIR OCBRACE ( declarations )* CCBRACE ( objset_decl )* ID SEMICOLON -> ^( DIR_ ID ( objset_decl )* ( declarations )* ) )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:200:21: DIR OCBRACE ( declarations )* CCBRACE ( objset_decl )* ID SEMICOLON
                pass 
                DIR83 = self.match(self.input, DIR, self.FOLLOW_DIR_in_dir_block1487) 
                stream_DIR.add(DIR83)


                OCBRACE84 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_dir_block1489) 
                stream_OCBRACE.add(OCBRACE84)


                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:200:33: ( declarations )*
                while True: #loop14
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if (LA14_0 in {BOOLID, DATA, INTID, NID, SET, STATE}) :
                        alt14 = 1


                    if alt14 == 1:
                        # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:200:33: declarations
                        pass 
                        self._state.following.append(self.FOLLOW_declarations_in_dir_block1491)
                        declarations85 = self.declarations()

                        self._state.following.pop()
                        stream_declarations.add(declarations85.tree)



                    else:
                        break #loop14


                CCBRACE86 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_dir_block1494) 
                stream_CCBRACE.add(CCBRACE86)


                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:200:55: ( objset_decl )*
                while True: #loop15
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if (LA15_0 == SET) :
                        alt15 = 1


                    if alt15 == 1:
                        # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:200:55: objset_decl
                        pass 
                        self._state.following.append(self.FOLLOW_objset_decl_in_dir_block1496)
                        objset_decl87 = self.objset_decl()

                        self._state.following.pop()
                        stream_objset_decl.add(objset_decl87.tree)



                    else:
                        break #loop15


                ID88 = self.match(self.input, ID, self.FOLLOW_ID_in_dir_block1499) 
                stream_ID.add(ID88)


                SEMICOLON89 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_dir_block1501) 
                stream_SEMICOLON.add(SEMICOLON89)


                # AST Rewrite
                # elements: ID, objset_decl, declarations
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 200:81: -> ^( DIR_ ID ( objset_decl )* ( declarations )* )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:201:13: ^( DIR_ ID ( objset_decl )* ( declarations )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(DIR_, "DIR_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:201:23: ( objset_decl )*
                while stream_objset_decl.hasNext():
                    self._adaptor.addChild(root_1, stream_objset_decl.nextTree())


                stream_objset_decl.reset();

                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:201:36: ( declarations )*
                while stream_declarations.hasNext():
                    self._adaptor.addChild(root_1, stream_declarations.nextTree())


                stream_declarations.reset();

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "dir_block"


    class network_block_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "network_block"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:204:5: network_block : NETWORK OCBRACE ( network_element )* CCBRACE SEMICOLON -> ^( NETWORK_ ( network_element )* ) ;
    def network_block(self, ):
        retval = self.network_block_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NETWORK90 = None
        OCBRACE91 = None
        CCBRACE93 = None
        SEMICOLON94 = None
        network_element92 = None

        NETWORK90_tree = None
        OCBRACE91_tree = None
        CCBRACE93_tree = None
        SEMICOLON94_tree = None
        stream_NETWORK = RewriteRuleTokenStream(self._adaptor, "token NETWORK")
        stream_OCBRACE = RewriteRuleTokenStream(self._adaptor, "token OCBRACE")
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_CCBRACE = RewriteRuleTokenStream(self._adaptor, "token CCBRACE")
        stream_network_element = RewriteRuleSubtreeStream(self._adaptor, "rule network_element")
        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:204:19: ( NETWORK OCBRACE ( network_element )* CCBRACE SEMICOLON -> ^( NETWORK_ ( network_element )* ) )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:204:21: NETWORK OCBRACE ( network_element )* CCBRACE SEMICOLON
                pass 
                NETWORK90 = self.match(self.input, NETWORK, self.FOLLOW_NETWORK_in_network_block1545) 
                stream_NETWORK.add(NETWORK90)


                OCBRACE91 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_network_block1547) 
                stream_OCBRACE.add(OCBRACE91)


                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:204:37: ( network_element )*
                while True: #loop16
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if (LA16_0 in {93, 94}) :
                        alt16 = 1


                    if alt16 == 1:
                        # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:204:37: network_element
                        pass 
                        self._state.following.append(self.FOLLOW_network_element_in_network_block1549)
                        network_element92 = self.network_element()

                        self._state.following.pop()
                        stream_network_element.add(network_element92.tree)



                    else:
                        break #loop16


                CCBRACE93 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_network_block1552) 
                stream_CCBRACE.add(CCBRACE93)


                SEMICOLON94 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_network_block1554) 
                stream_SEMICOLON.add(SEMICOLON94)


                # AST Rewrite
                # elements: network_element
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 204:72: -> ^( NETWORK_ ( network_element )* )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:204:75: ^( NETWORK_ ( network_element )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(NETWORK_, "NETWORK_")
                , root_1)

                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:204:86: ( network_element )*
                while stream_network_element.hasNext():
                    self._adaptor.addChild(root_1, stream_network_element.nextTree())


                stream_network_element.reset();

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "network_block"


    class element_type_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "element_type"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:205:9: element_type : ( 'Ordered' | 'Unordered' );
    def element_type(self, ):
        retval = self.element_type_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set95 = None

        set95_tree = None

        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:205:22: ( 'Ordered' | 'Unordered' )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:
                pass 
                root_0 = self._adaptor.nil()


                set95 = self.input.LT(1)

                if self.input.LA(1) in {93, 94}:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set95))

                    self._state.errorRecovery = False


                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "element_type"


    class network_element_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "network_element"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:206:9: network_element : element_type ID SEMICOLON -> ^( ELEMENT_ element_type ID ) ;
    def network_element(self, ):
        retval = self.network_element_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID97 = None
        SEMICOLON98 = None
        element_type96 = None

        ID97_tree = None
        SEMICOLON98_tree = None
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_element_type = RewriteRuleSubtreeStream(self._adaptor, "rule element_type")
        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:206:25: ( element_type ID SEMICOLON -> ^( ELEMENT_ element_type ID ) )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:206:27: element_type ID SEMICOLON
                pass 
                self._state.following.append(self.FOLLOW_element_type_in_network_element1597)
                element_type96 = self.element_type()

                self._state.following.pop()
                stream_element_type.add(element_type96.tree)


                ID97 = self.match(self.input, ID, self.FOLLOW_ID_in_network_element1599) 
                stream_ID.add(ID97)


                SEMICOLON98 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_network_element1601) 
                stream_SEMICOLON.add(SEMICOLON98)


                # AST Rewrite
                # elements: element_type, ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 206:53: -> ^( ELEMENT_ element_type ID )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:206:56: ^( ELEMENT_ element_type ID )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(ELEMENT_, "ELEMENT_")
                , root_1)

                self._adaptor.addChild(root_1, stream_element_type.nextTree())

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "network_element"


    class network_send_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "network_send"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:207:5: network_send : ID DOT send_function OBRACE ID CBRACE SEMICOLON -> ^( SEND_ ID ID ) ;
    def network_send(self, ):
        retval = self.network_send_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID99 = None
        DOT100 = None
        OBRACE102 = None
        ID103 = None
        CBRACE104 = None
        SEMICOLON105 = None
        send_function101 = None

        ID99_tree = None
        DOT100_tree = None
        OBRACE102_tree = None
        ID103_tree = None
        CBRACE104_tree = None
        SEMICOLON105_tree = None
        stream_OBRACE = RewriteRuleTokenStream(self._adaptor, "token OBRACE")
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CBRACE = RewriteRuleTokenStream(self._adaptor, "token CBRACE")
        stream_send_function = RewriteRuleSubtreeStream(self._adaptor, "rule send_function")
        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:207:18: ( ID DOT send_function OBRACE ID CBRACE SEMICOLON -> ^( SEND_ ID ID ) )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:207:20: ID DOT send_function OBRACE ID CBRACE SEMICOLON
                pass 
                ID99 = self.match(self.input, ID, self.FOLLOW_ID_in_network_send1622) 
                stream_ID.add(ID99)


                DOT100 = self.match(self.input, DOT, self.FOLLOW_DOT_in_network_send1624) 
                stream_DOT.add(DOT100)


                self._state.following.append(self.FOLLOW_send_function_in_network_send1626)
                send_function101 = self.send_function()

                self._state.following.pop()
                stream_send_function.add(send_function101.tree)


                OBRACE102 = self.match(self.input, OBRACE, self.FOLLOW_OBRACE_in_network_send1628) 
                stream_OBRACE.add(OBRACE102)


                ID103 = self.match(self.input, ID, self.FOLLOW_ID_in_network_send1630) 
                stream_ID.add(ID103)


                CBRACE104 = self.match(self.input, CBRACE, self.FOLLOW_CBRACE_in_network_send1632) 
                stream_CBRACE.add(CBRACE104)


                SEMICOLON105 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_network_send1634) 
                stream_SEMICOLON.add(SEMICOLON105)


                # AST Rewrite
                # elements: ID, ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 207:68: -> ^( SEND_ ID ID )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:207:71: ^( SEND_ ID ID )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(SEND_, "SEND_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "network_send"


    class network_mcast_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "network_mcast"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:208:5: network_mcast : ID DOT mcast_function OBRACE ID COMMA ID CBRACE SEMICOLON -> ^( MCAST_ ID ID ID ) ;
    def network_mcast(self, ):
        retval = self.network_mcast_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID106 = None
        DOT107 = None
        OBRACE109 = None
        ID110 = None
        COMMA111 = None
        ID112 = None
        CBRACE113 = None
        SEMICOLON114 = None
        mcast_function108 = None

        ID106_tree = None
        DOT107_tree = None
        OBRACE109_tree = None
        ID110_tree = None
        COMMA111_tree = None
        ID112_tree = None
        CBRACE113_tree = None
        SEMICOLON114_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_OBRACE = RewriteRuleTokenStream(self._adaptor, "token OBRACE")
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CBRACE = RewriteRuleTokenStream(self._adaptor, "token CBRACE")
        stream_mcast_function = RewriteRuleSubtreeStream(self._adaptor, "rule mcast_function")
        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:208:18: ( ID DOT mcast_function OBRACE ID COMMA ID CBRACE SEMICOLON -> ^( MCAST_ ID ID ID ) )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:208:20: ID DOT mcast_function OBRACE ID COMMA ID CBRACE SEMICOLON
                pass 
                ID106 = self.match(self.input, ID, self.FOLLOW_ID_in_network_mcast1654) 
                stream_ID.add(ID106)


                DOT107 = self.match(self.input, DOT, self.FOLLOW_DOT_in_network_mcast1656) 
                stream_DOT.add(DOT107)


                self._state.following.append(self.FOLLOW_mcast_function_in_network_mcast1658)
                mcast_function108 = self.mcast_function()

                self._state.following.pop()
                stream_mcast_function.add(mcast_function108.tree)


                OBRACE109 = self.match(self.input, OBRACE, self.FOLLOW_OBRACE_in_network_mcast1660) 
                stream_OBRACE.add(OBRACE109)


                ID110 = self.match(self.input, ID, self.FOLLOW_ID_in_network_mcast1662) 
                stream_ID.add(ID110)


                COMMA111 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_network_mcast1664) 
                stream_COMMA.add(COMMA111)


                ID112 = self.match(self.input, ID, self.FOLLOW_ID_in_network_mcast1666) 
                stream_ID.add(ID112)


                CBRACE113 = self.match(self.input, CBRACE, self.FOLLOW_CBRACE_in_network_mcast1668) 
                stream_CBRACE.add(CBRACE113)


                SEMICOLON114 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_network_mcast1670) 
                stream_SEMICOLON.add(SEMICOLON114)


                # AST Rewrite
                # elements: ID, ID, ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 208:78: -> ^( MCAST_ ID ID ID )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:208:81: ^( MCAST_ ID ID ID )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(MCAST_, "MCAST_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "network_mcast"


    class message_block_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "message_block"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:211:5: message_block : MSG ID OCBRACE ( declarations )* CCBRACE SEMICOLON -> ^( MSG_ ID ( declarations )* ) ;
    def message_block(self, ):
        retval = self.message_block_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MSG115 = None
        ID116 = None
        OCBRACE117 = None
        CCBRACE119 = None
        SEMICOLON120 = None
        declarations118 = None

        MSG115_tree = None
        ID116_tree = None
        OCBRACE117_tree = None
        CCBRACE119_tree = None
        SEMICOLON120_tree = None
        stream_MSG = RewriteRuleTokenStream(self._adaptor, "token MSG")
        stream_OCBRACE = RewriteRuleTokenStream(self._adaptor, "token OCBRACE")
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CCBRACE = RewriteRuleTokenStream(self._adaptor, "token CCBRACE")
        stream_declarations = RewriteRuleSubtreeStream(self._adaptor, "rule declarations")
        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:211:19: ( MSG ID OCBRACE ( declarations )* CCBRACE SEMICOLON -> ^( MSG_ ID ( declarations )* ) )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:211:21: MSG ID OCBRACE ( declarations )* CCBRACE SEMICOLON
                pass 
                MSG115 = self.match(self.input, MSG, self.FOLLOW_MSG_in_message_block1700) 
                stream_MSG.add(MSG115)


                ID116 = self.match(self.input, ID, self.FOLLOW_ID_in_message_block1702) 
                stream_ID.add(ID116)


                OCBRACE117 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_message_block1704) 
                stream_OCBRACE.add(OCBRACE117)


                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:211:36: ( declarations )*
                while True: #loop17
                    alt17 = 2
                    LA17_0 = self.input.LA(1)

                    if (LA17_0 in {BOOLID, DATA, INTID, NID, SET, STATE}) :
                        alt17 = 1


                    if alt17 == 1:
                        # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:211:36: declarations
                        pass 
                        self._state.following.append(self.FOLLOW_declarations_in_message_block1706)
                        declarations118 = self.declarations()

                        self._state.following.pop()
                        stream_declarations.add(declarations118.tree)



                    else:
                        break #loop17


                CCBRACE119 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_message_block1709) 
                stream_CCBRACE.add(CCBRACE119)


                SEMICOLON120 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_message_block1711) 
                stream_SEMICOLON.add(SEMICOLON120)


                # AST Rewrite
                # elements: ID, declarations
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 211:68: -> ^( MSG_ ID ( declarations )* )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:211:71: ^( MSG_ ID ( declarations )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(MSG_, "MSG_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:211:81: ( declarations )*
                while stream_declarations.hasNext():
                    self._adaptor.addChild(root_1, stream_declarations.nextTree())


                stream_declarations.reset();

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "message_block"


    class message_constr_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "message_constr"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:212:5: message_constr : ID OBRACE ( message_expr )* ( COMMA message_expr )* CBRACE -> ^( MSGCSTR_ ID ( message_expr )* ) ;
    def message_constr(self, ):
        retval = self.message_constr_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID121 = None
        OBRACE122 = None
        COMMA124 = None
        CBRACE126 = None
        message_expr123 = None
        message_expr125 = None

        ID121_tree = None
        OBRACE122_tree = None
        COMMA124_tree = None
        CBRACE126_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_OBRACE = RewriteRuleTokenStream(self._adaptor, "token OBRACE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CBRACE = RewriteRuleTokenStream(self._adaptor, "token CBRACE")
        stream_message_expr = RewriteRuleSubtreeStream(self._adaptor, "rule message_expr")
        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:212:20: ( ID OBRACE ( message_expr )* ( COMMA message_expr )* CBRACE -> ^( MSGCSTR_ ID ( message_expr )* ) )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:212:22: ID OBRACE ( message_expr )* ( COMMA message_expr )* CBRACE
                pass 
                ID121 = self.match(self.input, ID, self.FOLLOW_ID_in_message_constr1733) 
                stream_ID.add(ID121)


                OBRACE122 = self.match(self.input, OBRACE, self.FOLLOW_OBRACE_in_message_constr1735) 
                stream_OBRACE.add(OBRACE122)


                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:212:32: ( message_expr )*
                while True: #loop18
                    alt18 = 2
                    LA18_0 = self.input.LA(1)

                    if (LA18_0 in {BOOL, ID, INT, NID}) :
                        alt18 = 1


                    if alt18 == 1:
                        # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:212:32: message_expr
                        pass 
                        self._state.following.append(self.FOLLOW_message_expr_in_message_constr1737)
                        message_expr123 = self.message_expr()

                        self._state.following.pop()
                        stream_message_expr.add(message_expr123.tree)



                    else:
                        break #loop18


                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:212:46: ( COMMA message_expr )*
                while True: #loop19
                    alt19 = 2
                    LA19_0 = self.input.LA(1)

                    if (LA19_0 == COMMA) :
                        alt19 = 1


                    if alt19 == 1:
                        # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:212:47: COMMA message_expr
                        pass 
                        COMMA124 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_message_constr1741) 
                        stream_COMMA.add(COMMA124)


                        self._state.following.append(self.FOLLOW_message_expr_in_message_constr1743)
                        message_expr125 = self.message_expr()

                        self._state.following.pop()
                        stream_message_expr.add(message_expr125.tree)



                    else:
                        break #loop19


                CBRACE126 = self.match(self.input, CBRACE, self.FOLLOW_CBRACE_in_message_constr1747) 
                stream_CBRACE.add(CBRACE126)


                # AST Rewrite
                # elements: ID, message_expr
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 212:75: -> ^( MSGCSTR_ ID ( message_expr )* )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:212:78: ^( MSGCSTR_ ID ( message_expr )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(MSGCSTR_, "MSGCSTR_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:212:92: ( message_expr )*
                while stream_message_expr.hasNext():
                    self._adaptor.addChild(root_1, stream_message_expr.nextTree())


                stream_message_expr.reset();

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "message_constr"


    class message_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "message_expr"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:213:5: message_expr : ( object_expr | set_func | INT | BOOL | NID );
    def message_expr(self, ):
        retval = self.message_expr_return()
        retval.start = self.input.LT(1)


        root_0 = None

        INT129 = None
        BOOL130 = None
        NID131 = None
        object_expr127 = None
        set_func128 = None

        INT129_tree = None
        BOOL130_tree = None
        NID131_tree = None

        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:213:18: ( object_expr | set_func | INT | BOOL | NID )
                alt20 = 5
                LA20 = self.input.LA(1)
                if LA20 in {ID}:
                    LA20_1 = self.input.LA(2)

                    if (LA20_1 == DOT) :
                        LA20_5 = self.input.LA(3)

                        if (LA20_5 in {ID, NID}) :
                            alt20 = 1
                        elif ((95 <= LA20_5 <= 99) or LA20_5 in {}) :
                            alt20 = 2
                        else:
                            nvae = NoViableAltException("", 20, 5, self.input)

                            raise nvae


                    elif (LA20_1 in {BOOL, CBRACE, COMMA, ID, INT, NID}) :
                        alt20 = 1
                    else:
                        nvae = NoViableAltException("", 20, 1, self.input)

                        raise nvae


                elif LA20 in {INT}:
                    alt20 = 3
                elif LA20 in {BOOL}:
                    alt20 = 4
                elif LA20 in {NID}:
                    alt20 = 5
                else:
                    nvae = NoViableAltException("", 20, 0, self.input)

                    raise nvae


                if alt20 == 1:
                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:213:20: object_expr
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_object_expr_in_message_expr1769)
                    object_expr127 = self.object_expr()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, object_expr127.tree)



                elif alt20 == 2:
                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:213:34: set_func
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_set_func_in_message_expr1773)
                    set_func128 = self.set_func()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, set_func128.tree)



                elif alt20 == 3:
                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:213:45: INT
                    pass 
                    root_0 = self._adaptor.nil()


                    INT129 = self.match(self.input, INT, self.FOLLOW_INT_in_message_expr1777)
                    INT129_tree = self._adaptor.createWithPayload(INT129)
                    self._adaptor.addChild(root_0, INT129_tree)




                elif alt20 == 4:
                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:213:51: BOOL
                    pass 
                    root_0 = self._adaptor.nil()


                    BOOL130 = self.match(self.input, BOOL, self.FOLLOW_BOOL_in_message_expr1781)
                    BOOL130_tree = self._adaptor.createWithPayload(BOOL130)
                    self._adaptor.addChild(root_0, BOOL130_tree)




                elif alt20 == 5:
                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:213:58: NID
                    pass 
                    root_0 = self._adaptor.nil()


                    NID131 = self.match(self.input, NID, self.FOLLOW_NID_in_message_expr1785)
                    NID131_tree = self._adaptor.createWithPayload(NID131)
                    self._adaptor.addChild(root_0, NID131_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "message_expr"


    class set_block_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "set_block"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:216:5: set_block : set_func SEMICOLON -> set_func ;
    def set_block(self, ):
        retval = self.set_block_return()
        retval.start = self.input.LT(1)


        root_0 = None

        SEMICOLON133 = None
        set_func132 = None

        SEMICOLON133_tree = None
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_set_func = RewriteRuleSubtreeStream(self._adaptor, "rule set_func")
        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:216:15: ( set_func SEMICOLON -> set_func )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:216:17: set_func SEMICOLON
                pass 
                self._state.following.append(self.FOLLOW_set_func_in_set_block1803)
                set_func132 = self.set_func()

                self._state.following.pop()
                stream_set_func.add(set_func132.tree)


                SEMICOLON133 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_set_block1805) 
                stream_SEMICOLON.add(SEMICOLON133)


                # AST Rewrite
                # elements: set_func
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 216:36: -> set_func
                self._adaptor.addChild(root_0, stream_set_func.nextTree())




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "set_block"


    class set_func_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "set_func"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:217:5: set_func : ID DOT set_function_types OBRACE ( set_nest )* CBRACE -> ^( SETFUNC_ ID DOT set_function_types OBRACE ( set_nest )* CBRACE ) ;
    def set_func(self, ):
        retval = self.set_func_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID134 = None
        DOT135 = None
        OBRACE137 = None
        CBRACE139 = None
        set_function_types136 = None
        set_nest138 = None

        ID134_tree = None
        DOT135_tree = None
        OBRACE137_tree = None
        CBRACE139_tree = None
        stream_OBRACE = RewriteRuleTokenStream(self._adaptor, "token OBRACE")
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CBRACE = RewriteRuleTokenStream(self._adaptor, "token CBRACE")
        stream_set_function_types = RewriteRuleSubtreeStream(self._adaptor, "rule set_function_types")
        stream_set_nest = RewriteRuleSubtreeStream(self._adaptor, "rule set_nest")
        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:217:14: ( ID DOT set_function_types OBRACE ( set_nest )* CBRACE -> ^( SETFUNC_ ID DOT set_function_types OBRACE ( set_nest )* CBRACE ) )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:217:16: ID DOT set_function_types OBRACE ( set_nest )* CBRACE
                pass 
                ID134 = self.match(self.input, ID, self.FOLLOW_ID_in_set_func1820) 
                stream_ID.add(ID134)


                DOT135 = self.match(self.input, DOT, self.FOLLOW_DOT_in_set_func1822) 
                stream_DOT.add(DOT135)


                self._state.following.append(self.FOLLOW_set_function_types_in_set_func1824)
                set_function_types136 = self.set_function_types()

                self._state.following.pop()
                stream_set_function_types.add(set_function_types136.tree)


                OBRACE137 = self.match(self.input, OBRACE, self.FOLLOW_OBRACE_in_set_func1826) 
                stream_OBRACE.add(OBRACE137)


                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:217:49: ( set_nest )*
                while True: #loop21
                    alt21 = 2
                    LA21_0 = self.input.LA(1)

                    if (LA21_0 == ID) :
                        alt21 = 1


                    if alt21 == 1:
                        # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:217:49: set_nest
                        pass 
                        self._state.following.append(self.FOLLOW_set_nest_in_set_func1828)
                        set_nest138 = self.set_nest()

                        self._state.following.pop()
                        stream_set_nest.add(set_nest138.tree)



                    else:
                        break #loop21


                CBRACE139 = self.match(self.input, CBRACE, self.FOLLOW_CBRACE_in_set_func1831) 
                stream_CBRACE.add(CBRACE139)


                # AST Rewrite
                # elements: ID, DOT, set_function_types, OBRACE, set_nest, CBRACE
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 217:66: -> ^( SETFUNC_ ID DOT set_function_types OBRACE ( set_nest )* CBRACE )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:218:9: ^( SETFUNC_ ID DOT set_function_types OBRACE ( set_nest )* CBRACE )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(SETFUNC_, "SETFUNC_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_1, 
                stream_DOT.nextNode()
                )

                self._adaptor.addChild(root_1, stream_set_function_types.nextTree())

                self._adaptor.addChild(root_1, 
                stream_OBRACE.nextNode()
                )

                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:218:53: ( set_nest )*
                while stream_set_nest.hasNext():
                    self._adaptor.addChild(root_1, stream_set_nest.nextTree())


                stream_set_nest.reset();

                self._adaptor.addChild(root_1, 
                stream_CBRACE.nextNode()
                )

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "set_func"


    class set_nest_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "set_nest"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:219:5: set_nest : ( set_func | object_expr );
    def set_nest(self, ):
        retval = self.set_nest_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set_func140 = None
        object_expr141 = None


        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:219:14: ( set_func | object_expr )
                alt22 = 2
                LA22_0 = self.input.LA(1)

                if (LA22_0 == ID) :
                    LA22_1 = self.input.LA(2)

                    if (LA22_1 == DOT) :
                        LA22_2 = self.input.LA(3)

                        if ((95 <= LA22_2 <= 99) or LA22_2 in {}) :
                            alt22 = 1
                        elif (LA22_2 in {ID, NID}) :
                            alt22 = 2
                        else:
                            nvae = NoViableAltException("", 22, 2, self.input)

                            raise nvae


                    elif (LA22_1 in {CBRACE, ID}) :
                        alt22 = 2
                    else:
                        nvae = NoViableAltException("", 22, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 22, 0, self.input)

                    raise nvae


                if alt22 == 1:
                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:219:16: set_func
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_set_func_in_set_nest1869)
                    set_func140 = self.set_func()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, set_func140.tree)



                elif alt22 == 2:
                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:219:27: object_expr
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_object_expr_in_set_nest1873)
                    object_expr141 = self.object_expr()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, object_expr141.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "set_nest"


    class arch_block_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "arch_block"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:222:1: arch_block : ARCH ID OCBRACE arch_body CCBRACE -> ^( ARCH_ ^( MACHN_ ID ) arch_body ) ;
    def arch_block(self, ):
        retval = self.arch_block_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ARCH142 = None
        ID143 = None
        OCBRACE144 = None
        CCBRACE146 = None
        arch_body145 = None

        ARCH142_tree = None
        ID143_tree = None
        OCBRACE144_tree = None
        CCBRACE146_tree = None
        stream_OCBRACE = RewriteRuleTokenStream(self._adaptor, "token OCBRACE")
        stream_ARCH = RewriteRuleTokenStream(self._adaptor, "token ARCH")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CCBRACE = RewriteRuleTokenStream(self._adaptor, "token CCBRACE")
        stream_arch_body = RewriteRuleSubtreeStream(self._adaptor, "rule arch_body")
        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:222:12: ( ARCH ID OCBRACE arch_body CCBRACE -> ^( ARCH_ ^( MACHN_ ID ) arch_body ) )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:222:14: ARCH ID OCBRACE arch_body CCBRACE
                pass 
                ARCH142 = self.match(self.input, ARCH, self.FOLLOW_ARCH_in_arch_block1883) 
                stream_ARCH.add(ARCH142)


                ID143 = self.match(self.input, ID, self.FOLLOW_ID_in_arch_block1885) 
                stream_ID.add(ID143)


                OCBRACE144 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_arch_block1887) 
                stream_OCBRACE.add(OCBRACE144)


                self._state.following.append(self.FOLLOW_arch_body_in_arch_block1889)
                arch_body145 = self.arch_body()

                self._state.following.pop()
                stream_arch_body.add(arch_body145.tree)


                CCBRACE146 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_arch_block1891) 
                stream_CCBRACE.add(CCBRACE146)


                # AST Rewrite
                # elements: ID, arch_body
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 222:48: -> ^( ARCH_ ^( MACHN_ ID ) arch_body )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:222:51: ^( ARCH_ ^( MACHN_ ID ) arch_body )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(ARCH_, "ARCH_")
                , root_1)

                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:222:59: ^( MACHN_ ID )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(MACHN_, "MACHN_")
                , root_2)

                self._adaptor.addChild(root_2, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_1, root_2)

                self._adaptor.addChild(root_1, stream_arch_body.nextTree())

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "arch_block"


    class arch_body_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "arch_body"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:224:1: arch_body : ( stable_def | process_block )* ;
    def arch_body(self, ):
        retval = self.arch_body_return()
        retval.start = self.input.LT(1)


        root_0 = None

        stable_def147 = None
        process_block148 = None


        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:224:10: ( ( stable_def | process_block )* )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:224:12: ( stable_def | process_block )*
                pass 
                root_0 = self._adaptor.nil()


                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:224:12: ( stable_def | process_block )*
                while True: #loop23
                    alt23 = 3
                    LA23_0 = self.input.LA(1)

                    if (LA23_0 == STABLE) :
                        alt23 = 1
                    elif (LA23_0 == PROC) :
                        alt23 = 2


                    if alt23 == 1:
                        # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:224:13: stable_def
                        pass 
                        self._state.following.append(self.FOLLOW_stable_def_in_arch_body1913)
                        stable_def147 = self.stable_def()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, stable_def147.tree)



                    elif alt23 == 2:
                        # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:224:26: process_block
                        pass 
                        self._state.following.append(self.FOLLOW_process_block_in_arch_body1917)
                        process_block148 = self.process_block()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, process_block148.tree)



                    else:
                        break #loop23




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "arch_body"


    class stable_def_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "stable_def"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:226:1: stable_def : STABLE OCBRACE ID ( COMMA ID )* CCBRACE -> ^( STABLE_ ID ( ID )* ) ;
    def stable_def(self, ):
        retval = self.stable_def_return()
        retval.start = self.input.LT(1)


        root_0 = None

        STABLE149 = None
        OCBRACE150 = None
        ID151 = None
        COMMA152 = None
        ID153 = None
        CCBRACE154 = None

        STABLE149_tree = None
        OCBRACE150_tree = None
        ID151_tree = None
        COMMA152_tree = None
        ID153_tree = None
        CCBRACE154_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_OCBRACE = RewriteRuleTokenStream(self._adaptor, "token OCBRACE")
        stream_STABLE = RewriteRuleTokenStream(self._adaptor, "token STABLE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CCBRACE = RewriteRuleTokenStream(self._adaptor, "token CCBRACE")

        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:226:12: ( STABLE OCBRACE ID ( COMMA ID )* CCBRACE -> ^( STABLE_ ID ( ID )* ) )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:226:14: STABLE OCBRACE ID ( COMMA ID )* CCBRACE
                pass 
                STABLE149 = self.match(self.input, STABLE, self.FOLLOW_STABLE_in_stable_def1927) 
                stream_STABLE.add(STABLE149)


                OCBRACE150 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_stable_def1929) 
                stream_OCBRACE.add(OCBRACE150)


                ID151 = self.match(self.input, ID, self.FOLLOW_ID_in_stable_def1931) 
                stream_ID.add(ID151)


                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:226:32: ( COMMA ID )*
                while True: #loop24
                    alt24 = 2
                    LA24_0 = self.input.LA(1)

                    if (LA24_0 == COMMA) :
                        alt24 = 1


                    if alt24 == 1:
                        # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:226:33: COMMA ID
                        pass 
                        COMMA152 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_stable_def1934) 
                        stream_COMMA.add(COMMA152)


                        ID153 = self.match(self.input, ID, self.FOLLOW_ID_in_stable_def1936) 
                        stream_ID.add(ID153)



                    else:
                        break #loop24


                CCBRACE154 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_stable_def1940) 
                stream_CCBRACE.add(CCBRACE154)


                # AST Rewrite
                # elements: ID, ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 226:52: -> ^( STABLE_ ID ( ID )* )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:226:55: ^( STABLE_ ID ( ID )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(STABLE_, "STABLE_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:226:68: ( ID )*
                while stream_ID.hasNext():
                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )


                stream_ID.reset();

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "stable_def"


    class process_block_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "process_block"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:228:1: process_block : PROC process_trans OCBRACE ( process_expr )* CCBRACE -> ^( PROC_ process_trans ( process_expr )* ^( ENDPROC_ ) ) ;
    def process_block(self, ):
        retval = self.process_block_return()
        retval.start = self.input.LT(1)


        root_0 = None

        PROC155 = None
        OCBRACE157 = None
        CCBRACE159 = None
        process_trans156 = None
        process_expr158 = None

        PROC155_tree = None
        OCBRACE157_tree = None
        CCBRACE159_tree = None
        stream_PROC = RewriteRuleTokenStream(self._adaptor, "token PROC")
        stream_OCBRACE = RewriteRuleTokenStream(self._adaptor, "token OCBRACE")
        stream_CCBRACE = RewriteRuleTokenStream(self._adaptor, "token CCBRACE")
        stream_process_trans = RewriteRuleSubtreeStream(self._adaptor, "rule process_trans")
        stream_process_expr = RewriteRuleSubtreeStream(self._adaptor, "rule process_expr")
        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:228:15: ( PROC process_trans OCBRACE ( process_expr )* CCBRACE -> ^( PROC_ process_trans ( process_expr )* ^( ENDPROC_ ) ) )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:228:17: PROC process_trans OCBRACE ( process_expr )* CCBRACE
                pass 
                PROC155 = self.match(self.input, PROC, self.FOLLOW_PROC_in_process_block1959) 
                stream_PROC.add(PROC155)


                self._state.following.append(self.FOLLOW_process_trans_in_process_block1961)
                process_trans156 = self.process_trans()

                self._state.following.pop()
                stream_process_trans.add(process_trans156.tree)


                OCBRACE157 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_process_block1963) 
                stream_OCBRACE.add(OCBRACE157)


                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:228:44: ( process_expr )*
                while True: #loop25
                    alt25 = 2
                    LA25_0 = self.input.LA(1)

                    if (LA25_0 in {AWAIT, ID, IF, STATE}) :
                        alt25 = 1


                    if alt25 == 1:
                        # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:228:44: process_expr
                        pass 
                        self._state.following.append(self.FOLLOW_process_expr_in_process_block1965)
                        process_expr158 = self.process_expr()

                        self._state.following.pop()
                        stream_process_expr.add(process_expr158.tree)



                    else:
                        break #loop25


                CCBRACE159 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_process_block1968) 
                stream_CCBRACE.add(CCBRACE159)


                # AST Rewrite
                # elements: process_trans, process_expr
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 228:66: -> ^( PROC_ process_trans ( process_expr )* ^( ENDPROC_ ) )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:228:69: ^( PROC_ process_trans ( process_expr )* ^( ENDPROC_ ) )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(PROC_, "PROC_")
                , root_1)

                self._adaptor.addChild(root_1, stream_process_trans.nextTree())

                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:228:91: ( process_expr )*
                while stream_process_expr.hasNext():
                    self._adaptor.addChild(root_1, stream_process_expr.nextTree())


                stream_process_expr.reset();

                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:228:105: ^( ENDPROC_ )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(ENDPROC_, "ENDPROC_")
                , root_2)

                self._adaptor.addChild(root_1, root_2)

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "process_block"


    class process_trans_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "process_trans"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:229:5: process_trans : OBRACE ID COMMA process_events ( process_finalstate )* CBRACE -> ^( TRANS_ ID process_events ( process_finalstate )* ) ;
    def process_trans(self, ):
        retval = self.process_trans_return()
        retval.start = self.input.LT(1)


        root_0 = None

        OBRACE160 = None
        ID161 = None
        COMMA162 = None
        CBRACE165 = None
        process_events163 = None
        process_finalstate164 = None

        OBRACE160_tree = None
        ID161_tree = None
        COMMA162_tree = None
        CBRACE165_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_OBRACE = RewriteRuleTokenStream(self._adaptor, "token OBRACE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CBRACE = RewriteRuleTokenStream(self._adaptor, "token CBRACE")
        stream_process_events = RewriteRuleSubtreeStream(self._adaptor, "rule process_events")
        stream_process_finalstate = RewriteRuleSubtreeStream(self._adaptor, "rule process_finalstate")
        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:229:19: ( OBRACE ID COMMA process_events ( process_finalstate )* CBRACE -> ^( TRANS_ ID process_events ( process_finalstate )* ) )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:229:21: OBRACE ID COMMA process_events ( process_finalstate )* CBRACE
                pass 
                OBRACE160 = self.match(self.input, OBRACE, self.FOLLOW_OBRACE_in_process_trans1994) 
                stream_OBRACE.add(OBRACE160)


                ID161 = self.match(self.input, ID, self.FOLLOW_ID_in_process_trans1996) 
                stream_ID.add(ID161)


                COMMA162 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_process_trans1998) 
                stream_COMMA.add(COMMA162)


                self._state.following.append(self.FOLLOW_process_events_in_process_trans2000)
                process_events163 = self.process_events()

                self._state.following.pop()
                stream_process_events.add(process_events163.tree)


                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:229:52: ( process_finalstate )*
                while True: #loop26
                    alt26 = 2
                    LA26_0 = self.input.LA(1)

                    if (LA26_0 == COMMA) :
                        alt26 = 1


                    if alt26 == 1:
                        # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:229:52: process_finalstate
                        pass 
                        self._state.following.append(self.FOLLOW_process_finalstate_in_process_trans2002)
                        process_finalstate164 = self.process_finalstate()

                        self._state.following.pop()
                        stream_process_finalstate.add(process_finalstate164.tree)



                    else:
                        break #loop26


                CBRACE165 = self.match(self.input, CBRACE, self.FOLLOW_CBRACE_in_process_trans2005) 
                stream_CBRACE.add(CBRACE165)


                # AST Rewrite
                # elements: ID, process_events, process_finalstate
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 229:79: -> ^( TRANS_ ID process_events ( process_finalstate )* )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:229:82: ^( TRANS_ ID process_events ( process_finalstate )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TRANS_, "TRANS_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_1, stream_process_events.nextTree())

                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:229:109: ( process_finalstate )*
                while stream_process_finalstate.hasNext():
                    self._adaptor.addChild(root_1, stream_process_finalstate.nextTree())


                stream_process_finalstate.reset();

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "process_trans"


    class process_finalstate_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "process_finalstate"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:230:5: process_finalstate : COMMA process_finalident -> ^( process_finalident ) ;
    def process_finalstate(self, ):
        retval = self.process_finalstate_return()
        retval.start = self.input.LT(1)


        root_0 = None

        COMMA166 = None
        process_finalident167 = None

        COMMA166_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_process_finalident = RewriteRuleSubtreeStream(self._adaptor, "rule process_finalident")
        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:230:23: ( COMMA process_finalident -> ^( process_finalident ) )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:230:25: COMMA process_finalident
                pass 
                COMMA166 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_process_finalstate2028) 
                stream_COMMA.add(COMMA166)


                self._state.following.append(self.FOLLOW_process_finalident_in_process_finalstate2030)
                process_finalident167 = self.process_finalident()

                self._state.following.pop()
                stream_process_finalident.add(process_finalident167.tree)


                # AST Rewrite
                # elements: process_finalident
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 230:50: -> ^( process_finalident )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:230:53: ^( process_finalident )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_process_finalident.nextNode(), root_1)

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "process_finalstate"


    class process_finalident_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "process_finalident"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:231:5: process_finalident : ( ID | STATE ) ;
    def process_finalident(self, ):
        retval = self.process_finalident_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set168 = None

        set168_tree = None

        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:231:23: ( ( ID | STATE ) )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:
                pass 
                root_0 = self._adaptor.nil()


                set168 = self.input.LT(1)

                if self.input.LA(1) in {ID, STATE}:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set168))

                    self._state.errorRecovery = False


                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "process_finalident"


    class process_events_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "process_events"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:232:5: process_events : ( ACCESS | ID ) ;
    def process_events(self, ):
        retval = self.process_events_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set169 = None

        set169_tree = None

        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:232:20: ( ( ACCESS | ID ) )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:
                pass 
                root_0 = self._adaptor.nil()


                set169 = self.input.LT(1)

                if self.input.LA(1) in {ACCESS, ID}:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set169))

                    self._state.errorRecovery = False


                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "process_events"


    class process_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "process_expr"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:233:5: process_expr : ( expressions | network_send | network_mcast | transaction );
    def process_expr(self, ):
        retval = self.process_expr_return()
        retval.start = self.input.LT(1)


        root_0 = None

        expressions170 = None
        network_send171 = None
        network_mcast172 = None
        transaction173 = None


        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:233:17: ( expressions | network_send | network_mcast | transaction )
                alt27 = 4
                LA27 = self.input.LA(1)
                if LA27 in {ID}:
                    LA27_1 = self.input.LA(2)

                    if (LA27_1 == DOT) :
                        LA27 = self.input.LA(3)
                        if LA27 in {ID, NID, 95, 96, 97, 98, 99}:
                            alt27 = 1
                        elif LA27 in {101}:
                            alt27 = 2
                        elif LA27 in {100}:
                            alt27 = 3
                        else:
                            nvae = NoViableAltException("", 27, 5, self.input)

                            raise nvae


                    elif (LA27_1 in {EQUALSIGN, SEMICOLON}) :
                        alt27 = 1
                    else:
                        nvae = NoViableAltException("", 27, 1, self.input)

                        raise nvae


                elif LA27 in {IF, STATE}:
                    alt27 = 1
                elif LA27 in {AWAIT}:
                    alt27 = 4
                else:
                    nvae = NoViableAltException("", 27, 0, self.input)

                    raise nvae


                if alt27 == 1:
                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:233:19: expressions
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_expressions_in_process_expr2079)
                    expressions170 = self.expressions()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, expressions170.tree)



                elif alt27 == 2:
                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:233:33: network_send
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_network_send_in_process_expr2083)
                    network_send171 = self.network_send()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, network_send171.tree)



                elif alt27 == 3:
                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:233:48: network_mcast
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_network_mcast_in_process_expr2087)
                    network_mcast172 = self.network_mcast()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, network_mcast172.tree)



                elif alt27 == 4:
                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:233:64: transaction
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_transaction_in_process_expr2091)
                    transaction173 = self.transaction()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, transaction173.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "process_expr"


    class transaction_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "transaction"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:236:1: transaction : AWAIT OCBRACE ( trans )* CCBRACE -> ^( AWAIT_ ( trans )* ) ;
    def transaction(self, ):
        retval = self.transaction_return()
        retval.start = self.input.LT(1)


        root_0 = None

        AWAIT174 = None
        OCBRACE175 = None
        CCBRACE177 = None
        trans176 = None

        AWAIT174_tree = None
        OCBRACE175_tree = None
        CCBRACE177_tree = None
        stream_OCBRACE = RewriteRuleTokenStream(self._adaptor, "token OCBRACE")
        stream_AWAIT = RewriteRuleTokenStream(self._adaptor, "token AWAIT")
        stream_CCBRACE = RewriteRuleTokenStream(self._adaptor, "token CCBRACE")
        stream_trans = RewriteRuleSubtreeStream(self._adaptor, "rule trans")
        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:236:13: ( AWAIT OCBRACE ( trans )* CCBRACE -> ^( AWAIT_ ( trans )* ) )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:236:15: AWAIT OCBRACE ( trans )* CCBRACE
                pass 
                AWAIT174 = self.match(self.input, AWAIT, self.FOLLOW_AWAIT_in_transaction2101) 
                stream_AWAIT.add(AWAIT174)


                OCBRACE175 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_transaction2103) 
                stream_OCBRACE.add(OCBRACE175)


                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:236:29: ( trans )*
                while True: #loop28
                    alt28 = 2
                    LA28_0 = self.input.LA(1)

                    if (LA28_0 == WHEN) :
                        alt28 = 1


                    if alt28 == 1:
                        # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:236:29: trans
                        pass 
                        self._state.following.append(self.FOLLOW_trans_in_transaction2105)
                        trans176 = self.trans()

                        self._state.following.pop()
                        stream_trans.add(trans176.tree)



                    else:
                        break #loop28


                CCBRACE177 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_transaction2108) 
                stream_CCBRACE.add(CCBRACE177)


                # AST Rewrite
                # elements: trans
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 236:44: -> ^( AWAIT_ ( trans )* )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:236:47: ^( AWAIT_ ( trans )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(AWAIT_, "AWAIT_")
                , root_1)

                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:236:56: ( trans )*
                while stream_trans.hasNext():
                    self._adaptor.addChild(root_1, stream_trans.nextTree())


                stream_trans.reset();

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "transaction"


    class trans_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "trans"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:237:5: trans : WHEN ID DDOT ( trans_body )* -> ^( WHEN_ ^( GUARD_ ID ) ( trans_body )* ENDWHEN_ ) ;
    def trans(self, ):
        retval = self.trans_return()
        retval.start = self.input.LT(1)


        root_0 = None

        WHEN178 = None
        ID179 = None
        DDOT180 = None
        trans_body181 = None

        WHEN178_tree = None
        ID179_tree = None
        DDOT180_tree = None
        stream_WHEN = RewriteRuleTokenStream(self._adaptor, "token WHEN")
        stream_DDOT = RewriteRuleTokenStream(self._adaptor, "token DDOT")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_trans_body = RewriteRuleSubtreeStream(self._adaptor, "rule trans_body")
        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:237:11: ( WHEN ID DDOT ( trans_body )* -> ^( WHEN_ ^( GUARD_ ID ) ( trans_body )* ENDWHEN_ ) )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:237:13: WHEN ID DDOT ( trans_body )*
                pass 
                WHEN178 = self.match(self.input, WHEN, self.FOLLOW_WHEN_in_trans2128) 
                stream_WHEN.add(WHEN178)


                ID179 = self.match(self.input, ID, self.FOLLOW_ID_in_trans2130) 
                stream_ID.add(ID179)


                DDOT180 = self.match(self.input, DDOT, self.FOLLOW_DDOT_in_trans2132) 
                stream_DDOT.add(DDOT180)


                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:237:26: ( trans_body )*
                while True: #loop29
                    alt29 = 2
                    LA29_0 = self.input.LA(1)

                    if (LA29_0 in {AWAIT, BREAK, ID, IF, NEXT, STATE}) :
                        alt29 = 1


                    if alt29 == 1:
                        # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:237:26: trans_body
                        pass 
                        self._state.following.append(self.FOLLOW_trans_body_in_trans2134)
                        trans_body181 = self.trans_body()

                        self._state.following.pop()
                        stream_trans_body.add(trans_body181.tree)



                    else:
                        break #loop29


                # AST Rewrite
                # elements: ID, trans_body
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 237:38: -> ^( WHEN_ ^( GUARD_ ID ) ( trans_body )* ENDWHEN_ )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:237:41: ^( WHEN_ ^( GUARD_ ID ) ( trans_body )* ENDWHEN_ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(WHEN_, "WHEN_")
                , root_1)

                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:237:49: ^( GUARD_ ID )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(GUARD_, "GUARD_")
                , root_2)

                self._adaptor.addChild(root_2, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_1, root_2)

                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:237:62: ( trans_body )*
                while stream_trans_body.hasNext():
                    self._adaptor.addChild(root_1, stream_trans_body.nextTree())


                stream_trans_body.reset();

                self._adaptor.addChild(root_1, 
                self._adaptor.createFromType(ENDWHEN_, "ENDWHEN_")
                )

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "trans"


    class trans_body_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "trans_body"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:238:9: trans_body : ( expressions | next_trans | next_break | transaction );
    def trans_body(self, ):
        retval = self.trans_body_return()
        retval.start = self.input.LT(1)


        root_0 = None

        expressions182 = None
        next_trans183 = None
        next_break184 = None
        transaction185 = None


        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:238:20: ( expressions | next_trans | next_break | transaction )
                alt30 = 4
                LA30 = self.input.LA(1)
                if LA30 in {ID, IF, STATE}:
                    alt30 = 1
                elif LA30 in {NEXT}:
                    alt30 = 2
                elif LA30 in {BREAK}:
                    alt30 = 3
                elif LA30 in {AWAIT}:
                    alt30 = 4
                else:
                    nvae = NoViableAltException("", 30, 0, self.input)

                    raise nvae


                if alt30 == 1:
                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:238:22: expressions
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_expressions_in_trans_body2167)
                    expressions182 = self.expressions()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, expressions182.tree)



                elif alt30 == 2:
                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:238:36: next_trans
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_next_trans_in_trans_body2171)
                    next_trans183 = self.next_trans()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, next_trans183.tree)



                elif alt30 == 3:
                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:238:49: next_break
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_next_break_in_trans_body2175)
                    next_break184 = self.next_break()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, next_break184.tree)



                elif alt30 == 4:
                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:238:62: transaction
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_transaction_in_trans_body2179)
                    transaction185 = self.transaction()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, transaction185.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "trans_body"


    class next_trans_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "next_trans"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:239:13: next_trans : NEXT OCBRACE ( trans )* CCBRACE -> ^( NEXT_ ( trans )* ) ;
    def next_trans(self, ):
        retval = self.next_trans_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEXT186 = None
        OCBRACE187 = None
        CCBRACE189 = None
        trans188 = None

        NEXT186_tree = None
        OCBRACE187_tree = None
        CCBRACE189_tree = None
        stream_OCBRACE = RewriteRuleTokenStream(self._adaptor, "token OCBRACE")
        stream_NEXT = RewriteRuleTokenStream(self._adaptor, "token NEXT")
        stream_CCBRACE = RewriteRuleTokenStream(self._adaptor, "token CCBRACE")
        stream_trans = RewriteRuleSubtreeStream(self._adaptor, "rule trans")
        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:239:23: ( NEXT OCBRACE ( trans )* CCBRACE -> ^( NEXT_ ( trans )* ) )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:239:25: NEXT OCBRACE ( trans )* CCBRACE
                pass 
                NEXT186 = self.match(self.input, NEXT, self.FOLLOW_NEXT_in_next_trans2197) 
                stream_NEXT.add(NEXT186)


                OCBRACE187 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_next_trans2199) 
                stream_OCBRACE.add(OCBRACE187)


                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:239:38: ( trans )*
                while True: #loop31
                    alt31 = 2
                    LA31_0 = self.input.LA(1)

                    if (LA31_0 == WHEN) :
                        alt31 = 1


                    if alt31 == 1:
                        # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:239:38: trans
                        pass 
                        self._state.following.append(self.FOLLOW_trans_in_next_trans2201)
                        trans188 = self.trans()

                        self._state.following.pop()
                        stream_trans.add(trans188.tree)



                    else:
                        break #loop31


                CCBRACE189 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_next_trans2204) 
                stream_CCBRACE.add(CCBRACE189)


                # AST Rewrite
                # elements: trans
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 239:53: -> ^( NEXT_ ( trans )* )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:239:56: ^( NEXT_ ( trans )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(NEXT_, "NEXT_")
                , root_1)

                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:239:64: ( trans )*
                while stream_trans.hasNext():
                    self._adaptor.addChild(root_1, stream_trans.nextTree())


                stream_trans.reset();

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "next_trans"


    class next_break_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "next_break"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:241:1: next_break : BREAK SEMICOLON -> ^( BREAK_ ) ;
    def next_break(self, ):
        retval = self.next_break_return()
        retval.start = self.input.LT(1)


        root_0 = None

        BREAK190 = None
        SEMICOLON191 = None

        BREAK190_tree = None
        SEMICOLON191_tree = None
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_BREAK = RewriteRuleTokenStream(self._adaptor, "token BREAK")

        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:241:12: ( BREAK SEMICOLON -> ^( BREAK_ ) )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:241:14: BREAK SEMICOLON
                pass 
                BREAK190 = self.match(self.input, BREAK, self.FOLLOW_BREAK_in_next_break2221) 
                stream_BREAK.add(BREAK190)


                SEMICOLON191 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_next_break2223) 
                stream_SEMICOLON.add(SEMICOLON191)


                # AST Rewrite
                # elements: 
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 241:30: -> ^( BREAK_ )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:241:33: ^( BREAK_ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(BREAK_, "BREAK_")
                , root_1)

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "next_break"


    class expressions_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "expressions"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:244:1: expressions : ( assignment | conditional | object_block | set_block );
    def expressions(self, ):
        retval = self.expressions_return()
        retval.start = self.input.LT(1)


        root_0 = None

        assignment192 = None
        conditional193 = None
        object_block194 = None
        set_block195 = None


        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:244:13: ( assignment | conditional | object_block | set_block )
                alt32 = 4
                LA32 = self.input.LA(1)
                if LA32 in {ID}:
                    LA32 = self.input.LA(2)
                    if LA32 in {DOT}:
                        LA32_4 = self.input.LA(3)

                        if (LA32_4 in {ID, NID}) :
                            alt32 = 3
                        elif ((95 <= LA32_4 <= 99) or LA32_4 in {}) :
                            alt32 = 4
                        else:
                            nvae = NoViableAltException("", 32, 4, self.input)

                            raise nvae


                    elif LA32 in {EQUALSIGN}:
                        alt32 = 1
                    elif LA32 in {SEMICOLON}:
                        alt32 = 3
                    else:
                        nvae = NoViableAltException("", 32, 1, self.input)

                        raise nvae


                elif LA32 in {IF}:
                    alt32 = 2
                elif LA32 in {STATE}:
                    alt32 = 1
                else:
                    nvae = NoViableAltException("", 32, 0, self.input)

                    raise nvae


                if alt32 == 1:
                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:244:15: assignment
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_assignment_in_expressions2239)
                    assignment192 = self.assignment()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, assignment192.tree)



                elif alt32 == 2:
                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:244:28: conditional
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_conditional_in_expressions2243)
                    conditional193 = self.conditional()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, conditional193.tree)



                elif alt32 == 3:
                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:244:42: object_block
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_object_block_in_expressions2247)
                    object_block194 = self.object_block()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, object_block194.tree)



                elif alt32 == 4:
                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:244:57: set_block
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_set_block_in_expressions2251)
                    set_block195 = self.set_block()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, set_block195.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "expressions"


    class assignment_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "assignment"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:245:1: assignment : process_finalident EQUALSIGN assign_types SEMICOLON -> ^( ASSIGN_ process_finalident EQUALSIGN assign_types ) ;
    def assignment(self, ):
        retval = self.assignment_return()
        retval.start = self.input.LT(1)


        root_0 = None

        EQUALSIGN197 = None
        SEMICOLON199 = None
        process_finalident196 = None
        assign_types198 = None

        EQUALSIGN197_tree = None
        SEMICOLON199_tree = None
        stream_EQUALSIGN = RewriteRuleTokenStream(self._adaptor, "token EQUALSIGN")
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_assign_types = RewriteRuleSubtreeStream(self._adaptor, "rule assign_types")
        stream_process_finalident = RewriteRuleSubtreeStream(self._adaptor, "rule process_finalident")
        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:245:12: ( process_finalident EQUALSIGN assign_types SEMICOLON -> ^( ASSIGN_ process_finalident EQUALSIGN assign_types ) )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:245:14: process_finalident EQUALSIGN assign_types SEMICOLON
                pass 
                self._state.following.append(self.FOLLOW_process_finalident_in_assignment2258)
                process_finalident196 = self.process_finalident()

                self._state.following.pop()
                stream_process_finalident.add(process_finalident196.tree)


                EQUALSIGN197 = self.match(self.input, EQUALSIGN, self.FOLLOW_EQUALSIGN_in_assignment2260) 
                stream_EQUALSIGN.add(EQUALSIGN197)


                self._state.following.append(self.FOLLOW_assign_types_in_assignment2262)
                assign_types198 = self.assign_types()

                self._state.following.pop()
                stream_assign_types.add(assign_types198.tree)


                SEMICOLON199 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_assignment2264) 
                stream_SEMICOLON.add(SEMICOLON199)


                # AST Rewrite
                # elements: process_finalident, EQUALSIGN, assign_types
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 245:65: -> ^( ASSIGN_ process_finalident EQUALSIGN assign_types )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:245:68: ^( ASSIGN_ process_finalident EQUALSIGN assign_types )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(ASSIGN_, "ASSIGN_")
                , root_1)

                self._adaptor.addChild(root_1, stream_process_finalident.nextTree())

                self._adaptor.addChild(root_1, 
                stream_EQUALSIGN.nextNode()
                )

                self._adaptor.addChild(root_1, stream_assign_types.nextTree())

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "assignment"


    class assign_types_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "assign_types"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:246:5: assign_types : ( object_expr | message_constr | math_op | set_func | INT | BOOL );
    def assign_types(self, ):
        retval = self.assign_types_return()
        retval.start = self.input.LT(1)


        root_0 = None

        INT204 = None
        BOOL205 = None
        object_expr200 = None
        message_constr201 = None
        math_op202 = None
        set_func203 = None

        INT204_tree = None
        BOOL205_tree = None

        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:246:18: ( object_expr | message_constr | math_op | set_func | INT | BOOL )
                alt33 = 6
                LA33 = self.input.LA(1)
                if LA33 in {ID}:
                    LA33 = self.input.LA(2)
                    if LA33 in {DOT}:
                        LA33_4 = self.input.LA(3)

                        if (LA33_4 in {ID, NID}) :
                            alt33 = 1
                        elif ((95 <= LA33_4 <= 99) or LA33_4 in {}) :
                            alt33 = 4
                        else:
                            nvae = NoViableAltException("", 33, 4, self.input)

                            raise nvae


                    elif LA33 in {OBRACE}:
                        alt33 = 2
                    elif LA33 in {SEMICOLON}:
                        alt33 = 1
                    elif LA33 in {MINUS, PLUS}:
                        alt33 = 3
                    else:
                        nvae = NoViableAltException("", 33, 1, self.input)

                        raise nvae


                elif LA33 in {INT}:
                    LA33_2 = self.input.LA(2)

                    if (LA33_2 in {MINUS, PLUS}) :
                        alt33 = 3
                    elif (LA33_2 == SEMICOLON) :
                        alt33 = 5
                    else:
                        nvae = NoViableAltException("", 33, 2, self.input)

                        raise nvae


                elif LA33 in {BOOL}:
                    alt33 = 6
                else:
                    nvae = NoViableAltException("", 33, 0, self.input)

                    raise nvae


                if alt33 == 1:
                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:246:20: object_expr
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_object_expr_in_assign_types2286)
                    object_expr200 = self.object_expr()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, object_expr200.tree)



                elif alt33 == 2:
                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:246:34: message_constr
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_message_constr_in_assign_types2290)
                    message_constr201 = self.message_constr()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, message_constr201.tree)



                elif alt33 == 3:
                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:246:51: math_op
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_math_op_in_assign_types2294)
                    math_op202 = self.math_op()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, math_op202.tree)



                elif alt33 == 4:
                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:246:61: set_func
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_set_func_in_assign_types2298)
                    set_func203 = self.set_func()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, set_func203.tree)



                elif alt33 == 5:
                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:246:72: INT
                    pass 
                    root_0 = self._adaptor.nil()


                    INT204 = self.match(self.input, INT, self.FOLLOW_INT_in_assign_types2302)
                    INT204_tree = self._adaptor.createWithPayload(INT204)
                    self._adaptor.addChild(root_0, INT204_tree)




                elif alt33 == 6:
                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:246:78: BOOL
                    pass 
                    root_0 = self._adaptor.nil()


                    BOOL205 = self.match(self.input, BOOL, self.FOLLOW_BOOL_in_assign_types2306)
                    BOOL205_tree = self._adaptor.createWithPayload(BOOL205)
                    self._adaptor.addChild(root_0, BOOL205_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "assign_types"


    class math_op_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "math_op"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:247:5: math_op : val_range ( PLUS | MINUS ) val_range ;
    def math_op(self, ):
        retval = self.math_op_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set207 = None
        val_range206 = None
        val_range208 = None

        set207_tree = None

        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:247:13: ( val_range ( PLUS | MINUS ) val_range )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:247:15: val_range ( PLUS | MINUS ) val_range
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_val_range_in_math_op2317)
                val_range206 = self.val_range()

                self._state.following.pop()
                self._adaptor.addChild(root_0, val_range206.tree)


                set207 = self.input.LT(1)

                if self.input.LA(1) in {MINUS, PLUS}:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set207))

                    self._state.errorRecovery = False


                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse



                self._state.following.append(self.FOLLOW_val_range_in_math_op2327)
                val_range208 = self.val_range()

                self._state.following.pop()
                self._adaptor.addChild(root_0, val_range208.tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "math_op"


    class conditional_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "conditional"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:250:1: conditional : if_stmt ;
    def conditional(self, ):
        retval = self.conditional_return()
        retval.start = self.input.LT(1)


        root_0 = None

        if_stmt209 = None


        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:250:12: ( if_stmt )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:250:14: if_stmt
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_if_stmt_in_conditional2336)
                if_stmt209 = self.if_stmt()

                self._state.following.pop()
                self._adaptor.addChild(root_0, if_stmt209.tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "conditional"


    class if_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "if_stmt"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:251:5: if_stmt : IF cond_comb OCBRACE if_expression CCBRACE ( ELSE OCBRACE else_expression CCBRACE )* -> {t_else}? ^( IFELSE_ ^( IF_ ^( COND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( NCOND_ cond_comb ) ( else_expression )* ENDIF_ ) ) -> ^( IFELSE_ ^( IF_ ^( COND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( NCOND_ cond_comb ) ENDIF_ ) ) ;
    def if_stmt(self, ):
        retval = self.if_stmt_return()
        retval.start = self.input.LT(1)


        root_0 = None

        IF210 = None
        OCBRACE212 = None
        CCBRACE214 = None
        ELSE215 = None
        OCBRACE216 = None
        CCBRACE218 = None
        cond_comb211 = None
        if_expression213 = None
        else_expression217 = None

        IF210_tree = None
        OCBRACE212_tree = None
        CCBRACE214_tree = None
        ELSE215_tree = None
        OCBRACE216_tree = None
        CCBRACE218_tree = None
        stream_OCBRACE = RewriteRuleTokenStream(self._adaptor, "token OCBRACE")
        stream_ELSE = RewriteRuleTokenStream(self._adaptor, "token ELSE")
        stream_IF = RewriteRuleTokenStream(self._adaptor, "token IF")
        stream_CCBRACE = RewriteRuleTokenStream(self._adaptor, "token CCBRACE")
        stream_else_expression = RewriteRuleSubtreeStream(self._adaptor, "rule else_expression")
        stream_if_expression = RewriteRuleSubtreeStream(self._adaptor, "rule if_expression")
        stream_cond_comb = RewriteRuleSubtreeStream(self._adaptor, "rule cond_comb")
        t_else = 0
        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:252:5: ( IF cond_comb OCBRACE if_expression CCBRACE ( ELSE OCBRACE else_expression CCBRACE )* -> {t_else}? ^( IFELSE_ ^( IF_ ^( COND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( NCOND_ cond_comb ) ( else_expression )* ENDIF_ ) ) -> ^( IFELSE_ ^( IF_ ^( COND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( NCOND_ cond_comb ) ENDIF_ ) ) )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:252:7: IF cond_comb OCBRACE if_expression CCBRACE ( ELSE OCBRACE else_expression CCBRACE )*
                pass 
                IF210 = self.match(self.input, IF, self.FOLLOW_IF_in_if_stmt2355) 
                stream_IF.add(IF210)


                self._state.following.append(self.FOLLOW_cond_comb_in_if_stmt2357)
                cond_comb211 = self.cond_comb()

                self._state.following.pop()
                stream_cond_comb.add(cond_comb211.tree)


                OCBRACE212 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_if_stmt2359) 
                stream_OCBRACE.add(OCBRACE212)


                self._state.following.append(self.FOLLOW_if_expression_in_if_stmt2361)
                if_expression213 = self.if_expression()

                self._state.following.pop()
                stream_if_expression.add(if_expression213.tree)


                CCBRACE214 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_if_stmt2363) 
                stream_CCBRACE.add(CCBRACE214)


                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:253:5: ( ELSE OCBRACE else_expression CCBRACE )*
                while True: #loop34
                    alt34 = 2
                    LA34_0 = self.input.LA(1)

                    if (LA34_0 == ELSE) :
                        alt34 = 1


                    if alt34 == 1:
                        # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:253:6: ELSE OCBRACE else_expression CCBRACE
                        pass 
                        ELSE215 = self.match(self.input, ELSE, self.FOLLOW_ELSE_in_if_stmt2370) 
                        stream_ELSE.add(ELSE215)


                        #action start
                        t_else=1
                        #action end


                        OCBRACE216 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_if_stmt2374) 
                        stream_OCBRACE.add(OCBRACE216)


                        self._state.following.append(self.FOLLOW_else_expression_in_if_stmt2376)
                        else_expression217 = self.else_expression()

                        self._state.following.pop()
                        stream_else_expression.add(else_expression217.tree)


                        CCBRACE218 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_if_stmt2378) 
                        stream_CCBRACE.add(CCBRACE218)



                    else:
                        break #loop34


                # AST Rewrite
                # elements: cond_comb, if_expression, cond_comb, else_expression, cond_comb, if_expression, cond_comb
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                if t_else:
                    # 254:5: -> {t_else}? ^( IFELSE_ ^( IF_ ^( COND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( NCOND_ cond_comb ) ( else_expression )* ENDIF_ ) )
                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:254:18: ^( IFELSE_ ^( IF_ ^( COND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( NCOND_ cond_comb ) ( else_expression )* ENDIF_ ) )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(IFELSE_, "IFELSE_")
                    , root_1)

                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:254:28: ^( IF_ ^( COND_ cond_comb ) ( if_expression )* ENDIF_ )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(IF_, "IF_")
                    , root_2)

                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:254:34: ^( COND_ cond_comb )
                    root_3 = self._adaptor.nil()
                    root_3 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(COND_, "COND_")
                    , root_3)

                    self._adaptor.addChild(root_3, stream_cond_comb.nextTree())

                    self._adaptor.addChild(root_2, root_3)

                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:254:53: ( if_expression )*
                    while stream_if_expression.hasNext():
                        self._adaptor.addChild(root_2, stream_if_expression.nextTree())


                    stream_if_expression.reset();

                    self._adaptor.addChild(root_2, 
                    self._adaptor.createFromType(ENDIF_, "ENDIF_")
                    )

                    self._adaptor.addChild(root_1, root_2)

                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:254:76: ^( IF_ ^( NCOND_ cond_comb ) ( else_expression )* ENDIF_ )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(IF_, "IF_")
                    , root_2)

                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:254:82: ^( NCOND_ cond_comb )
                    root_3 = self._adaptor.nil()
                    root_3 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(NCOND_, "NCOND_")
                    , root_3)

                    self._adaptor.addChild(root_3, stream_cond_comb.nextTree())

                    self._adaptor.addChild(root_2, root_3)

                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:254:102: ( else_expression )*
                    while stream_else_expression.hasNext():
                        self._adaptor.addChild(root_2, stream_else_expression.nextTree())


                    stream_else_expression.reset();

                    self._adaptor.addChild(root_2, 
                    self._adaptor.createFromType(ENDIF_, "ENDIF_")
                    )

                    self._adaptor.addChild(root_1, root_2)

                    self._adaptor.addChild(root_0, root_1)



                else: 
                    # 255:5: -> ^( IFELSE_ ^( IF_ ^( COND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( NCOND_ cond_comb ) ENDIF_ ) )
                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:255:8: ^( IFELSE_ ^( IF_ ^( COND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( NCOND_ cond_comb ) ENDIF_ ) )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(IFELSE_, "IFELSE_")
                    , root_1)

                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:255:18: ^( IF_ ^( COND_ cond_comb ) ( if_expression )* ENDIF_ )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(IF_, "IF_")
                    , root_2)

                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:255:24: ^( COND_ cond_comb )
                    root_3 = self._adaptor.nil()
                    root_3 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(COND_, "COND_")
                    , root_3)

                    self._adaptor.addChild(root_3, stream_cond_comb.nextTree())

                    self._adaptor.addChild(root_2, root_3)

                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:255:43: ( if_expression )*
                    while stream_if_expression.hasNext():
                        self._adaptor.addChild(root_2, stream_if_expression.nextTree())


                    stream_if_expression.reset();

                    self._adaptor.addChild(root_2, 
                    self._adaptor.createFromType(ENDIF_, "ENDIF_")
                    )

                    self._adaptor.addChild(root_1, root_2)

                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:255:66: ^( IF_ ^( NCOND_ cond_comb ) ENDIF_ )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(IF_, "IF_")
                    , root_2)

                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:255:72: ^( NCOND_ cond_comb )
                    root_3 = self._adaptor.nil()
                    root_3 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(NCOND_, "NCOND_")
                    , root_3)

                    self._adaptor.addChild(root_3, stream_cond_comb.nextTree())

                    self._adaptor.addChild(root_2, root_3)

                    self._adaptor.addChild(root_2, 
                    self._adaptor.createFromType(ENDIF_, "ENDIF_")
                    )

                    self._adaptor.addChild(root_1, root_2)

                    self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "if_stmt"


    class if_expression_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "if_expression"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:257:9: if_expression : ( exprwbreak )* ;
    def if_expression(self, ):
        retval = self.if_expression_return()
        retval.start = self.input.LT(1)


        root_0 = None

        exprwbreak219 = None


        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:257:22: ( ( exprwbreak )* )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:257:24: ( exprwbreak )*
                pass 
                root_0 = self._adaptor.nil()


                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:257:24: ( exprwbreak )*
                while True: #loop35
                    alt35 = 2
                    LA35_0 = self.input.LA(1)

                    if (LA35_0 in {BREAK, ID, IF, STATE}) :
                        alt35 = 1


                    if alt35 == 1:
                        # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:257:24: exprwbreak
                        pass 
                        self._state.following.append(self.FOLLOW_exprwbreak_in_if_expression2478)
                        exprwbreak219 = self.exprwbreak()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, exprwbreak219.tree)



                    else:
                        break #loop35




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "if_expression"


    class else_expression_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "else_expression"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:258:9: else_expression : ( exprwbreak )* ;
    def else_expression(self, ):
        retval = self.else_expression_return()
        retval.start = self.input.LT(1)


        root_0 = None

        exprwbreak220 = None


        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:258:24: ( ( exprwbreak )* )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:258:26: ( exprwbreak )*
                pass 
                root_0 = self._adaptor.nil()


                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:258:26: ( exprwbreak )*
                while True: #loop36
                    alt36 = 2
                    LA36_0 = self.input.LA(1)

                    if (LA36_0 in {BREAK, ID, IF, STATE}) :
                        alt36 = 1


                    if alt36 == 1:
                        # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:258:26: exprwbreak
                        pass 
                        self._state.following.append(self.FOLLOW_exprwbreak_in_else_expression2493)
                        exprwbreak220 = self.exprwbreak()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, exprwbreak220.tree)



                    else:
                        break #loop36




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "else_expression"


    class exprwbreak_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "exprwbreak"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:259:9: exprwbreak : ( expressions | network_send | network_mcast | next_break );
    def exprwbreak(self, ):
        retval = self.exprwbreak_return()
        retval.start = self.input.LT(1)


        root_0 = None

        expressions221 = None
        network_send222 = None
        network_mcast223 = None
        next_break224 = None


        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:259:19: ( expressions | network_send | network_mcast | next_break )
                alt37 = 4
                LA37 = self.input.LA(1)
                if LA37 in {ID}:
                    LA37_1 = self.input.LA(2)

                    if (LA37_1 == DOT) :
                        LA37 = self.input.LA(3)
                        if LA37 in {ID, NID, 95, 96, 97, 98, 99}:
                            alt37 = 1
                        elif LA37 in {101}:
                            alt37 = 2
                        elif LA37 in {100}:
                            alt37 = 3
                        else:
                            nvae = NoViableAltException("", 37, 5, self.input)

                            raise nvae


                    elif (LA37_1 in {EQUALSIGN, SEMICOLON}) :
                        alt37 = 1
                    else:
                        nvae = NoViableAltException("", 37, 1, self.input)

                        raise nvae


                elif LA37 in {IF, STATE}:
                    alt37 = 1
                elif LA37 in {BREAK}:
                    alt37 = 4
                else:
                    nvae = NoViableAltException("", 37, 0, self.input)

                    raise nvae


                if alt37 == 1:
                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:259:21: expressions
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_expressions_in_exprwbreak2508)
                    expressions221 = self.expressions()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, expressions221.tree)



                elif alt37 == 2:
                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:259:35: network_send
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_network_send_in_exprwbreak2512)
                    network_send222 = self.network_send()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, network_send222.tree)



                elif alt37 == 3:
                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:259:50: network_mcast
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_network_mcast_in_exprwbreak2516)
                    network_mcast223 = self.network_mcast()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, network_mcast223.tree)



                elif alt37 == 4:
                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:259:66: next_break
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_next_break_in_exprwbreak2520)
                    next_break224 = self.next_break()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, next_break224.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "exprwbreak"


    class cond_comb_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "cond_comb"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:260:9: cond_comb : cond_rel ( combinatorial_operator cond_rel )* ;
    def cond_comb(self, ):
        retval = self.cond_comb_return()
        retval.start = self.input.LT(1)


        root_0 = None

        cond_rel225 = None
        combinatorial_operator226 = None
        cond_rel227 = None


        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:260:18: ( cond_rel ( combinatorial_operator cond_rel )* )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:260:20: cond_rel ( combinatorial_operator cond_rel )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_cond_rel_in_cond_comb2534)
                cond_rel225 = self.cond_rel()

                self._state.following.pop()
                self._adaptor.addChild(root_0, cond_rel225.tree)


                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:260:29: ( combinatorial_operator cond_rel )*
                while True: #loop38
                    alt38 = 2
                    LA38_0 = self.input.LA(1)

                    if (LA38_0 in {87, 102}) :
                        alt38 = 1


                    if alt38 == 1:
                        # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:260:30: combinatorial_operator cond_rel
                        pass 
                        self._state.following.append(self.FOLLOW_combinatorial_operator_in_cond_comb2537)
                        combinatorial_operator226 = self.combinatorial_operator()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, combinatorial_operator226.tree)


                        self._state.following.append(self.FOLLOW_cond_rel_in_cond_comb2539)
                        cond_rel227 = self.cond_rel()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, cond_rel227.tree)



                    else:
                        break #loop38




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "cond_comb"


    class cond_rel_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "cond_rel"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:261:9: cond_rel : ( OBRACE )* cond_sel ( CBRACE )* -> cond_sel ;
    def cond_rel(self, ):
        retval = self.cond_rel_return()
        retval.start = self.input.LT(1)


        root_0 = None

        OBRACE228 = None
        CBRACE230 = None
        cond_sel229 = None

        OBRACE228_tree = None
        CBRACE230_tree = None
        stream_OBRACE = RewriteRuleTokenStream(self._adaptor, "token OBRACE")
        stream_CBRACE = RewriteRuleTokenStream(self._adaptor, "token CBRACE")
        stream_cond_sel = RewriteRuleSubtreeStream(self._adaptor, "rule cond_sel")
        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:261:18: ( ( OBRACE )* cond_sel ( CBRACE )* -> cond_sel )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:261:20: ( OBRACE )* cond_sel ( CBRACE )*
                pass 
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:261:20: ( OBRACE )*
                while True: #loop39
                    alt39 = 2
                    LA39_0 = self.input.LA(1)

                    if (LA39_0 == OBRACE) :
                        alt39 = 1


                    if alt39 == 1:
                        # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:261:20: OBRACE
                        pass 
                        OBRACE228 = self.match(self.input, OBRACE, self.FOLLOW_OBRACE_in_cond_rel2556) 
                        stream_OBRACE.add(OBRACE228)



                    else:
                        break #loop39


                self._state.following.append(self.FOLLOW_cond_sel_in_cond_rel2559)
                cond_sel229 = self.cond_sel()

                self._state.following.pop()
                stream_cond_sel.add(cond_sel229.tree)


                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:261:37: ( CBRACE )*
                while True: #loop40
                    alt40 = 2
                    LA40_0 = self.input.LA(1)

                    if (LA40_0 == CBRACE) :
                        alt40 = 1


                    if alt40 == 1:
                        # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:261:37: CBRACE
                        pass 
                        CBRACE230 = self.match(self.input, CBRACE, self.FOLLOW_CBRACE_in_cond_rel2561) 
                        stream_CBRACE.add(CBRACE230)



                    else:
                        break #loop40


                # AST Rewrite
                # elements: cond_sel
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 261:45: -> cond_sel
                self._adaptor.addChild(root_0, stream_cond_sel.nextTree())




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "cond_rel"


    class cond_sel_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "cond_sel"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:262:13: cond_sel : cond_types ( relational_operator cond_types )* ;
    def cond_sel(self, ):
        retval = self.cond_sel_return()
        retval.start = self.input.LT(1)


        root_0 = None

        cond_types231 = None
        relational_operator232 = None
        cond_types233 = None


        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:262:22: ( cond_types ( relational_operator cond_types )* )
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:262:24: cond_types ( relational_operator cond_types )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_cond_types_in_cond_sel2585)
                cond_types231 = self.cond_types()

                self._state.following.pop()
                self._adaptor.addChild(root_0, cond_types231.tree)


                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:262:35: ( relational_operator cond_types )*
                while True: #loop41
                    alt41 = 2
                    LA41_0 = self.input.LA(1)

                    if ((88 <= LA41_0 <= 92) or LA41_0 in {86}) :
                        alt41 = 1


                    if alt41 == 1:
                        # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:262:36: relational_operator cond_types
                        pass 
                        self._state.following.append(self.FOLLOW_relational_operator_in_cond_sel2588)
                        relational_operator232 = self.relational_operator()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, relational_operator232.tree)


                        self._state.following.append(self.FOLLOW_cond_types_in_cond_sel2590)
                        cond_types233 = self.cond_types()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, cond_types233.tree)



                    else:
                        break #loop41




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "cond_sel"


    class cond_types_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "cond_types"
    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:263:13: cond_types : ( object_expr | set_func | INT | BOOL );
    def cond_types(self, ):
        retval = self.cond_types_return()
        retval.start = self.input.LT(1)


        root_0 = None

        INT236 = None
        BOOL237 = None
        object_expr234 = None
        set_func235 = None

        INT236_tree = None
        BOOL237_tree = None

        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:263:24: ( object_expr | set_func | INT | BOOL )
                alt42 = 4
                LA42 = self.input.LA(1)
                if LA42 in {ID}:
                    LA42_1 = self.input.LA(2)

                    if (LA42_1 == DOT) :
                        LA42_4 = self.input.LA(3)

                        if (LA42_4 in {ID, NID}) :
                            alt42 = 1
                        elif ((95 <= LA42_4 <= 99) or LA42_4 in {}) :
                            alt42 = 2
                        else:
                            nvae = NoViableAltException("", 42, 4, self.input)

                            raise nvae


                    elif ((86 <= LA42_1 <= 92) or LA42_1 in {CBRACE, OCBRACE, 102}) :
                        alt42 = 1
                    else:
                        nvae = NoViableAltException("", 42, 1, self.input)

                        raise nvae


                elif LA42 in {INT}:
                    alt42 = 3
                elif LA42 in {BOOL}:
                    alt42 = 4
                else:
                    nvae = NoViableAltException("", 42, 0, self.input)

                    raise nvae


                if alt42 == 1:
                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:263:26: object_expr
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_object_expr_in_cond_types2611)
                    object_expr234 = self.object_expr()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, object_expr234.tree)



                elif alt42 == 2:
                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:263:40: set_func
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_set_func_in_cond_types2615)
                    set_func235 = self.set_func()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, set_func235.tree)



                elif alt42 == 3:
                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:263:51: INT
                    pass 
                    root_0 = self._adaptor.nil()


                    INT236 = self.match(self.input, INT, self.FOLLOW_INT_in_cond_types2619)
                    INT236_tree = self._adaptor.createWithPayload(INT236)
                    self._adaptor.addChild(root_0, INT236_tree)




                elif alt42 == 4:
                    # /home/tux/PycharmProjects/ProtoGen/Parser/ProtoCC.g:263:57: BOOL
                    pass 
                    root_0 = self._adaptor.nil()


                    BOOL237 = self.match(self.input, BOOL, self.FOLLOW_BOOL_in_cond_types2623)
                    BOOL237_tree = self._adaptor.createWithPayload(BOOL237)
                    self._adaptor.addChild(root_0, BOOL237_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "cond_types"



 

    FOLLOW_101_in_send_function571 = frozenset([1])
    FOLLOW_100_in_mcast_function582 = frozenset([1])
    FOLLOW_const_decl_in_document903 = frozenset([1, 5, 17, 25, 30, 43, 45, 57, 61, 81])
    FOLLOW_init_hw_in_document907 = frozenset([1, 5, 17, 25, 30, 43, 45, 57, 61, 81])
    FOLLOW_arch_block_in_document911 = frozenset([1, 5, 17, 25, 30, 43, 45, 57, 61, 81])
    FOLLOW_expressions_in_document915 = frozenset([1, 5, 17, 25, 30, 43, 45, 57, 61, 81])
    FOLLOW_int_decl_in_declarations928 = frozenset([1])
    FOLLOW_bool_decl_in_declarations932 = frozenset([1])
    FOLLOW_state_decl_in_declarations936 = frozenset([1])
    FOLLOW_data_decl_in_declarations940 = frozenset([1])
    FOLLOW_id_decl_in_declarations944 = frozenset([1])
    FOLLOW_CONSTANT_in_const_decl956 = frozenset([43])
    FOLLOW_ID_in_const_decl958 = frozenset([50])
    FOLLOW_INT_in_const_decl960 = frozenset([1])
    FOLLOW_INTID_in_int_decl982 = frozenset([69])
    FOLLOW_range_in_int_decl984 = frozenset([43])
    FOLLOW_ID_in_int_decl986 = frozenset([39, 74])
    FOLLOW_EQUALSIGN_in_int_decl989 = frozenset([50])
    FOLLOW_INT_in_int_decl991 = frozenset([39, 74])
    FOLLOW_SEMICOLON_in_int_decl995 = frozenset([1])
    FOLLOW_BOOLID_in_bool_decl1023 = frozenset([43])
    FOLLOW_ID_in_bool_decl1025 = frozenset([39, 74])
    FOLLOW_EQUALSIGN_in_bool_decl1028 = frozenset([12])
    FOLLOW_BOOL_in_bool_decl1030 = frozenset([39, 74])
    FOLLOW_SEMICOLON_in_bool_decl1034 = frozenset([1])
    FOLLOW_STATE_in_state_decl1061 = frozenset([43])
    FOLLOW_ID_in_state_decl1063 = frozenset([74])
    FOLLOW_SEMICOLON_in_state_decl1065 = frozenset([1])
    FOLLOW_DATA_in_data_decl1084 = frozenset([43])
    FOLLOW_ID_in_data_decl1086 = frozenset([74])
    FOLLOW_SEMICOLON_in_data_decl1088 = frozenset([1])
    FOLLOW_set_decl_in_id_decl1107 = frozenset([65, 76])
    FOLLOW_NID_in_id_decl1110 = frozenset([43])
    FOLLOW_ID_in_id_decl1112 = frozenset([74])
    FOLLOW_SEMICOLON_in_id_decl1114 = frozenset([1])
    FOLLOW_SET_in_set_decl1136 = frozenset([69])
    FOLLOW_OEBRACE_in_set_decl1138 = frozenset([43, 50])
    FOLLOW_val_range_in_set_decl1140 = frozenset([21])
    FOLLOW_CEBRACE_in_set_decl1142 = frozenset([1])
    FOLLOW_SET_in_objset_decl1161 = frozenset([69])
    FOLLOW_OEBRACE_in_objset_decl1163 = frozenset([43, 50])
    FOLLOW_val_range_in_objset_decl1165 = frozenset([21])
    FOLLOW_CEBRACE_in_objset_decl1167 = frozenset([1])
    FOLLOW_OEBRACE_in_range1191 = frozenset([43, 50])
    FOLLOW_val_range_in_range1193 = frozenset([32])
    FOLLOW_DOT_in_range1195 = frozenset([32])
    FOLLOW_DOT_in_range1197 = frozenset([43, 50])
    FOLLOW_val_range_in_range1199 = frozenset([21])
    FOLLOW_CEBRACE_in_range1201 = frozenset([1])
    FOLLOW_ARRAY_in_array_decl1250 = frozenset([69])
    FOLLOW_range_in_array_decl1252 = frozenset([1])
    FOLLOW_FIFO_in_fifo_decl1262 = frozenset([69])
    FOLLOW_range_in_fifo_decl1264 = frozenset([1])
    FOLLOW_network_block_in_init_hw1274 = frozenset([1])
    FOLLOW_machines_in_init_hw1278 = frozenset([1])
    FOLLOW_message_block_in_init_hw1282 = frozenset([1])
    FOLLOW_object_expr_in_object_block1293 = frozenset([74])
    FOLLOW_SEMICOLON_in_object_block1295 = frozenset([1])
    FOLLOW_ID_in_object_expr1310 = frozenset([1])
    FOLLOW_object_func_in_object_expr1314 = frozenset([1])
    FOLLOW_ID_in_object_func1325 = frozenset([32])
    FOLLOW_DOT_in_object_func1327 = frozenset([43, 65])
    FOLLOW_object_idres_in_object_func1329 = frozenset([1, 67])
    FOLLOW_OBRACE_in_object_func1332 = frozenset([19, 22, 43])
    FOLLOW_object_expr_in_object_func1334 = frozenset([19, 22, 43])
    FOLLOW_COMMA_in_object_func1338 = frozenset([43])
    FOLLOW_object_expr_in_object_func1340 = frozenset([19, 22])
    FOLLOW_CBRACE_in_object_func1344 = frozenset([1, 67])
    FOLLOW_cache_block_in_machines1413 = frozenset([1])
    FOLLOW_dir_block_in_machines1417 = frozenset([1])
    FOLLOW_CACHE_in_cache_block1432 = frozenset([68])
    FOLLOW_OCBRACE_in_cache_block1434 = frozenset([13, 20, 27, 51, 65, 76, 81])
    FOLLOW_declarations_in_cache_block1436 = frozenset([13, 20, 27, 51, 65, 76, 81])
    FOLLOW_CCBRACE_in_cache_block1439 = frozenset([43, 76])
    FOLLOW_objset_decl_in_cache_block1441 = frozenset([43, 76])
    FOLLOW_ID_in_cache_block1444 = frozenset([74])
    FOLLOW_SEMICOLON_in_cache_block1446 = frozenset([1])
    FOLLOW_DIR_in_dir_block1487 = frozenset([68])
    FOLLOW_OCBRACE_in_dir_block1489 = frozenset([13, 20, 27, 51, 65, 76, 81])
    FOLLOW_declarations_in_dir_block1491 = frozenset([13, 20, 27, 51, 65, 76, 81])
    FOLLOW_CCBRACE_in_dir_block1494 = frozenset([43, 76])
    FOLLOW_objset_decl_in_dir_block1496 = frozenset([43, 76])
    FOLLOW_ID_in_dir_block1499 = frozenset([74])
    FOLLOW_SEMICOLON_in_dir_block1501 = frozenset([1])
    FOLLOW_NETWORK_in_network_block1545 = frozenset([68])
    FOLLOW_OCBRACE_in_network_block1547 = frozenset([20, 93, 94])
    FOLLOW_network_element_in_network_block1549 = frozenset([20, 93, 94])
    FOLLOW_CCBRACE_in_network_block1552 = frozenset([74])
    FOLLOW_SEMICOLON_in_network_block1554 = frozenset([1])
    FOLLOW_element_type_in_network_element1597 = frozenset([43])
    FOLLOW_ID_in_network_element1599 = frozenset([74])
    FOLLOW_SEMICOLON_in_network_element1601 = frozenset([1])
    FOLLOW_ID_in_network_send1622 = frozenset([32])
    FOLLOW_DOT_in_network_send1624 = frozenset([101])
    FOLLOW_send_function_in_network_send1626 = frozenset([67])
    FOLLOW_OBRACE_in_network_send1628 = frozenset([43])
    FOLLOW_ID_in_network_send1630 = frozenset([19])
    FOLLOW_CBRACE_in_network_send1632 = frozenset([74])
    FOLLOW_SEMICOLON_in_network_send1634 = frozenset([1])
    FOLLOW_ID_in_network_mcast1654 = frozenset([32])
    FOLLOW_DOT_in_network_mcast1656 = frozenset([100])
    FOLLOW_mcast_function_in_network_mcast1658 = frozenset([67])
    FOLLOW_OBRACE_in_network_mcast1660 = frozenset([43])
    FOLLOW_ID_in_network_mcast1662 = frozenset([22])
    FOLLOW_COMMA_in_network_mcast1664 = frozenset([43])
    FOLLOW_ID_in_network_mcast1666 = frozenset([19])
    FOLLOW_CBRACE_in_network_mcast1668 = frozenset([74])
    FOLLOW_SEMICOLON_in_network_mcast1670 = frozenset([1])
    FOLLOW_MSG_in_message_block1700 = frozenset([43])
    FOLLOW_ID_in_message_block1702 = frozenset([68])
    FOLLOW_OCBRACE_in_message_block1704 = frozenset([13, 20, 27, 51, 65, 76, 81])
    FOLLOW_declarations_in_message_block1706 = frozenset([13, 20, 27, 51, 65, 76, 81])
    FOLLOW_CCBRACE_in_message_block1709 = frozenset([74])
    FOLLOW_SEMICOLON_in_message_block1711 = frozenset([1])
    FOLLOW_ID_in_message_constr1733 = frozenset([67])
    FOLLOW_OBRACE_in_message_constr1735 = frozenset([12, 19, 22, 43, 50, 65])
    FOLLOW_message_expr_in_message_constr1737 = frozenset([12, 19, 22, 43, 50, 65])
    FOLLOW_COMMA_in_message_constr1741 = frozenset([12, 43, 50, 65])
    FOLLOW_message_expr_in_message_constr1743 = frozenset([19, 22])
    FOLLOW_CBRACE_in_message_constr1747 = frozenset([1])
    FOLLOW_object_expr_in_message_expr1769 = frozenset([1])
    FOLLOW_set_func_in_message_expr1773 = frozenset([1])
    FOLLOW_INT_in_message_expr1777 = frozenset([1])
    FOLLOW_BOOL_in_message_expr1781 = frozenset([1])
    FOLLOW_NID_in_message_expr1785 = frozenset([1])
    FOLLOW_set_func_in_set_block1803 = frozenset([74])
    FOLLOW_SEMICOLON_in_set_block1805 = frozenset([1])
    FOLLOW_ID_in_set_func1820 = frozenset([32])
    FOLLOW_DOT_in_set_func1822 = frozenset([95, 96, 97, 98, 99])
    FOLLOW_set_function_types_in_set_func1824 = frozenset([67])
    FOLLOW_OBRACE_in_set_func1826 = frozenset([19, 43])
    FOLLOW_set_nest_in_set_func1828 = frozenset([19, 43])
    FOLLOW_CBRACE_in_set_func1831 = frozenset([1])
    FOLLOW_set_func_in_set_nest1869 = frozenset([1])
    FOLLOW_object_expr_in_set_nest1873 = frozenset([1])
    FOLLOW_ARCH_in_arch_block1883 = frozenset([43])
    FOLLOW_ID_in_arch_block1885 = frozenset([68])
    FOLLOW_OCBRACE_in_arch_block1887 = frozenset([20, 71, 79])
    FOLLOW_arch_body_in_arch_block1889 = frozenset([20])
    FOLLOW_CCBRACE_in_arch_block1891 = frozenset([1])
    FOLLOW_stable_def_in_arch_body1913 = frozenset([1, 71, 79])
    FOLLOW_process_block_in_arch_body1917 = frozenset([1, 71, 79])
    FOLLOW_STABLE_in_stable_def1927 = frozenset([68])
    FOLLOW_OCBRACE_in_stable_def1929 = frozenset([43])
    FOLLOW_ID_in_stable_def1931 = frozenset([20, 22])
    FOLLOW_COMMA_in_stable_def1934 = frozenset([43])
    FOLLOW_ID_in_stable_def1936 = frozenset([20, 22])
    FOLLOW_CCBRACE_in_stable_def1940 = frozenset([1])
    FOLLOW_PROC_in_process_block1959 = frozenset([67])
    FOLLOW_process_trans_in_process_block1961 = frozenset([68])
    FOLLOW_OCBRACE_in_process_block1963 = frozenset([10, 20, 43, 45, 81])
    FOLLOW_process_expr_in_process_block1965 = frozenset([10, 20, 43, 45, 81])
    FOLLOW_CCBRACE_in_process_block1968 = frozenset([1])
    FOLLOW_OBRACE_in_process_trans1994 = frozenset([43])
    FOLLOW_ID_in_process_trans1996 = frozenset([22])
    FOLLOW_COMMA_in_process_trans1998 = frozenset([4, 43])
    FOLLOW_process_events_in_process_trans2000 = frozenset([19, 22])
    FOLLOW_process_finalstate_in_process_trans2002 = frozenset([19, 22])
    FOLLOW_CBRACE_in_process_trans2005 = frozenset([1])
    FOLLOW_COMMA_in_process_finalstate2028 = frozenset([43, 81])
    FOLLOW_process_finalident_in_process_finalstate2030 = frozenset([1])
    FOLLOW_expressions_in_process_expr2079 = frozenset([1])
    FOLLOW_network_send_in_process_expr2083 = frozenset([1])
    FOLLOW_network_mcast_in_process_expr2087 = frozenset([1])
    FOLLOW_transaction_in_process_expr2091 = frozenset([1])
    FOLLOW_AWAIT_in_transaction2101 = frozenset([68])
    FOLLOW_OCBRACE_in_transaction2103 = frozenset([20, 83])
    FOLLOW_trans_in_transaction2105 = frozenset([20, 83])
    FOLLOW_CCBRACE_in_transaction2108 = frozenset([1])
    FOLLOW_WHEN_in_trans2128 = frozenset([43])
    FOLLOW_ID_in_trans2130 = frozenset([29])
    FOLLOW_DDOT_in_trans2132 = frozenset([1, 10, 15, 43, 45, 63, 81])
    FOLLOW_trans_body_in_trans2134 = frozenset([1, 10, 15, 43, 45, 63, 81])
    FOLLOW_expressions_in_trans_body2167 = frozenset([1])
    FOLLOW_next_trans_in_trans_body2171 = frozenset([1])
    FOLLOW_next_break_in_trans_body2175 = frozenset([1])
    FOLLOW_transaction_in_trans_body2179 = frozenset([1])
    FOLLOW_NEXT_in_next_trans2197 = frozenset([68])
    FOLLOW_OCBRACE_in_next_trans2199 = frozenset([20, 83])
    FOLLOW_trans_in_next_trans2201 = frozenset([20, 83])
    FOLLOW_CCBRACE_in_next_trans2204 = frozenset([1])
    FOLLOW_BREAK_in_next_break2221 = frozenset([74])
    FOLLOW_SEMICOLON_in_next_break2223 = frozenset([1])
    FOLLOW_assignment_in_expressions2239 = frozenset([1])
    FOLLOW_conditional_in_expressions2243 = frozenset([1])
    FOLLOW_object_block_in_expressions2247 = frozenset([1])
    FOLLOW_set_block_in_expressions2251 = frozenset([1])
    FOLLOW_process_finalident_in_assignment2258 = frozenset([39])
    FOLLOW_EQUALSIGN_in_assignment2260 = frozenset([12, 43, 50])
    FOLLOW_assign_types_in_assignment2262 = frozenset([74])
    FOLLOW_SEMICOLON_in_assignment2264 = frozenset([1])
    FOLLOW_object_expr_in_assign_types2286 = frozenset([1])
    FOLLOW_message_constr_in_assign_types2290 = frozenset([1])
    FOLLOW_math_op_in_assign_types2294 = frozenset([1])
    FOLLOW_set_func_in_assign_types2298 = frozenset([1])
    FOLLOW_INT_in_assign_types2302 = frozenset([1])
    FOLLOW_BOOL_in_assign_types2306 = frozenset([1])
    FOLLOW_val_range_in_math_op2317 = frozenset([56, 70])
    FOLLOW_set_in_math_op2319 = frozenset([43, 50])
    FOLLOW_val_range_in_math_op2327 = frozenset([1])
    FOLLOW_if_stmt_in_conditional2336 = frozenset([1])
    FOLLOW_IF_in_if_stmt2355 = frozenset([12, 43, 50, 67])
    FOLLOW_cond_comb_in_if_stmt2357 = frozenset([68])
    FOLLOW_OCBRACE_in_if_stmt2359 = frozenset([15, 20, 43, 45, 81])
    FOLLOW_if_expression_in_if_stmt2361 = frozenset([20])
    FOLLOW_CCBRACE_in_if_stmt2363 = frozenset([1, 34])
    FOLLOW_ELSE_in_if_stmt2370 = frozenset([68])
    FOLLOW_OCBRACE_in_if_stmt2374 = frozenset([15, 20, 43, 45, 81])
    FOLLOW_else_expression_in_if_stmt2376 = frozenset([20])
    FOLLOW_CCBRACE_in_if_stmt2378 = frozenset([1, 34])
    FOLLOW_exprwbreak_in_if_expression2478 = frozenset([1, 15, 43, 45, 81])
    FOLLOW_exprwbreak_in_else_expression2493 = frozenset([1, 15, 43, 45, 81])
    FOLLOW_expressions_in_exprwbreak2508 = frozenset([1])
    FOLLOW_network_send_in_exprwbreak2512 = frozenset([1])
    FOLLOW_network_mcast_in_exprwbreak2516 = frozenset([1])
    FOLLOW_next_break_in_exprwbreak2520 = frozenset([1])
    FOLLOW_cond_rel_in_cond_comb2534 = frozenset([1, 87, 102])
    FOLLOW_combinatorial_operator_in_cond_comb2537 = frozenset([12, 43, 50, 67])
    FOLLOW_cond_rel_in_cond_comb2539 = frozenset([1, 87, 102])
    FOLLOW_OBRACE_in_cond_rel2556 = frozenset([12, 43, 50, 67])
    FOLLOW_cond_sel_in_cond_rel2559 = frozenset([1, 19])
    FOLLOW_CBRACE_in_cond_rel2561 = frozenset([1, 19])
    FOLLOW_cond_types_in_cond_sel2585 = frozenset([1, 86, 88, 89, 90, 91, 92])
    FOLLOW_relational_operator_in_cond_sel2588 = frozenset([12, 43, 50])
    FOLLOW_cond_types_in_cond_sel2590 = frozenset([1, 86, 88, 89, 90, 91, 92])
    FOLLOW_object_expr_in_cond_types2611 = frozenset([1])
    FOLLOW_set_func_in_cond_types2615 = frozenset([1])
    FOLLOW_INT_in_cond_types2619 = frozenset([1])
    FOLLOW_BOOL_in_cond_types2623 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("ProtoCCLexer", ProtoCCParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
