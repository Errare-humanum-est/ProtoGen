import inspect
import os
import re
import subprocess

from Parser.ProtoCCcomTreeFct import *
from Monitor.Debug import *

class Murphi:

    nl = "\n"
    sem = ";"
    end = sem + nl

    tab = "  "

    defaccess = "none"
    defval = "undefined"
    defset = "undefine"

    statesuf = "s_"
    vectorsuf = "v_"
    countsuf = "cnt_"
    instsuf = "i_"

    TemplateDir = "MurphiTemp"
    fconst = "const.m"

    ffifo = "fifo.m"
    ffifofunc = "fifofunc.m"
    ffiforule = "fiforule.m"
    ffifoinit = "fifoinit.m"

    fbuffer = "buffer.m"
    fbufferfunc = "bufferfunc.m"

    fdeferpushfunc = "deferpushfunc.m"
    fdeferpopfunc = "deferpopfunc.m"

    fonetwork = "onetworkfunc.m"
    forderedrule = "orderedrule.m"
    forderedinit = "orderedinit.m"

    funetwork = "unetworkfunc.m"
    funorderedrule = "unorderedrule.m"
    funorderedinit = "unorderedinit.m"

    fmulticast = "multicastfunc.m"
    fvector = "vectorfunc.m"

    # Invariants
    finvariantws = "invariantWS.m"

    # Makefile template
    ftmpmake = "tmpmakefile"

    # Enum keywords
    kaccess = "Access"
    kmessages = "MessageType"
    kaddress = "Address"
    kcacheval = "ClValue"
    kmachines = "Machines"

    # Record keywords
    rmessage = "Message"
    rfifo = "FIFO"
    rbuffer = "Buffer"

    # const
    cvalcntid = "VAL_COUNT"
    cvalmax = 1
    cadrcntid = "ADR_COUNT"
    cadrcnt = 1

    SetKey = 'OBJSET_'
    EntryKey = 'ENTRY_'
    MachKey = 'MACH_'
    ObjKey = "OBJ_"
    Initval = 'INITVAL_'

    CLIdent = 'CL'

    DataDef = {
        'OBJSET_': '_PassNode',
        'INITSTATE_': '_setInitState',
        'DATA_': '_genData',
        'ID_': '_genID',
        'INT_': '_genInt',
        'BOOL_': '_genBool',
        'MSG_': '_genMSG',
    }

    defmsgname = "msg"

    cadr = "adr"
    ccle = "cle"
    cmtype = "mtype"
    cinmsg = "inmsg"

    madr = {cadr: kaddress}
    mtype = {cmtype: kmessages}
    msrc = {"src": kmachines}
    mdst = {"dst": kmachines}

    # Machine instances
    iState = 'State'
    iID = 'ID'
    iFifo = 'Defermsg'
    iAccess = 'Perm'

    # Network parameters
    cordered = "O_NET_MAX"
    cunordered = "U_NET_MAX"
    ordered = "Ordered"
    orderedcnt = "Orderedcnt"
    k_onetwork = "onet_"
    unordered = "Unordered"
    k_unetwork = "unet_"

    # FIFOs
    k_fifo = "buf_"

    SetFuncDef = {
        'add': '_genVectAdd',
        'del': '_genVectDel',
        'clear': '_genVectClear',
        'contains': '_genVectCont',
        'empty': '_genVectEmpty',
        'count': '_genVectCnt',
    }

    Opmap = {
        '==': '=',
        '>=': '>=',
        '<=': '<=',
        '!=': '!=',
        '<': '<',
        '>': '>',
    }

    tMSGCSTR = "MSGCSTR_"
    tSETFUNC = "SETFUNC_"

    tCOND = "COND_"
    tNCOND = "NCOND_"
    tASSIGN = "ASSIGN_"
    tSEND = "SEND_"
    tMCAST = "MCAST_"

    unlock_ss = "stable_state" 
    lock_set = "lock_owner_set"

    ssp_prefix = "SSP_"

    # Config Parameters
    cfifomax = 1
    enableFifo = 0
    corderedsz = cadrcnt * 3 * 2 * 2
    cunorderedsz = cadrcnt * 3 * 2 * 2

    def __init__(self, parser, algorithm, verify_ssp):

        """ The following keywords need to be instance-specific. If they
            are not then verifying multiple protocols within one process
            (for example SSP + ProtoGen output) will lead to syntax errors
            in all but the very first of the generated Murphi files."""

        self.kmachnames = []

        self.BaseMsg = [self.madr, self.mtype, self.msrc, self.mdst]
        self.SuperMsg = []

        self.Machines = []
        self.Vectordef = []
        self.Vectormap = {}
        self.Vectorassign = {}
        self.GlobalInit = {}
        self.Messageassignmap ={}

        self.ONetworks = []
        self.UNetworks = []

        file_name = parser.getFilename().split(".")[0] + ".m"
        if verify_ssp:
            file_name = self.ssp_prefix + file_name

        murphifile = open(file_name, "w")
        self.parser = parser

        self.memaccessdef = parser.getAccess()
        self.maxdeferdepth = str(2)
        self.messageslist = algorithm.getMessages() + list(algorithm.getRenamedMessages().keys())

        self.templatepath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + \
                            "/" + \
                            self.TemplateDir

        self.DCconservativeInv = algorithm.getDCconservativeInv()

        self.defer = algorithm.testNonStalling()

        murphiout = ""
        murphiout += self._generateConst(parser) + self.nl
        murphiout += self._generateTypes(parser, algorithm) + self.nl
        murphiout += self._generateVars(parser, verify_ssp) + self.nl
        murphiout += self._generateFunc(parser) + self.nl
        murphiout += self._generateObjFunc(algorithm, verify_ssp) + self.nl
        if verify_ssp:
            arch = "cache" # TODO is there a way around hardcoding this?
            stable_states = parser.getStableStates().get(arch)
            murphiout += self._generateUnlockRules(arch, stable_states)
        murphiout += self._generateFIFORecvRule(parser) + self.nl
        murphiout += self._generateNetworkRules(parser) + self.nl
        murphiout += self._generateStartState(parser, verify_ssp) + self.nl
        murphiout += self._generateInvariants(parser) + self.nl

        murphifile.write(murphiout)


