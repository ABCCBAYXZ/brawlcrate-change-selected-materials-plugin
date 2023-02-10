__author__ = "Okin"
__version__ = "1.0"

from BrawlCrate.API import *
from  BrawlLib.Wii.Graphics import *
from BrawlLib.SSBB.ResourceNodes import *

selNodes = BrawlAPI.SelectedNodes

text = BrawlAPI.UserStringInput("insert shadow texture name", "")

child = MDL0MaterialRefNode()



for node in selNodes:
    for childs in node.Children:
        if childs.Name == text:
            BrawlAPI.ShowMessage("Materialname is already defined for " + node.Name, "error")
            break
    else:
        node.AddChild(child)
        node.Children[len(node.Children)-1].Name = text
        node.Children[len(node.Children)-1].Coordinates = TexSourceRow.TexCoord1
        node.Children[len(node.Children)-1].EmbossSource = 5
    

BrawlAPI.ShowMessage("finished", "")

