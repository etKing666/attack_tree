import json
from anytree import Node, RenderTree, PreOrderIter
from anytree.exporter import DotExporter

with open('../data/data.json', 'r') as file:
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

print(root_node)
print(nodes)
print(RenderTree(root_node))

leaves = []
for key in nodes:
    if nodes[key].is_leaf: # Filtering the nodes with no children
        print(nodes[key])
        leaves.append(nodes[key])

print(f"The bottom leaves are: {leaves}")

leafValues = dict()
for leaf in leaves:
    siblings = [leaf]
    siblings.extend(leaf.siblings)
    if leaf.parent in leafValues:
        pass
    else:
        leafValues[leaf.parent] = siblings

#

# Iterative value calculation:
height = root_node.height
reqDepth = height - 1
for key in leafValues.keys():
    print(f"Number of children: {len(key.children)}")


while reqDepth >= 0:
    for key in leafValues.keys(): #keys are automatically first parents
        if key.depth == reqDepth:
            numChild = len(key.children) # The number of children the parent node has
            if numChild == 0:
                numChild = 1 # In order escape the division by zero error for leaves with no children
            total = 0
            for leaf in leafValues[key]:
                print(leafValues[key])
                print(leaf)
                print(leaf.value)
                total += leaf.value
            key.value = total / numChild
            print(f"Found it! It is: {key.name} and its value is {key.value}")
    reqDepth-=1
#print(f"The value is: {key.value}")

DotExporter(root_node).to_picture("root.png")