########################################################################################################################
# RUN MURPHI
########################################################################################################################

    def runMurphi(self, verify_ssp):
        makefile = open("Makefile", "w")
        murphiname = self.parser.getFilename().split(".")[0]
        mem = 2000

        if verify_ssp:
            murphiname = self.ssp_prefix + murphiname

        template = self._openTemplate(self.ftmpmake)
        replacekeys = [murphiname]

        for ind in range(0, len(replacekeys)):
            template = self._stringRepl(template, ind, replacekeys[ind])

        makefile.write(template)
        makefile.flush()

        self._runCompilation(murphiname)

        if os.path.isfile("./" + murphiname):
            cmd = ["./" + murphiname, "-tv", "-pr", "-m", str(mem)]
            report = subprocess.run(cmd, stdout=subprocess.PIPE).stdout.decode("utf-8")
            reportfile = open(murphiname + "_results" + ".txt", "w")
            reportfile.write(report)
            reportfile.close()

            if "No error found" not in report:
                pdebug(report)

    def _runCompilation(self, murphiname):
        compile = subprocess.run(["make"], stdout=subprocess.PIPE).stdout.decode("utf-8")
        compilefile = open(murphiname + "_compile" + ".txt", "w")
        compilefile.write(compile)
        compilefile.close()

        res = re.search(r'Makefile:[\w\s:]*\'[\w\s.]*\'\s*failed', compile)
        if res:
            pdebug(compile)
            perror("ProtoGen terminated due to Murphi compilation error")


########################################################################################################################
# CONST
########################################################################################################################

    def _generateConst(self, parser):

        conststr = self._stringReplKeys(self._openTemplate(self.fconst),
                                        ["true" if self.enableFifo else "false"]
                                        )

        constantdict = parser.getConstants()

        conststr += self.tab + self.cvalcntid + ": " + str(self.cvalmax) + self.end
        conststr += self.tab + self.cadrcntid + ": " + str(self.cadrcnt) + self.end
        conststr += self.nl
        conststr += self.tab + self.cordered + ": " + str(self.corderedsz) + self.end
        conststr += self.tab + self.cunordered + ": " + str(self.cunorderedsz) + self.end
        conststr += self.nl

        for constdecl in sorted(constantdict.keys()):
            constdef = constantdict[constdecl].getChildren()
            conststr += self.tab + constdef[0].getText() + ": " + constdef[1].getText() + self.end

        return conststr

