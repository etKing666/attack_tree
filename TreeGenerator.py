import json
from anytree import Node, RenderTree
from anytree.exporter import DotExporter

with open('data.json', 'r') as file:
    data = json.load(file)

length = len(data)
key_names = list(data.keys())
nodes = dict()

for i in range(length):
    leaf = key_names[i]
    name = data[leaf]['name']
    parent = data[leaf]['parent']
    if parent == "None":
        parent=None #For root node, the parent value is set to "None" as per the anytree documentation
    elif parent == "root":
        parent=root_node
    else:
        for x in nodes.keys():
            if parent == x:
                parent = nodes[x]
            else:
                pass

    probability = data[leaf]['probability']
    print(probability)
    leaf = Node(name=name, parent=parent, probability=probability)

    if leaf.parent == None:
        root_node = leaf
        nodes["root"] = root_node
    else:
        nodes[leaf.name] = leaf

print(RenderTree(root_node))
DotExporter(root_node).to_picture("root.png")
