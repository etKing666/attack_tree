import json
from time import sleep
from anytree import Node, RenderTree
from anytree.exporter import DotExporter

# Global variables
data = dict()
root_node = Node("default")
nodes = dict()


def load_file():
    global data, root_node, nodes
    filename = input("""Please enter the file name (incl. extension) to load to memory - e.g. 'filename.json'.
NOTE: 
1. Make sure that the file you are referring to is in the same folder with the app.
2. If you do not enter a file name and hit 'Enter', default file name (data.json) will be used.
File name:""")
    if filename == "":
        with open('../data.json', 'r') as file:
            data = json.load(file)
            print("File 'data.json' is loaded to the memory.\n")
    else:
        try:
            with open(f'{filename}', 'r') as file:
                data = json.load(file)
                print(f"File '{filename}' is loaded to the memory.\n")
        except:
            print("File couldn't be loaded. Please check the file name and extension and try again.")
            return

    length = len(data)
    key_names = list(data.keys())

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


def generate():
    """Generates the tree on the console."""
    if not root_node.children:  # Checks if a .json document is loaded to the memory ("Default" node with no children means no .json document)
        print("ERROR: No .json document is loaded to the memory. Please load a .json document containing attack tree data first.\n")
        return
    else:
        print(RenderTree(root_node))
    return


def visualise():
    """Generates a visual diagram of the tree in .png format and saves (exports) it to the working folder"""
    if not root_node.children:  # Checks if a .json document is loaded to the memory ("Default" node with no children means no .json document)
        print("ERROR: No .json document is loaded to the memory. Please load a .json document containing attack tree data first.\n")
        return
    temp_tree = nodes  # Copies the data to make some adjustments for visualization so that the original data remains intact.
    for leaf in temp_tree.values():
        leaf.name = f"{leaf.name}\n{leaf.value}"  # So that the name is on the first line and the value is on the second.
        if leaf.parent is None:
            tree_root = leaf
    filename = input("""Please enter a file name for the attack tree that will be exported as a .png file (e.g. 'attack_tree').
If you do not enter a file name and hit 'Enter', the file name will default to 'tree.png'.
File name:""")
    if filename == "":
        filename = "tree.png"
    else:
        filename = filename + ".png"
    DotExporter(tree_root).to_picture(f"{filename}")
    return


def calculate():
    if not root_node.children:  # Checks if a .json document is loaded to the memory ("Default" node with no children means no .json document)
        print(
            "ERROR: No .json document is loaded to the memory. Please load a .json document containing attack tree data first.\n")
        return
    height = root_node.height  # Calculating total height of the tree
    req_depth = height - 1  # To reach the first parents, required depth is height-1

    # Iterative value calculation:
    while req_depth >= 0:
        for node in nodes.values():
            if node.children:
                if node.depth == req_depth:
                    children = []
                    children.extend(node.children)
                    num_child = len(children)  # The number of children the parent node has
                    if num_child == 0:
                        num_child = 1  # In order escape the division by zero error for leaves with no children
                    total = 0
                    if node.value is 0.0:  # Overrides children node values if a value is provided for the parent node
                        for child in children:
                            total += child.value
                        node.value = total / num_child
        req_depth -= 1

    print("""=================
    THE TREE WITH CALCULATED VALUES:
==============""")
    print(RenderTree(root_node))
    # Evaluation of the value according to the scale.
    if 10 >= root_node.value > 9.5:
        rating = "VERY HIGH"
    elif 9.5 >= root_node.value > 7.9:
        rating = "HIGH"
    elif 7.9 >= root_node.value > 2.0:
        rating = "MODERATE"
    elif 2.0 >= root_node.value > 0.5:
        rating = "LOW"
    elif 0.5 >= root_node.value >= 0:
        rating = "VERY LOW"
    else:
        rating = "NOT CALCULATED (INVALID VALUES). Please check the values you entered for the leaf nodes"  # In order to catch any invalid values (i.e. higher than 10)
    print(f"\nThe overall value is: {root_node.value} and overall threat rating is {rating}.\n")
    print("If you think that the tree looks OK, you can get a .png version of it by using 'visualise' feature.\n")
    return


def analyse():
    if not root_node.children:  # Checks if a .json document is loaded to the memory ("Default" node with no children means no .json document)
        print(
            "ERROR: No .json document is loaded to the memory. Please load a .json document containing attack tree data first.\n")
        return
    print("""\nFrom this section, you can enter different values to the nodes to analyse the possible impact of potential threats to the business. The values suggested by Microsoft are:
You can also enter DREAD values. 
Remember:
1. You can enter a value to a parent node. In this case, the value calculated using the children nodes will be overriden.
2. The algorithm uses a simple average. Keeping this in mind, you can enter any value (be it potential damage, cost 
or any other value). However, it doesn't make probabilistic (OR/AND) calculations. 
================================
THE CURRENT STATE OF THE TREE:
=========================""")
    print(RenderTree(root_node))

    while True:
        node_select = input("""\nPlease enter the node/leaf that you want to enter a value.
HINT: If the node is: '/Business/Threat_Category/Threat_Name' you should enter Threat_Name to select the node.
Hit ENTER to exit.
Enter node/leaf name:""")
        if node_select == "":
            break
        elif node_select not in nodes.keys():
            print("The node couldn't be found. Please check the node name and try again.\n")
            sleep(1)
            continue
        else:
            while True:  # Gets and validates user input
                try:
                    new_value = input(
                        """\nPlease enter a floating point or integer value between 0.0 and 10.0. or hit ENTER to exit.\nValue:""")
                    if new_value == "":
                        break
                    elif 0 <= float(new_value) <= 10:
                        nodes[node_select].value = float(new_value)
                        print("The value has been updated.\n")
                        sleep(1)
                        break
                    else:
                        print("Please enter a value between 0.0 and 10.0\n")
                        continue
                except ValueError:
                    print("Please enter a valid floating point value.\n")

        another = input("Do you want to a value for another node/leaf? (Y/N)")
        if another == "y" or another == "Y":
            analyse()
        elif another == "n" or another == "N":
            print("You can see the impact of the new values by using 'calculate' feature.\n")
            break
        else:
            print("Please enter a valid value (Y/N).")
    return
