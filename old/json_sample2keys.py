from anytree.importer import JsonImporter
from anytree import Node, RenderTree
import json
from anytree.exporter import DotExporter

with open('sample.json', 'r') as file:
    data = json.load(file)



length = len(data)
key_names = list(data.keys())
nodes = []

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
        len_nodes = len(nodes)
        for i in range(len_nodes):
            if parent == nodes[i].parent:
                parent = nodes[i]
            else:
                pass
    print(parent)
    probability = data[leaf_name]['probability']
    print(probability)
    leaf_name = Node(name=name, parent=parent, probability=probability)
    if leaf_name.parent == None:
        root_node = leaf_name
    nodes.append(leaf_name)
    print(nodes)



#for leaf in data:
    #name = get.key(leaf)
    #name = name = Node(name=data.get(name).get('name'), parent=data.get(name).get('parent'), probability=data.get(name).get('probability'))


#print(data["leaf0"])
#data = json.dumps(raw_data)
#importer = JsonImporter()
#root = importer.import_(data)
#print(RenderTree(root))
#DotExporter(root).to_picture("sample.png")


