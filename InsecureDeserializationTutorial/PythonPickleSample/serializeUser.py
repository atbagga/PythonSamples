import pickle

class User(object):
    def __init__(self, name):
        self.name = name

n1 = input("Enter your name: ")
u1 = User(n1)

serialized = pickle.dumps(u1)
filename = 'serialized.user'

with open(filename, 'wb') as fobj:
    fobj.write(serialized)
    fobj.flush()
    fobj.close()