########################################################################################################################
# TYPES
########################################################################################################################

    def _generateTypes(self, parser, algorithm):

        machinetypes = {}

        typestr = self.nl + "type" + self.nl
        typestr += self._generateEnums(parser, algorithm) + self.nl

        typestr += self._typeStatic() + self.nl
        typestr += self._typeMachines(parser.getCaches(), machinetypes) + self.nl
        typestr += self._typeMachines(parser.getDir(), machinetypes) + self.nl
        typestr += self._typeMachineUnion(machinetypes) + self.nl

        self.kmachnames = sorted(list(machinetypes.values()))

        machstr = self._genMessage(parser.getMessageNodes()) + self.nl

        machstr += self._typeFIFO() + self.nl

        if self.defer:
            machstr += self._typeBuffer() + self.nl

        machstr += self._genMachine(parser.getCaches(), parser.getCacheSeq()) + self.nl
        machstr += self._genMachine(parser.getDir(), parser.getDirSeq()) + self.nl

        for entry in self.Vectordef:
            typestr += entry + self.nl

        typestr += machstr

        typestr += self._genMultipleAddress(parser.getCacheSeq()) + self.nl
        typestr += self._genMultipleAddress(parser.getDirSeq()) + self.nl

        typestr += self._genMachineObjects(parser.getCacheSeq()) + self.nl
        typestr += self._genMachineObjects(parser.getDirSeq()) + self.nl

        typestr += self._genNetworkObjects() + self.nl

        typestr += self._genFIFOObjects() + self.nl

        return typestr

    ####################################################################################################################
    # ENUMS
    ####################################################################################################################

    def _generateEnums(self, parser, algorithm):
        typestr = ""

        # Access
        typestr += self._enumaccess(parser.getAccess()) + self.nl
        # Messagetypes
        typestr += self._enummessages(self.messageslist) + self.nl
        # Caches
        typestr += self._enummachinestates(algorithm.getCacheStates(), self.statesuf) + self.nl
        # Directories
        typestr += self._enummachinestates(algorithm.getDirStates(), self.statesuf) + self.nl

        return typestr

    def _enumaccess(self, accesses):
        retstr = self.kaccess + ": enum {" + self.nl + self.tab + "none"
        for access in accesses:
            retstr += "," + self.nl + self.tab + access
        retstr += self.nl + "};" + self.nl

        return retstr

    def _enummessages(self, messages):
        sortmessages = sorted(messages)
        retstr = self.kmessages + ": enum { " + self.nl
        for ind in range(0, len(messages)-1):
            retstr += self.tab + sortmessages[ind] + "," + self.nl
        if sortmessages:
            retstr += self.tab + sortmessages[-1] + self.nl

        retstr += "};" + self.nl

        return retstr

    def _enummachinestates(self, machine, suffix):
        retstr = ""

        for machinekey in sorted(machine.keys()):
            retstr += self.nl + suffix + machinekey + ": enum { " + self.nl

            statekeys = sorted(machine[machinekey].keys())

            for ind in range(0, len(statekeys) - 1):
                retstr += self.tab + machinekey + "_" + statekeys[ind] + "," + self.nl
            if statekeys:
                retstr += self.tab + machinekey + "_" + statekeys[-1] + self.nl

            retstr += "};" + self.nl

        return retstr

    ####################################################################################################################
    # OBJECTS
    ####################################################################################################################

    def _genMessage(self, objects):
        typedefs = {}
        objstr = self.rmessage + ": record" + self.nl

        for defpair in self.BaseMsg:
            for definition in defpair:
                objstr += self.tab + definition + ": " + defpair[definition] + self.end

        for obj in objects:
            defintions = obj.getnode().getChildren()

            for inddef in range(1, len(defintions)):
                if not defintions[inddef].getText() == self.SetKey:

                    definition = toStringList(defintions[inddef])
                    if self.Initval in definition:
                        typedefs.update({definition[definition.index(self.Initval) - 1]: defintions[inddef]})
                    else:
                        typedefs.update({definition[-1]: defintions[inddef]})

        for typekey in sorted(typedefs.keys()):
            method_fct = self.DataDef[typedefs[typekey].getText()]
            method = getattr(self, method_fct, lambda: '_PassNode')
            res = method(typedefs[typekey])

            if res:
                self.SuperMsg.append(res)
                for definition in res:
                    objstr += self.tab + definition + ": " + res[definition] + self.end

        objstr += "end" + self.end

        return objstr

    def _genMachine(self, objects, sequence):

        objstr = ""
        for machine in sequence:
            init = {}
            objstr += self.EntryKey + machine + ": record" + self.nl

            objstr += self.tab + self.iState + ": " + self.statesuf + machine + self.end

            if self.defer:
                objstr += self.tab + self.iFifo + ": " + self.rbuffer + self.end

            objstr += self.tab + self.iAccess + ": " + self.kaccess + self.end

            defintions = objects[machine].getnode().getChildren()

            for inddef in range(1, len(defintions)):
                method_fct = self.DataDef[defintions[inddef].getText()]
                method = getattr(self, method_fct, lambda: '_PassNode')
                res = method(defintions[inddef], init, machine)

                if res:
                    for definition in res:
                        objstr += self.tab + definition + ": " + res[definition] + self.end

            objstr += "end" + self.end

            self.GlobalInit.update({machine: init})

        return objstr

    ####################################################################################################################
    # TYPES
    ####################################################################################################################

    def _typeStatic(self):
        typestr = ""
        typestr += self._makescalarset(self.kaddress, self.cadrcntid)
        typestr += self.kcacheval + ": " + "0.." + self.cvalcntid + self.end

        return typestr

    def _typeFIFO(self):
        return self._stringReplKeys(self._openTemplate(self.ffifo),
                                    [str(self.cfifomax)]
                                    ) + self.nl

    def _typeBuffer(self):
        return self._stringReplKeys(self._openTemplate(self.fbuffer),
                                    [self.maxdeferdepth]
                                    ) + self.nl

    def _typeMachines(self, objects, machinetypes):
        typestr = ""
        objkeys = sorted(objects.keys())

        for indobj in range(0, len(objkeys)):
            objname = objkeys[indobj]
            self.Machines.append(objname)
            defintions = objects[objname].getnode().getChildren()
            if defintions[1].getText() == self.SetKey:
                setconst = defintions[1].getChildren()[0].getText()
                typedef = self._makescalarset(self.SetKey+objname, setconst)
            else:
                typedef = self._makeenum(self.SetKey + objname, objname)

            machinetypes.update({objname: self.SetKey + objname})
            typestr += typedef

        return typestr

    def _typeMachineUnion(self, machinetypes):
        return self._makeunion(self.kmachines, list(machinetypes.values()))

    ####################################################################################################################
    # SET TYPES
    ####################################################################################################################

    def _makeunion(self, typename, elements):
        elmstr = ""
        for ind in range(0, len(elements)-1):
            elmstr += elements[ind] + ", "

        elmstr += elements[-1]

        return typename + ": " + "union{" + elmstr + "};" + self.nl

    def _makeenum(self, typename, machineid):
        return typename + ": " + "enum{" + machineid + "};" + self.nl

    def _makescalarset(self, typename, setsize):
        return typename + ": " + "scalarset(" + setsize + ");" + self.nl

    def _makerange(self, typename, maxval):
        return typename + ": " + "0.." + maxval + ";" + self.nl

    ####################################################################################################################
    # DATA TYPES
    ####################################################################################################################

    def _PassNode(self, definition, initial=0, machine=0):
        return 0

    def _genMultiset(self, definition, machname, refname):
        machineset = self.SetKey + refname
        if machineset in self.kmachnames:
            vectorname = self.vectorsuf + definition.getChildren()[0].getText() + "_" + machineset
            vectorrangename = self.countsuf + self.vectorsuf + definition.getChildren()[0].getText() + "_" + machineset

            vector = vectorname + ": " + \
                     "multiset[" + definition.getChildren()[0].getText() + "] of " + \
                     machineset + self.end

            vector += vectorrangename + ": 0.." + definition.getChildren()[0].getText() + self.end

            if vector not in self.Vectordef:
                self.Vectordef.append(vector)
            self.Vectormap.update({vectorname: machineset})
            if machname:
                self.Vectorassign.update({refname: {machineset: vectorname}})

            return vectorname
        else:
            return 0

    def _setInitState(self, definition, initial=0, machine=0):
        if isinstance(initial, dict):
            initial.update({self.iState: definition.getChildren()[0].getText()})
        else:
            return {definition.getText(): definition.getChildren()[0].getText()}
        return 0

    def _genData(self, definition, initial=0, machine=0):
        definitions = definition.getChildren()
        if len(definitions) > 1:
            settype = self._genMultiset(definitions[0], machine, definitions[-1].getText())
            return {definitions[-1].getText(): settype}
        else:
            if isinstance(initial, dict):
                initial.update({definitions[-1].getText(): "0"})
            return {definitions[-1].getText(): self.kcacheval}

    def _genID(self, definition, initial=0, machine=0):
        definitions = definition.getChildren()
        if len(definitions) > 1:
            settype = self._genMultiset(definitions[0], machine, definitions[-1].getText())
            return {definitions[-1].getText(): settype}
        else:
            return {definitions[-1].getText(): self.kmachines}

    def _genInt(self, definition, initial=0, machine=0):
        children = definition.getChildren()
        if len(children) > 2 and isinstance(initial, dict):
            initial.update({children[1].getText(): children[-1].getText()})

        outstr = ""
        rangedef = children[0].getChildren()
        for ind in range(1, len(rangedef)-1):
            outstr += rangedef[ind].getText()

        return {children[1].getText(): outstr}

    def _genBool(self, definition, initial=0, machine=0):
        children = definition.getChildren()
        if len(children) > 2 and isinstance(initial, dict):
            initial.update({children[1].getText(): children[-1].getText()})
        else:
            initial.update({children[1].getText(): self.defval})

        return {children[1].getText(): "".join(childsToStringList(children[0]))}

    def _genMSG(self, definition, initial=0, machine=0):
        if isinstance(initial, dict):
            initial.update({definition.getChildren()[0].getText(): self.defval})
        return {definition.getChildren()[0].getText(): self.rmessage}

    ####################################################################################################################
    # MULTIPLE ADDRESS
    ####################################################################################################################

    def _genMultipleAddress(self, machines):
        objstr = ""
        for machine in machines:
            objstr += self.MachKey + machine + ": record" + self.nl
            objstr += self.tab + self.CLIdent + ": array[" + self.kaddress + "] of " \
                      + self.EntryKey + machine + self.end
            objstr += "end" + self.end

        return objstr

    def _genMachineObjects(self, machines):
        objstr = ""
        for machine in machines:
            objstr += self.ObjKey + machine +": array[" + self.SetKey + machine + "] of " + \
                     self.MachKey + machine + self.end

        return objstr

    def _genNetworkObjects(self):
        objstr = ""
        # Ordered Network
        objstr += self.ObjKey + self.ordered + ": array[" + self.kmachines + \
                  "] of array[0.." + self.cordered + "-1] of " + self.rmessage + self.end
        objstr += self.ObjKey + self.orderedcnt + ": array[" + self.kmachines + \
                  "] of 0.." + self.cordered + self.end
        objstr += self.ObjKey + self.unordered + ": array[" + self.kmachines + \
                  "] of multiset[" + self.cunordered + "] of " + self.rmessage + self.end

        return objstr

    def _genFIFOObjects(self):
        return self.ObjKey + self.rfifo + ": array[" + self.kmachines + "] of " + self.rfifo + self.end


