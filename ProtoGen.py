import time
import sys

from Parser.ClassProtoParser import ProtoParser
from Algorithm.ProtoAlgorithm import ProtoAlgorithm
from Algorithm.ProtoConfig import ProtoConfig

from Murphi.Murphi import Murphi

from Monitor.Debug import *

spacer = "\n\n\n"

if len(sys.argv[1:]) == 0:
    file = "MOSI.pcc"
else:
    assert len(sys.argv[1:]) > 1, "No or to many arguments"
    file = sys.argv[1]

Config = ProtoConfig()

# Frontend
pheader("PROTOGEN PARSER")
Parser = ProtoParser(file)

talgo = time.time()
pheader(spacer+"PROTOGEN ALGORITHM")
Algorithm = ProtoAlgorithm(Parser, Config)
pheader(spacer+"PROTOGEN BACKEND")
MurphiDesc = Murphi(Parser, Algorithm)
pdebug("ProtoGen runtime: " + str(time.time()-talgo) + '\n')

pheader(spacer+"Murphi make and run")
talgo = time.time()
MurphiDesc.runMurphi()
pdebug("Murphi runtime: " + str(time.time()-talgo) + '\n')

