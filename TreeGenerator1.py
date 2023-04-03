import json
from anytree import Node, RenderTree
from anytree.exporter import DotExporter

with open('data.json', 'r') as file:
    data = json.load(file)


length = len(data)
key_names = list(data.keys())
nodes = dict()

for i in range(length):
    leaf_name = key_names[i]
    name = data[leaf_name]['name']
    print(name)
    parent = data[leaf_name]['parent']
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

    print(parent)
    probability = data[leaf_name]['probability']
    print(probability)
    leaf_name = Node(name=name, parent=parent, probability=probability)

    if leaf_name.parent == None:
        root_node = leaf_name
        nodes["root"] = root_node
    else:
        nodes[leaf_name.name] = leaf_name

    print(nodes)

print(RenderTree(root_node))
DotExporter(root_node).to_picture("root.png")
