import json
from anytree import Node, RenderTree, PreOrderIter
from anytree.exporter import DotExporter

with open('../data.json', 'r') as file:
    data = json.load(file)

length = len(data)
key_names = list(data.keys())
nodes = dict()

for i in range(length):
    leaf = key_names[i]
    name = data[leaf]['name']
    parent = data[leaf]['parent']
    if parent == "None":
        parent = None  # For root node, the parent value is set to "None" as per the anytree documentation
    elif parent == "root":
        parent = root_node
    else:
        for x in nodes.keys():
            if parent == x:
                parent = nodes[x]
            else:
                pass

    value = data[leaf]['value']
    if value is None:
        value = 0.0 # In order to have a numeric value
    else:
        value = float(value)  # In order to prevent possible errors in user input (e.g. integer values)

    leaf = Node(name=name, parent=parent, value=value)

    if leaf.parent is None:
        root_node = leaf
        nodes["root"] = root_node
    else:
        nodes[leaf.name] = leaf

print(nodes)
print(RenderTree(root_node))
DotExporter(root_node).to_picture("root.png")

# Iterative value calculation:
height = root_node.height
reqDepth = height - 1

while reqDepth >= 0:
    for node in nodes.values():
        if node.children:
            if node.depth == reqDepth:
                numChild = 0
                children = []
                children.extend(node.children)
                numChild = len(children) # The number of children the parent node has
                if numChild == 0:
                    numChild = 1 # In order escape the division by zero error for leaves with no children
                total = 0
                for child in children:
                    total += child.value
                node.value = total / numChild
                #print(f"Found it! It is: {node.name} and its value is {node.value}")
    reqDepth-=1

print("""=================
THE FINAL TREE:
==============""")
print(RenderTree(root_node))
print(f"The overall value is: {root_node.value}")



