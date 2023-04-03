from anytree.importer import JsonImporter
from anytree import Node, RenderTree
import json
from anytree.exporter import DotExporter

with open('sample.json', 'r') as file:
    data = json.load(file)

print(data)
#print(data["leaf0"])

root = Node("root")
print(root)

try:
    for x in range(100):
        exec("leaf" + str(x))


for x in range(100):
    for y in range(100):
        leaf data


#data = json.dumps(raw_data)
#importer = JsonImporter()
#root = importer.import_(data)
#print(RenderTree(root))
#DotExporter(root).to_picture("sample.png")