########################################################################################################################
# VARIABLES
########################################################################################################################
    def _generateVars(self, parser, verify_ssp):
        varstr = "var " + self.nl
        varstr += self._genMachines(parser.getCacheSeq())
        varstr += self._genMachines(parser.getDirSeq())
        varstr += self.nl
        varstr += self._genNetwork(parser.getNetwork())
        varstr += self.nl
        varstr += self._genFIFOs()

        if verify_ssp: # add extra bookkeeping for locking/unlocking
            varstr += self.nl
            varstr += self.tab + self.lock_set + ": multiset[1] of " + self.SetKey \
                    + "cache" #TODO make this less hardcoded maybe
            varstr += self.end
            varstr += self.tab + self.unlock_ss + ": " + self.statesuf + "cache"
            varstr += self.end

        return varstr

    def _genMachines(self, machines):
        varstr = ""
        for machine in machines:
           varstr += self.tab + self.instsuf + machine + ": " + self.ObjKey + machine + self.end

        return varstr

    def _genNetwork(self, networks):
        varstr = ""
        for network in networks:
            definitions = network.getChildren()
            for definition in definitions:
                varstr += self._classNetwork(definition)

        return varstr

    def _classNetwork(self, definition):
        setup = definition.getChildren()
        if setup[0].getText() == self.ordered:
            return self._genOrderedNetwork(setup[1].getText())
        else:
            return self._genUnorderedNetwork(setup[1].getText())

    def _genOrderedNetwork(self, name):
        self.ONetworks.append(name)
        onet = self.tab + name + ": " + self.ObjKey + self.ordered + self.end
        onet += self.tab + self.countsuf + name + ": " + self.ObjKey + self.orderedcnt + self.end
        return onet

    def _genUnorderedNetwork(self, name):
        self.UNetworks.append(name)
        return self.tab + name + ": " + self.ObjKey + self.unordered + self.end

    def _genFIFOs(self):
        varstr = ""
        for network in self.ONetworks + self.UNetworks:
            varstr += self.tab + self.k_fifo + network + ": " + self.ObjKey + self.rfifo + self.end
        return varstr

########################################################################################################################
# FRAMEWORK FUNCTIONS
########################################################################################################################
    def _generateFunc(self, parser):
        funcstr = ""

        # Fifo functions
        funcstr += self._stringReplKeys(self._openTemplate(self.ffifofunc),
                                    [str(self.cfifomax)]
                                    ) + self.nl

        # Generate Message Constructors
        funcstr += self._genMessageConstr(parser.getMessageNodes())

        # Ordered Networks Send
        funcstr += self._genordsendFunc() + self.nl

        # Unordered Networks Send
        funcstr += self._genunordsendFunc() + self.nl
        funcstr += self._genMulticastFunc() + self.nl
        funcstr += self._genVectorFunc() + self.nl

        return funcstr

    def _genMessageConstr(self, objects):
        constrstr = ""

        for obj in objects:
            objname = obj.getname()
            items = []

            constr = "function " + objname + "("

            for defpair in self.BaseMsg:
                for definition in defpair:
                    constr += definition + ": " + defpair[definition] + "; "
                    items.append(definition)

            defintions = obj.getnode().getChildren()
            for inddef in range(1, len(defintions)):
                definition = defintions[inddef].getChildren()[-1].getText()
                for defpair in self.SuperMsg:
                    if definition in defpair:
                        constr += definition + ": " + defpair[definition] + "; "
                        items.append(definition)

            constr = constr.rsplit(';', 1)[0]
            constr += ") : " + self.rmessage + self.end
            constr += "var " + self.defmsgname + ": " + self.rmessage + self.end
            constr += "begin" + self.nl

            for defpair in self.BaseMsg:
                for definition in defpair:
                    constr += self.tab + self.defmsgname + "." + definition + " := " + definition + self.end

            for defpair in self.SuperMsg:
                for definition in defpair:
                    if definition in items:
                        constr += self.tab + self.defmsgname + "." + definition + " := " + definition + self.end
                    else:
                        constr += self.tab + self.defmsgname + "." + definition + " := " + self.defval + self.end

            constr += self.tab + "return " + self.defmsgname + self.end
            constr += "end" + self.end

            constrstr += constr + self.nl

        return constrstr

    def _genordsendFunc(self):
        sendfunc = ""
        for network in self.ONetworks:
            replacekeys = [network, self.countsuf + network, self.cordered]
            inputstr = self._openTemplate(self.fonetwork)

            for ind in range(0, len(replacekeys)):
                inputstr = self._stringRepl(inputstr, ind, replacekeys[ind])

            sendfunc += inputstr + self.nl

        return sendfunc

    def _genunordsendFunc(self):
        sendfunc = ""
        for network in self.UNetworks:
            replacekeys = [network, self.cunordered]
            inputstr = self._openTemplate(self.funetwork)

            for ind in range(0, len(replacekeys)):
                inputstr = self._stringRepl(inputstr, ind, replacekeys[ind])

            sendfunc += inputstr + self.nl

        return sendfunc

    def _genMulticastFunc(self):
        sendfunc = ""
        for network in self.ONetworks+self.UNetworks:
            for vector in self.Vectormap:
                replacekeys = [network, vector]
                inputstr = self._openTemplate(self.fmulticast)

                for ind in range(0, len(replacekeys)):
                    inputstr = self._stringRepl(inputstr, ind, replacekeys[ind])

                sendfunc += inputstr + self.nl

        return sendfunc

    def _genVectorFunc(self):
        vecfunc = ""

        for vector in self.Vectormap:
            replacekeys = [vector, self.Vectormap[vector], self.countsuf + vector]
            inputstr = self._openTemplate(self.fvector)

            for ind in range(0, len(replacekeys)):
                inputstr = self._stringRepl(inputstr, ind, replacekeys[ind])

            vecfunc += inputstr + self.nl

        return vecfunc

