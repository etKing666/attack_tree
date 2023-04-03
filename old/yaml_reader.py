""" YAML reader """

import yaml

from yaml.loader import SafeLoader
# Opening yaml file in read mode with context reader so that we do not have to close file later on
with open('sampleyaml.yaml', 'r') as f:
    data = list(yaml.load(f))
    print(data)

