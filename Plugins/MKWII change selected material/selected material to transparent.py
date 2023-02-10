__author__ = "Okin"
__version__ = "1.0"

from BrawlCrate.API import *
from  BrawlLib.Wii.Graphics import *
from BrawlLib.SSBB.ResourceNodes import *

selNodes = BrawlAPI.SelectedNodes

for node in selNodes:
    node.Ref0 = 128
    node.Ref1 = 255
    node.Comp0 = AlphaCompare.GreaterOrEqual
    node.Comp1 = AlphaCompare.LessOrEqual

BrawlAPI.ShowMessage("selected are now transperent", "")