########################################################################################################################
# OBJECT FUNCTIONS
# Sorry for the code below..... it will evolve if required
########################################################################################################################
    def _generateObjFunc(self, algorithm, verify_ssp):
        behavstr = ""
        archs = algorithm.getArchStates()

        # Generate non-access function
        for arch in sorted(archs.keys()):
            deferstr = ""
            if self.defer:
                deferstr += self._genDeferFunc(arch)

            archfuncstr = self._genArchNonAccessFunc(arch, archs[arch])

            if self.defer:
                deferstr = self._genDeferUpdateFunc(arch) + deferstr

            behavstr += deferstr + archfuncstr

        behavstr += self.nl + self.nl

        # Generate access function
        for arch in archs:
            behavstr += self._genArchAccessFunc(arch, archs[arch], verify_ssp)

        return behavstr

    def _genArchNonAccessFunc(self, arch, states):
        fctstr = self._genArchHeader(arch) + self.nl

        for state in sorted(states.keys()):
            fctstr += self._genArchState(arch, states[state]) + self.nl

        fctstr += self._genArchEnd() + self.nl

        return fctstr

    def _genArchState(self, arch, state):
        statestr = "case " + arch + "_" + state.getstatename() + ":" + self.nl
        statestr += "switch " + self.cinmsg + "." + self.cmtype + self.nl

        transitions = state.getdataack() + state.getremote()
        transitions.sort(key=lambda transition: (transition.getguard(),
                                                 transition.getcond(),
                                                 transition.getfinalstate().getstatename()))

        # Guard clustering
        guards = []
        for transition in transitions:
            guard =  transition.getguard()
            if guard not in guards:
                guards.append(guard)

        guardmap = []
        for guard in guards:
            cluster = []
            for transition in transitions:
                if transition.getguard() == guard:
                    cluster.append(transition)
            guardmap.append([guard, cluster])

        for guardcluster in guardmap:
            # Sort transitions
            guard = guardcluster[0]
            cluster = guardcluster[1]

            maxdepth = 0
            condmap = []
            for transition in cluster:
                conditions = transition.getcond()

                condorder = []
                condpreset = []
                condstr = []
                for condition in conditions:
                    condflag = ""
                    if condition.startswith(self.tCOND):
                        condpreset.append(self.tCOND)
                        condflag = "0"
                    elif condition.startswith(self.tNCOND):
                        condpreset.append(self.tNCOND)
                        condflag = "1"
                    else:
                        perror("Unrecognized condition prefix")

                    condstr.append(condition.split("_", 1)[1])
                    condorder.append(condstr[-1] + condflag)

                maxdepth = len(condpreset) if len(condpreset) > maxdepth else maxdepth

                condmap.append(["".join(condorder), condstr, condpreset, transition])

            condmap.sort(key=lambda transition: (transition[0]))

            # REMOVE DUPLICATES RELATED TO REDUNDANT IFs. DO PERFECT NESTING.
            prevcond = ""
            prevop = ""
            for indcond in range(0, maxdepth):
                for indtrans in range(0, len(condmap)):
                    condentry = condmap[indtrans][1]
                    if len(condentry) > indcond:
                        if condmap[indtrans][1][indcond] == prevcond and condmap[indtrans][2][indcond] == prevop:
                            # Clear condpreset entry if duplicates
                            prevop = condmap[indtrans][2][indcond]
                            condmap[indtrans][2][indcond] = ""
                        else:
                            prevcond = condmap[indtrans][1][indcond]
                            prevop = condmap[indtrans][2][indcond]
                    else:
                        prevcond = ""
                        prevop = ""

            if len(condmap) > 2:
                print("STOP")

            prevtranstype = ""
            for condentry in condmap:
                # [COND_, "", NCOND]
                condsel = condentry[2]
                transition = condentry[3]

                statestr += self._genTransition(arch, transition, prevtranstype, 0, condsel) + self.nl

                prevtranstype = transition.getguard()


        #prevtranstype = ""

        #for ind in range(0, len(transitions)):
        #    statestr += self._genTransition(arch, transitions[ind], prevtranstype, 0) + self.nl

        #    prevtranstype = transitions[ind].getguard()


        statestr += self.tab + " else return false" + self.end
        statestr += "endswitch" + self.end

        return statestr

    # THIS FUNCTION WORKS FOR CURRENT USE CASE, HOWEVER A MORE SOPHISTICATED VERSION MIGHT BE REQUIRED FOR DIFFERENT
    # PROTOCOLS
    def _genTransition(self, arch, transition, prevtranstype="", parseop=0, condsel=0):
        final = 0
        condcount = 0

        message = []
        msgmap = {}

        inmsgtype = transition.getrefguard() if transition.getrefguard() else transition.getguard()

        if inmsgtype != prevtranstype:
            headerstr = self.tab + "case " + transition.getguard() + ":" + self.nl
            parseop = 1
        else:
            headerstr = ""

        statestr = ""
        operations = transition.getoperation()

        for operation in operations:
            if operation.getText() == self.tASSIGN:
                tmpstr = self._genArchAssignment(operation, arch, inmsgtype, msgmap, message, transition)

                if parseop:
                    statestr += tmpstr

                    if operation.getChildren()[0].getText() == self.iState:
                        statestr += self._genArchAccess(transition)
                        final = 1

            if operation.getText() == self.tSEND and parseop:
                statestr += self._genSendFunction(arch, operation, transition, msgmap, message)

            if operation.getText() == self.tMCAST and parseop:
                statestr += self._genMCastFunction(operation, transition, msgmap, message) + self.end

            # For every if cond=true, there exists an else (if cond=false)
            if operation.getText() == self.tCOND:
                condimp = condsel[condcount]
                if condimp:
                    statestr += self._genIfCondFunction(operation, 0, arch, inmsgtype) + self.nl
                condcount += 1
                parseop = 1

            if operation.getText() == self.tNCOND:
                condimp = condsel[condcount]
                if condimp:
                    statestr += self._genElseCondFunction() + self.nl
                condcount += 1
                parseop = 1

            if operation.getText() == self.tSETFUNC and parseop:
                statestr += self._genSetFunction(operation, arch, inmsgtype) + self.end

        if len(message) != len(transition.getoutmsgtypes()):
            statestr += self._genmsgDeferpop(arch)

        if not final:
            statestr += self.ccle + "." + self.iState + " := " + \
                        arch + "_" + transition.getfinalstate().getstatename() + self.end
            statestr += self._genArchAccess(transition)

        # TODO
        # Only for the number of NCOND_
        #for cnt in range(0, ):
        #    statestr += "endif" + self.end

        statestr = self._addtabs(statestr, 2)

        return headerstr + statestr

    ####################################################################################################################
    # DeferMsgs
    ####################################################################################################################

    def _genDeferFunc(self, arch):
        return self._stringReplKeys(self._openTemplate(self.fbufferfunc),
                                    [self.instsuf + arch, self.SetKey + arch, self.maxdeferdepth]
                                    ) + self.nl

    def _genDeferUpdateFunc(self, arch):
        return ""

    def _genmsgDeferpush(self, arch, message):
        return self._stringReplKeys(self._openTemplate(self.fdeferpushfunc),
                                    [self.instsuf + arch, message]
                                    ) + self.nl

    def _genmsgDeferpop(self, arch):
        return self._stringReplKeys(self._openTemplate(self.fdeferpopfunc),
                                    [self.instsuf + arch]
                                    ) + self.nl

    ####################################################################################################################
    # VARIABLE ASSIGNMENT
    ####################################################################################################################

    def _genArchAssignment(self, operation, arch, inmsgtype, msgmap, message, transition):
        statestr = ""
        tokens = operation.getChildren()
        varname = tokens[0].getText()
        if tokens[-1].getText() == self.tMSGCSTR:
            statestr += varname + " := "
            statestr += self._genMessageAssignment(arch, inmsgtype, tokens[-1], message, transition.getoutmsgrenamed())
            msgmap.update({varname: message[-1]})
        else:
            statestr += self._resolveVarNames(varname) + " := "
            if tokens[0].getText() == self.iState:
                statestr += arch + "_" + transition.getfinalstate().getstatename()
            elif tokens[-1].getText() == self.tSETFUNC:
                statestr += self._genSetFunction(tokens[-1], arch, inmsgtype)
            else:
                for ind in range(2, len(tokens)):
                    statestr += self._resolveChildren(tokens[ind])

        statestr += self.end

        return statestr

    ####################################################################################################################
    # ACCESS PERMISSION ASSIGNMENT
    ####################################################################################################################

    def _genArchAccess(self, transition):
        access = transition.getfinalstate().getaccesshit()

        guards = [guard.getguard() for guard in access]

        accesstype = self.defaccess

        if len(access):
            for memaccess in self.memaccessdef:
                if memaccess in guards:
                    accesstype = memaccess

        return self.ccle + "." + self.iAccess + " := " + accesstype + self.end

    ####################################################################################################################
    # ARCH HEADER
    ####################################################################################################################

    def _genArchHeader(self, arch):
        fctheader = "function Func_" + arch + \
                    "(" + self.cinmsg + ":" + self.rmessage + "; m:" + self.SetKey + arch + ") : boolean" + self.end
        fctheader += "var " + self.defmsgname + ": " + self.rmessage + self.end
        fctheader += "begin" + self.nl
        fctheader += self.tab + "alias " + self.cadr + ": " + self.cinmsg + "." + self.cadr + " do" + self.nl
        fctheader += self.tab + "alias " + self.ccle + \
                     ": " + self.instsuf + arch + "[m]." + self.CLIdent + "[" + self.cadr + "] do" + self.nl
        fctheader += "switch " + self.ccle + "." + self.iState + self.nl

        return fctheader

    def _genArchEnd(self):
        fctfooter = "endswitch" + self.end
        endalias = "endalias" + self.end
        endalias += "endalias" + self.end
        fctfooter += self._addtabs(endalias, 1) + self.nl
        fctfooter += "return true" + self.end
        fctfooter += "end" + self.end
        return fctfooter

    ####################################################################################################################
    # SET FUNCTION
    ####################################################################################################################

    def _genSetFunction(self, objects, arch, guard):
        objectstr = ''.join(childsToStringList(objects))
        param = re.search("\((.*)\)", objectstr).group(1)
        func = re.sub("\((.*)\)", "", objectstr)
        split = func.rsplit('.', 1)

        param1 = self._resolveMsgScrDest(split[0], arch, guard)
        param2 = self._resolveMsgScrDest(param, arch, guard)

        method_fct = self.SetFuncDef[split[1]]
        method = getattr(self, method_fct, lambda: '_PassNode')
        return method(list(self.Vectorassign[split[0]].values())[0], param1, param2)

    @staticmethod
    def _genVectAdd(vectortype, param1, param2):
        return "AddElement_" + vectortype + "(" + param1 + "," + param2 + ")"

    @staticmethod
    def _genVectDel(vectortype, param1, param2):
        return "RemoveElement_" + vectortype + "(" + param1 + "," + param2 + ")"

    @staticmethod
    def _genVectClear(vectortype, param1, param2):
        return "ClearVector_" + vectortype + "(" + param1 + ")"

    @staticmethod
    def _genVectCont(vectortype, param1, param2):
        return "IsElement_" + vectortype + "(" + param1 + "," + param2 + ")"

    @staticmethod
    def _genVectEmpty(vectortype, param1, param2):
        return "HasElement_" + vectortype + "(" + param1 + "," + param2 + ")"

    @staticmethod
    def _genVectCnt(vectortype, param1, param2):
        return "VectorCount_" + vectortype + "(" + param1 + ")" #TODO why does this fn take 3 args?

    @staticmethod
    def _genBagCnt(multiset, element_identifier, condition):
        # To pass conditions on the form "multiset[x] = y", make sure to also
        # pass element_identifier = "x"
        return "MultiSetCount(" + element_identifier + ":" + multiset + ", " + condition + ")"

    @staticmethod
    def _genBagAdd(element, multiset):
        return "MultiSetAdd(" + element +", " + multiset +")"

    @staticmethod
    def _genBagDel(multiset, element_identifier, condition):
        # To pass conditions on the form "multiset[x] = y", make sure to also
        # pass element_identifier = "x"
        return "MultiSetRemovePred(" + element_identifier + ":" + multiset\
                + ", " + condition +")"

    ####################################################################################################################
    # SEND FUNCTION
    ####################################################################################################################

    def _genSendFunction(self, arch, objects, transition, msgmap, message):
        objectstr = ""
        # Check transition defer messages
        definitions = objects.getChildren()

        network = definitions[0].getText()
        msgname = definitions[1].getText()

        defermsg = transition.getdefermsg()

        msg = msgmap[msgname]

        if defermsg:
            for refmsg in defermsg:
                if self._msgCompare(msg, refmsg):
                    objectstr += self._genmsgDeferpush(arch, msgname)
                    message.remove(msg)
                    return objectstr

        # Does not need to be deferred
        objectstr += "Send_" + network + "(" + msgname + ")" + self.end

        return objectstr

    def _genMCastFunction(self, objects, transition, msgmap, message):
        objectstr = ""
        # Check transition defer messages
        definitions = objects.getChildren()

        network = definitions[0].getText()
        msgname = definitions[1].getText()
        vectorname = definitions[2].getText()

        defermsg = transition.getdefermsg()

        msg = msgmap[msgname]

        if defermsg:

            for refmsg in defermsg:
                if self._msgCompare(msg, refmsg):
                    pwarning("Multicast msg deferring not supported yet")
                    try:
                        message.remove(msg)

                    except ValueError:
                        print("STOP")

        # Does not need to be deferred
        objectstr += "Multicast_" + network + "_" + list(self.Vectorassign[vectorname].values())[0] + \
                     "(" + msgname + "," + self.ccle + "." + vectorname + ")"

        return objectstr

    @ staticmethod
    def _msgCompare(msg1, msg2):
        ref1 = msg1 if isinstance(msg1, str) else msg1.getmsgtype()
        ref2 = msg2 if isinstance(msg2, str) else msg2.getmsgtype()

        if ref1 == ref2:
            return True
        return False

    ####################################################################################################################
    # COND FUNCTION
    ####################################################################################################################
    def _genIfCondFunction(self, objects, negation, arch, inmsgtype):
        definitions = objects.getChildren()

        outstr = "if "

        if negation:
            outstr += "!"

        outstr += "("

        for definition in definitions:
            sel = definition.getText()
            if sel == self.tSETFUNC:
                outstr += self._genSetFunction(definition, arch, inmsgtype)

            elif sel in self.Opmap:
                outstr += self.Opmap[sel]

            else:
                outstr += self._resolveVarNames(''.join(toStringList(definition)))

        outstr += ") then"

        return outstr

    def _genElseCondFunction(self):
        return "else"

    ####################################################################################################################
    # MESSAGE ASSIGNMENT
    ####################################################################################################################

    def _genMessageAssignment(self, arch, message, objects, messagelist, renamedlist):
        definition = objects.getChildren()
        msgobj = definition[0].getText()

        msgtype = renamedlist[definition[1].getText()] if definition[1].getText() in renamedlist \
            else definition[1].getText()

        msgsrc = self._resolveMsgScrDest("".join(toStringList(definition[2])), arch, message)
        msgdst = self._resolveMsgScrDest("".join(toStringList(definition[3])), arch, message)

        messagelist.append(msgtype)

        # Request(adr: Address; mtype: MessageType; src: Machines; dst: Machines;

        conststr = msgobj + "("
        # Address
        conststr += self.cadr + ","
        # Messagetype
        conststr += msgtype + ","
        conststr += msgsrc + ","
        conststr += msgdst

        if len(definition) > 4:
            for ind in range(4, len(definition)):
                if definition[ind].getText() == self.tSETFUNC:
                    conststr += "," + self._genSetFunction(definition[ind], arch, message)
                else:
                    conststr += "," + self._resolveChildren(definition[ind])

        conststr += ")"

        return conststr

    def _resolveChildren(self, definition):
        if isinstance(definition, str):
            objectstr = definition
        elif definition.getChildren():
            objectstr = ''.join(toStringList(definition))
        else:
            objectstr = definition.getText()

        return self._resolveVarNames(objectstr)

    def _resolveMsgScrDest(self, objectstr, arch, guard):
        split = objectstr.split('.', 1)

        if len(split) > 1:
            if split[0] == guard:
                return self.cinmsg + '.' + split[1]
            elif split[0] in self.messageslist:
                pwarning("Message substituted: " + guard)
                return self.cinmsg + '.' + split[1]
            else:
                return split[0]
        if split[0] == self.iID:
            return 'm'
        else:
            return self.ccle + '.' + split[0]

    def _resolveVarNames(self, objectstr):
        split = objectstr.split('.', 1)

        if split[0] in self.messageslist:
            del split[0]
            return self.cinmsg + '.' + ''.join(split)
        else:
            if len(split) == 1:
                if self._testInt(split[0]) or not split[0].isalpha():
                    return split[0]
            return self.ccle + '.' + ''.join(split)

