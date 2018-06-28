import time
import sys

from Parser.ClassProtoParser import ProtoParser
from Algorithm.ProtoAlgorithm import ProtoAlgorithm
from Algorithm.ProtoConfig import ProtoConfig

from Murphi.Murphi import Murphi

from Monitor.Debug import *

spacer = "\n\n\n"

if len(sys.argv[1:]) == 0:
    file = "MSI_Proto.pcc"
    #file = "MESI_unordered.pcc"
    file = "John_MESI_unordered.pcc"
else:
    assert len(sys.argv[1:]) == 1, "Too many arguments"
    file = sys.argv[1]

Config = ProtoConfig()

# Frontend
pheader("PROTOGEN PARSER")
Parser = ProtoParser(file)
if not Parser.checkAccessBehaviourDefined():
    print("Exiting.")
    sys.exit(1)
if not Parser.checkAllStatesReachable():
    print("Exiting.")
    sys.exit(1)

talgo = time.time()
pheader(spacer+"PROTOGEN ALGORITHM")
Algorithm = ProtoAlgorithm(Parser, Config)
pheader(spacer+"PROTOGEN BACKEND")
SSP_MurphiDesc = Murphi(Parser, Algorithm, True)
MurphiDesc = Murphi(Parser, Algorithm, False)
pdebug("ProtoGen runtime: " + str(time.time()-talgo) + '\n')

pheader(spacer+"Murphi make and run")
talgo = time.time()

pheader(spacer+"Starting SSP verification" + '\n')
SSP_MurphiDesc.runMurphi(True)
ssp_success = False

try:
    resultsfile = open("SSP_" + file.split(".")[0] + "_results.txt")
except FileNotFoundError:
    pwarning("SSP results file does not exist - did it compile correctly?"
             "\nPlease check SSP_" + file.split(".")[0] + "_compile.txt"
             " for details, and make sure your input is correctly specified.")
else:
    if "No error found" in resultsfile.read():
        psuccess("SSP verified without error")
        ssp_success = True
    else:
        pwarning("SSP did not verify correctly; please see SSP_"
                 + file.split(".")[0] + "_results.txt for the Murphi output.")
    resultsfile.close()
if ssp_success:
    pheader(spacer+"Starting full protocol verification" + '\n')
    MurphiDesc.runMurphi(False)
    try:
        resultsfile = open(file.split(".")[0] + "_results.txt")
    except FileNotFoundError:
        pwarning("Results file does not exist - did it compile correctly?"
                 "\nPlease check " + file.split(".")[0] + "_compile.txt "
                 "for details, and make sure your input is correctly specified"
                 ".")
    else:
        if "No error found" in resultsfile.read():
            psuccess("Full protocol verified without error")
        else:
            pwarning("Full protocol did not verify correctly; please see "
                     + file.split(".")[0] + "_results.txt for the Murphi "
                     " output.")
        resultsfile.close()
else:
    pwarning("Aborting full protocol verification as SSP deemed incorrect.")
pdebug(spacer + "Murphi runtime: " + str(time.time()-talgo) + '\n')
