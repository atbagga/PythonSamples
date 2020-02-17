import pickle

class User(object):
    def __init__(self, name):
        self.name = name

filename = input('Enter filename to deserialize: ')
if not filename:
    filename = 'serialized.user'

with open(filename, 'rb') as fobj:
    raw_data = fobj.read()

deserialized = pickle.loads(raw_data)
print(deserialized.name)