########################################################################################################################
# RULESET
########################################################################################################################
    def _genArchAccessFunc(self, arch, states, verify_ssp):
        sendfctstr = ""
        rulesetstr = ""

        accesses = [1 for state in states if len(states[state].getaccess() + states[state].getevictmiss())]

        if accesses:

            rulesetstr = self._genAccessHeader(arch) + self.nl

            rulestr = ""
            for state in sorted(states.keys()):
                if len(states[state].getaccessmiss() + states[state].getevictmiss()):
                    retstrs = self._genAccessState(arch, states[state], verify_ssp)
                    rulestr += retstrs[0] + self.nl
                    sendfctstr += retstrs[1] + self.nl

            rulesetstr += self._addtabs(rulestr, 1)

            rulesetstr += self._genAccessEnd() + self.nl

        return sendfctstr + rulesetstr

    def _genAccessHeader(self, arch):
        fctstr = "ruleset m:" + self.SetKey + arch + " do" + self.nl
        fctstr += "ruleset "+ self.cadr +":" + self.kaddress + " do" + self.nl
        fctstr += self.tab + "alias " + self.ccle + ":" + self.instsuf + arch + "[m]." + \
                    self.CLIdent + "[adr] do" + self.nl

        return fctstr

    def _genAccessEnd(self):
        statestr = self.tab + "endalias" + self.end
        statestr += "endruleset" + self.end
        statestr += "endruleset" + self.end

        return statestr

    def _genAccessState(self, arch, state, verify_ssp):
        transitions = state.getaccess() + state.getevictmiss()
        transitions.sort(key=lambda transition: (transition.getguard(),
                                                 transition.getcond(),
                                                 transition.getfinalstate().getstatename()))

        statestr = ""
        sendfctstr = ""

        for transition in transitions:

            ruleid = arch + "_" + transition.getstartstate().getstatename() + "_" + transition.getguard()
            sendfctstr += self._genSendFunctionHeader(arch, ruleid, transition) + self.nl

            ccle_dot_state = self.ccle + "." + self.iState

            statestr += "rule \"" + ruleid + "\"" + self.nl
            statestr += self.tab + ccle_dot_state + " = " + arch + "_" \
                     + state.getstatename() + self.nl
            if verify_ssp:
                statestr += " & (" + self._genBagCnt(self.lock_set, "l", "true") + " = 0)"
            statestr += self.nl
            statestr += "==>" + self.nl
            if verify_ssp:
                statestr += self.tab + self.unlock_ss + " := " + ccle_dot_state
                statestr += self.end
            statestr += self.tab + self.tSEND + ruleid + "(" + self.cadr + ", m)" + self.end
            if verify_ssp:
                statestr += self.tab + "if !(" + self.unlock_ss + " = " + ccle_dot_state \
                         + ") then" + self.nl
                statestr += self.tab + self.tab + self._genBagAdd("m", self.lock_set)
                statestr += self.end
                statestr += self.tab + "endif" + self.end
            statestr += "endrule" + self.end + self.nl

        return [statestr, sendfctstr]

    def _generateUnlockRules(self, arch, stable_states):
        
        rulesetstr = self._genAccessHeader(arch) + self.nl
        rulestr = ""

        for state in stable_states:
            ruleid = "Unlocking " + arch + "_" + state
            rulestr += "rule \"" + ruleid + "\"" + self.nl
            rulestr += self.tab + self.ccle + "." + self.iState + " = " + arch \
                    + "_" + state
            rulestr += " & !(" + self.ccle + "." + self.iState + " = " \
                    + self.unlock_ss + ") & !(" + self._genBagCnt(\
                    self.lock_set, "l", self.lock_set + "[l] = m") + " = 0)" 
                    #TODO is it possible to not have "m" hardcoded here?
            rulestr += self.nl
            rulestr += "==>" + self.nl
            rulestr += self.tab + self._genBagDel(self.lock_set, "l", "true") 
            rulestr += self.end
            rulestr += "endrule" + self.end + self.nl

        rulesetstr += self._addtabs(rulestr, 1)
        rulesetstr += self._genAccessEnd() + self.nl

        return rulesetstr


    def _genSendFunctionHeader(self, arch, ruleid, transition):
        fctstr = "procedure " + self.tSEND + ruleid + \
                    "(" + self.cadr + ":" + self.kaddress + "; m:" + self.SetKey + arch + ")" + self.end
        fctstr += "var " + self.defmsgname + ": " + self.rmessage + self.end
        fctstr += "begin" + self.nl
        fctstr += self.tab + "alias " + self.ccle + ": " + self.instsuf + arch + "[m]." + \
                    self.CLIdent + "[adr] do" + self.nl
        fctstr += self._genTransition(arch, transition, transition.getguard(), 1)
        fctstr += "endalias" + self.end
        fctstr += "end" + self.end + self.nl

        return fctstr

