from anytree.importer import JsonImporter
from anytree import RenderTree
import json
from anytree.exporter import DotExporter

with open('sample.json', 'r') as file:
    raw_data = json.load(file)

print(raw_data)


data = json.dumps(raw_data)
importer = JsonImporter()
root = importer.import_(data)
print(RenderTree(root))
DotExporter(root).to_picture("sample.png")


