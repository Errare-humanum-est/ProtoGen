# ProtoGen

*ProtoGen is still under development. This is version is discontinued and replaced by HeteroGen https://github.com/Errare-humanum-est/HeteroGen*

There is currently no type checking implemented for the ProtoCC language frontend, but it will be provided in the near future. Furthermore, multiple new features are in development, which will be published in the near future. 

ProtoGen v0.5: Now supports SSP verification. The SSP is verified before ProtoGen generates the concurrent protocol.

**A detailed description of the ProtoGen algorithm is provided here:** [ProtoGen ISCA'18](https://github.com/Errare-humanum-est/ProtoGen/blob/e11c9b88f626dd03c5fa5d6fc947db32d25d5ea9/ISCA_ProtoGen.pdf)

If you have questions, you want to contribute or simply report any bugs, please contact: proto.gen at ed.ac.uk

## Running ProtoGen

Before running ProtoGen, please edit the MURPHIPATH in Murphi/MurphiTemp/tmpmakefile so that Murphi can be invoked correctly.

Then run:

```
ProtoGen.py PROTOCOL.pcc
```
Where PROTOCOL.pcc is the protocol (implemented in the DSL) that you wish to run ProtoGen on.

Four example protocols are provided:

- MSI_Proto.pcc
- MESI.pcc
- MESI_unordered.pcc
- MOSI.pcc

## Requirements:

Python 3.5 or higher.

Packages: antlr-python3-runtime 3.4; colorama 0.3.9; tabulate 0.8.2; seqdiag 0.9.5.

Other versions may work but have not been tested.
