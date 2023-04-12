import json
from copy import deepcopy
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
        with open('data/data.json', 'r') as file:
            data = json.load(file)
            print("File 'data.json' is loaded to the memory.\n")
            sleep(1)
    else:
        try:
            with open(f'data/{filename}', 'r') as file:
                data = json.load(file)
                print(f"File '{filename}' is loaded to the memory.\n")
                sleep(1)
        except:
            print("File couldn't be loaded. Please check the file name and extension and try again.")
            sleep(2)
            return

    length = len(data)
    key_names = list(data.keys())
    root_name = data["root"]["name"]

    for i in range(length):
        leaf = key_names[i]
        name = data[leaf]['name']
        parent = data[leaf]['parent']
        if parent == "None":
            parent = None  # For root node, the parent value is set to "None" as per the anytree documentation
        elif parent == root_name:
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
            value = round(float(value), 2)  # In order to prevent possible errors in user input (e.g. integer values)

        leaf = Node(name=name, parent=parent, value=value)

        if leaf.parent is None:
            root_node = leaf
            nodes["root"] = root_node
        else:
            nodes[leaf.name] = leaf


def generate():
    """Generates the tree on the console."""
    if not root_node.children:  # Checks if a .json document is loaded to the memory ("Default" node with no children means no .json document)
        print(
            "ERROR: No .json document is loaded to the memory. Please load a .json document containing attack tree data first.\n")
        return
    else:
        print(100 * "=" + "\n                                          THE ATTACK TREE:\n" + 100 * "=")
        print(RenderTree(root_node))
    sleep(2)
    return


def visualise():
    """Generates a visual diagram of the tree in .png format and saves (exports) it to the working folder"""
    if not root_node.children:  # Checks if a .json document is loaded to the memory ("Default" node with no children means no .json document)
        print(
            "ERROR: No .json document is loaded to the memory. Please load a .json document containing attack tree data first.\n")
        return
    generate()
    select_root = input(
        "\nPlease refer to the attack tree above and select the leaf node which you'd like to start visualising your tree.\nYou can select the root node to visualise the whole tree or you can select a leaf node and visualise the tree partially. This may come in handy when your attack tree is too big to visualise appropriately or when you want to focus on a specific part of the tree.\nHINT: If the node is: '/Business/Threat_Category/Threat_Name' you should enter Threat_Name to select the node. You can also enter 'root' to visualise whole attack tree. Hit ENTER to exit.\nStarting leaf node:")
    while True:
        if select_root == "":
            break
        elif select_root == "root":
            temp_tree = nodes
            file_generate(temp_tree, root_node)
            break
        elif select_root not in nodes.keys():
            print("The node couldn't be found. Please check the node name and try again.\n")
            sleep(1)
            break
        else:
            temp_tree = dict()  # Creates an empty dict for temporary tree
            tree_root = nodes[select_root]
            temp_tree[select_root] = nodes[select_root]
            temp_children = nodes[
                select_root].descendants  # Copies a tuple of the selected leaf node's childred. Will be used for creating a dictionary of nodes iteratively.
            for child in temp_children:
                temp_tree[child.name] = nodes[child.name]
            file_generate(temp_tree, tree_root)
            break
    sleep(2)
    return


def file_generate(tree, selected_node):
    """A helper function for visualise() which allows the user to create sub-trees instead of whole tree."""
    gen_tree = deepcopy(
        tree)  # Copies the tree to keep temporary tree ata intact, in case user wants to make aditonal calculations/visualisations.
    for item in gen_tree.values():
        if item.name == selected_node.name:
            gen_root = item
        item.name = f"{item.name}\n{item.value}"  # So that the name is on the first line and the value is on the second.
    if gen_root == None:
        print("\nERROR: The leaf node couldn't be found. Please check your input and try again.")
        return
    filename = input("""\nPlease enter a file name for the attack tree that will be exported as a .png file (e.g. 'attack_tree').
If you do not enter a file name and hit 'Enter', the file name will default to 'tree.png'.
File name:""")

    if filename == "":
        filename = "tree.png"
    else:
        filename = filename + ".png"

    DotExporter(gen_root).to_picture(f"trees/{filename}")
    print("The tree image has been exported to the /trees folder.")
    sleep(1)
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
                    for child in children:
                        total += child.value
                    node.value = round((total / num_child), 2)
        req_depth -= 1

    print(100 * "=" + "\n                                  THE TREE WITH CALCULATED VALUES:\n" + 100 * "=")
    print(RenderTree(root_node))
    evaluate(root_node)
    print("HINT: If you think that the tree looks OK, you can get a .png version of it by using 'visualise' feature.\n")
    sleep(2)
    return


def evaluate(tree_root):
    """Evaluates the overall risk rating value according to the scale."""
    if 10 >= tree_root.value > 9.5:
        rating = "VERY HIGH"
    elif 9.5 >= tree_root.value > 7.9:
        rating = "HIGH"
    elif 7.9 >= tree_root.value > 2.0:
        rating = "MODERATE"
    elif 2.0 >= tree_root.value > 0.5:
        rating = "LOW"
    elif 0.5 >= tree_root.value >= 0:
        rating = "VERY LOW"
    else:
        rating = "NOT CALCULATED (INVALID VALUES). Please check the values you entered for the leaf nodes"  # In order to catch any invalid values (i.e. higher than 10)
    print(f"\n====>The overall value is: {tree_root.value} and overall threat rating is {rating}.<====\n")
    return


def analyse():
    if not root_node.children:  # Checks if a .json document is loaded to the memory ("Default" node with no children means no .json document)
        print(
            "ERROR: No .json document is loaded to the memory. Please load a .json document containing attack tree data first.\n")
        return
    print("""\nFrom this section, you can enter the probability of potential threats to take place and analyse the different scenarios and how these scenarios may impact your business. The values suggested by NIST vary between 0-10. Please refer to the readme file for details.
Instructions:
1. Only values (floating point or integer) on a scale of 0-10 are accepted.
2. You can only enter a value to leaves, not the parent nodes.
3. The algorithm uses a simple average and it doesn't make probabilistic (OR/AND) calculations.\n""")
    print(100 * "=" + "\n                                   THE CURRENT STATE OF THE TREE:\n" + 100 * "=")
    print(RenderTree(root_node))

    while True:
        node_select = input("""\nPlease enter the leaf that you want to enter a value.
->HINT: If the node is: '/Business/Threat_Category/Threat_Name' you should enter Threat_Name to select the leaf.
->Hit ENTER to exit.
->CAUTION: You can only enter a value for leaves (at the bottom of the tree), not the leaves (the higher levels).
Enter leaf name:""")
        if node_select == "":
            break
        elif node_select not in nodes.keys():
            print("ERROR: The node couldn't be found. Please check the node name and try again.\n")
            sleep(1)
            continue
        elif len(nodes[node_select].children) != 0:  # Checks if the user input indicates a leaf node or a leaf
            print(
                "ERROR: You can only enter a value for leaves (at the bottom of the tree), not the leaf nodes (the higher levels). Please check your input and try again.\n")
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
