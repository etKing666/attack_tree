from anytree import Node, RenderTree
from anytree.exporter import DotExporter

udo = Node("Udo")
marc = Node("Marc", parent=udo)
lian = Node("Lian", parent=marc)
dan = Node("Dan", parent=udo)
jet = Node("Jet", parent=dan)
jan = Node("Jan", parent=dan)
joe = Node("Joe", parent=dan)

DotExporter(udo).to_picture("udo.png")
