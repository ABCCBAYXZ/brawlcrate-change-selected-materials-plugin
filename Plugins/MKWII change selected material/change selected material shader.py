__author__ = "Okin"
__version__ = "1.0"

from BrawlCrate.API import *
from BrawlLib.SSBB.ResourceNodes import *

selNodes = BrawlAPI.SelectedNodes
success = 1
num = BrawlAPI.UserStringInput("shader number", "")

for node in selNodes:
    node.Shader = "Shader " + num
    if node.Shader != "Shader " + num:
        success = 0

if success:
    BrawlAPI.ShowMessage("shader changed", "")
else:
    BrawlAPI.ShowMessage("didnt changed shader.", "")
