import yaml
import subprocess

filename = input('Enter filename: ')

if not filename:
    filename = 'exploit.yaml'

with open(filename) as yml_file:
    yml = yml_file.read()
    content = yaml.load(yml, Loader=yaml.UnsafeLoader)
    
print(content['user'])