########################################################################################################################
# FIFO RECEIVE RULE
########################################################################################################################

    def _generateFIFORecvRule(self, parser):

        rulestr = ""

        for network in self.ONetworks + self.UNetworks:
            for cache in parser.getCacheSeq():
                for directory in parser.getDirSeq():
                    inputstr = self._openTemplate(self.ffiforule)
                    replacekeys = [self.k_fifo+network, self.SetKey + directory, directory, cache]

                    for ind in range(0, len(replacekeys)):
                        inputstr = self._stringRepl(inputstr, ind, replacekeys[ind])

                    rulestr += inputstr + self.nl

        return rulestr

########################################################################################################################
# NETWORK RECEIVE RULES
########################################################################################################################

    def _generateNetworkRules(self, parser):
        rulestr = self._genUnorderedNetRule(parser)
        rulestr += self._genOrderedNetRule(parser)

        return rulestr

    def _genUnorderedNetRule(self, parser):

        rulestr = ""
        for network in self.UNetworks:
            for cache in parser.getCacheSeq():
                for directory in parser.getDirSeq():
                    inputstr = self._openTemplate(self.funorderedrule)
                    replacekeys = [network, self.k_fifo+network, self.SetKey + directory, directory, cache]

                    for ind in range(0, len(replacekeys)):
                        inputstr = self._stringRepl(inputstr, ind, replacekeys[ind])

                    rulestr += inputstr + self.nl

        return rulestr

    def _genOrderedNetRule(self, parser):

        rulestr = ""
        for network in self.ONetworks:
            for cache in parser.getCacheSeq():
                for directory in parser.getDirSeq():
                    inputstr = self._openTemplate(self.forderedrule)
                    replacekeys = [network,
                                   self.countsuf + network,
                                   self.k_fifo+network,
                                   self.SetKey + directory,
                                   directory,
                                   cache]

                    for ind in range(0, len(replacekeys)):
                        inputstr = self._stringRepl(inputstr, ind, replacekeys[ind])

                    rulestr += inputstr + self.nl

        return rulestr

