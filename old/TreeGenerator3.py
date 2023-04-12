import json
from anytree import Node, RenderTree
from anytree.exporter import DotExporter

# Global variables
data = dict()
root_node = Node("default")

def generate():
    filename = input("""Please enter the file name (incl. extension) to load to memory - e.g. 'filename.json'.
    NOTE: 
    1. Make sure that the file you are referring to is in the same folder with the app.
    2. If you do not enter a filename and hit 'Enter', default filename (data.json) will be used.
    Filename:
    """)
    if filename == "":
        with open('../data/data.json', 'r') as file:
            data = json.load(file)
            print("File 'data.json' is loaded to the memory.\n")
    else:
        try:
            with open(f'{filename}', 'r') as file:
                data = json.load(file)
                print(f"File '{filename}' is loaded to the memory.\n")
        except:
            print("File couldn't be loaded. Please check the filename and extension and try again.")
            return


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
            value = 0.0  # In order to have a numeric value
        else:
            value = float(value)  # In order to prevent possible errors in user input (e.g. integer values)

        leaf = Node(name=name, parent=parent, value=value)

        if leaf.parent is None:
            root_node = leaf
            nodes["root"] = root_node
        else:
            nodes[leaf.name] = leaf
    print(RenderTree(root_node))

def visualise():
    """Generates the tree on the console as well as exports a visual diagram to the working folder"""
    DotExporter(root_node).to_picture("root.png")
    return

def calculate():
    height = root_node.height  # Calculating total height of the tree
    reqDepth = height - 1  # To reach the first parents, required depth is height-1

    # Iterative value calculation:
    while reqDepth >= 0:
        for node in nodes.values():
            if node.children:
                if node.depth == reqDepth:
                    children = []
                    children.extend(node.children)
                    numChild = len(children)  # The number of children the parent node has
                    if numChild == 0:
                        numChild = 1  # In order escape the division by zero error for leaves with no children
                    total = 0
                    for child in children:
                        total += child.value
                    node.value = total / numChild

        reqDepth -= 1

    print("""=================
    THE FINAL TREE:
    ==============""")
    print(RenderTree(root_node))
    print(f"The overall value is: {root_node.value}")
    return

def analyse():
    print("""From this section, you can enter different values to the nodes to analyse the possible impact of potential
    threats to the business. The values suggested by Microsoft are:
    You can also enter DREAD values. 
    Remember:
    1. You can enter a value to a parent node. In this case, the value calculated using the children nodes will be overriden.
    2. The algorithm uses a simple average. Keeping this in mind, you can enter any value (be it potential damage, cost 
    or any other value). However, it doesn't make probabilistic (OR/AND) calculations. 
    ================================
    THE CURRENT STATE OF THE TREE:
    =========================""")
    print(RenderTree(root_node))
    nodeSelect  = input("""Please enter the node that you want to enter a value. HELP: If the node is:"
                        '/Business/Threat_Category/Threat_Name' you should enter Threat_Name to select the node.""")
    while True:
        pass
        return False
