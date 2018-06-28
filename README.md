ProtoGen is still under development. This is an alpha release. 

There is currently no type checking implemented for the ProtoCC language frontend, but it will be provided in the near future. Furthermore, multiple new features are in development, which will be published in the near future. 

ProtoGen v0.5: Now supports SSP verification. The SSP is verified before ProtoGen generates the concurrent protocol. 

A detailed descritpion of the ProtoGen algorithm is provided here: http://homepages.inf.ed.ac.uk/vnagaraj/papers/isca18a.pdf

If you have questions, you want to contribute or simply report any bugs, please contact: proto.gen at ed.ac.uk

Examples MSI.pcc, MESI.pcc, MOSI.pcc provided
Run ProtoGen.py PROTOCOL.pcc

Requirements:
Python 3.5 or higher
Packages: antlr-python3-runtime 3.4; colorama 0.3.9; tabulate 0.8.2

Please edit Murphi path in /Murphi/MurphiTemp/tmpmakefile

