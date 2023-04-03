from anytree.importer import JsonImporter
from anytree import Node, RenderTree
import json
from anytree.exporter import DotExporter

with open('sample2numbers.json', 'r') as file:
    data = json.load(file)


print(data)
length = len(data)
print(length)

for i in range(length):
    leafname = "leaf" + str(i)
    print(leafname)
    leafname = Node(i["name"], parent=i["parent"], probability=i["probability"])
    #print(leaf)


#print(data["leaf0"])
#data = json.dumps(raw_data)
#importer = JsonImporter()
#root = importer.import_(data)
#print(RenderTree(root))
#DotExporter(root).to_picture("sample.png")


