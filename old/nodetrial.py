from anytree import Node, RenderTree
from anytree.exporter import DotExporter

udo = Node("Udo", id="root")
marc = Node("Marc", parent=udo, id="node1")
lian = Node("Lian", parent=marc, id="node11")
dan = Node("Dan", parent=udo, id="node2")
jet = Node("Jet", parent=dan, id="node21")
jan = Node("Jan", parent=dan, id="node22")
joe = Node("Joe", parent=dan, id="node23")

udo.name = f"{udo.name}\n{udo.id}"

print(RenderTree(udo))
DotExporter(udo).to_picture("udo.png")