########################################################################################################################
# GENERATE START STATES
########################################################################################################################

    def _generateStartState(self, parser, verify_ssp):
        startstr = "startstate" + self.nl + self.nl

        startdef = self._genDirectoryInit(parser)

        startdef += self._genCacheInit(parser)

        startdef += self._genFIFOInit()
        startdef += self._genNetworkInit()

        # TODO the code below is quite hacky, is there a way to make it better?
        if verify_ssp:
            # any cache will do as they have identical startstates
            cache = parser.getCacheSeq()[0] 
            startdef += self.tab + self.unlock_ss + " := cache_" \
                        + self.GlobalInit[cache]['State'] + self.end
        
        startstr += self._addtabs(startdef, 1)

        startstr += self.nl + "endstartstate" + self.end

        return startstr

    def _genDirectoryInit(self, parser):
        startstr = ""

        for directory in parser.getDirSeq():
            dirstr = self._genInitObjectHeader(directory)

            dirprefix = self.instsuf + directory + "[i]." + self.CLIdent + "[a]."
            dirstr += self._addtabs(self._genObjectInit(dirprefix, directory, self.GlobalInit[directory]) +
                                    self._genAccessInit(dirprefix), 1)

            dirstr += self._genInitObjectEnd()

            startstr += dirstr + self.nl

        return startstr

    def _genCacheInit(self, parser):
        startstr = ""

        for cache in parser.getCacheSeq():
            cachestr = self._genInitObjectHeader(cache)

            cacheprefix = self.instsuf + cache + "[i]." + self.CLIdent + "[a]."
            cachestr += self._addtabs(self._genObjectInit(cacheprefix, cache, self.GlobalInit[cache]) +
                                      self._genAccessInit(cacheprefix), 1)

            cachestr += self._genInitObjectEnd()

            startstr += cachestr

        return startstr

    def _genInitObjectHeader(self, objname):
        header = "for i:" + self.SetKey + objname + " do" + self.nl
        header += "for a:" + self.kaddress + " do" + self.nl
        return header

    def _genInitObjectEnd(self):
        return "endfor" + self.end + "endfor" + self.end

    def _genObjectInit(self, prefix, arch, definitions):
        startstr = ""
        for definition in sorted(definitions):
            if definition == self.iState:
                startstr += prefix + definition + " := " + arch + "_" + definitions[definition] + self.end
            else:
                startstr += prefix + definition + " := " + definitions[definition] + self.end

        if self.defer:
            startstr += prefix + self.iFifo + ".QueueInd := 0" + self.end

        return startstr

    def _genFIFOInit(self):

        startstr = ""
        for network in self.ONetworks + self.UNetworks:
            inputstr = self._openTemplate(self.ffifoinit)
            replacekeys = [self.k_fifo + network]

            for ind in range(0, len(replacekeys)):
                inputstr = self._stringRepl(inputstr, ind, replacekeys[ind])

            startstr += inputstr + self.nl

        return startstr

    def _genNetworkInit(self):

        startstr = self._genUnorderedNetInit()
        startstr += self._genOrderedNetInit()

        return startstr

    def _genUnorderedNetInit(self):

        startstr = ""
        for network in self.UNetworks:
            startstr += self._stringReplKeys(self._openTemplate(self.funorderedinit), [network]) + self.nl

        return startstr

    def _genOrderedNetInit(self):

        startstr = ""
        for network in self.ONetworks:
            startstr += self._stringReplKeys(self._openTemplate(self.forderedinit),
                                             [network, self.countsuf + network]
                                             ) + self.nl

        return startstr

    def _genAccessInit(self, dirprefix):
        return dirprefix + self.iAccess + " := " + self.defaccess + self.end

########################################################################################################################
# GENERATE INVARIANTS
########################################################################################################################

    def _generateInvariants(self, parser):
        invstr = self._genInvariantWS(parser)

        return invstr

    def _genInvariantWS(self, parser):
        invstr = ""

        for cache in parser.getCacheSeq():
            invstr += self._stringReplKeys(self._openTemplate(self.finvariantws),
                                            [self.SetKey + cache,
                                             self.kaddress,
                                             self.iAccess,
                                             self.instsuf + cache,
                                             self.CLIdent,
                                             self.iAccess,
                                             self.memaccessdef[-1]]
                                            ) + self.nl

        return invstr

########################################################################################################################
# REPLACE DYNAMIC
########################################################################################################################
    def _openTemplate(self, filename):
        return re.sub(r'^\#.*\n?', '', open(self.templatepath + "/" + filename, "r").read(), flags=re.MULTILINE)

    def _stringReplKeys(self, refstring, replacekeys):
        inputstr = refstring
        for ind in range(0, len(replacekeys)):
            inputstr = self._stringRepl(inputstr, ind, replacekeys[ind])
        return inputstr

    def _stringRepl(self, string, ind, keyword):
        return re.sub(r"\$" + str(ind) + "\$", keyword, string)

    def _addtabs(self, string, count):
        tabstring = ""
        for ind in range(0, count):
            tabstring += self.tab

        outstr = ""
        for line in string.splitlines():
            outstr += tabstring + line + self.nl

        return outstr

    @ staticmethod
    def _testInt(string):
        try:
            int(string)
            return True
        except ValueError:
            return False

    @ staticmethod
    def _testOperator(string):
        if string.isalpha():
            return True
        return False
