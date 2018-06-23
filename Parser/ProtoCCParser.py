# $ANTLR 3.5.2 /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g 2018-06-22 21:37:10

import sys
from antlr3 import *

from antlr3.tree import *




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
    "MSGCSTR_", "MSG_", "NCOND_", "NEG", "NETWORK", "NETWORK_", "NEXT", 
    "NEXT_", "NID", "OBJSET_", "OBRACE", "OCBRACE", "OEBRACE", "PLUS", "PROC", 
    "PROC_", "RANGE_", "SEMICOLON", "SEND_", "SET", "SETFUNC_", "SET_", 
    "STABLE", "STABLE_", "STATE", "TRANS_", "WHEN", "WHEN_", "WS", "'!='", 
    "'&'", "'<'", "'<='", "'=='", "'>'", "'>='", "'Ordered'", "'Unordered'", 
    "'add'", "'clear'", "'contains'", "'count'", "'del'", "'mcast'", "'send'", 
    "'|'"
]



class ProtoCCParser(Parser):
    grammarFileName = "/home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g"
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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:111:1: send_function : 'send' ;
    def send_function(self, ):
        retval = self.send_function_return()
        retval.start = self.input.LT(1)


        root_0 = None

        string_literal1 = None

        string_literal1_tree = None

        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:112:2: ( 'send' )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:112:4: 'send'
                pass 
                root_0 = self._adaptor.nil()


                string_literal1 = self.match(self.input, 102, self.FOLLOW_102_in_send_function580)
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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:115:1: mcast_function : 'mcast' ;
    def mcast_function(self, ):
        retval = self.mcast_function_return()
        retval.start = self.input.LT(1)


        root_0 = None

        string_literal2 = None

        string_literal2_tree = None

        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:116:2: ( 'mcast' )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:116:4: 'mcast'
                pass 
                root_0 = self._adaptor.nil()


                string_literal2 = self.match(self.input, 101, self.FOLLOW_101_in_mcast_function591)
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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:119:1: set_function_types : ( 'add' | 'count' | 'contains' | 'del' | 'clear' );
    def set_function_types(self, ):
        retval = self.set_function_types_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set3 = None

        set3_tree = None

        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:120:2: ( 'add' | 'count' | 'contains' | 'del' | 'clear' )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:
                pass 
                root_0 = self._adaptor.nil()


                set3 = self.input.LT(1)

                if (96 <= self.input.LA(1) <= 100) or self.input.LA(1) in {}:
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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:127:1: relational_operator : ( '==' | '!=' | '<=' | '>=' | '<' | '>' );
    def relational_operator(self, ):
        retval = self.relational_operator_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set4 = None

        set4_tree = None

        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:128:2: ( '==' | '!=' | '<=' | '>=' | '<' | '>' )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:
                pass 
                root_0 = self._adaptor.nil()


                set4 = self.input.LT(1)

                if (89 <= self.input.LA(1) <= 93) or self.input.LA(1) in {87}:
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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:136:1: combinatorial_operator : ( '&' | '|' );
    def combinatorial_operator(self, ):
        retval = self.combinatorial_operator_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set5 = None

        set5_tree = None

        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:137:5: ( '&' | '|' )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:
                pass 
                root_0 = self._adaptor.nil()


                set5 = self.input.LT(1)

                if self.input.LA(1) in {88, 103}:
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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:166:1: document : ( const_decl | init_hw | arch_block | expressions )* ;
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
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:167:2: ( ( const_decl | init_hw | arch_block | expressions )* )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:167:4: ( const_decl | init_hw | arch_block | expressions )*
                pass 
                root_0 = self._adaptor.nil()


                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:167:4: ( const_decl | init_hw | arch_block | expressions )*
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
                        # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:167:5: const_decl
                        pass 
                        self._state.following.append(self.FOLLOW_const_decl_in_document912)
                        const_decl6 = self.const_decl()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, const_decl6.tree)



                    elif alt1 == 2:
                        # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:167:18: init_hw
                        pass 
                        self._state.following.append(self.FOLLOW_init_hw_in_document916)
                        init_hw7 = self.init_hw()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, init_hw7.tree)



                    elif alt1 == 3:
                        # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:167:28: arch_block
                        pass 
                        self._state.following.append(self.FOLLOW_arch_block_in_document920)
                        arch_block8 = self.arch_block()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, arch_block8.tree)



                    elif alt1 == 4:
                        # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:167:41: expressions
                        pass 
                        self._state.following.append(self.FOLLOW_expressions_in_document924)
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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:171:1: declarations : ( int_decl | bool_decl | state_decl | data_decl | id_decl );
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
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:171:14: ( int_decl | bool_decl | state_decl | data_decl | id_decl )
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
                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:171:16: int_decl
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_int_decl_in_declarations937)
                    int_decl10 = self.int_decl()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, int_decl10.tree)



                elif alt2 == 2:
                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:171:27: bool_decl
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_bool_decl_in_declarations941)
                    bool_decl11 = self.bool_decl()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, bool_decl11.tree)



                elif alt2 == 3:
                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:171:39: state_decl
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_state_decl_in_declarations945)
                    state_decl12 = self.state_decl()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, state_decl12.tree)



                elif alt2 == 4:
                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:171:52: data_decl
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_data_decl_in_declarations949)
                    data_decl13 = self.data_decl()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, data_decl13.tree)



                elif alt2 == 5:
                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:171:64: id_decl
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_id_decl_in_declarations953)
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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:173:5: const_decl : CONSTANT ID INT -> ^( CONSTANT_ ID INT ) ;
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
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:173:16: ( CONSTANT ID INT -> ^( CONSTANT_ ID INT ) )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:173:18: CONSTANT ID INT
                pass 
                CONSTANT15 = self.match(self.input, CONSTANT, self.FOLLOW_CONSTANT_in_const_decl965) 
                stream_CONSTANT.add(CONSTANT15)


                ID16 = self.match(self.input, ID, self.FOLLOW_ID_in_const_decl967) 
                stream_ID.add(ID16)


                INT17 = self.match(self.input, INT, self.FOLLOW_INT_in_const_decl969) 
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
                # 173:34: -> ^( CONSTANT_ ID INT )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:173:37: ^( CONSTANT_ ID INT )
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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:175:5: int_decl : INTID range ID ( EQUALSIGN INT )* SEMICOLON -> ^( INT_ range ID ( INITVAL_ INT )* ) ;
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
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:175:14: ( INTID range ID ( EQUALSIGN INT )* SEMICOLON -> ^( INT_ range ID ( INITVAL_ INT )* ) )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:175:16: INTID range ID ( EQUALSIGN INT )* SEMICOLON
                pass 
                INTID18 = self.match(self.input, INTID, self.FOLLOW_INTID_in_int_decl991) 
                stream_INTID.add(INTID18)


                self._state.following.append(self.FOLLOW_range_in_int_decl993)
                range19 = self.range()

                self._state.following.pop()
                stream_range.add(range19.tree)


                ID20 = self.match(self.input, ID, self.FOLLOW_ID_in_int_decl995) 
                stream_ID.add(ID20)


                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:175:31: ( EQUALSIGN INT )*
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == EQUALSIGN) :
                        alt3 = 1


                    if alt3 == 1:
                        # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:175:32: EQUALSIGN INT
                        pass 
                        EQUALSIGN21 = self.match(self.input, EQUALSIGN, self.FOLLOW_EQUALSIGN_in_int_decl998) 
                        stream_EQUALSIGN.add(EQUALSIGN21)


                        INT22 = self.match(self.input, INT, self.FOLLOW_INT_in_int_decl1000) 
                        stream_INT.add(INT22)



                    else:
                        break #loop3


                SEMICOLON23 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_int_decl1004) 
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
                # 175:58: -> ^( INT_ range ID ( INITVAL_ INT )* )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:175:61: ^( INT_ range ID ( INITVAL_ INT )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(INT_, "INT_")
                , root_1)

                self._adaptor.addChild(root_1, stream_range.nextTree())

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:175:77: ( INITVAL_ INT )*
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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:176:5: bool_decl : BOOLID ID ( EQUALSIGN BOOL )* SEMICOLON -> ^( BOOL_ ID ( INITVAL_ BOOL )* ) ;
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
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:176:15: ( BOOLID ID ( EQUALSIGN BOOL )* SEMICOLON -> ^( BOOL_ ID ( INITVAL_ BOOL )* ) )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:176:17: BOOLID ID ( EQUALSIGN BOOL )* SEMICOLON
                pass 
                BOOLID24 = self.match(self.input, BOOLID, self.FOLLOW_BOOLID_in_bool_decl1032) 
                stream_BOOLID.add(BOOLID24)


                ID25 = self.match(self.input, ID, self.FOLLOW_ID_in_bool_decl1034) 
                stream_ID.add(ID25)


                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:176:27: ( EQUALSIGN BOOL )*
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == EQUALSIGN) :
                        alt4 = 1


                    if alt4 == 1:
                        # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:176:28: EQUALSIGN BOOL
                        pass 
                        EQUALSIGN26 = self.match(self.input, EQUALSIGN, self.FOLLOW_EQUALSIGN_in_bool_decl1037) 
                        stream_EQUALSIGN.add(EQUALSIGN26)


                        BOOL27 = self.match(self.input, BOOL, self.FOLLOW_BOOL_in_bool_decl1039) 
                        stream_BOOL.add(BOOL27)



                    else:
                        break #loop4


                SEMICOLON28 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_bool_decl1043) 
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
                # 176:55: -> ^( BOOL_ ID ( INITVAL_ BOOL )* )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:176:58: ^( BOOL_ ID ( INITVAL_ BOOL )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(BOOL_, "BOOL_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:176:69: ( INITVAL_ BOOL )*
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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:178:5: state_decl : STATE ID SEMICOLON -> ^( INITSTATE_ ID ) ;
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
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:178:16: ( STATE ID SEMICOLON -> ^( INITSTATE_ ID ) )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:178:18: STATE ID SEMICOLON
                pass 
                STATE29 = self.match(self.input, STATE, self.FOLLOW_STATE_in_state_decl1070) 
                stream_STATE.add(STATE29)


                ID30 = self.match(self.input, ID, self.FOLLOW_ID_in_state_decl1072) 
                stream_ID.add(ID30)


                SEMICOLON31 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_state_decl1074) 
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
                # 178:37: -> ^( INITSTATE_ ID )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:178:40: ^( INITSTATE_ ID )
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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:179:5: data_decl : DATA ID SEMICOLON -> ^( DATA_ ID ) ;
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
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:179:15: ( DATA ID SEMICOLON -> ^( DATA_ ID ) )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:179:17: DATA ID SEMICOLON
                pass 
                DATA32 = self.match(self.input, DATA, self.FOLLOW_DATA_in_data_decl1093) 
                stream_DATA.add(DATA32)


                ID33 = self.match(self.input, ID, self.FOLLOW_ID_in_data_decl1095) 
                stream_ID.add(ID33)


                SEMICOLON34 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_data_decl1097) 
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
                # 179:35: -> ^( DATA_ ID )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:179:38: ^( DATA_ ID )
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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:180:5: id_decl : ( set_decl )* NID ID SEMICOLON -> ^( ID_ ( set_decl )* ID ) ;
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
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:180:13: ( ( set_decl )* NID ID SEMICOLON -> ^( ID_ ( set_decl )* ID ) )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:180:15: ( set_decl )* NID ID SEMICOLON
                pass 
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:180:15: ( set_decl )*
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == SET) :
                        alt5 = 1


                    if alt5 == 1:
                        # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:180:15: set_decl
                        pass 
                        self._state.following.append(self.FOLLOW_set_decl_in_id_decl1116)
                        set_decl35 = self.set_decl()

                        self._state.following.pop()
                        stream_set_decl.add(set_decl35.tree)



                    else:
                        break #loop5


                NID36 = self.match(self.input, NID, self.FOLLOW_NID_in_id_decl1119) 
                stream_NID.add(NID36)


                ID37 = self.match(self.input, ID, self.FOLLOW_ID_in_id_decl1121) 
                stream_ID.add(ID37)


                SEMICOLON38 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_id_decl1123) 
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
                # 180:42: -> ^( ID_ ( set_decl )* ID )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:180:45: ^( ID_ ( set_decl )* ID )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(ID_, "ID_")
                , root_1)

                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:180:51: ( set_decl )*
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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:181:5: set_decl : SET OEBRACE val_range CEBRACE -> ^( SET_ val_range ) ;
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
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:181:14: ( SET OEBRACE val_range CEBRACE -> ^( SET_ val_range ) )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:181:16: SET OEBRACE val_range CEBRACE
                pass 
                SET39 = self.match(self.input, SET, self.FOLLOW_SET_in_set_decl1145) 
                stream_SET.add(SET39)


                OEBRACE40 = self.match(self.input, OEBRACE, self.FOLLOW_OEBRACE_in_set_decl1147) 
                stream_OEBRACE.add(OEBRACE40)


                self._state.following.append(self.FOLLOW_val_range_in_set_decl1149)
                val_range41 = self.val_range()

                self._state.following.pop()
                stream_val_range.add(val_range41.tree)


                CEBRACE42 = self.match(self.input, CEBRACE, self.FOLLOW_CEBRACE_in_set_decl1151) 
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
                # 181:46: -> ^( SET_ val_range )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:181:49: ^( SET_ val_range )
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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:182:5: objset_decl : SET OEBRACE val_range CEBRACE -> ^( OBJSET_ val_range ) ;
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
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:182:17: ( SET OEBRACE val_range CEBRACE -> ^( OBJSET_ val_range ) )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:182:19: SET OEBRACE val_range CEBRACE
                pass 
                SET43 = self.match(self.input, SET, self.FOLLOW_SET_in_objset_decl1170) 
                stream_SET.add(SET43)


                OEBRACE44 = self.match(self.input, OEBRACE, self.FOLLOW_OEBRACE_in_objset_decl1172) 
                stream_OEBRACE.add(OEBRACE44)


                self._state.following.append(self.FOLLOW_val_range_in_objset_decl1174)
                val_range45 = self.val_range()

                self._state.following.pop()
                stream_val_range.add(val_range45.tree)


                CEBRACE46 = self.match(self.input, CEBRACE, self.FOLLOW_CEBRACE_in_objset_decl1176) 
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
                # 182:49: -> ^( OBJSET_ val_range )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:182:52: ^( OBJSET_ val_range )
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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:184:9: range : OEBRACE val_range DOT DOT val_range CEBRACE -> ^( RANGE_ OEBRACE val_range DOT DOT val_range CEBRACE ) ;
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
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:184:15: ( OEBRACE val_range DOT DOT val_range CEBRACE -> ^( RANGE_ OEBRACE val_range DOT DOT val_range CEBRACE ) )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:184:17: OEBRACE val_range DOT DOT val_range CEBRACE
                pass 
                OEBRACE47 = self.match(self.input, OEBRACE, self.FOLLOW_OEBRACE_in_range1200) 
                stream_OEBRACE.add(OEBRACE47)


                self._state.following.append(self.FOLLOW_val_range_in_range1202)
                val_range48 = self.val_range()

                self._state.following.pop()
                stream_val_range.add(val_range48.tree)


                DOT49 = self.match(self.input, DOT, self.FOLLOW_DOT_in_range1204) 
                stream_DOT.add(DOT49)


                DOT50 = self.match(self.input, DOT, self.FOLLOW_DOT_in_range1206) 
                stream_DOT.add(DOT50)


                self._state.following.append(self.FOLLOW_val_range_in_range1208)
                val_range51 = self.val_range()

                self._state.following.pop()
                stream_val_range.add(val_range51.tree)


                CEBRACE52 = self.match(self.input, CEBRACE, self.FOLLOW_CEBRACE_in_range1210) 
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
                # 184:61: -> ^( RANGE_ OEBRACE val_range DOT DOT val_range CEBRACE )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:184:64: ^( RANGE_ OEBRACE val_range DOT DOT val_range CEBRACE )
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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:185:9: val_range : ( INT | ID );
    def val_range(self, ):
        retval = self.val_range_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set53 = None

        set53_tree = None

        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:185:19: ( INT | ID )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:
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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:187:5: array_decl : ARRAY range ;
    def array_decl(self, ):
        retval = self.array_decl_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ARRAY54 = None
        range55 = None

        ARRAY54_tree = None

        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:187:16: ( ARRAY range )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:187:18: ARRAY range
                pass 
                root_0 = self._adaptor.nil()


                ARRAY54 = self.match(self.input, ARRAY, self.FOLLOW_ARRAY_in_array_decl1259)
                ARRAY54_tree = self._adaptor.createWithPayload(ARRAY54)
                self._adaptor.addChild(root_0, ARRAY54_tree)



                self._state.following.append(self.FOLLOW_range_in_array_decl1261)
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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:188:5: fifo_decl : FIFO range ;
    def fifo_decl(self, ):
        retval = self.fifo_decl_return()
        retval.start = self.input.LT(1)


        root_0 = None

        FIFO56 = None
        range57 = None

        FIFO56_tree = None

        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:188:14: ( FIFO range )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:188:16: FIFO range
                pass 
                root_0 = self._adaptor.nil()


                FIFO56 = self.match(self.input, FIFO, self.FOLLOW_FIFO_in_fifo_decl1271)
                FIFO56_tree = self._adaptor.createWithPayload(FIFO56)
                self._adaptor.addChild(root_0, FIFO56_tree)



                self._state.following.append(self.FOLLOW_range_in_fifo_decl1273)
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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:191:1: init_hw : ( network_block | machines | message_block );
    def init_hw(self, ):
        retval = self.init_hw_return()
        retval.start = self.input.LT(1)


        root_0 = None

        network_block58 = None
        machines59 = None
        message_block60 = None


        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:191:9: ( network_block | machines | message_block )
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
                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:191:11: network_block
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_network_block_in_init_hw1283)
                    network_block58 = self.network_block()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, network_block58.tree)



                elif alt6 == 2:
                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:191:27: machines
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_machines_in_init_hw1287)
                    machines59 = self.machines()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, machines59.tree)



                elif alt6 == 3:
                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:191:38: message_block
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_message_block_in_init_hw1291)
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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:192:5: object_block : object_expr SEMICOLON -> object_expr ;
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
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:192:18: ( object_expr SEMICOLON -> object_expr )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:192:20: object_expr SEMICOLON
                pass 
                self._state.following.append(self.FOLLOW_object_expr_in_object_block1302)
                object_expr61 = self.object_expr()

                self._state.following.pop()
                stream_object_expr.add(object_expr61.tree)


                SEMICOLON62 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_object_block1304) 
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
                # 192:42: -> object_expr
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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:193:5: object_expr : ( ID | object_func );
    def object_expr(self, ):
        retval = self.object_expr_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID63 = None
        object_func64 = None

        ID63_tree = None

        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:193:17: ( ID | object_func )
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == ID) :
                    LA7_1 = self.input.LA(2)

                    if (LA7_1 == DOT) :
                        alt7 = 2
                    elif ((87 <= LA7_1 <= 93) or LA7_1 in {BOOL, CBRACE, COMMA, ID, INT, NID, OCBRACE, SEMICOLON, 103}) :
                        alt7 = 1
                    else:
                        nvae = NoViableAltException("", 7, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 7, 0, self.input)

                    raise nvae


                if alt7 == 1:
                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:193:19: ID
                    pass 
                    root_0 = self._adaptor.nil()


                    ID63 = self.match(self.input, ID, self.FOLLOW_ID_in_object_expr1319)
                    ID63_tree = self._adaptor.createWithPayload(ID63)
                    self._adaptor.addChild(root_0, ID63_tree)




                elif alt7 == 2:
                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:193:24: object_func
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_object_func_in_object_expr1323)
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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:194:5: object_func : ID DOT object_idres ( OBRACE ( object_expr )* ( COMMA object_expr )* CBRACE )* -> ^( ID DOT object_idres ( OBRACE ( object_expr )* ( COMMA object_expr )* CBRACE )* ) ;
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
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:194:17: ( ID DOT object_idres ( OBRACE ( object_expr )* ( COMMA object_expr )* CBRACE )* -> ^( ID DOT object_idres ( OBRACE ( object_expr )* ( COMMA object_expr )* CBRACE )* ) )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:194:19: ID DOT object_idres ( OBRACE ( object_expr )* ( COMMA object_expr )* CBRACE )*
                pass 
                ID65 = self.match(self.input, ID, self.FOLLOW_ID_in_object_func1334) 
                stream_ID.add(ID65)


                DOT66 = self.match(self.input, DOT, self.FOLLOW_DOT_in_object_func1336) 
                stream_DOT.add(DOT66)


                self._state.following.append(self.FOLLOW_object_idres_in_object_func1338)
                object_idres67 = self.object_idres()

                self._state.following.pop()
                stream_object_idres.add(object_idres67.tree)


                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:194:39: ( OBRACE ( object_expr )* ( COMMA object_expr )* CBRACE )*
                while True: #loop10
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == OBRACE) :
                        alt10 = 1


                    if alt10 == 1:
                        # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:194:40: OBRACE ( object_expr )* ( COMMA object_expr )* CBRACE
                        pass 
                        OBRACE68 = self.match(self.input, OBRACE, self.FOLLOW_OBRACE_in_object_func1341) 
                        stream_OBRACE.add(OBRACE68)


                        # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:194:47: ( object_expr )*
                        while True: #loop8
                            alt8 = 2
                            LA8_0 = self.input.LA(1)

                            if (LA8_0 == ID) :
                                alt8 = 1


                            if alt8 == 1:
                                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:194:47: object_expr
                                pass 
                                self._state.following.append(self.FOLLOW_object_expr_in_object_func1343)
                                object_expr69 = self.object_expr()

                                self._state.following.pop()
                                stream_object_expr.add(object_expr69.tree)



                            else:
                                break #loop8


                        # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:194:60: ( COMMA object_expr )*
                        while True: #loop9
                            alt9 = 2
                            LA9_0 = self.input.LA(1)

                            if (LA9_0 == COMMA) :
                                alt9 = 1


                            if alt9 == 1:
                                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:194:61: COMMA object_expr
                                pass 
                                COMMA70 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_object_func1347) 
                                stream_COMMA.add(COMMA70)


                                self._state.following.append(self.FOLLOW_object_expr_in_object_func1349)
                                object_expr71 = self.object_expr()

                                self._state.following.pop()
                                stream_object_expr.add(object_expr71.tree)



                            else:
                                break #loop9


                        CBRACE72 = self.match(self.input, CBRACE, self.FOLLOW_CBRACE_in_object_func1353) 
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
                # 194:90: -> ^( ID DOT object_idres ( OBRACE ( object_expr )* ( COMMA object_expr )* CBRACE )* )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:195:9: ^( ID DOT object_idres ( OBRACE ( object_expr )* ( COMMA object_expr )* CBRACE )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                stream_ID.nextNode()
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_DOT.nextNode()
                )

                self._adaptor.addChild(root_1, stream_object_idres.nextTree())

                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:195:31: ( OBRACE ( object_expr )* ( COMMA object_expr )* CBRACE )*
                while stream_OBRACE.hasNext() or stream_CBRACE.hasNext():
                    self._adaptor.addChild(root_1, 
                    stream_OBRACE.nextNode()
                    )

                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:195:39: ( object_expr )*
                    while stream_object_expr.hasNext():
                        self._adaptor.addChild(root_1, stream_object_expr.nextTree())


                    stream_object_expr.reset();

                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:195:52: ( COMMA object_expr )*
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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:196:5: object_idres : ( ID | NID );
    def object_idres(self, ):
        retval = self.object_idres_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set73 = None

        set73_tree = None

        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:196:17: ( ID | NID )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:
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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:199:5: machines : ( cache_block | dir_block );
    def machines(self, ):
        retval = self.machines_return()
        retval.start = self.input.LT(1)


        root_0 = None

        cache_block74 = None
        dir_block75 = None


        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:199:14: ( cache_block | dir_block )
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
                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:199:16: cache_block
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_cache_block_in_machines1422)
                    cache_block74 = self.cache_block()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, cache_block74.tree)



                elif alt11 == 2:
                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:199:30: dir_block
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_dir_block_in_machines1426)
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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:200:9: cache_block : CACHE OCBRACE ( declarations )* CCBRACE ( objset_decl )* ID SEMICOLON -> ^( CACHE_ ID ( objset_decl )* ( declarations )* ) ;
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
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:200:21: ( CACHE OCBRACE ( declarations )* CCBRACE ( objset_decl )* ID SEMICOLON -> ^( CACHE_ ID ( objset_decl )* ( declarations )* ) )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:200:23: CACHE OCBRACE ( declarations )* CCBRACE ( objset_decl )* ID SEMICOLON
                pass 
                CACHE76 = self.match(self.input, CACHE, self.FOLLOW_CACHE_in_cache_block1441) 
                stream_CACHE.add(CACHE76)


                OCBRACE77 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_cache_block1443) 
                stream_OCBRACE.add(OCBRACE77)


                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:200:37: ( declarations )*
                while True: #loop12
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if (LA12_0 in {BOOLID, DATA, INTID, NID, SET, STATE}) :
                        alt12 = 1


                    if alt12 == 1:
                        # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:200:37: declarations
                        pass 
                        self._state.following.append(self.FOLLOW_declarations_in_cache_block1445)
                        declarations78 = self.declarations()

                        self._state.following.pop()
                        stream_declarations.add(declarations78.tree)



                    else:
                        break #loop12


                CCBRACE79 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_cache_block1448) 
                stream_CCBRACE.add(CCBRACE79)


                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:200:59: ( objset_decl )*
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if (LA13_0 == SET) :
                        alt13 = 1


                    if alt13 == 1:
                        # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:200:59: objset_decl
                        pass 
                        self._state.following.append(self.FOLLOW_objset_decl_in_cache_block1450)
                        objset_decl80 = self.objset_decl()

                        self._state.following.pop()
                        stream_objset_decl.add(objset_decl80.tree)



                    else:
                        break #loop13


                ID81 = self.match(self.input, ID, self.FOLLOW_ID_in_cache_block1453) 
                stream_ID.add(ID81)


                SEMICOLON82 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_cache_block1455) 
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
                # 200:85: -> ^( CACHE_ ID ( objset_decl )* ( declarations )* )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:201:13: ^( CACHE_ ID ( objset_decl )* ( declarations )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(CACHE_, "CACHE_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:201:25: ( objset_decl )*
                while stream_objset_decl.hasNext():
                    self._adaptor.addChild(root_1, stream_objset_decl.nextTree())


                stream_objset_decl.reset();

                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:201:38: ( declarations )*
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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:202:9: dir_block : DIR OCBRACE ( declarations )* CCBRACE ( objset_decl )* ID SEMICOLON -> ^( DIR_ ID ( objset_decl )* ( declarations )* ) ;
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
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:202:19: ( DIR OCBRACE ( declarations )* CCBRACE ( objset_decl )* ID SEMICOLON -> ^( DIR_ ID ( objset_decl )* ( declarations )* ) )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:202:21: DIR OCBRACE ( declarations )* CCBRACE ( objset_decl )* ID SEMICOLON
                pass 
                DIR83 = self.match(self.input, DIR, self.FOLLOW_DIR_in_dir_block1496) 
                stream_DIR.add(DIR83)


                OCBRACE84 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_dir_block1498) 
                stream_OCBRACE.add(OCBRACE84)


                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:202:33: ( declarations )*
                while True: #loop14
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if (LA14_0 in {BOOLID, DATA, INTID, NID, SET, STATE}) :
                        alt14 = 1


                    if alt14 == 1:
                        # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:202:33: declarations
                        pass 
                        self._state.following.append(self.FOLLOW_declarations_in_dir_block1500)
                        declarations85 = self.declarations()

                        self._state.following.pop()
                        stream_declarations.add(declarations85.tree)



                    else:
                        break #loop14


                CCBRACE86 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_dir_block1503) 
                stream_CCBRACE.add(CCBRACE86)


                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:202:55: ( objset_decl )*
                while True: #loop15
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if (LA15_0 == SET) :
                        alt15 = 1


                    if alt15 == 1:
                        # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:202:55: objset_decl
                        pass 
                        self._state.following.append(self.FOLLOW_objset_decl_in_dir_block1505)
                        objset_decl87 = self.objset_decl()

                        self._state.following.pop()
                        stream_objset_decl.add(objset_decl87.tree)



                    else:
                        break #loop15


                ID88 = self.match(self.input, ID, self.FOLLOW_ID_in_dir_block1508) 
                stream_ID.add(ID88)


                SEMICOLON89 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_dir_block1510) 
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
                # 202:81: -> ^( DIR_ ID ( objset_decl )* ( declarations )* )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:203:13: ^( DIR_ ID ( objset_decl )* ( declarations )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(DIR_, "DIR_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:203:23: ( objset_decl )*
                while stream_objset_decl.hasNext():
                    self._adaptor.addChild(root_1, stream_objset_decl.nextTree())


                stream_objset_decl.reset();

                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:203:36: ( declarations )*
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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:206:5: network_block : NETWORK OCBRACE ( network_element )* CCBRACE SEMICOLON -> ^( NETWORK_ ( network_element )* ) ;
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
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:206:19: ( NETWORK OCBRACE ( network_element )* CCBRACE SEMICOLON -> ^( NETWORK_ ( network_element )* ) )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:206:21: NETWORK OCBRACE ( network_element )* CCBRACE SEMICOLON
                pass 
                NETWORK90 = self.match(self.input, NETWORK, self.FOLLOW_NETWORK_in_network_block1554) 
                stream_NETWORK.add(NETWORK90)


                OCBRACE91 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_network_block1556) 
                stream_OCBRACE.add(OCBRACE91)


                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:206:37: ( network_element )*
                while True: #loop16
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if (LA16_0 in {94, 95}) :
                        alt16 = 1


                    if alt16 == 1:
                        # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:206:37: network_element
                        pass 
                        self._state.following.append(self.FOLLOW_network_element_in_network_block1558)
                        network_element92 = self.network_element()

                        self._state.following.pop()
                        stream_network_element.add(network_element92.tree)



                    else:
                        break #loop16


                CCBRACE93 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_network_block1561) 
                stream_CCBRACE.add(CCBRACE93)


                SEMICOLON94 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_network_block1563) 
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
                # 206:72: -> ^( NETWORK_ ( network_element )* )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:206:75: ^( NETWORK_ ( network_element )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(NETWORK_, "NETWORK_")
                , root_1)

                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:206:86: ( network_element )*
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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:207:9: element_type : ( 'Ordered' | 'Unordered' );
    def element_type(self, ):
        retval = self.element_type_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set95 = None

        set95_tree = None

        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:207:22: ( 'Ordered' | 'Unordered' )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:
                pass 
                root_0 = self._adaptor.nil()


                set95 = self.input.LT(1)

                if self.input.LA(1) in {94, 95}:
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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:208:9: network_element : element_type ID SEMICOLON -> ^( ELEMENT_ element_type ID ) ;
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
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:208:25: ( element_type ID SEMICOLON -> ^( ELEMENT_ element_type ID ) )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:208:27: element_type ID SEMICOLON
                pass 
                self._state.following.append(self.FOLLOW_element_type_in_network_element1606)
                element_type96 = self.element_type()

                self._state.following.pop()
                stream_element_type.add(element_type96.tree)


                ID97 = self.match(self.input, ID, self.FOLLOW_ID_in_network_element1608) 
                stream_ID.add(ID97)


                SEMICOLON98 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_network_element1610) 
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
                # 208:53: -> ^( ELEMENT_ element_type ID )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:208:56: ^( ELEMENT_ element_type ID )
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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:209:5: network_send : ID DOT send_function OBRACE ID CBRACE SEMICOLON -> ^( SEND_ ID ID ) ;
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
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:209:18: ( ID DOT send_function OBRACE ID CBRACE SEMICOLON -> ^( SEND_ ID ID ) )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:209:20: ID DOT send_function OBRACE ID CBRACE SEMICOLON
                pass 
                ID99 = self.match(self.input, ID, self.FOLLOW_ID_in_network_send1631) 
                stream_ID.add(ID99)


                DOT100 = self.match(self.input, DOT, self.FOLLOW_DOT_in_network_send1633) 
                stream_DOT.add(DOT100)


                self._state.following.append(self.FOLLOW_send_function_in_network_send1635)
                send_function101 = self.send_function()

                self._state.following.pop()
                stream_send_function.add(send_function101.tree)


                OBRACE102 = self.match(self.input, OBRACE, self.FOLLOW_OBRACE_in_network_send1637) 
                stream_OBRACE.add(OBRACE102)


                ID103 = self.match(self.input, ID, self.FOLLOW_ID_in_network_send1639) 
                stream_ID.add(ID103)


                CBRACE104 = self.match(self.input, CBRACE, self.FOLLOW_CBRACE_in_network_send1641) 
                stream_CBRACE.add(CBRACE104)


                SEMICOLON105 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_network_send1643) 
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
                # 209:68: -> ^( SEND_ ID ID )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:209:71: ^( SEND_ ID ID )
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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:210:5: network_mcast : ID DOT mcast_function OBRACE ID COMMA ID CBRACE SEMICOLON -> ^( MCAST_ ID ID ID ) ;
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
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:210:18: ( ID DOT mcast_function OBRACE ID COMMA ID CBRACE SEMICOLON -> ^( MCAST_ ID ID ID ) )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:210:20: ID DOT mcast_function OBRACE ID COMMA ID CBRACE SEMICOLON
                pass 
                ID106 = self.match(self.input, ID, self.FOLLOW_ID_in_network_mcast1663) 
                stream_ID.add(ID106)


                DOT107 = self.match(self.input, DOT, self.FOLLOW_DOT_in_network_mcast1665) 
                stream_DOT.add(DOT107)


                self._state.following.append(self.FOLLOW_mcast_function_in_network_mcast1667)
                mcast_function108 = self.mcast_function()

                self._state.following.pop()
                stream_mcast_function.add(mcast_function108.tree)


                OBRACE109 = self.match(self.input, OBRACE, self.FOLLOW_OBRACE_in_network_mcast1669) 
                stream_OBRACE.add(OBRACE109)


                ID110 = self.match(self.input, ID, self.FOLLOW_ID_in_network_mcast1671) 
                stream_ID.add(ID110)


                COMMA111 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_network_mcast1673) 
                stream_COMMA.add(COMMA111)


                ID112 = self.match(self.input, ID, self.FOLLOW_ID_in_network_mcast1675) 
                stream_ID.add(ID112)


                CBRACE113 = self.match(self.input, CBRACE, self.FOLLOW_CBRACE_in_network_mcast1677) 
                stream_CBRACE.add(CBRACE113)


                SEMICOLON114 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_network_mcast1679) 
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
                # 210:78: -> ^( MCAST_ ID ID ID )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:210:81: ^( MCAST_ ID ID ID )
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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:213:5: message_block : MSG ID OCBRACE ( declarations )* CCBRACE SEMICOLON -> ^( MSG_ ID ( declarations )* ) ;
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
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:213:19: ( MSG ID OCBRACE ( declarations )* CCBRACE SEMICOLON -> ^( MSG_ ID ( declarations )* ) )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:213:21: MSG ID OCBRACE ( declarations )* CCBRACE SEMICOLON
                pass 
                MSG115 = self.match(self.input, MSG, self.FOLLOW_MSG_in_message_block1709) 
                stream_MSG.add(MSG115)


                ID116 = self.match(self.input, ID, self.FOLLOW_ID_in_message_block1711) 
                stream_ID.add(ID116)


                OCBRACE117 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_message_block1713) 
                stream_OCBRACE.add(OCBRACE117)


                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:213:36: ( declarations )*
                while True: #loop17
                    alt17 = 2
                    LA17_0 = self.input.LA(1)

                    if (LA17_0 in {BOOLID, DATA, INTID, NID, SET, STATE}) :
                        alt17 = 1


                    if alt17 == 1:
                        # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:213:36: declarations
                        pass 
                        self._state.following.append(self.FOLLOW_declarations_in_message_block1715)
                        declarations118 = self.declarations()

                        self._state.following.pop()
                        stream_declarations.add(declarations118.tree)



                    else:
                        break #loop17


                CCBRACE119 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_message_block1718) 
                stream_CCBRACE.add(CCBRACE119)


                SEMICOLON120 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_message_block1720) 
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
                # 213:68: -> ^( MSG_ ID ( declarations )* )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:213:71: ^( MSG_ ID ( declarations )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(MSG_, "MSG_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:213:81: ( declarations )*
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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:214:5: message_constr : ID OBRACE ( message_expr )* ( COMMA message_expr )* CBRACE -> ^( MSGCSTR_ ID ( message_expr )* ) ;
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
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:214:20: ( ID OBRACE ( message_expr )* ( COMMA message_expr )* CBRACE -> ^( MSGCSTR_ ID ( message_expr )* ) )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:214:22: ID OBRACE ( message_expr )* ( COMMA message_expr )* CBRACE
                pass 
                ID121 = self.match(self.input, ID, self.FOLLOW_ID_in_message_constr1742) 
                stream_ID.add(ID121)


                OBRACE122 = self.match(self.input, OBRACE, self.FOLLOW_OBRACE_in_message_constr1744) 
                stream_OBRACE.add(OBRACE122)


                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:214:32: ( message_expr )*
                while True: #loop18
                    alt18 = 2
                    LA18_0 = self.input.LA(1)

                    if (LA18_0 in {BOOL, ID, INT, NID}) :
                        alt18 = 1


                    if alt18 == 1:
                        # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:214:32: message_expr
                        pass 
                        self._state.following.append(self.FOLLOW_message_expr_in_message_constr1746)
                        message_expr123 = self.message_expr()

                        self._state.following.pop()
                        stream_message_expr.add(message_expr123.tree)



                    else:
                        break #loop18


                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:214:46: ( COMMA message_expr )*
                while True: #loop19
                    alt19 = 2
                    LA19_0 = self.input.LA(1)

                    if (LA19_0 == COMMA) :
                        alt19 = 1


                    if alt19 == 1:
                        # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:214:47: COMMA message_expr
                        pass 
                        COMMA124 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_message_constr1750) 
                        stream_COMMA.add(COMMA124)


                        self._state.following.append(self.FOLLOW_message_expr_in_message_constr1752)
                        message_expr125 = self.message_expr()

                        self._state.following.pop()
                        stream_message_expr.add(message_expr125.tree)



                    else:
                        break #loop19


                CBRACE126 = self.match(self.input, CBRACE, self.FOLLOW_CBRACE_in_message_constr1756) 
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
                # 214:75: -> ^( MSGCSTR_ ID ( message_expr )* )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:214:78: ^( MSGCSTR_ ID ( message_expr )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(MSGCSTR_, "MSGCSTR_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:214:92: ( message_expr )*
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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:215:5: message_expr : ( object_expr | set_func | INT | BOOL | NID );
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
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:215:18: ( object_expr | set_func | INT | BOOL | NID )
                alt20 = 5
                LA20 = self.input.LA(1)
                if LA20 in {ID}:
                    LA20_1 = self.input.LA(2)

                    if (LA20_1 == DOT) :
                        LA20_5 = self.input.LA(3)

                        if (LA20_5 in {ID, NID}) :
                            alt20 = 1
                        elif ((96 <= LA20_5 <= 100) or LA20_5 in {}) :
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
                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:215:20: object_expr
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_object_expr_in_message_expr1778)
                    object_expr127 = self.object_expr()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, object_expr127.tree)



                elif alt20 == 2:
                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:215:34: set_func
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_set_func_in_message_expr1782)
                    set_func128 = self.set_func()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, set_func128.tree)



                elif alt20 == 3:
                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:215:45: INT
                    pass 
                    root_0 = self._adaptor.nil()


                    INT129 = self.match(self.input, INT, self.FOLLOW_INT_in_message_expr1786)
                    INT129_tree = self._adaptor.createWithPayload(INT129)
                    self._adaptor.addChild(root_0, INT129_tree)




                elif alt20 == 4:
                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:215:51: BOOL
                    pass 
                    root_0 = self._adaptor.nil()


                    BOOL130 = self.match(self.input, BOOL, self.FOLLOW_BOOL_in_message_expr1790)
                    BOOL130_tree = self._adaptor.createWithPayload(BOOL130)
                    self._adaptor.addChild(root_0, BOOL130_tree)




                elif alt20 == 5:
                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:215:58: NID
                    pass 
                    root_0 = self._adaptor.nil()


                    NID131 = self.match(self.input, NID, self.FOLLOW_NID_in_message_expr1794)
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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:218:5: set_block : set_func SEMICOLON -> set_func ;
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
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:218:15: ( set_func SEMICOLON -> set_func )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:218:17: set_func SEMICOLON
                pass 
                self._state.following.append(self.FOLLOW_set_func_in_set_block1812)
                set_func132 = self.set_func()

                self._state.following.pop()
                stream_set_func.add(set_func132.tree)


                SEMICOLON133 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_set_block1814) 
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
                # 218:36: -> set_func
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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:219:5: set_func : ID DOT set_function_types OBRACE ( set_nest )* CBRACE -> ^( SETFUNC_ ID DOT set_function_types OBRACE ( set_nest )* CBRACE ) ;
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
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:219:14: ( ID DOT set_function_types OBRACE ( set_nest )* CBRACE -> ^( SETFUNC_ ID DOT set_function_types OBRACE ( set_nest )* CBRACE ) )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:219:16: ID DOT set_function_types OBRACE ( set_nest )* CBRACE
                pass 
                ID134 = self.match(self.input, ID, self.FOLLOW_ID_in_set_func1829) 
                stream_ID.add(ID134)


                DOT135 = self.match(self.input, DOT, self.FOLLOW_DOT_in_set_func1831) 
                stream_DOT.add(DOT135)


                self._state.following.append(self.FOLLOW_set_function_types_in_set_func1833)
                set_function_types136 = self.set_function_types()

                self._state.following.pop()
                stream_set_function_types.add(set_function_types136.tree)


                OBRACE137 = self.match(self.input, OBRACE, self.FOLLOW_OBRACE_in_set_func1835) 
                stream_OBRACE.add(OBRACE137)


                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:219:49: ( set_nest )*
                while True: #loop21
                    alt21 = 2
                    LA21_0 = self.input.LA(1)

                    if (LA21_0 == ID) :
                        alt21 = 1


                    if alt21 == 1:
                        # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:219:49: set_nest
                        pass 
                        self._state.following.append(self.FOLLOW_set_nest_in_set_func1837)
                        set_nest138 = self.set_nest()

                        self._state.following.pop()
                        stream_set_nest.add(set_nest138.tree)



                    else:
                        break #loop21


                CBRACE139 = self.match(self.input, CBRACE, self.FOLLOW_CBRACE_in_set_func1840) 
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
                # 219:66: -> ^( SETFUNC_ ID DOT set_function_types OBRACE ( set_nest )* CBRACE )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:220:9: ^( SETFUNC_ ID DOT set_function_types OBRACE ( set_nest )* CBRACE )
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

                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:220:53: ( set_nest )*
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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:221:5: set_nest : ( set_func | object_expr );
    def set_nest(self, ):
        retval = self.set_nest_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set_func140 = None
        object_expr141 = None


        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:221:14: ( set_func | object_expr )
                alt22 = 2
                LA22_0 = self.input.LA(1)

                if (LA22_0 == ID) :
                    LA22_1 = self.input.LA(2)

                    if (LA22_1 == DOT) :
                        LA22_2 = self.input.LA(3)

                        if ((96 <= LA22_2 <= 100) or LA22_2 in {}) :
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
                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:221:16: set_func
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_set_func_in_set_nest1878)
                    set_func140 = self.set_func()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, set_func140.tree)



                elif alt22 == 2:
                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:221:27: object_expr
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_object_expr_in_set_nest1882)
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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:224:1: arch_block : ARCH ID OCBRACE arch_body CCBRACE -> ^( ARCH_ ^( MACHN_ ID ) arch_body ) ;
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
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:224:12: ( ARCH ID OCBRACE arch_body CCBRACE -> ^( ARCH_ ^( MACHN_ ID ) arch_body ) )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:224:14: ARCH ID OCBRACE arch_body CCBRACE
                pass 
                ARCH142 = self.match(self.input, ARCH, self.FOLLOW_ARCH_in_arch_block1892) 
                stream_ARCH.add(ARCH142)


                ID143 = self.match(self.input, ID, self.FOLLOW_ID_in_arch_block1894) 
                stream_ID.add(ID143)


                OCBRACE144 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_arch_block1896) 
                stream_OCBRACE.add(OCBRACE144)


                self._state.following.append(self.FOLLOW_arch_body_in_arch_block1898)
                arch_body145 = self.arch_body()

                self._state.following.pop()
                stream_arch_body.add(arch_body145.tree)


                CCBRACE146 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_arch_block1900) 
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
                # 224:48: -> ^( ARCH_ ^( MACHN_ ID ) arch_body )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:224:51: ^( ARCH_ ^( MACHN_ ID ) arch_body )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(ARCH_, "ARCH_")
                , root_1)

                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:224:59: ^( MACHN_ ID )
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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:226:1: arch_body : ( stable_def | process_block )* ;
    def arch_body(self, ):
        retval = self.arch_body_return()
        retval.start = self.input.LT(1)


        root_0 = None

        stable_def147 = None
        process_block148 = None


        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:226:10: ( ( stable_def | process_block )* )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:226:12: ( stable_def | process_block )*
                pass 
                root_0 = self._adaptor.nil()


                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:226:12: ( stable_def | process_block )*
                while True: #loop23
                    alt23 = 3
                    LA23_0 = self.input.LA(1)

                    if (LA23_0 == STABLE) :
                        alt23 = 1
                    elif (LA23_0 == PROC) :
                        alt23 = 2


                    if alt23 == 1:
                        # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:226:13: stable_def
                        pass 
                        self._state.following.append(self.FOLLOW_stable_def_in_arch_body1922)
                        stable_def147 = self.stable_def()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, stable_def147.tree)



                    elif alt23 == 2:
                        # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:226:26: process_block
                        pass 
                        self._state.following.append(self.FOLLOW_process_block_in_arch_body1926)
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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:228:1: stable_def : STABLE OCBRACE ID ( COMMA ID )* CCBRACE -> ^( STABLE_ ID ( ID )* ) ;
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
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:228:12: ( STABLE OCBRACE ID ( COMMA ID )* CCBRACE -> ^( STABLE_ ID ( ID )* ) )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:228:14: STABLE OCBRACE ID ( COMMA ID )* CCBRACE
                pass 
                STABLE149 = self.match(self.input, STABLE, self.FOLLOW_STABLE_in_stable_def1936) 
                stream_STABLE.add(STABLE149)


                OCBRACE150 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_stable_def1938) 
                stream_OCBRACE.add(OCBRACE150)


                ID151 = self.match(self.input, ID, self.FOLLOW_ID_in_stable_def1940) 
                stream_ID.add(ID151)


                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:228:32: ( COMMA ID )*
                while True: #loop24
                    alt24 = 2
                    LA24_0 = self.input.LA(1)

                    if (LA24_0 == COMMA) :
                        alt24 = 1


                    if alt24 == 1:
                        # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:228:33: COMMA ID
                        pass 
                        COMMA152 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_stable_def1943) 
                        stream_COMMA.add(COMMA152)


                        ID153 = self.match(self.input, ID, self.FOLLOW_ID_in_stable_def1945) 
                        stream_ID.add(ID153)



                    else:
                        break #loop24


                CCBRACE154 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_stable_def1949) 
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
                # 228:52: -> ^( STABLE_ ID ( ID )* )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:228:55: ^( STABLE_ ID ( ID )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(STABLE_, "STABLE_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:228:68: ( ID )*
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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:230:1: process_block : PROC process_trans OCBRACE ( process_expr )* CCBRACE -> ^( PROC_ process_trans ( process_expr )* ^( ENDPROC_ ) ) ;
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
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:230:15: ( PROC process_trans OCBRACE ( process_expr )* CCBRACE -> ^( PROC_ process_trans ( process_expr )* ^( ENDPROC_ ) ) )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:230:17: PROC process_trans OCBRACE ( process_expr )* CCBRACE
                pass 
                PROC155 = self.match(self.input, PROC, self.FOLLOW_PROC_in_process_block1968) 
                stream_PROC.add(PROC155)


                self._state.following.append(self.FOLLOW_process_trans_in_process_block1970)
                process_trans156 = self.process_trans()

                self._state.following.pop()
                stream_process_trans.add(process_trans156.tree)


                OCBRACE157 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_process_block1972) 
                stream_OCBRACE.add(OCBRACE157)


                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:230:44: ( process_expr )*
                while True: #loop25
                    alt25 = 2
                    LA25_0 = self.input.LA(1)

                    if (LA25_0 in {AWAIT, ID, IF, STATE}) :
                        alt25 = 1


                    if alt25 == 1:
                        # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:230:44: process_expr
                        pass 
                        self._state.following.append(self.FOLLOW_process_expr_in_process_block1974)
                        process_expr158 = self.process_expr()

                        self._state.following.pop()
                        stream_process_expr.add(process_expr158.tree)



                    else:
                        break #loop25


                CCBRACE159 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_process_block1977) 
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
                # 230:66: -> ^( PROC_ process_trans ( process_expr )* ^( ENDPROC_ ) )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:230:69: ^( PROC_ process_trans ( process_expr )* ^( ENDPROC_ ) )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(PROC_, "PROC_")
                , root_1)

                self._adaptor.addChild(root_1, stream_process_trans.nextTree())

                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:230:91: ( process_expr )*
                while stream_process_expr.hasNext():
                    self._adaptor.addChild(root_1, stream_process_expr.nextTree())


                stream_process_expr.reset();

                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:230:105: ^( ENDPROC_ )
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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:231:5: process_trans : OBRACE ID COMMA process_events ( process_finalstate )* CBRACE -> ^( TRANS_ ID process_events ( process_finalstate )* ) ;
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
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:231:19: ( OBRACE ID COMMA process_events ( process_finalstate )* CBRACE -> ^( TRANS_ ID process_events ( process_finalstate )* ) )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:231:21: OBRACE ID COMMA process_events ( process_finalstate )* CBRACE
                pass 
                OBRACE160 = self.match(self.input, OBRACE, self.FOLLOW_OBRACE_in_process_trans2003) 
                stream_OBRACE.add(OBRACE160)


                ID161 = self.match(self.input, ID, self.FOLLOW_ID_in_process_trans2005) 
                stream_ID.add(ID161)


                COMMA162 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_process_trans2007) 
                stream_COMMA.add(COMMA162)


                self._state.following.append(self.FOLLOW_process_events_in_process_trans2009)
                process_events163 = self.process_events()

                self._state.following.pop()
                stream_process_events.add(process_events163.tree)


                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:231:52: ( process_finalstate )*
                while True: #loop26
                    alt26 = 2
                    LA26_0 = self.input.LA(1)

                    if (LA26_0 == COMMA) :
                        alt26 = 1


                    if alt26 == 1:
                        # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:231:52: process_finalstate
                        pass 
                        self._state.following.append(self.FOLLOW_process_finalstate_in_process_trans2011)
                        process_finalstate164 = self.process_finalstate()

                        self._state.following.pop()
                        stream_process_finalstate.add(process_finalstate164.tree)



                    else:
                        break #loop26


                CBRACE165 = self.match(self.input, CBRACE, self.FOLLOW_CBRACE_in_process_trans2014) 
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
                # 231:79: -> ^( TRANS_ ID process_events ( process_finalstate )* )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:231:82: ^( TRANS_ ID process_events ( process_finalstate )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TRANS_, "TRANS_")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_1, stream_process_events.nextTree())

                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:231:109: ( process_finalstate )*
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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:232:5: process_finalstate : COMMA process_finalident -> ^( process_finalident ) ;
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
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:232:23: ( COMMA process_finalident -> ^( process_finalident ) )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:232:25: COMMA process_finalident
                pass 
                COMMA166 = self.match(self.input, COMMA, self.FOLLOW_COMMA_in_process_finalstate2037) 
                stream_COMMA.add(COMMA166)


                self._state.following.append(self.FOLLOW_process_finalident_in_process_finalstate2039)
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
                # 232:50: -> ^( process_finalident )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:232:53: ^( process_finalident )
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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:233:5: process_finalident : ( ID | STATE ) ;
    def process_finalident(self, ):
        retval = self.process_finalident_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set168 = None

        set168_tree = None

        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:233:23: ( ( ID | STATE ) )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:
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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:234:5: process_events : ( ACCESS | ID ) ;
    def process_events(self, ):
        retval = self.process_events_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set169 = None

        set169_tree = None

        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:234:20: ( ( ACCESS | ID ) )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:
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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:235:5: process_expr : ( expressions | network_send | network_mcast | transaction );
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
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:235:17: ( expressions | network_send | network_mcast | transaction )
                alt27 = 4
                LA27 = self.input.LA(1)
                if LA27 in {ID}:
                    LA27_1 = self.input.LA(2)

                    if (LA27_1 == DOT) :
                        LA27 = self.input.LA(3)
                        if LA27 in {ID, NID, 96, 97, 98, 99, 100}:
                            alt27 = 1
                        elif LA27 in {102}:
                            alt27 = 2
                        elif LA27 in {101}:
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
                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:235:19: expressions
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_expressions_in_process_expr2088)
                    expressions170 = self.expressions()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, expressions170.tree)



                elif alt27 == 2:
                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:235:33: network_send
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_network_send_in_process_expr2092)
                    network_send171 = self.network_send()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, network_send171.tree)



                elif alt27 == 3:
                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:235:48: network_mcast
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_network_mcast_in_process_expr2096)
                    network_mcast172 = self.network_mcast()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, network_mcast172.tree)



                elif alt27 == 4:
                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:235:64: transaction
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_transaction_in_process_expr2100)
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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:238:1: transaction : AWAIT OCBRACE ( trans )* CCBRACE -> ^( AWAIT_ ( trans )* ) ;
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
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:238:13: ( AWAIT OCBRACE ( trans )* CCBRACE -> ^( AWAIT_ ( trans )* ) )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:238:15: AWAIT OCBRACE ( trans )* CCBRACE
                pass 
                AWAIT174 = self.match(self.input, AWAIT, self.FOLLOW_AWAIT_in_transaction2110) 
                stream_AWAIT.add(AWAIT174)


                OCBRACE175 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_transaction2112) 
                stream_OCBRACE.add(OCBRACE175)


                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:238:29: ( trans )*
                while True: #loop28
                    alt28 = 2
                    LA28_0 = self.input.LA(1)

                    if (LA28_0 == WHEN) :
                        alt28 = 1


                    if alt28 == 1:
                        # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:238:29: trans
                        pass 
                        self._state.following.append(self.FOLLOW_trans_in_transaction2114)
                        trans176 = self.trans()

                        self._state.following.pop()
                        stream_trans.add(trans176.tree)



                    else:
                        break #loop28


                CCBRACE177 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_transaction2117) 
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
                # 238:44: -> ^( AWAIT_ ( trans )* )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:238:47: ^( AWAIT_ ( trans )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(AWAIT_, "AWAIT_")
                , root_1)

                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:238:56: ( trans )*
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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:239:5: trans : WHEN ID DDOT ( trans_body )* -> ^( WHEN_ ^( GUARD_ ID ) ( trans_body )* ENDWHEN_ ) ;
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
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:239:11: ( WHEN ID DDOT ( trans_body )* -> ^( WHEN_ ^( GUARD_ ID ) ( trans_body )* ENDWHEN_ ) )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:239:13: WHEN ID DDOT ( trans_body )*
                pass 
                WHEN178 = self.match(self.input, WHEN, self.FOLLOW_WHEN_in_trans2137) 
                stream_WHEN.add(WHEN178)


                ID179 = self.match(self.input, ID, self.FOLLOW_ID_in_trans2139) 
                stream_ID.add(ID179)


                DDOT180 = self.match(self.input, DDOT, self.FOLLOW_DDOT_in_trans2141) 
                stream_DDOT.add(DDOT180)


                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:239:26: ( trans_body )*
                while True: #loop29
                    alt29 = 2
                    LA29_0 = self.input.LA(1)

                    if (LA29_0 in {AWAIT, BREAK, ID, IF, NEXT, STATE}) :
                        alt29 = 1


                    if alt29 == 1:
                        # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:239:26: trans_body
                        pass 
                        self._state.following.append(self.FOLLOW_trans_body_in_trans2143)
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
                # 239:38: -> ^( WHEN_ ^( GUARD_ ID ) ( trans_body )* ENDWHEN_ )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:239:41: ^( WHEN_ ^( GUARD_ ID ) ( trans_body )* ENDWHEN_ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(WHEN_, "WHEN_")
                , root_1)

                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:239:49: ^( GUARD_ ID )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(GUARD_, "GUARD_")
                , root_2)

                self._adaptor.addChild(root_2, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_1, root_2)

                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:239:62: ( trans_body )*
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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:240:9: trans_body : ( expressions | next_trans | next_break | transaction | network_send | network_mcast );
    def trans_body(self, ):
        retval = self.trans_body_return()
        retval.start = self.input.LT(1)


        root_0 = None

        expressions182 = None
        next_trans183 = None
        next_break184 = None
        transaction185 = None
        network_send186 = None
        network_mcast187 = None


        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:240:20: ( expressions | next_trans | next_break | transaction | network_send | network_mcast )
                alt30 = 6
                LA30 = self.input.LA(1)
                if LA30 in {ID}:
                    LA30_1 = self.input.LA(2)

                    if (LA30_1 == DOT) :
                        LA30 = self.input.LA(3)
                        if LA30 in {ID, NID, 96, 97, 98, 99, 100}:
                            alt30 = 1
                        elif LA30 in {102}:
                            alt30 = 5
                        elif LA30 in {101}:
                            alt30 = 6
                        else:
                            nvae = NoViableAltException("", 30, 7, self.input)

                            raise nvae


                    elif (LA30_1 in {EQUALSIGN, SEMICOLON}) :
                        alt30 = 1
                    else:
                        nvae = NoViableAltException("", 30, 1, self.input)

                        raise nvae


                elif LA30 in {IF, STATE}:
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
                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:240:22: expressions
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_expressions_in_trans_body2176)
                    expressions182 = self.expressions()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, expressions182.tree)



                elif alt30 == 2:
                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:240:36: next_trans
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_next_trans_in_trans_body2180)
                    next_trans183 = self.next_trans()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, next_trans183.tree)



                elif alt30 == 3:
                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:240:49: next_break
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_next_break_in_trans_body2184)
                    next_break184 = self.next_break()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, next_break184.tree)



                elif alt30 == 4:
                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:240:62: transaction
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_transaction_in_trans_body2188)
                    transaction185 = self.transaction()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, transaction185.tree)



                elif alt30 == 5:
                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:240:76: network_send
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_network_send_in_trans_body2192)
                    network_send186 = self.network_send()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, network_send186.tree)



                elif alt30 == 6:
                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:240:91: network_mcast
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_network_mcast_in_trans_body2196)
                    network_mcast187 = self.network_mcast()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, network_mcast187.tree)



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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:241:13: next_trans : NEXT OCBRACE ( trans )* CCBRACE -> ^( NEXT_ ( trans )* ) ;
    def next_trans(self, ):
        retval = self.next_trans_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEXT188 = None
        OCBRACE189 = None
        CCBRACE191 = None
        trans190 = None

        NEXT188_tree = None
        OCBRACE189_tree = None
        CCBRACE191_tree = None
        stream_OCBRACE = RewriteRuleTokenStream(self._adaptor, "token OCBRACE")
        stream_NEXT = RewriteRuleTokenStream(self._adaptor, "token NEXT")
        stream_CCBRACE = RewriteRuleTokenStream(self._adaptor, "token CCBRACE")
        stream_trans = RewriteRuleSubtreeStream(self._adaptor, "rule trans")
        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:241:23: ( NEXT OCBRACE ( trans )* CCBRACE -> ^( NEXT_ ( trans )* ) )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:241:25: NEXT OCBRACE ( trans )* CCBRACE
                pass 
                NEXT188 = self.match(self.input, NEXT, self.FOLLOW_NEXT_in_next_trans2214) 
                stream_NEXT.add(NEXT188)


                OCBRACE189 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_next_trans2216) 
                stream_OCBRACE.add(OCBRACE189)


                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:241:38: ( trans )*
                while True: #loop31
                    alt31 = 2
                    LA31_0 = self.input.LA(1)

                    if (LA31_0 == WHEN) :
                        alt31 = 1


                    if alt31 == 1:
                        # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:241:38: trans
                        pass 
                        self._state.following.append(self.FOLLOW_trans_in_next_trans2218)
                        trans190 = self.trans()

                        self._state.following.pop()
                        stream_trans.add(trans190.tree)



                    else:
                        break #loop31


                CCBRACE191 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_next_trans2221) 
                stream_CCBRACE.add(CCBRACE191)


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
                # 241:53: -> ^( NEXT_ ( trans )* )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:241:56: ^( NEXT_ ( trans )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(NEXT_, "NEXT_")
                , root_1)

                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:241:64: ( trans )*
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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:243:1: next_break : BREAK SEMICOLON -> ^( BREAK_ ) ;
    def next_break(self, ):
        retval = self.next_break_return()
        retval.start = self.input.LT(1)


        root_0 = None

        BREAK192 = None
        SEMICOLON193 = None

        BREAK192_tree = None
        SEMICOLON193_tree = None
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_BREAK = RewriteRuleTokenStream(self._adaptor, "token BREAK")

        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:243:12: ( BREAK SEMICOLON -> ^( BREAK_ ) )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:243:14: BREAK SEMICOLON
                pass 
                BREAK192 = self.match(self.input, BREAK, self.FOLLOW_BREAK_in_next_break2238) 
                stream_BREAK.add(BREAK192)


                SEMICOLON193 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_next_break2240) 
                stream_SEMICOLON.add(SEMICOLON193)


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
                # 243:30: -> ^( BREAK_ )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:243:33: ^( BREAK_ )
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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:246:1: expressions : ( assignment | conditional | object_block | set_block );
    def expressions(self, ):
        retval = self.expressions_return()
        retval.start = self.input.LT(1)


        root_0 = None

        assignment194 = None
        conditional195 = None
        object_block196 = None
        set_block197 = None


        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:246:13: ( assignment | conditional | object_block | set_block )
                alt32 = 4
                LA32 = self.input.LA(1)
                if LA32 in {ID}:
                    LA32 = self.input.LA(2)
                    if LA32 in {DOT}:
                        LA32_4 = self.input.LA(3)

                        if (LA32_4 in {ID, NID}) :
                            alt32 = 3
                        elif ((96 <= LA32_4 <= 100) or LA32_4 in {}) :
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
                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:246:15: assignment
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_assignment_in_expressions2256)
                    assignment194 = self.assignment()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, assignment194.tree)



                elif alt32 == 2:
                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:246:28: conditional
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_conditional_in_expressions2260)
                    conditional195 = self.conditional()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, conditional195.tree)



                elif alt32 == 3:
                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:246:42: object_block
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_object_block_in_expressions2264)
                    object_block196 = self.object_block()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, object_block196.tree)



                elif alt32 == 4:
                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:246:57: set_block
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_set_block_in_expressions2268)
                    set_block197 = self.set_block()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, set_block197.tree)



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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:247:1: assignment : process_finalident EQUALSIGN assign_types SEMICOLON -> ^( ASSIGN_ process_finalident EQUALSIGN assign_types ) ;
    def assignment(self, ):
        retval = self.assignment_return()
        retval.start = self.input.LT(1)


        root_0 = None

        EQUALSIGN199 = None
        SEMICOLON201 = None
        process_finalident198 = None
        assign_types200 = None

        EQUALSIGN199_tree = None
        SEMICOLON201_tree = None
        stream_EQUALSIGN = RewriteRuleTokenStream(self._adaptor, "token EQUALSIGN")
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_assign_types = RewriteRuleSubtreeStream(self._adaptor, "rule assign_types")
        stream_process_finalident = RewriteRuleSubtreeStream(self._adaptor, "rule process_finalident")
        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:247:12: ( process_finalident EQUALSIGN assign_types SEMICOLON -> ^( ASSIGN_ process_finalident EQUALSIGN assign_types ) )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:247:14: process_finalident EQUALSIGN assign_types SEMICOLON
                pass 
                self._state.following.append(self.FOLLOW_process_finalident_in_assignment2275)
                process_finalident198 = self.process_finalident()

                self._state.following.pop()
                stream_process_finalident.add(process_finalident198.tree)


                EQUALSIGN199 = self.match(self.input, EQUALSIGN, self.FOLLOW_EQUALSIGN_in_assignment2277) 
                stream_EQUALSIGN.add(EQUALSIGN199)


                self._state.following.append(self.FOLLOW_assign_types_in_assignment2279)
                assign_types200 = self.assign_types()

                self._state.following.pop()
                stream_assign_types.add(assign_types200.tree)


                SEMICOLON201 = self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_assignment2281) 
                stream_SEMICOLON.add(SEMICOLON201)


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
                # 247:65: -> ^( ASSIGN_ process_finalident EQUALSIGN assign_types )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:247:68: ^( ASSIGN_ process_finalident EQUALSIGN assign_types )
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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:248:5: assign_types : ( object_expr | message_constr | math_op | set_func | INT | BOOL );
    def assign_types(self, ):
        retval = self.assign_types_return()
        retval.start = self.input.LT(1)


        root_0 = None

        INT206 = None
        BOOL207 = None
        object_expr202 = None
        message_constr203 = None
        math_op204 = None
        set_func205 = None

        INT206_tree = None
        BOOL207_tree = None

        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:248:18: ( object_expr | message_constr | math_op | set_func | INT | BOOL )
                alt33 = 6
                LA33 = self.input.LA(1)
                if LA33 in {ID}:
                    LA33 = self.input.LA(2)
                    if LA33 in {DOT}:
                        LA33_4 = self.input.LA(3)

                        if (LA33_4 in {ID, NID}) :
                            alt33 = 1
                        elif ((96 <= LA33_4 <= 100) or LA33_4 in {}) :
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
                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:248:20: object_expr
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_object_expr_in_assign_types2303)
                    object_expr202 = self.object_expr()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, object_expr202.tree)



                elif alt33 == 2:
                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:248:34: message_constr
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_message_constr_in_assign_types2307)
                    message_constr203 = self.message_constr()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, message_constr203.tree)



                elif alt33 == 3:
                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:248:51: math_op
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_math_op_in_assign_types2311)
                    math_op204 = self.math_op()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, math_op204.tree)



                elif alt33 == 4:
                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:248:61: set_func
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_set_func_in_assign_types2315)
                    set_func205 = self.set_func()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, set_func205.tree)



                elif alt33 == 5:
                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:248:72: INT
                    pass 
                    root_0 = self._adaptor.nil()


                    INT206 = self.match(self.input, INT, self.FOLLOW_INT_in_assign_types2319)
                    INT206_tree = self._adaptor.createWithPayload(INT206)
                    self._adaptor.addChild(root_0, INT206_tree)




                elif alt33 == 6:
                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:248:78: BOOL
                    pass 
                    root_0 = self._adaptor.nil()


                    BOOL207 = self.match(self.input, BOOL, self.FOLLOW_BOOL_in_assign_types2323)
                    BOOL207_tree = self._adaptor.createWithPayload(BOOL207)
                    self._adaptor.addChild(root_0, BOOL207_tree)




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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:249:5: math_op : val_range ( PLUS | MINUS ) val_range ;
    def math_op(self, ):
        retval = self.math_op_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set209 = None
        val_range208 = None
        val_range210 = None

        set209_tree = None

        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:249:13: ( val_range ( PLUS | MINUS ) val_range )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:249:15: val_range ( PLUS | MINUS ) val_range
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_val_range_in_math_op2334)
                val_range208 = self.val_range()

                self._state.following.pop()
                self._adaptor.addChild(root_0, val_range208.tree)


                set209 = self.input.LT(1)

                if self.input.LA(1) in {MINUS, PLUS}:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set209))

                    self._state.errorRecovery = False


                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse



                self._state.following.append(self.FOLLOW_val_range_in_math_op2344)
                val_range210 = self.val_range()

                self._state.following.pop()
                self._adaptor.addChild(root_0, val_range210.tree)




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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:252:1: conditional : ( if_stmt | ifnot_stmt );
    def conditional(self, ):
        retval = self.conditional_return()
        retval.start = self.input.LT(1)


        root_0 = None

        if_stmt211 = None
        ifnot_stmt212 = None


        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:252:12: ( if_stmt | ifnot_stmt )
                alt34 = 2
                LA34_0 = self.input.LA(1)

                if (LA34_0 == IF) :
                    LA34_1 = self.input.LA(2)

                    if (LA34_1 == NEG) :
                        alt34 = 2
                    elif (LA34_1 in {BOOL, ID, INT, OBRACE}) :
                        alt34 = 1
                    else:
                        nvae = NoViableAltException("", 34, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 34, 0, self.input)

                    raise nvae


                if alt34 == 1:
                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:252:14: if_stmt
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_if_stmt_in_conditional2353)
                    if_stmt211 = self.if_stmt()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, if_stmt211.tree)



                elif alt34 == 2:
                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:252:24: ifnot_stmt
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_ifnot_stmt_in_conditional2357)
                    ifnot_stmt212 = self.ifnot_stmt()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, ifnot_stmt212.tree)



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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:253:5: if_stmt : IF cond_comb OCBRACE if_expression CCBRACE ( ELSE OCBRACE else_expression CCBRACE )* -> {t_else}? ^( IFELSE_ ^( IF_ ^( COND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( NCOND_ cond_comb ) ( else_expression )* ENDIF_ ) ) -> ^( IFELSE_ ^( IF_ ^( COND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( NCOND_ cond_comb ) ENDIF_ ) ) ;
    def if_stmt(self, ):
        retval = self.if_stmt_return()
        retval.start = self.input.LT(1)


        root_0 = None

        IF213 = None
        OCBRACE215 = None
        CCBRACE217 = None
        ELSE218 = None
        OCBRACE219 = None
        CCBRACE221 = None
        cond_comb214 = None
        if_expression216 = None
        else_expression220 = None

        IF213_tree = None
        OCBRACE215_tree = None
        CCBRACE217_tree = None
        ELSE218_tree = None
        OCBRACE219_tree = None
        CCBRACE221_tree = None
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
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:254:5: ( IF cond_comb OCBRACE if_expression CCBRACE ( ELSE OCBRACE else_expression CCBRACE )* -> {t_else}? ^( IFELSE_ ^( IF_ ^( COND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( NCOND_ cond_comb ) ( else_expression )* ENDIF_ ) ) -> ^( IFELSE_ ^( IF_ ^( COND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( NCOND_ cond_comb ) ENDIF_ ) ) )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:254:7: IF cond_comb OCBRACE if_expression CCBRACE ( ELSE OCBRACE else_expression CCBRACE )*
                pass 
                IF213 = self.match(self.input, IF, self.FOLLOW_IF_in_if_stmt2376) 
                stream_IF.add(IF213)


                self._state.following.append(self.FOLLOW_cond_comb_in_if_stmt2378)
                cond_comb214 = self.cond_comb()

                self._state.following.pop()
                stream_cond_comb.add(cond_comb214.tree)


                OCBRACE215 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_if_stmt2380) 
                stream_OCBRACE.add(OCBRACE215)


                self._state.following.append(self.FOLLOW_if_expression_in_if_stmt2382)
                if_expression216 = self.if_expression()

                self._state.following.pop()
                stream_if_expression.add(if_expression216.tree)


                CCBRACE217 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_if_stmt2384) 
                stream_CCBRACE.add(CCBRACE217)


                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:255:5: ( ELSE OCBRACE else_expression CCBRACE )*
                while True: #loop35
                    alt35 = 2
                    LA35_0 = self.input.LA(1)

                    if (LA35_0 == ELSE) :
                        alt35 = 1


                    if alt35 == 1:
                        # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:255:6: ELSE OCBRACE else_expression CCBRACE
                        pass 
                        ELSE218 = self.match(self.input, ELSE, self.FOLLOW_ELSE_in_if_stmt2391) 
                        stream_ELSE.add(ELSE218)


                        #action start
                        t_else=1
                        #action end


                        OCBRACE219 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_if_stmt2395) 
                        stream_OCBRACE.add(OCBRACE219)


                        self._state.following.append(self.FOLLOW_else_expression_in_if_stmt2397)
                        else_expression220 = self.else_expression()

                        self._state.following.pop()
                        stream_else_expression.add(else_expression220.tree)


                        CCBRACE221 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_if_stmt2399) 
                        stream_CCBRACE.add(CCBRACE221)



                    else:
                        break #loop35


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
                    # 256:5: -> {t_else}? ^( IFELSE_ ^( IF_ ^( COND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( NCOND_ cond_comb ) ( else_expression )* ENDIF_ ) )
                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:256:18: ^( IFELSE_ ^( IF_ ^( COND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( NCOND_ cond_comb ) ( else_expression )* ENDIF_ ) )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(IFELSE_, "IFELSE_")
                    , root_1)

                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:256:28: ^( IF_ ^( COND_ cond_comb ) ( if_expression )* ENDIF_ )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(IF_, "IF_")
                    , root_2)

                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:256:34: ^( COND_ cond_comb )
                    root_3 = self._adaptor.nil()
                    root_3 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(COND_, "COND_")
                    , root_3)

                    self._adaptor.addChild(root_3, stream_cond_comb.nextTree())

                    self._adaptor.addChild(root_2, root_3)

                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:256:53: ( if_expression )*
                    while stream_if_expression.hasNext():
                        self._adaptor.addChild(root_2, stream_if_expression.nextTree())


                    stream_if_expression.reset();

                    self._adaptor.addChild(root_2, 
                    self._adaptor.createFromType(ENDIF_, "ENDIF_")
                    )

                    self._adaptor.addChild(root_1, root_2)

                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:256:76: ^( IF_ ^( NCOND_ cond_comb ) ( else_expression )* ENDIF_ )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(IF_, "IF_")
                    , root_2)

                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:256:82: ^( NCOND_ cond_comb )
                    root_3 = self._adaptor.nil()
                    root_3 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(NCOND_, "NCOND_")
                    , root_3)

                    self._adaptor.addChild(root_3, stream_cond_comb.nextTree())

                    self._adaptor.addChild(root_2, root_3)

                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:256:102: ( else_expression )*
                    while stream_else_expression.hasNext():
                        self._adaptor.addChild(root_2, stream_else_expression.nextTree())


                    stream_else_expression.reset();

                    self._adaptor.addChild(root_2, 
                    self._adaptor.createFromType(ENDIF_, "ENDIF_")
                    )

                    self._adaptor.addChild(root_1, root_2)

                    self._adaptor.addChild(root_0, root_1)



                else: 
                    # 257:5: -> ^( IFELSE_ ^( IF_ ^( COND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( NCOND_ cond_comb ) ENDIF_ ) )
                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:257:8: ^( IFELSE_ ^( IF_ ^( COND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( NCOND_ cond_comb ) ENDIF_ ) )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(IFELSE_, "IFELSE_")
                    , root_1)

                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:257:18: ^( IF_ ^( COND_ cond_comb ) ( if_expression )* ENDIF_ )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(IF_, "IF_")
                    , root_2)

                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:257:24: ^( COND_ cond_comb )
                    root_3 = self._adaptor.nil()
                    root_3 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(COND_, "COND_")
                    , root_3)

                    self._adaptor.addChild(root_3, stream_cond_comb.nextTree())

                    self._adaptor.addChild(root_2, root_3)

                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:257:43: ( if_expression )*
                    while stream_if_expression.hasNext():
                        self._adaptor.addChild(root_2, stream_if_expression.nextTree())


                    stream_if_expression.reset();

                    self._adaptor.addChild(root_2, 
                    self._adaptor.createFromType(ENDIF_, "ENDIF_")
                    )

                    self._adaptor.addChild(root_1, root_2)

                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:257:66: ^( IF_ ^( NCOND_ cond_comb ) ENDIF_ )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(IF_, "IF_")
                    , root_2)

                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:257:72: ^( NCOND_ cond_comb )
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


    class ifnot_stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "ifnot_stmt"
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:260:5: ifnot_stmt : IF NEG cond_comb OCBRACE if_expression CCBRACE ( ELSE OCBRACE else_expression CCBRACE )* -> {t_else}? ^( IFELSE_ ^( IF_ ^( NCOND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( COND_ cond_comb ) ( else_expression )* ENDIF_ ) ) -> ^( IFELSE_ ^( IF_ ^( NCOND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( COND_ cond_comb ) ENDIF_ ) ) ;
    def ifnot_stmt(self, ):
        retval = self.ifnot_stmt_return()
        retval.start = self.input.LT(1)


        root_0 = None

        IF222 = None
        NEG223 = None
        OCBRACE225 = None
        CCBRACE227 = None
        ELSE228 = None
        OCBRACE229 = None
        CCBRACE231 = None
        cond_comb224 = None
        if_expression226 = None
        else_expression230 = None

        IF222_tree = None
        NEG223_tree = None
        OCBRACE225_tree = None
        CCBRACE227_tree = None
        ELSE228_tree = None
        OCBRACE229_tree = None
        CCBRACE231_tree = None
        stream_NEG = RewriteRuleTokenStream(self._adaptor, "token NEG")
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
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:261:5: ( IF NEG cond_comb OCBRACE if_expression CCBRACE ( ELSE OCBRACE else_expression CCBRACE )* -> {t_else}? ^( IFELSE_ ^( IF_ ^( NCOND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( COND_ cond_comb ) ( else_expression )* ENDIF_ ) ) -> ^( IFELSE_ ^( IF_ ^( NCOND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( COND_ cond_comb ) ENDIF_ ) ) )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:261:7: IF NEG cond_comb OCBRACE if_expression CCBRACE ( ELSE OCBRACE else_expression CCBRACE )*
                pass 
                IF222 = self.match(self.input, IF, self.FOLLOW_IF_in_ifnot_stmt2505) 
                stream_IF.add(IF222)


                NEG223 = self.match(self.input, NEG, self.FOLLOW_NEG_in_ifnot_stmt2507) 
                stream_NEG.add(NEG223)


                self._state.following.append(self.FOLLOW_cond_comb_in_ifnot_stmt2509)
                cond_comb224 = self.cond_comb()

                self._state.following.pop()
                stream_cond_comb.add(cond_comb224.tree)


                OCBRACE225 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_ifnot_stmt2511) 
                stream_OCBRACE.add(OCBRACE225)


                self._state.following.append(self.FOLLOW_if_expression_in_ifnot_stmt2513)
                if_expression226 = self.if_expression()

                self._state.following.pop()
                stream_if_expression.add(if_expression226.tree)


                CCBRACE227 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_ifnot_stmt2515) 
                stream_CCBRACE.add(CCBRACE227)


                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:262:5: ( ELSE OCBRACE else_expression CCBRACE )*
                while True: #loop36
                    alt36 = 2
                    LA36_0 = self.input.LA(1)

                    if (LA36_0 == ELSE) :
                        alt36 = 1


                    if alt36 == 1:
                        # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:262:6: ELSE OCBRACE else_expression CCBRACE
                        pass 
                        ELSE228 = self.match(self.input, ELSE, self.FOLLOW_ELSE_in_ifnot_stmt2522) 
                        stream_ELSE.add(ELSE228)


                        #action start
                        t_else=1
                        #action end


                        OCBRACE229 = self.match(self.input, OCBRACE, self.FOLLOW_OCBRACE_in_ifnot_stmt2526) 
                        stream_OCBRACE.add(OCBRACE229)


                        self._state.following.append(self.FOLLOW_else_expression_in_ifnot_stmt2528)
                        else_expression230 = self.else_expression()

                        self._state.following.pop()
                        stream_else_expression.add(else_expression230.tree)


                        CCBRACE231 = self.match(self.input, CCBRACE, self.FOLLOW_CCBRACE_in_ifnot_stmt2530) 
                        stream_CCBRACE.add(CCBRACE231)



                    else:
                        break #loop36


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
                    # 263:5: -> {t_else}? ^( IFELSE_ ^( IF_ ^( NCOND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( COND_ cond_comb ) ( else_expression )* ENDIF_ ) )
                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:263:18: ^( IFELSE_ ^( IF_ ^( NCOND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( COND_ cond_comb ) ( else_expression )* ENDIF_ ) )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(IFELSE_, "IFELSE_")
                    , root_1)

                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:263:28: ^( IF_ ^( NCOND_ cond_comb ) ( if_expression )* ENDIF_ )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(IF_, "IF_")
                    , root_2)

                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:263:34: ^( NCOND_ cond_comb )
                    root_3 = self._adaptor.nil()
                    root_3 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(NCOND_, "NCOND_")
                    , root_3)

                    self._adaptor.addChild(root_3, stream_cond_comb.nextTree())

                    self._adaptor.addChild(root_2, root_3)

                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:263:54: ( if_expression )*
                    while stream_if_expression.hasNext():
                        self._adaptor.addChild(root_2, stream_if_expression.nextTree())


                    stream_if_expression.reset();

                    self._adaptor.addChild(root_2, 
                    self._adaptor.createFromType(ENDIF_, "ENDIF_")
                    )

                    self._adaptor.addChild(root_1, root_2)

                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:263:77: ^( IF_ ^( COND_ cond_comb ) ( else_expression )* ENDIF_ )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(IF_, "IF_")
                    , root_2)

                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:263:83: ^( COND_ cond_comb )
                    root_3 = self._adaptor.nil()
                    root_3 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(COND_, "COND_")
                    , root_3)

                    self._adaptor.addChild(root_3, stream_cond_comb.nextTree())

                    self._adaptor.addChild(root_2, root_3)

                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:263:102: ( else_expression )*
                    while stream_else_expression.hasNext():
                        self._adaptor.addChild(root_2, stream_else_expression.nextTree())


                    stream_else_expression.reset();

                    self._adaptor.addChild(root_2, 
                    self._adaptor.createFromType(ENDIF_, "ENDIF_")
                    )

                    self._adaptor.addChild(root_1, root_2)

                    self._adaptor.addChild(root_0, root_1)



                else: 
                    # 264:5: -> ^( IFELSE_ ^( IF_ ^( NCOND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( COND_ cond_comb ) ENDIF_ ) )
                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:264:8: ^( IFELSE_ ^( IF_ ^( NCOND_ cond_comb ) ( if_expression )* ENDIF_ ) ^( IF_ ^( COND_ cond_comb ) ENDIF_ ) )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(IFELSE_, "IFELSE_")
                    , root_1)

                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:264:18: ^( IF_ ^( NCOND_ cond_comb ) ( if_expression )* ENDIF_ )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(IF_, "IF_")
                    , root_2)

                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:264:24: ^( NCOND_ cond_comb )
                    root_3 = self._adaptor.nil()
                    root_3 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(NCOND_, "NCOND_")
                    , root_3)

                    self._adaptor.addChild(root_3, stream_cond_comb.nextTree())

                    self._adaptor.addChild(root_2, root_3)

                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:264:44: ( if_expression )*
                    while stream_if_expression.hasNext():
                        self._adaptor.addChild(root_2, stream_if_expression.nextTree())


                    stream_if_expression.reset();

                    self._adaptor.addChild(root_2, 
                    self._adaptor.createFromType(ENDIF_, "ENDIF_")
                    )

                    self._adaptor.addChild(root_1, root_2)

                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:264:67: ^( IF_ ^( COND_ cond_comb ) ENDIF_ )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(IF_, "IF_")
                    , root_2)

                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:264:73: ^( COND_ cond_comb )
                    root_3 = self._adaptor.nil()
                    root_3 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(COND_, "COND_")
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

    # $ANTLR end "ifnot_stmt"


    class if_expression_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "if_expression"
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:267:9: if_expression : ( exprwbreak )* ;
    def if_expression(self, ):
        retval = self.if_expression_return()
        retval.start = self.input.LT(1)


        root_0 = None

        exprwbreak232 = None


        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:267:22: ( ( exprwbreak )* )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:267:24: ( exprwbreak )*
                pass 
                root_0 = self._adaptor.nil()


                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:267:24: ( exprwbreak )*
                while True: #loop37
                    alt37 = 2
                    LA37_0 = self.input.LA(1)

                    if (LA37_0 in {BREAK, ID, IF, STATE}) :
                        alt37 = 1


                    if alt37 == 1:
                        # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:267:24: exprwbreak
                        pass 
                        self._state.following.append(self.FOLLOW_exprwbreak_in_if_expression2631)
                        exprwbreak232 = self.exprwbreak()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, exprwbreak232.tree)



                    else:
                        break #loop37




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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:268:9: else_expression : ( exprwbreak )* ;
    def else_expression(self, ):
        retval = self.else_expression_return()
        retval.start = self.input.LT(1)


        root_0 = None

        exprwbreak233 = None


        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:268:24: ( ( exprwbreak )* )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:268:26: ( exprwbreak )*
                pass 
                root_0 = self._adaptor.nil()


                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:268:26: ( exprwbreak )*
                while True: #loop38
                    alt38 = 2
                    LA38_0 = self.input.LA(1)

                    if (LA38_0 in {BREAK, ID, IF, STATE}) :
                        alt38 = 1


                    if alt38 == 1:
                        # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:268:26: exprwbreak
                        pass 
                        self._state.following.append(self.FOLLOW_exprwbreak_in_else_expression2646)
                        exprwbreak233 = self.exprwbreak()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, exprwbreak233.tree)



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

    # $ANTLR end "else_expression"


    class exprwbreak_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "exprwbreak"
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:269:9: exprwbreak : ( expressions | network_send | network_mcast | next_break );
    def exprwbreak(self, ):
        retval = self.exprwbreak_return()
        retval.start = self.input.LT(1)


        root_0 = None

        expressions234 = None
        network_send235 = None
        network_mcast236 = None
        next_break237 = None


        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:269:19: ( expressions | network_send | network_mcast | next_break )
                alt39 = 4
                LA39 = self.input.LA(1)
                if LA39 in {ID}:
                    LA39_1 = self.input.LA(2)

                    if (LA39_1 == DOT) :
                        LA39 = self.input.LA(3)
                        if LA39 in {ID, NID, 96, 97, 98, 99, 100}:
                            alt39 = 1
                        elif LA39 in {102}:
                            alt39 = 2
                        elif LA39 in {101}:
                            alt39 = 3
                        else:
                            nvae = NoViableAltException("", 39, 5, self.input)

                            raise nvae


                    elif (LA39_1 in {EQUALSIGN, SEMICOLON}) :
                        alt39 = 1
                    else:
                        nvae = NoViableAltException("", 39, 1, self.input)

                        raise nvae


                elif LA39 in {IF, STATE}:
                    alt39 = 1
                elif LA39 in {BREAK}:
                    alt39 = 4
                else:
                    nvae = NoViableAltException("", 39, 0, self.input)

                    raise nvae


                if alt39 == 1:
                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:269:21: expressions
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_expressions_in_exprwbreak2661)
                    expressions234 = self.expressions()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, expressions234.tree)



                elif alt39 == 2:
                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:269:35: network_send
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_network_send_in_exprwbreak2665)
                    network_send235 = self.network_send()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, network_send235.tree)



                elif alt39 == 3:
                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:269:50: network_mcast
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_network_mcast_in_exprwbreak2669)
                    network_mcast236 = self.network_mcast()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, network_mcast236.tree)



                elif alt39 == 4:
                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:269:66: next_break
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_next_break_in_exprwbreak2673)
                    next_break237 = self.next_break()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, next_break237.tree)



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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:270:9: cond_comb : cond_rel ( combinatorial_operator cond_rel )* ;
    def cond_comb(self, ):
        retval = self.cond_comb_return()
        retval.start = self.input.LT(1)


        root_0 = None

        cond_rel238 = None
        combinatorial_operator239 = None
        cond_rel240 = None


        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:270:18: ( cond_rel ( combinatorial_operator cond_rel )* )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:270:20: cond_rel ( combinatorial_operator cond_rel )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_cond_rel_in_cond_comb2687)
                cond_rel238 = self.cond_rel()

                self._state.following.pop()
                self._adaptor.addChild(root_0, cond_rel238.tree)


                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:270:29: ( combinatorial_operator cond_rel )*
                while True: #loop40
                    alt40 = 2
                    LA40_0 = self.input.LA(1)

                    if (LA40_0 in {88, 103}) :
                        alt40 = 1


                    if alt40 == 1:
                        # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:270:30: combinatorial_operator cond_rel
                        pass 
                        self._state.following.append(self.FOLLOW_combinatorial_operator_in_cond_comb2690)
                        combinatorial_operator239 = self.combinatorial_operator()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, combinatorial_operator239.tree)


                        self._state.following.append(self.FOLLOW_cond_rel_in_cond_comb2692)
                        cond_rel240 = self.cond_rel()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, cond_rel240.tree)



                    else:
                        break #loop40




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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:271:9: cond_rel : ( OBRACE )* cond_sel ( CBRACE )* -> cond_sel ;
    def cond_rel(self, ):
        retval = self.cond_rel_return()
        retval.start = self.input.LT(1)


        root_0 = None

        OBRACE241 = None
        CBRACE243 = None
        cond_sel242 = None

        OBRACE241_tree = None
        CBRACE243_tree = None
        stream_OBRACE = RewriteRuleTokenStream(self._adaptor, "token OBRACE")
        stream_CBRACE = RewriteRuleTokenStream(self._adaptor, "token CBRACE")
        stream_cond_sel = RewriteRuleSubtreeStream(self._adaptor, "rule cond_sel")
        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:271:18: ( ( OBRACE )* cond_sel ( CBRACE )* -> cond_sel )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:271:20: ( OBRACE )* cond_sel ( CBRACE )*
                pass 
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:271:20: ( OBRACE )*
                while True: #loop41
                    alt41 = 2
                    LA41_0 = self.input.LA(1)

                    if (LA41_0 == OBRACE) :
                        alt41 = 1


                    if alt41 == 1:
                        # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:271:20: OBRACE
                        pass 
                        OBRACE241 = self.match(self.input, OBRACE, self.FOLLOW_OBRACE_in_cond_rel2709) 
                        stream_OBRACE.add(OBRACE241)



                    else:
                        break #loop41


                self._state.following.append(self.FOLLOW_cond_sel_in_cond_rel2712)
                cond_sel242 = self.cond_sel()

                self._state.following.pop()
                stream_cond_sel.add(cond_sel242.tree)


                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:271:37: ( CBRACE )*
                while True: #loop42
                    alt42 = 2
                    LA42_0 = self.input.LA(1)

                    if (LA42_0 == CBRACE) :
                        alt42 = 1


                    if alt42 == 1:
                        # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:271:37: CBRACE
                        pass 
                        CBRACE243 = self.match(self.input, CBRACE, self.FOLLOW_CBRACE_in_cond_rel2714) 
                        stream_CBRACE.add(CBRACE243)



                    else:
                        break #loop42


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
                # 271:45: -> cond_sel
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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:272:13: cond_sel : cond_types ( relational_operator cond_types )* ;
    def cond_sel(self, ):
        retval = self.cond_sel_return()
        retval.start = self.input.LT(1)


        root_0 = None

        cond_types244 = None
        relational_operator245 = None
        cond_types246 = None


        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:272:22: ( cond_types ( relational_operator cond_types )* )
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:272:24: cond_types ( relational_operator cond_types )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_cond_types_in_cond_sel2738)
                cond_types244 = self.cond_types()

                self._state.following.pop()
                self._adaptor.addChild(root_0, cond_types244.tree)


                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:272:35: ( relational_operator cond_types )*
                while True: #loop43
                    alt43 = 2
                    LA43_0 = self.input.LA(1)

                    if ((89 <= LA43_0 <= 93) or LA43_0 in {87}) :
                        alt43 = 1


                    if alt43 == 1:
                        # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:272:36: relational_operator cond_types
                        pass 
                        self._state.following.append(self.FOLLOW_relational_operator_in_cond_sel2741)
                        relational_operator245 = self.relational_operator()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, relational_operator245.tree)


                        self._state.following.append(self.FOLLOW_cond_types_in_cond_sel2743)
                        cond_types246 = self.cond_types()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, cond_types246.tree)



                    else:
                        break #loop43




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
    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:273:13: cond_types : ( object_expr | set_func | INT | BOOL );
    def cond_types(self, ):
        retval = self.cond_types_return()
        retval.start = self.input.LT(1)


        root_0 = None

        INT249 = None
        BOOL250 = None
        object_expr247 = None
        set_func248 = None

        INT249_tree = None
        BOOL250_tree = None

        try:
            try:
                # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:273:24: ( object_expr | set_func | INT | BOOL )
                alt44 = 4
                LA44 = self.input.LA(1)
                if LA44 in {ID}:
                    LA44_1 = self.input.LA(2)

                    if (LA44_1 == DOT) :
                        LA44_4 = self.input.LA(3)

                        if (LA44_4 in {ID, NID}) :
                            alt44 = 1
                        elif ((96 <= LA44_4 <= 100) or LA44_4 in {}) :
                            alt44 = 2
                        else:
                            nvae = NoViableAltException("", 44, 4, self.input)

                            raise nvae


                    elif ((87 <= LA44_1 <= 93) or LA44_1 in {CBRACE, OCBRACE, 103}) :
                        alt44 = 1
                    else:
                        nvae = NoViableAltException("", 44, 1, self.input)

                        raise nvae


                elif LA44 in {INT}:
                    alt44 = 3
                elif LA44 in {BOOL}:
                    alt44 = 4
                else:
                    nvae = NoViableAltException("", 44, 0, self.input)

                    raise nvae


                if alt44 == 1:
                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:273:26: object_expr
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_object_expr_in_cond_types2764)
                    object_expr247 = self.object_expr()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, object_expr247.tree)



                elif alt44 == 2:
                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:273:40: set_func
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_set_func_in_cond_types2768)
                    set_func248 = self.set_func()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, set_func248.tree)



                elif alt44 == 3:
                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:273:51: INT
                    pass 
                    root_0 = self._adaptor.nil()


                    INT249 = self.match(self.input, INT, self.FOLLOW_INT_in_cond_types2772)
                    INT249_tree = self._adaptor.createWithPayload(INT249)
                    self._adaptor.addChild(root_0, INT249_tree)




                elif alt44 == 4:
                    # /home/tux/PycharmProjects/ProtoGen_public/Parser/ProtoCC.g:273:57: BOOL
                    pass 
                    root_0 = self._adaptor.nil()


                    BOOL250 = self.match(self.input, BOOL, self.FOLLOW_BOOL_in_cond_types2776)
                    BOOL250_tree = self._adaptor.createWithPayload(BOOL250)
                    self._adaptor.addChild(root_0, BOOL250_tree)




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



 

    FOLLOW_102_in_send_function580 = frozenset([1])
    FOLLOW_101_in_mcast_function591 = frozenset([1])
    FOLLOW_const_decl_in_document912 = frozenset([1, 5, 17, 25, 30, 43, 45, 57, 62, 82])
    FOLLOW_init_hw_in_document916 = frozenset([1, 5, 17, 25, 30, 43, 45, 57, 62, 82])
    FOLLOW_arch_block_in_document920 = frozenset([1, 5, 17, 25, 30, 43, 45, 57, 62, 82])
    FOLLOW_expressions_in_document924 = frozenset([1, 5, 17, 25, 30, 43, 45, 57, 62, 82])
    FOLLOW_int_decl_in_declarations937 = frozenset([1])
    FOLLOW_bool_decl_in_declarations941 = frozenset([1])
    FOLLOW_state_decl_in_declarations945 = frozenset([1])
    FOLLOW_data_decl_in_declarations949 = frozenset([1])
    FOLLOW_id_decl_in_declarations953 = frozenset([1])
    FOLLOW_CONSTANT_in_const_decl965 = frozenset([43])
    FOLLOW_ID_in_const_decl967 = frozenset([50])
    FOLLOW_INT_in_const_decl969 = frozenset([1])
    FOLLOW_INTID_in_int_decl991 = frozenset([70])
    FOLLOW_range_in_int_decl993 = frozenset([43])
    FOLLOW_ID_in_int_decl995 = frozenset([39, 75])
    FOLLOW_EQUALSIGN_in_int_decl998 = frozenset([50])
    FOLLOW_INT_in_int_decl1000 = frozenset([39, 75])
    FOLLOW_SEMICOLON_in_int_decl1004 = frozenset([1])
    FOLLOW_BOOLID_in_bool_decl1032 = frozenset([43])
    FOLLOW_ID_in_bool_decl1034 = frozenset([39, 75])
    FOLLOW_EQUALSIGN_in_bool_decl1037 = frozenset([12])
    FOLLOW_BOOL_in_bool_decl1039 = frozenset([39, 75])
    FOLLOW_SEMICOLON_in_bool_decl1043 = frozenset([1])
    FOLLOW_STATE_in_state_decl1070 = frozenset([43])
    FOLLOW_ID_in_state_decl1072 = frozenset([75])
    FOLLOW_SEMICOLON_in_state_decl1074 = frozenset([1])
    FOLLOW_DATA_in_data_decl1093 = frozenset([43])
    FOLLOW_ID_in_data_decl1095 = frozenset([75])
    FOLLOW_SEMICOLON_in_data_decl1097 = frozenset([1])
    FOLLOW_set_decl_in_id_decl1116 = frozenset([66, 77])
    FOLLOW_NID_in_id_decl1119 = frozenset([43])
    FOLLOW_ID_in_id_decl1121 = frozenset([75])
    FOLLOW_SEMICOLON_in_id_decl1123 = frozenset([1])
    FOLLOW_SET_in_set_decl1145 = frozenset([70])
    FOLLOW_OEBRACE_in_set_decl1147 = frozenset([43, 50])
    FOLLOW_val_range_in_set_decl1149 = frozenset([21])
    FOLLOW_CEBRACE_in_set_decl1151 = frozenset([1])
    FOLLOW_SET_in_objset_decl1170 = frozenset([70])
    FOLLOW_OEBRACE_in_objset_decl1172 = frozenset([43, 50])
    FOLLOW_val_range_in_objset_decl1174 = frozenset([21])
    FOLLOW_CEBRACE_in_objset_decl1176 = frozenset([1])
    FOLLOW_OEBRACE_in_range1200 = frozenset([43, 50])
    FOLLOW_val_range_in_range1202 = frozenset([32])
    FOLLOW_DOT_in_range1204 = frozenset([32])
    FOLLOW_DOT_in_range1206 = frozenset([43, 50])
    FOLLOW_val_range_in_range1208 = frozenset([21])
    FOLLOW_CEBRACE_in_range1210 = frozenset([1])
    FOLLOW_ARRAY_in_array_decl1259 = frozenset([70])
    FOLLOW_range_in_array_decl1261 = frozenset([1])
    FOLLOW_FIFO_in_fifo_decl1271 = frozenset([70])
    FOLLOW_range_in_fifo_decl1273 = frozenset([1])
    FOLLOW_network_block_in_init_hw1283 = frozenset([1])
    FOLLOW_machines_in_init_hw1287 = frozenset([1])
    FOLLOW_message_block_in_init_hw1291 = frozenset([1])
    FOLLOW_object_expr_in_object_block1302 = frozenset([75])
    FOLLOW_SEMICOLON_in_object_block1304 = frozenset([1])
    FOLLOW_ID_in_object_expr1319 = frozenset([1])
    FOLLOW_object_func_in_object_expr1323 = frozenset([1])
    FOLLOW_ID_in_object_func1334 = frozenset([32])
    FOLLOW_DOT_in_object_func1336 = frozenset([43, 66])
    FOLLOW_object_idres_in_object_func1338 = frozenset([1, 68])
    FOLLOW_OBRACE_in_object_func1341 = frozenset([19, 22, 43])
    FOLLOW_object_expr_in_object_func1343 = frozenset([19, 22, 43])
    FOLLOW_COMMA_in_object_func1347 = frozenset([43])
    FOLLOW_object_expr_in_object_func1349 = frozenset([19, 22])
    FOLLOW_CBRACE_in_object_func1353 = frozenset([1, 68])
    FOLLOW_cache_block_in_machines1422 = frozenset([1])
    FOLLOW_dir_block_in_machines1426 = frozenset([1])
    FOLLOW_CACHE_in_cache_block1441 = frozenset([69])
    FOLLOW_OCBRACE_in_cache_block1443 = frozenset([13, 20, 27, 51, 66, 77, 82])
    FOLLOW_declarations_in_cache_block1445 = frozenset([13, 20, 27, 51, 66, 77, 82])
    FOLLOW_CCBRACE_in_cache_block1448 = frozenset([43, 77])
    FOLLOW_objset_decl_in_cache_block1450 = frozenset([43, 77])
    FOLLOW_ID_in_cache_block1453 = frozenset([75])
    FOLLOW_SEMICOLON_in_cache_block1455 = frozenset([1])
    FOLLOW_DIR_in_dir_block1496 = frozenset([69])
    FOLLOW_OCBRACE_in_dir_block1498 = frozenset([13, 20, 27, 51, 66, 77, 82])
    FOLLOW_declarations_in_dir_block1500 = frozenset([13, 20, 27, 51, 66, 77, 82])
    FOLLOW_CCBRACE_in_dir_block1503 = frozenset([43, 77])
    FOLLOW_objset_decl_in_dir_block1505 = frozenset([43, 77])
    FOLLOW_ID_in_dir_block1508 = frozenset([75])
    FOLLOW_SEMICOLON_in_dir_block1510 = frozenset([1])
    FOLLOW_NETWORK_in_network_block1554 = frozenset([69])
    FOLLOW_OCBRACE_in_network_block1556 = frozenset([20, 94, 95])
    FOLLOW_network_element_in_network_block1558 = frozenset([20, 94, 95])
    FOLLOW_CCBRACE_in_network_block1561 = frozenset([75])
    FOLLOW_SEMICOLON_in_network_block1563 = frozenset([1])
    FOLLOW_element_type_in_network_element1606 = frozenset([43])
    FOLLOW_ID_in_network_element1608 = frozenset([75])
    FOLLOW_SEMICOLON_in_network_element1610 = frozenset([1])
    FOLLOW_ID_in_network_send1631 = frozenset([32])
    FOLLOW_DOT_in_network_send1633 = frozenset([102])
    FOLLOW_send_function_in_network_send1635 = frozenset([68])
    FOLLOW_OBRACE_in_network_send1637 = frozenset([43])
    FOLLOW_ID_in_network_send1639 = frozenset([19])
    FOLLOW_CBRACE_in_network_send1641 = frozenset([75])
    FOLLOW_SEMICOLON_in_network_send1643 = frozenset([1])
    FOLLOW_ID_in_network_mcast1663 = frozenset([32])
    FOLLOW_DOT_in_network_mcast1665 = frozenset([101])
    FOLLOW_mcast_function_in_network_mcast1667 = frozenset([68])
    FOLLOW_OBRACE_in_network_mcast1669 = frozenset([43])
    FOLLOW_ID_in_network_mcast1671 = frozenset([22])
    FOLLOW_COMMA_in_network_mcast1673 = frozenset([43])
    FOLLOW_ID_in_network_mcast1675 = frozenset([19])
    FOLLOW_CBRACE_in_network_mcast1677 = frozenset([75])
    FOLLOW_SEMICOLON_in_network_mcast1679 = frozenset([1])
    FOLLOW_MSG_in_message_block1709 = frozenset([43])
    FOLLOW_ID_in_message_block1711 = frozenset([69])
    FOLLOW_OCBRACE_in_message_block1713 = frozenset([13, 20, 27, 51, 66, 77, 82])
    FOLLOW_declarations_in_message_block1715 = frozenset([13, 20, 27, 51, 66, 77, 82])
    FOLLOW_CCBRACE_in_message_block1718 = frozenset([75])
    FOLLOW_SEMICOLON_in_message_block1720 = frozenset([1])
    FOLLOW_ID_in_message_constr1742 = frozenset([68])
    FOLLOW_OBRACE_in_message_constr1744 = frozenset([12, 19, 22, 43, 50, 66])
    FOLLOW_message_expr_in_message_constr1746 = frozenset([12, 19, 22, 43, 50, 66])
    FOLLOW_COMMA_in_message_constr1750 = frozenset([12, 43, 50, 66])
    FOLLOW_message_expr_in_message_constr1752 = frozenset([19, 22])
    FOLLOW_CBRACE_in_message_constr1756 = frozenset([1])
    FOLLOW_object_expr_in_message_expr1778 = frozenset([1])
    FOLLOW_set_func_in_message_expr1782 = frozenset([1])
    FOLLOW_INT_in_message_expr1786 = frozenset([1])
    FOLLOW_BOOL_in_message_expr1790 = frozenset([1])
    FOLLOW_NID_in_message_expr1794 = frozenset([1])
    FOLLOW_set_func_in_set_block1812 = frozenset([75])
    FOLLOW_SEMICOLON_in_set_block1814 = frozenset([1])
    FOLLOW_ID_in_set_func1829 = frozenset([32])
    FOLLOW_DOT_in_set_func1831 = frozenset([96, 97, 98, 99, 100])
    FOLLOW_set_function_types_in_set_func1833 = frozenset([68])
    FOLLOW_OBRACE_in_set_func1835 = frozenset([19, 43])
    FOLLOW_set_nest_in_set_func1837 = frozenset([19, 43])
    FOLLOW_CBRACE_in_set_func1840 = frozenset([1])
    FOLLOW_set_func_in_set_nest1878 = frozenset([1])
    FOLLOW_object_expr_in_set_nest1882 = frozenset([1])
    FOLLOW_ARCH_in_arch_block1892 = frozenset([43])
    FOLLOW_ID_in_arch_block1894 = frozenset([69])
    FOLLOW_OCBRACE_in_arch_block1896 = frozenset([20, 72, 80])
    FOLLOW_arch_body_in_arch_block1898 = frozenset([20])
    FOLLOW_CCBRACE_in_arch_block1900 = frozenset([1])
    FOLLOW_stable_def_in_arch_body1922 = frozenset([1, 72, 80])
    FOLLOW_process_block_in_arch_body1926 = frozenset([1, 72, 80])
    FOLLOW_STABLE_in_stable_def1936 = frozenset([69])
    FOLLOW_OCBRACE_in_stable_def1938 = frozenset([43])
    FOLLOW_ID_in_stable_def1940 = frozenset([20, 22])
    FOLLOW_COMMA_in_stable_def1943 = frozenset([43])
    FOLLOW_ID_in_stable_def1945 = frozenset([20, 22])
    FOLLOW_CCBRACE_in_stable_def1949 = frozenset([1])
    FOLLOW_PROC_in_process_block1968 = frozenset([68])
    FOLLOW_process_trans_in_process_block1970 = frozenset([69])
    FOLLOW_OCBRACE_in_process_block1972 = frozenset([10, 20, 43, 45, 82])
    FOLLOW_process_expr_in_process_block1974 = frozenset([10, 20, 43, 45, 82])
    FOLLOW_CCBRACE_in_process_block1977 = frozenset([1])
    FOLLOW_OBRACE_in_process_trans2003 = frozenset([43])
    FOLLOW_ID_in_process_trans2005 = frozenset([22])
    FOLLOW_COMMA_in_process_trans2007 = frozenset([4, 43])
    FOLLOW_process_events_in_process_trans2009 = frozenset([19, 22])
    FOLLOW_process_finalstate_in_process_trans2011 = frozenset([19, 22])
    FOLLOW_CBRACE_in_process_trans2014 = frozenset([1])
    FOLLOW_COMMA_in_process_finalstate2037 = frozenset([43, 82])
    FOLLOW_process_finalident_in_process_finalstate2039 = frozenset([1])
    FOLLOW_expressions_in_process_expr2088 = frozenset([1])
    FOLLOW_network_send_in_process_expr2092 = frozenset([1])
    FOLLOW_network_mcast_in_process_expr2096 = frozenset([1])
    FOLLOW_transaction_in_process_expr2100 = frozenset([1])
    FOLLOW_AWAIT_in_transaction2110 = frozenset([69])
    FOLLOW_OCBRACE_in_transaction2112 = frozenset([20, 84])
    FOLLOW_trans_in_transaction2114 = frozenset([20, 84])
    FOLLOW_CCBRACE_in_transaction2117 = frozenset([1])
    FOLLOW_WHEN_in_trans2137 = frozenset([43])
    FOLLOW_ID_in_trans2139 = frozenset([29])
    FOLLOW_DDOT_in_trans2141 = frozenset([1, 10, 15, 43, 45, 64, 82])
    FOLLOW_trans_body_in_trans2143 = frozenset([1, 10, 15, 43, 45, 64, 82])
    FOLLOW_expressions_in_trans_body2176 = frozenset([1])
    FOLLOW_next_trans_in_trans_body2180 = frozenset([1])
    FOLLOW_next_break_in_trans_body2184 = frozenset([1])
    FOLLOW_transaction_in_trans_body2188 = frozenset([1])
    FOLLOW_network_send_in_trans_body2192 = frozenset([1])
    FOLLOW_network_mcast_in_trans_body2196 = frozenset([1])
    FOLLOW_NEXT_in_next_trans2214 = frozenset([69])
    FOLLOW_OCBRACE_in_next_trans2216 = frozenset([20, 84])
    FOLLOW_trans_in_next_trans2218 = frozenset([20, 84])
    FOLLOW_CCBRACE_in_next_trans2221 = frozenset([1])
    FOLLOW_BREAK_in_next_break2238 = frozenset([75])
    FOLLOW_SEMICOLON_in_next_break2240 = frozenset([1])
    FOLLOW_assignment_in_expressions2256 = frozenset([1])
    FOLLOW_conditional_in_expressions2260 = frozenset([1])
    FOLLOW_object_block_in_expressions2264 = frozenset([1])
    FOLLOW_set_block_in_expressions2268 = frozenset([1])
    FOLLOW_process_finalident_in_assignment2275 = frozenset([39])
    FOLLOW_EQUALSIGN_in_assignment2277 = frozenset([12, 43, 50])
    FOLLOW_assign_types_in_assignment2279 = frozenset([75])
    FOLLOW_SEMICOLON_in_assignment2281 = frozenset([1])
    FOLLOW_object_expr_in_assign_types2303 = frozenset([1])
    FOLLOW_message_constr_in_assign_types2307 = frozenset([1])
    FOLLOW_math_op_in_assign_types2311 = frozenset([1])
    FOLLOW_set_func_in_assign_types2315 = frozenset([1])
    FOLLOW_INT_in_assign_types2319 = frozenset([1])
    FOLLOW_BOOL_in_assign_types2323 = frozenset([1])
    FOLLOW_val_range_in_math_op2334 = frozenset([56, 71])
    FOLLOW_set_in_math_op2336 = frozenset([43, 50])
    FOLLOW_val_range_in_math_op2344 = frozenset([1])
    FOLLOW_if_stmt_in_conditional2353 = frozenset([1])
    FOLLOW_ifnot_stmt_in_conditional2357 = frozenset([1])
    FOLLOW_IF_in_if_stmt2376 = frozenset([12, 43, 50, 68])
    FOLLOW_cond_comb_in_if_stmt2378 = frozenset([69])
    FOLLOW_OCBRACE_in_if_stmt2380 = frozenset([15, 20, 43, 45, 82])
    FOLLOW_if_expression_in_if_stmt2382 = frozenset([20])
    FOLLOW_CCBRACE_in_if_stmt2384 = frozenset([1, 34])
    FOLLOW_ELSE_in_if_stmt2391 = frozenset([69])
    FOLLOW_OCBRACE_in_if_stmt2395 = frozenset([15, 20, 43, 45, 82])
    FOLLOW_else_expression_in_if_stmt2397 = frozenset([20])
    FOLLOW_CCBRACE_in_if_stmt2399 = frozenset([1, 34])
    FOLLOW_IF_in_ifnot_stmt2505 = frozenset([61])
    FOLLOW_NEG_in_ifnot_stmt2507 = frozenset([12, 43, 50, 68])
    FOLLOW_cond_comb_in_ifnot_stmt2509 = frozenset([69])
    FOLLOW_OCBRACE_in_ifnot_stmt2511 = frozenset([15, 20, 43, 45, 82])
    FOLLOW_if_expression_in_ifnot_stmt2513 = frozenset([20])
    FOLLOW_CCBRACE_in_ifnot_stmt2515 = frozenset([1, 34])
    FOLLOW_ELSE_in_ifnot_stmt2522 = frozenset([69])
    FOLLOW_OCBRACE_in_ifnot_stmt2526 = frozenset([15, 20, 43, 45, 82])
    FOLLOW_else_expression_in_ifnot_stmt2528 = frozenset([20])
    FOLLOW_CCBRACE_in_ifnot_stmt2530 = frozenset([1, 34])
    FOLLOW_exprwbreak_in_if_expression2631 = frozenset([1, 15, 43, 45, 82])
    FOLLOW_exprwbreak_in_else_expression2646 = frozenset([1, 15, 43, 45, 82])
    FOLLOW_expressions_in_exprwbreak2661 = frozenset([1])
    FOLLOW_network_send_in_exprwbreak2665 = frozenset([1])
    FOLLOW_network_mcast_in_exprwbreak2669 = frozenset([1])
    FOLLOW_next_break_in_exprwbreak2673 = frozenset([1])
    FOLLOW_cond_rel_in_cond_comb2687 = frozenset([1, 88, 103])
    FOLLOW_combinatorial_operator_in_cond_comb2690 = frozenset([12, 43, 50, 68])
    FOLLOW_cond_rel_in_cond_comb2692 = frozenset([1, 88, 103])
    FOLLOW_OBRACE_in_cond_rel2709 = frozenset([12, 43, 50, 68])
    FOLLOW_cond_sel_in_cond_rel2712 = frozenset([1, 19])
    FOLLOW_CBRACE_in_cond_rel2714 = frozenset([1, 19])
    FOLLOW_cond_types_in_cond_sel2738 = frozenset([1, 87, 89, 90, 91, 92, 93])
    FOLLOW_relational_operator_in_cond_sel2741 = frozenset([12, 43, 50])
    FOLLOW_cond_types_in_cond_sel2743 = frozenset([1, 87, 89, 90, 91, 92, 93])
    FOLLOW_object_expr_in_cond_types2764 = frozenset([1])
    FOLLOW_set_func_in_cond_types2768 = frozenset([1])
    FOLLOW_INT_in_cond_types2772 = frozenset([1])
    FOLLOW_BOOL_in_cond_types2776 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("ProtoCCLexer", ProtoCCParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
